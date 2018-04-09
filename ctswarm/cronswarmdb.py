from datetime import datetime, timedelta
from cantools.scripts.migrate import load_model
from cantools.web import respond
from cantools.util import log
from cantools import config
from model import *

def response():
	log("cronswarm (db)", important=True)
	if config.ctswarm.db.peers:
		cutoff = {
			"value": datetime.now() - timedelta(seconds=int(config.ctswarm.db.interval)),
			"comparator": ">="
		}
		peers = map(lambda x : x.split(":"), config.ctswarm.db.peers.split("|"))
		for modname, schema in db.get_schema().items():
			filters = {}
			if "modified" in schema:
				filters["modified"] = cutoff
			elif "date" in schema:
				filters["date"] = cutoff
			else:
				continue
			for (host, port) in peers:
				load_model(modname, host, port, db.session, filters,
					config.cache("remote admin password? "))
	log("cronswarm (db) complete")

respond(response)