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

####################################################################
# Set up Mininet and Controller
####################################################################

SCRIPTS = ../scripts

export MN_STRATUM_IMG = opennetworking/mn-stratum:latest
export ONOS_IMAGE = onosproject/onos:latest

export name ?=

.PHONY: mininet controller cli netcfg host

help:
	@echo "Example usage:"
	@echo "  sudo make mininet           Start Mininet"
	@echo "  sudo make controller        Start ONOS Controller"
	@echo "  sudo make cli               Access Controller CLI (password: rocks)"
	@echo "  sudo make netcfg            Connect Controller to Mininet"
	@echo "  sudo make host name=h1      Access Mininet Host"

mininet:
	$(SCRIPTS)/mn-stratum

controller:
	ONOS_APPS=gui,proxyarp,drivers.bmv2,lldpprovider,hostprovider \
	$(SCRIPTS)/onos

cli:
	$(SCRIPTS)/onos-cli

netcfg:
	$(SCRIPTS)/onos-netcfg cfg/netcfg.json

# Usage: make host name=h1
host:
	$(SCRIPTS)/utils/mn-stratum/exec $(name)
