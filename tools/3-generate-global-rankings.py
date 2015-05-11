#!/usr/bin/env python3
# -*- coding: utf-8
#
# Copyright (c) 2015 The Trustworthy Healthcare Initiative
#  https://TrustworthyHealthcare.org
#
# This software is released under the @@@ License:
#  @@@@@@@@@@
#
# Source: https://github.com/WhiteCoatAcademy/trustworthyhealthcare.org
#

import configparser
import pprint
import requests
# import simplejson
import socket
import subprocess
import urllib

_CONFIG = configparser.ConfigParser()
_CONFIG.read("secrets.cfg")

VIRUSTOTAL_API_KEY = _CONFIG.get('keys', 'virustotal')
SHODAN_API_KEY = _CONFIG.get('keys', 'shodan')


def establish_firewall():
    """
    This step establishes a firewall before any actions are taken.

    This firewall prevents us from sending a *single bit* of data to any
    healthcare provider.

    Where possible, prefer offline databases (e.g. scans.io). When using
    an API, make sure the API has a passive/cached-only mode (e.g. VirusTotal,
    which sends *no* data, just checks its own database.)

    To that end, only use *GET* API calls (not POST).

    """

    # WARNING: The use of sudo w/ shell=True is bad practice here. :/

    # Check we have sudo, and iptables has no outbound rules
    assert("2" == subprocess.check_output("sudo iptables -L OUTPUT | wc -l", shell=True, universal_newlines=True).strip())

    #####
    # Define whitelisted IPs
    #####

    # What's Virustotal's IP?
    virustotal_db = socket.gethostbyname('www.virustotal.com')  # Also their API endpoint
    shodan_db = socket.getbyhostname('api.shodan.io')

    whitelisted_ips = [virustotal_db, shodan_db]
    ####

    # Don't allow any outbound traffic
    # Non-zero return codes cause check_output to throw CalledProcessError (uncaught)
    print('Dropping all outbound internet traffic.')
    subprocess.check_output("sudo iptables --policy OUTPUT DROP", shell=True)

    # Whitelist APIs that only look at cached/stored datasets
    for ip in whitelisted_ips:
        print("\t Whitelisting %s" % (ip))
        subprocess.check_output("sudo iptables -A OUTPUT -d %s -j ACCEPT" % (ip), shell=True)


def test_firewall():
    """
    Check if our firewall really works.
    """
    print('Testing firewall sanity.')

    test_sites = ['https://www.google.com/', 'http://en.wikipedia.org', 'https://www.eff.org/', 'http://18.181.0.29']

    # Getting all these sites should fail
    for site in test_sites:
        try:
            print('\tTesting: %s' % (site))
            urllib.request.urlopen(site, timeout=2)
            assert(False)  # Still here? Exit - the firewall failed
        except urllib.error.URLError:
            pass

    print('Firewall working.')


def teardown_firewall():
    """
    Turn off the firewall (re-enable the internet) when we're done.
    """
    print('Turning the internet back on.')
    subprocess.check_output("sudo iptables --policy OUTPUT ACCEPT", shell=True)



def virustotal_url():
    """
    Get malware info on a specific URL. Probably not very useful - *maybe* on TLD.
    """
    assert(False)  # Disabled, since this is useless.

    api_endpoint = "https://www.virustotal.com/vtapi/v2/url/report"

    payload = {"resource": "http://www.google.com", "apikey": VIRUSTOTAL_API_KEY}
    # This does post, but it's really just a database lookup.
    r = requests.post(api_endpoint, data=payload)

    print(r.text)


def virustotal_domains():
    """
    Poll VirusTotal's free, public database about domains.

    Importantly, VirusTotal calls to this service do *NOT* result in any outgoing data on their end.

    This simply looks up the domain status in their database of malware, passive DNS, etc.
    """
    api_endpoint = "https://www.virustotal.com/vtapi/v2/domain/report"

    params = {"domain": "google.com", "apikey": VIRUSTOTAL_API_KEY}
    r = requests.get(api_endpoint, params=params)

    pprint.pprint(r.text)


def virustotal_ips():
    """
    Get malware info about an IP, including passive DNS.
    """
    api_endpoint = "https://www.virustotal.com/vtapi/v2/ip-address/report"

    params = {"ip": "8.8.8.8", "apikey": VIRUSTOTAL_API_KEY}
    r = requests.get(api_endpoint, params=params)

    print(r.text)


def shodan_ips():
    """
    Get Shodan info about an IP, including product fingerprinting, TLS data, etc.
    """
    ip = "8.8.8.8"

    api_endpoint = "https://api.shodan.io/shodan/host/%s" % (ip)
    print(api_endpoint)
    params = {"key": SHODAN_API_KEY}
    print(params)
    r = requests.get(api_endpoint, params=params)
    print(r.url)

    print(r.text)


def validate_hospital_list():
    """
    """
    pass

def parse_dns_info():
    """
    Via RAPID7's DNS database.
    """



def main():
    # Let's set up a firewall ASAP
    establish_firewall()

    # Test the firewall (and exit if it's not working)
    test_firewall()

    virustotal_domains()
    shodan_ips()

    teardown_firewall()


if __name__ == "__main__":
    main()
