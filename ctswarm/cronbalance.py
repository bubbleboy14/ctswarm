from dez.http.reverseproxy import startreverseproxy
from cantools.web import respond
from cantools.util import log
from cantools import config

def response():
	log("initiating cronbalance", important=True)
	log("checking for load balancer configuration...")
	options = config.ctswarm.revolver
	if options.cfg:
		log("initializing load balancer with config: %s"%(options.cfg))
		options.update("override_redirect", not options.redirect)
		startreverseproxy(options)
		if options.cert:
			log("starting SSL redirect (80->443)")
			startreverseproxy(options.sslredir)
	log("load balancer initialized")

respond(response)