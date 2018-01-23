from dez.http.reverseproxy import startreverseproxy
from cantools.web import respond, post
from cantools.hooks import memhook
from cantools.util import log
from cantools import config

def memswarm(params):
	log("synchronizing memcache", important=True)
	params["nohook"] = True
	for peer in config.ctswarm.memcache.split("|"):
		host, port = peer.split(":")
		post(host, "/_memcache", port, params, ctjson=True)

def response():
	log("initializing cronswarm", important=True)
	cfg = config.ctswarm
	revolver = cfg.revolver
	if revolver.cfg:
		log("initializing load balancer with config: %s"%(revolver.cfg), 1)
		revolver.update("override_redirect", not revolver.redirect)
		startreverseproxy(revolver, False)
		if revolver.cert:
			log("starting SSL redirect (80->443)", 2)
			startreverseproxy(revolver.sslredir, False)
		log("load balancer initialized", 1)
	if cfg.memcache:
		log("initializing memswarm", 1)
		memhook.register(memswarm)
	log("cronswarm initialized")

respond(response)