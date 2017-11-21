copies = {
	".": ["cron.yaml", "cronswarm.py", "cronbalance.py"]
}
cfg = {
    "peers": [],
    "interval": 5,
    "memcache": [],
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