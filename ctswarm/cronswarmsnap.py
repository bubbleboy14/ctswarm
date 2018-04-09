import os
from datetime import datetime
from cantools.web import respond
from cantools.util import log, cmd
from cantools import config

def response():
	log("cronswarm (snap)", important=True)
	if not os.path.exists("archive"):
		log("creating archive directory")
		os.mkdir("archive")
	cmd('cp data.db "%s"'%(os.path.join("archive",
		str(datetime.now()).rsplit(":", 1)[0]),))
	log("cronswarm (snap) complete")

respond(response)