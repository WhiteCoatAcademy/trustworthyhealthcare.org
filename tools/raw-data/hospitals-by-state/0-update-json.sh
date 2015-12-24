#!/bin/bash
# This script downloads .jsons of hospitals by state, via CMS.
#
# This is the super neat Medicare API, via Socrata: It's open / public domain! :)
#
# Latest: https://dev.socrata.com/foundry/#/data.medicare.gov/rbry-mqwu
#
# Stats:
#  Total Rows: 4,805
#  Source Domain: data.medicare.gov
#  Created: 3/20/2015, 11:02:57 PM
#  Last Updated: 12/9/2015, 6:36:05 PM

states_and_territories=('AL' 'AK' 'AZ' 'AR' 'CA' 'CO' 'CT' 'DE' 'DC' 'FL' 'GA' 'HI' 'ID' 'IL' 'IN' 'IA' 'KS' 'KY' 'LA' 'ME' 'MD' 'MA' 'MI' 'MN' 'MS' 'MO' 'MT' 'NE' 'NV' 'NH' 'NJ' 'NM' 'NY' 'NC' 'ND' 'OH' 'OK' 'OR' 'PA' 'RI' 'SC' 'SD' 'TN' 'TX' 'UT' 'VT' 'VA' 'WA' 'WV' 'WI' 'WY' 'AS' 'GU' 'MP' 'PR' 'VI')


## Add your API token here.
# This works without, but might truncate / throttle stuff.
# (Yes, I know I'm committing this to a git repo. It's a free/public api.)
app_token="aH1sk7hLaispfL5CPp1ezghkE"


# https://soda.demo.socrata.com/resource/4tka-6guv?$$app_token=APP_TOKEN
for state in "${states_and_territories[@]}"
do
    echo "Working on: ${state}"
    echo ${grabUrl}
    # NOTE: There are lots of awesome filters via the CMS data source.
    # We can filter by city, zip, hospital ownership, location region, etc.
    curl "https://data.medicare.gov/resource/rbry-mqwu.json?\$\$app_token=${app_token}&state=${state}" -o "${state}.json"
    sleep 3
done
