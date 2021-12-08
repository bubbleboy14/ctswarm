CT.require("CT.all");
CT.require("core");
CT.require("swarm.snap");

CT.onload(function() {
	CT.initCore();
	new swarm.snap.Snapper();
});