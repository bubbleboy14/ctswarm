import os
from datetime import datetime
from cantools.util import log, cmd, read, indir

def snap():
	log("attempting snap", important=True)
	if not os.path.exists("archive"):
		log("creating archive directory")
		os.mkdir("archive")
	data = read("data.db", binary=True)
	match = indir(data, "archive")
	if match:
		log("matching archive: %s - aborting snap"%(match,))
		return match
	aname = str(datetime.now()).rsplit(":", 1)[0].replace(" ", "_")
	cmd('cp data.db "%s"'%(os.path.join("archive", aname),))
	return aname

def swap(archname):
	snap()
	cmd('cp "%s" data.db'%(os.path.join("archive", archname),))