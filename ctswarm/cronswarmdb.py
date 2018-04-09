from datetime import datetime, timedelta
from cantools.scripts.migrate import load
from cantools.web import respond
from cantools.util import log
from cantools import config
from model import *

def response():
	log("cronswarm (db)", important=True)
	cutoff = datetime.now() - timedelta(seconds=int(config.ctswarm.db.interval))
	if config.ctswarm.db.peers:
		for modname, schema in db.get_schema().items():
			if "modified" in schema:
				for (host, port) in map(lambda x : x.split(":"), config.ctswarm.db.peers.split("|")):
					load(host, port, db.session, {
						"modified": {
							"value": cutoff,
							"comparator": ">="
						}
					})
	log("cronswarm (db) complete")

respond(response)