from datetime import datetime, timedelta
from cantools.scripts.migrate import load_model
from cantools.web import respond
from cantools.util import log
from cantools import config
from model import *

dbcfg = config.ctswarm.db

def modsche(snames):
	return list(map(lambda n : (n, db.get_schema(n)), snames))

def flfilt(schemas, rmlist):
	return list(filter(lambda i : i[0] not in rmlist, schemas))

if dbcfg.tables:
	schemas = modsche(dcfg.tables)
else:
	schemas = modsche(db.get_schema().keys())
	if dbcfg.firsts:
		schemas = modsche(dbcfg.firsts) + flfilt(schemas, dbcfg.firsts)
	if dbcfg.lasts:
		schemas = flfilt(schemas, dbcfg.lasts) + modsche(dbcfg.lasts)
	if dbcfg.besides:
		schemas = flfilt(schemas, dbcfg.besides)

def response():
	log("cronswarm (db)", important=True)
	if dbcfg.peers:
		cutoff = {
			"value": datetime.now() - timedelta(seconds=dbcfg.interval),
			"comparator": ">="
		}
		for modname, schema in schemas:
			filters = {}
			if "modified" in schema:
				filters["modified"] = cutoff
			elif "date" in schema:
				filters["date"] = cutoff
			else:
				continue
			for (host, port, protocol) in dbcfg.peers:
				load_model(modname, host, port, db.session, filters,
					protocol, config.cache("remote admin password? "), "edit")
	log("cronswarm (db) complete")

respond(response)