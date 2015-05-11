#!/usr/bin/env python3
# -*- coding: utf-8
#
#
# Create .json templates for every hospital based on their CMS ID.
#
# Run this script if there's an update to the data in 0-hospital-by-state
#
# Note, this is *exactly* the same public-domain data provided by CMS -- we're
# just splitting it up more cleanly, and adding some new blank fields to be filled in.
#
#
# Copyright (c) 2015 The Trustworthy Healthcare Initiative
#  https://TrustworthyHealthcare.org
#
# This software is released under the @@@ License:
#  @@@@@@@@@@
#
# Source: https://github.com/WhiteCoatAcademy/trustworthyhealthcare.org
#

import glob
import json
import os
import time
import us


OUTPUT_PATH = '1-hospital-by-cms-id'

# We want to be run from this path. Sorry :/
cms_data_by_state = 'raw-data/hospitals-by-state'
assert(os.path.isdir(cms_data_by_state))

# Grab  the .json files in cms_data_by_state
json_files_in_cms = glob.glob(cms_data_by_state + '/*.json')

state_abbreviations = set(list(map(lambda elt: elt.abbr, us.states.STATES_AND_TERRITORIES)))
observed_state_abbreviations = set(list(map(lambda elt: elt.rsplit('/')[-1][:2], json_files_in_cms)))

missing_states = state_abbreviations.symmetric_difference(observed_state_abbreviations)

# Missing territories from CMS
missing_from_cms = {'OL', 'DK', 'PI'}
if missing_states != missing_from_cms:
    print("Some territories and states might be missing: %s" % (missing_states))
    time.sleep(2)


###
# JSON Extra Parameters
###

# Mostly brainstorming here.
JSON_TEMPLATE = {
    # Raw, public, factual data.
    "network_info": {
        "websites": [],
        "as_numbers": [],
        "arin_handles": [],
        "netblock_ranges": []  # I imagine most will not have a full AS# assignment, but a smaller netblock
    },

    # Lots of hospitals are part of a parent org
    "parent_info": {
        "name": None,    # Parent name
        "websites": []  # Parent site(s)
    },

    # Data from SHODAN, etc.
    "raw_ratings": {},

    # Raw ratings, interpreted (e.g. 94%, "A", Great!)
    "numeric_ratings": {},

    # A global ranking (e.g. 7th in the US, 1st in Missouri!)
    "global_rank": {}
}

# Loop over all the JSONs and make (or update) existing .json items
seen_provider_ids = []

for filename in json_files_in_cms:
    with open(filename, 'r') as json_file:
        parsed_json = json.load(json_file)
        for item in parsed_json:
            output_filename = OUTPUT_PATH + '/' + item['provider_id'] + '.json'

            # Sanity check for duplicate provider IDs
            if item['provider_id'] in seen_provider_ids:
                raise ValueError
            seen_provider_ids.append(item['provider_id'])

            print('Working on provider: %s' % (item['provider_id']))

            json_to_write = JSON_TEMPLATE.copy()

            if os.path.isfile(output_filename):
                print('\tAlready exists. Updating.')
                with open(output_filename, 'r') as json_in:
                    existing_json_data = json.load(json_in)
                    json_to_write.update(existing_json_data)

            json_to_write.update(item)  # CMS is *always* right. Update from them.

            with open(output_filename, 'w') as json_out:
                json.dump(json_to_write, json_out, sort_keys=True, indent=4)
