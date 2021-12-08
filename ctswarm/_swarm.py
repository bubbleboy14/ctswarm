import os
from cantools.web import respond, succeed, cgi_get
from ctswarm.util import snap, swap

def response():
	action = cgi_get("action")
	if action == "list":
		succeed(os.listdir("archive"))
	if action == "snap":
		succeed(snap())
	if action == "swap":
		swap(cgi_get("archive"))

respond(response)