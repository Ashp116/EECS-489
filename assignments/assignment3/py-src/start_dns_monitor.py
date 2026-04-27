#!/usr/bin/env python

############################################################################
##
##     This file is part of the University of Michigan (U-M) EECS 489.
##
##     U-M EECS 489 is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     U-M EECS 489 is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with U-M EECS 489. If not, see <https://www.gnu.org/licenses/>.
##
#############################################################################

import threading
from collections import defaultdict

from scapy.all import *
from utils.rest import install_rule, delete_rule, install_group


ATTACK_THRESHOLD = 50
CLONE_PRIORITY = 40
DROP_PRIORITY = 100
ALLOW_PRIORITY = 200


class PacketHandler:

    def __init__(self, intf, mac_map, ip_map):
        self.intf = intf
        self.mac_map = mac_map
        self.ip_map = ip_map
        # TODO: Create and initialize additional instance variables
        #       for detection and mitigation
        # Maps host_ip -> set of pending DNS request IDs
        self.pending_requests = defaultdict(set)
        # Maps host_ip -> count of unmatched DNS responses
        self.unmatched_counts = defaultdict(int)
        # Set of hosts currently under attack (mitigation active)
        self.under_attack = set()
        # Lock for thread safety
        self.lock = threading.Lock()

    def start(self):
        t = threading.Thread(target=self._sniff, args=(self.intf,))
        t.start()

    def incoming(self, pkt, intf):
        macs = self.mac_map[intf]

        res = (pkt[Ether].src in macs or
               pkt[Ether].dst in macs)
        return res

    def handle_packet(self, pkt):
        # TODO: process the packet and install flow rules to perform DNS reflection
        #       attack detection and mitigation
        if IP not in pkt or DNS not in pkt:
            return

        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        dns_id = pkt[DNS].id
        is_response = pkt[DNS].qr == 1
        is_request = pkt[DNS].qr == 0

        with self.lock:
            if is_request:
                # Record this outgoing DNS request
                self.pending_requests[src_ip].add(dns_id)

                # If the host is already under attack, install an allow rule
                # so this legitimate response can pass the drop rule.
                # Use monitor=True so the response is also cloned to us,
                # allowing us to delete the allow rule after the response arrives.
                if src_ip in self.under_attack:
                    install_rule(table="monitor",
                                 ipv4_dst=src_ip,
                                 l4_src=53,
                                 dns_id=dns_id,
                                 monitor=True,
                                 priority=ALLOW_PRIORITY,
                                 is_permanent=True)

            elif is_response:
                # dst_ip is the host receiving the DNS response
                if dns_id in self.pending_requests[dst_ip]:
                    # Matched: legitimate response
                    self.pending_requests[dst_ip].discard(dns_id)

                    # Remove allow rule now that the response arrived
                    if dst_ip in self.under_attack:
                        delete_rule(table="monitor",
                                    ipv4_dst=dst_ip,
                                    l4_src=53,
                                    dns_id=dns_id)
                else:
                    # Unmatched response
                    self.unmatched_counts[dst_ip] += 1

                    if (self.unmatched_counts[dst_ip] > ATTACK_THRESHOLD and
                            dst_ip not in self.under_attack):
                        # Attack detected - install drop rule for all DNS responses to victim
                        self.under_attack.add(dst_ip)
                        install_rule(table="monitor",
                                     ipv4_dst=dst_ip,
                                     l4_src=53,
                                     priority=DROP_PRIORITY,
                                     is_permanent=True)

                        # Install allow rules for any pending legitimate requests
                        for pending_id in self.pending_requests[dst_ip]:
                            install_rule(table="monitor",
                                         ipv4_dst=dst_ip,
                                         l4_src=53,
                                         dns_id=pending_id,
                                         monitor=True,
                                         priority=ALLOW_PRIORITY,
                                         is_permanent=True)

    def _sniff(self, intf):
        sniff(iface=intf, prn=lambda x: self.handle_packet(x),
              lfilter=lambda x: self.incoming(x, intf))


if __name__ == "__main__":
    # TODO: Install flow rules to clone DNS packets from the switch to the monitor
    # Clone DNS responses (src port 53) to the monitoring service
    install_rule(table="monitor", l4_src=53, monitor=True,
                 priority=CLONE_PRIORITY, is_permanent=True)
    # Clone DNS requests (dst port 53) to the monitoring service
    install_rule(table="monitor", l4_dst=53, monitor=True,
                 priority=CLONE_PRIORITY, is_permanent=True)

    intf = "m1-eth1"
    mac_map = {intf: ["00:00:00:00:00:02", "00:00:00:00:00:03"]}
    ip_map = {intf: ["10.0.0.2", "10.0.0.3"]}
    handler = PacketHandler(intf, mac_map, ip_map)
    handler.start()

