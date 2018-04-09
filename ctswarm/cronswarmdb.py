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
			"value": datetime.now() - timedelta(seconds=config.ctswarm.db.interval),
			"comparator": ">="
		}
		for modname, schema in db.get_schema().items():
			filters = {}
			if "modified" in schema:
				filters["modified"] = cutoff
			elif "date" in schema:
				filters["date"] = cutoff
			else:
				continue
			for (host, port, protocol) in config.ctswarm.db.peers:
				load_model(modname, host, port, db.session, filters,
					protocol, config.cache("remote admin password? "), "edit")
	log("cronswarm (db) complete")

respond(response)