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

from scapy.all import IP, TCP, Raw, send, sniff, sr1, random
import sys
import threading
import time

SEND_PACKET_SIZE = 1000  # should be less than max packet size of 1500 bytes

# A client class for implementing TCP's three-way-handshake connection
# establishment and closing protocol, along with data transmission.


class Client3WH:

    def __init__(self, dip, dport):
        """Initializing variables"""
        self.dip = dip
        self.dport = dport
        # selecting a source port at random
        self.sport = random.randrange(0, 2**16)

        self.next_seq = 0                       # TCP's next sequence number
        self.next_ack = 0                       # TCP's next acknowledgement number

        self.ip = IP(dst=self.dip)              # IP header

        self.connected = False
        self.timeout = 3

    def _start_sniffer(self):
        t = threading.Thread(target=self._sniffer)
        t.start()

    def _filter(self, pkt):
        if (IP in pkt) and (TCP in pkt):  # capture only IP and TCP packets
            return True
        return False

    def _sniffer(self):
        while self.connected:
            sniff(prn=lambda x: self._handle_packet(
                x), lfilter=lambda x: self._filter(x), count=1, timeout=self.timeout)

    def _handle_packet(self, pkt):
        """TODO(1): Handle incoming packets from the server and acknowledge them accordingly. Here are some pointers on
           what you need to do:
           1. If the incoming packet has data (or payload), send an acknowledgement (TCP) packet with correct 
              `sequence` and `acknowledgement` numbers.
           2. If the incoming packet is a FIN (or FINACK) packet, send an appropriate acknowledgement or FINACK packet
              to the server with correct `sequence` and `acknowledgement` numbers.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        if pkt[TCP].dport != self.sport or pkt[TCP].sport != self.dport:
            return
        
        if Raw in pkt:
            payload_len = len(pkt[Raw].load)
            self.next_ack = pkt[TCP].seq + payload_len
            
            ack_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                    seq=self.next_seq, ack=self.next_ack,
                                    flags='A')
            send(ack_pkt, verbose=0)
        
        elif pkt[TCP].flags & 0x01:  # FIN flag
            self.next_ack = pkt[TCP].seq + 1
            
            finack_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                       seq=self.next_seq, ack=self.next_ack,
                                       flags='FA')
            send(finack_pkt, verbose=0)
            self.next_seq += 1
        ### END: ADD YOUR CODE HERE ... #####

    def connect(self):
        """TODO(2): Implement TCP's three-way-handshake protocol for establishing a connection. Here are some
           pointers on what you need to do:
           1. Handle SYN -> SYNACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        self.next_seq = random.randint(0, 2**32 - 1) 
        syn_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                seq=self.next_seq, flags='S')
        send(syn_pkt, verbose=0)
        self.next_seq += 1  
        
        synack_pkt = sniff(filter="tcp", count=1, timeout=self.timeout)
        
        if synack_pkt and len(synack_pkt) > 0 and synack_pkt[0].haslayer(TCP) and synack_pkt[0][TCP].flags & 0x12:  # SYN-ACK
            self.next_ack = synack_pkt[0][TCP].seq + 1
            
            ack_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                    seq=self.next_seq, ack=self.next_ack,
                                    flags='A')
            send(ack_pkt, verbose=0)
        else:
            print("Connection failed: No SYNACK received")
            return
        ### END: ADD YOUR CODE HERE ... #####

        self.connected = True
        self._start_sniffer()
        print('Connection Established')

    def close(self):
        """TODO(3): Implement TCP's three-way-handshake protocol for closing a connection. Here are some
           pointers on what you need to do:
           1. Handle FIN -> FINACK -> ACK packets.
           2. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###
        fin_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                seq=self.next_seq, ack=self.next_ack,
                                flags='FA')
        send(fin_pkt, verbose=0)
        self.next_seq += 1 
        
        time.sleep(0.5)  
        
        
        ### END: ADD YOUR CODE HERE ... #####

        self.connected = False
        print('Connection Closed')

    def send(self, payload):
        """TODO(4): Create and send TCP's data packets for sharing the given message (or file):
           1. Make sure to update the `sequence` and `acknowledgement` numbers correctly, along with the 
              TCP `flags`.
        """

        ### BEGIN: ADD YOUR CODE HERE ... ###

        data_pkt = self.ip / TCP(sport=self.sport, dport=self.dport,
                                 seq=self.next_seq, ack=self.next_ack,
                                 flags='PA') / Raw(load=payload)
        
        send(data_pkt, verbose=0)
        

        self.next_seq += len(payload)
        
        time.sleep(0.1) 
        ### END: ADD YOUR CODE HERE ... #####


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: ./client-3wh.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    client = Client3WH(server_ip, server_port)
    client.connect()

    message = sys.stdin.read(SEND_PACKET_SIZE)
    while message:
        client.send(message)
        message = sys.stdin.read(SEND_PACKET_SIZE)

    client.close()


if __name__ == "__main__":
    main()
