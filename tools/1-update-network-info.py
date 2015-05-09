#!/usr/bin/env python3
#
# Update .json templates with some factual metadata (ARIN WHOIS, etc.)
#
# Specifically, We try to complete the network_info section of the .json files.
#

import glob
import json
import os

# TODO: Modularize this shared code?
provider_by_cms_id = '1-hospital-by-cms-id'
assert(os.path.isdir(provider_by_cms_id))

json_files = glob.glob(provider_by_cms_id + '/*.json')

for filename in json_files:
    with open(filename, 'r') as json_file:
        parsed_json = json.load(json_file)

        # parsed_json is a dictionary of the file
        network_info = parsed_json['network_info']

        # This checks if a website is in the network_info, and prints out the first one
        if len(network_info['websites']) > 0:
            print(parsed_json['network_info']['websites'][0])


        # If you wanted to update the json, you could do this:
        json_to_write = parsed_json.copy()  # Let's get a copy to mess around with

        # Add a 'lolcats' string under network info & set to kittens
        json_to_write['network_info']['lolcats'] = 'Kittens'


        # Now, if you want to write out the file, you'd do this:
        with open(filename, 'w') as json_out:
            # reset to the original .json by CDing to the directory and running `git checkout *.json`
            json.dump(json_to_write, json_out, sort_keys=True, indent=4)
