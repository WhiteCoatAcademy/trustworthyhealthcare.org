#!/bin/bash

# This is the super neat Medicare API, via Socrata
# It's open / public domain! :)
#
# See: http://dev.socrata.com/foundry/#/data.medicare.gov/xubh-q36u

states_and_territories=('AL' 'AK' 'AZ' 'AR' 'CA' 'CO' 'CT' 'DE' 'DC' 'FL' 'GA' 'HI' 'ID' 'IL' 'IN' 'IA' 'KS' 'KY' 'LA' 'ME' 'MD' 'MA' 'MI' 'MN' 'MS' 'MO' 'MT' 'NE' 'NV' 'NH' 'NJ' 'NM' 'NY' 'NC' 'ND' 'OH' 'OK' 'OR' 'PA' 'RI' 'SC' 'SD' 'TN' 'TX' 'UT' 'VT' 'VA' 'WA' 'WV' 'WI' 'WY' 'AS' 'GU' 'MP' 'PR' 'VI')


# Add your API token here.
# This works without, but might truncate / throttle stuff.
# Yes, I know I'm committing this to a git repo. It's a free/public api.
app_token="aH1sk7hLaispfL5CPp1ezghkE"

# https://soda.demo.socrata.com/resource/4tka-6guv?$$app_token=APP_TOKEN
for state in "${states_and_territories[@]}"
do
    echo "Working on: ${state}"
    echo ${grabUrl}
    # NOTE: There are lots of awesome filters via the CMS data source.
    # We can filter by city, zip, hospital ownership, location region, etc.
    curl "https://data.medicare.gov/resource/xubh-q36u.json?\$\$app_token=${app_token}&state=${state}" -o "${state}.json"
    sleep 3
done
