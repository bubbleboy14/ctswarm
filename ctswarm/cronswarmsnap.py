from cantools.web import respond
from cantools.util import log
from cantools import config
from cronswarm.util import snap

def response():
	log("cronswarm (snap)", important=True)
	snap()
	log("cronswarm (snap) complete")

respond(response)