import ipaddress
import sys

excl=sys.argv[1]

n1 = ipaddress.ip_network('0.0.0.0/0')
n2 = ipaddress.ip_network(excl)
res = list(n1.address_exclude(n2))
print(",".join([str(ip) for ip in res]))