# Just a simple comment here
# update to force commit
import dns
import socket
import dns.resolver

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('amazon.com')

print(addr1, addr2)

domain='microsoft.com'
for x in dns.resolver.query(domain,'MX'):
 print(x.to_text())
