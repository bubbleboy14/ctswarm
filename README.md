# ctswarm
The aim of this plugin is to simplify the deployment and administration of cloud based web services, the magic of which chiefly consists of data synchronization and load balancing.

## synchronizer (cron @ cfg.ctswarm.interval)
 - fetch entities modded since last check
 - forward to cfg.ctswarm.peers
     - may be asymmetrical (e.g. for staging)
## revolver (drp-based load balancer!!!)
 - regular traffic is proxied as specified
 - media/big files are auto-302ed as necessary


# Back (Init Config)

    copies = {
    	".": ["cron.yaml", "cronswarm.py"]
    }
    cfg = {
        "peers": [],
        "interval": 5,
        "revolver": {
        	"port": 80,
        	"cfg": None,
        	"key": None,
        	"cert": None,
        	"verbose": False,
        	"redirect": True
        }
    }