from datetime import datetime, timedelta
from cantools.scripts.migrate import load
from cantools.web import respond
from cantools.util import log
from cantools import config
from model import *

def response():
	log("cronswarm (db)", important=True)
	cutoff = datetime.now() - timedelta(seconds=config.ctswarm.db.interval)
	if config.ctswarm.db.peers:
		for modname, schema in db.get_schema().items():
			if "modified" in schema:
				for (host, port) in config.ctswarm.db.peers.split("|").map(lambda x : x.split(":")):
					load(host, port, db.session, {
						"modified": {
							"value": cutoff,
							"comparator": ">="
						}
					})
	log("cronswarm (db) complete")

respond(response)