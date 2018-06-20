import dns
from dns import resolver

fqdn="www.dropbox.com"
r=resolver.Resolver
a= r.query(fqdn,"A")
ns= r.query(fqdn,"NS")
cname= r.query(fqdn,"CNAME")

for i in a:
    print (i)

for i in ns:
    print(i)

for i in cname:
    print(i)

