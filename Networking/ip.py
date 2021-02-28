#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import ipaddress

ip = ipaddress.IPv4Address("192.168.1.1")

print("Is global:", ip.is_global)

print("Is link-local:", ip.is_link_local)

# ip.is_reserved
# ip.is_multicast

print(ip + 1)

print(ip - 1)

network = ipaddress.IPv4Network("192.168.1.0/24")

print("Network mask:", network.netmask)

print("Broadcast address:", network.broadcast_address)

print("Number of hosts under", str(network), ":", network.num_addresses)

print("Hosts under", str(network), ":")
for host in network.hosts():
    print(host)

print("Subnets:")
for subnet in network.subnets(prefixlen_diff=2):
    print(subnet)

print("Supernet:", network.supernet(prefixlen_diff=1))

print("Overlaps 192.168.0.0/16:", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))

