# Tools to generate THI rankings

Our goal is to rank and analyze every healthcare institution without sending *any data* whatsoever to a given site.

## The First Rule

We rank sites without sending *any* data to healthcare providers. Not a single packet. We'll accomplish this by using only well-described, public databases of internet scans (see below).

To really reinforce this point -- and because healthcare providers & universities tend take a "shoot the messenger" approach -- we'll establish firewalls blocking access to every healthcare IP during report generation.

(TODO: Consider just having this work purely offline.)


## Workflow and Directories

1. Get raw data from CMS listing all hospitals (public domain), stored in `0-hospital-by-state`
2. Split to one .json per CMS-id, with original fields & stubs for rankings in `1-hospital-by-cms-id`
3. Run ranking code to update each individual json (still in `1-hospital-by-cms-id`)

We store one .json per CMS ID for easier git commit tracking & diffs. Might also make sense for front-end rendering.


## Raw Datasets
* CMS database of all healthcare providers (by name, zip, geolocation)
* SHODAN -- we have API bits here
* University of Michigan's https://scans.io/
* Google Malware Database?


## Other Great APIs

We'll hold off on using these for now. We can reconstruct Security Headers from SHODAN (awesome!). Same for startls.info. 

* SSL Labs: https://github.com/ssllabs/ssllabs-scan
* Security Headers: https://securityheaders.com/
* https://starttls.info/

## Other options?
* EFF SSL Observatory (is this deprecated?)
* Google's SSL API (deprecated? scans has this, too)