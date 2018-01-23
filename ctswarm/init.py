copies = {
	".": ["cron.yaml"]
}
syms = {
    ".": ["cronswarm.py", "cronswarmdb.py", "cronswarmup.py"]
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
    	"redirect": True,
    	"sslredir": {
    		"port": 80,
    		"verbose": False,
    		"ssl_redirect": "auto"
    	}
    }
}