import ipaddress
import sys

excl=sys.argv[1]

all_ipv6 = ipaddress.ip_network("::/0")
all_ipv4 = ipaddress.ip_network('0.0.0.0/0')
excluded_ipv4 = ipaddress.ip_network(excl)
result = list(all_ipv4.address_exclude(excluded_ipv4))
result.insert(0, all_ipv6)
print(",".join([str(ip) for ip in result]))


