from datetime import datetime, timedelta
from dez.http.reverseproxy import startreverseproxy
from cantools.web import respond, getmem, setmem
from cantools.scripts.migrate import load
from cantools.util import log
from cantools import config
from model import *

def response():
	log("initiating cronswarm", important=True)
	cutoff = datetime.now() - timedelta(seconds=config.ctswarm.interval)
	swarmopts = getmem("swarm")
	if not swarmopts: # later check for specific things...
		log("first run! checking for load balancer configuration...")
		options = config.ctswarm.revolver
		if options.cfg:
			log("initializing load balancer with config: %s"%(options.cfg))
			options.update("override_redirect", not options.redirect)
			startreverseproxy(options)
			if options.cert:
				log("starting SSL redirect (80->443)")
				startreverseproxy(options.sslredir)
		setmem("swarm", {
			"proxying": True
		})
	for modname, schema in db.get_schema().items():
		if "modified" in schema:
			for (host, port) in config.ctswarm.peers.map(lambda x : x.split(".")):
				load(host, port, db.session, {
					"modified": {
						"value": cutoff,
						"comparator": ">="
					}
				})
	log("cronswarm complete")

respond(response)