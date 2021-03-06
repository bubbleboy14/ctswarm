# ctswarm
The aim of this plugin is to simplify the deployment and administration of cloud based web services, the magic of which chiefly consists of monitoring, data synchronization, load balancing, and automated archival.

## monitor
 - ping peers (cfg.ctswarm.monitor[])
 - email admin on failure
## synchronizers
 - db (cron @ cfg.ctswarm.db.interval)
   - fetch entities modded since last check
   - forward to cfg.ctswarm.db.peers[]
     - may be asymmetrical (e.g. for staging)
 - memcache
   - propagate updates to peers (cfg.ctswarm.memcache[]) instantly (via hook)
## revolver (drp-based load balancer!!!)
 - regular traffic is proxied as specified
 - media/big files are auto-302ed as necessary
## snapper
 - back up / archive data.db

# Back (Init Config)

    syms = {
        ".": ["cronswarm.py", "cronswarmdb.py", "cronswarmup.py", "cronswarmsnap.py"]
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
    