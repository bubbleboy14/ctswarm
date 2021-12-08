syms = {
    ".": ["cronswarm.py", "cronswarmdb.py", "cronswarmup.py", "cronswarmsnap.py", "_swarm.py"],
    "js": ["swarm"],
    "html": ["swarm"]
}
routes = {
    "/_swarm": "_swarm.py"
}
cfg = {
    "db": {
        "peers": [],
        "interval": 120
    },
    "memcache": [],
    "monitor": [],
    "revolver": {
    	"port": 80,
    	"cfg": None,
    	"key": None,
    	"cert": None,
    	"verbose": False,
    	"redirect": False,
    	"sslredir": {
    		"port": 80,
    		"verbose": False,
    		"ssl_redirect": "auto"
    	}
    }
}
