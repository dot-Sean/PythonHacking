import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
import urllib2

print(urllib2.urlopen("http://www.wtfismyip.com").read())
