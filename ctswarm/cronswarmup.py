from cantools.web import respond, fetch, mail
from cantools.util import log
from cantools import config

TMP = """Hi there!

Looks like these servers aren't running:

%s

Oops!
"""

def response():
	log("cronswarm (up)", important=True)
	down = []
	for addr in config.ctswarm.monitor.split("|"):
		proto = "http"
		host = addr
		port = 80
		if "://" in addr:
			proto, host = addr.split("://")
		if ":" in host:
			host, port = host.split(":")
		elif proto == "https":
			port = 443
		try:
			fetch(host, port=port, protocol=proto, fakeua=True)
		except:
			log("SERVER DOWN: %s"%(addr,))
			down.append(addr)
	if down:
		dz = "\r\n".join(down)
		for contact in config.admin.contacts:
			mail.send_mail(to=contact, subject="Server(s) Unreachable", body=TMP%(dz,))
	log("cronswarm (up) complete")

respond(response)