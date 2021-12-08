swarm.snap.Snapper = CT.Class({
	CLASSNAME: "swarm.snap.Snapper",
	_: {
		s: function(cb, action, opts) {
			CT.net.post({
				path: "/_swarm",
				params: CT.merge({
					action: action || "list",
				}, opts),
				cb: cb
			});
		}
	},
	snap: function(s) {
		var _ = this._;
		return CT.dom.link(s, function() {
			_.s(function() {
				alert("you did it!");
			}, "swap", {
				archive: s
			});
		}, null, "block");
	},
	snapper: function() {
		var _ = this._, refresh = this.refresh;
		_.s(function(aname) {
			if (_.snaps.includes(aname))
				return alert("current snapshot already saved as " + aname);
			_.snaps.push(aname);
			refresh();
		}, "snap");
	},
	refresh: function(snaps) {
		this._.snaps = snaps;
		CT.dom.setMain([
			CT.dom.button("snap", this.snapper, "right"),
			CT.dom.div("your archives", "big centered"),
			snaps.length ? snaps.map(this.snap) : "no snapshots yet!"
		]);
	},
	init: function() {
		this._.s(this.refresh);
	}
});