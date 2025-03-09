from datetime import datetime, timedelta
from cantools.scripts.migrate import load_model, blobificator
from cantools.web import respond, post
from cantools.util import log
from cantools import config
from model import *

dbcfg = config.ctswarm.db

def modsche(snames):
	return list(map(lambda n : (n, db.get_schema(n)), snames))

def flfilt(schemas, rmlist):
	return list(filter(lambda i : i[0] not in rmlist, schemas))

if dbcfg.tables:
	schemas = modsche(dbcfg.tables)
else:
	schemas = modsche(db.get_schema().keys())
	if dbcfg.firsts:
		schemas = modsche(dbcfg.firsts) + flfilt(schemas, dbcfg.firsts)
	if dbcfg.lasts:
		schemas = flfilt(schemas, dbcfg.lasts) + modsche(dbcfg.lasts)
	if dbcfg.besides:
		schemas = flfilt(schemas, dbcfg.besides)
blobifier = blobificator(config.web.host, config.web.port, dbcfg.self)

def response():
	if not dbcfg.peers:
		return log("cronswarm (db) aborted - no peers")
	dbcfg.update("backlog", dbcfg.get("backlog", 0) + int(dbcfg.interval))
	log("cronswarm (db) @ %s"%(dbcfg.backlog,), important=True)
	pw = config.cache("remote admin password? ")
	delivered = 0
	cutoff = {
		"value": datetime.now() - timedelta(seconds=dbcfg.backlog),
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
			delivered += load_model(modname, host, port, None,
				filters, protocol, pw, "edits", blobifier)
	if delivered:
		log("delivered %s updates - clearing peer memcaches"%(delivered,))
		for (host, port, protocol) in dbcfg.peers:
			post(host, "/_memcache", port, {
				"pw": pw,
				"action": "clear"
			}, protocol=protocol)
	dbcfg.update("backlog", 0)
	log("cronswarm (db) complete")

respond(response)