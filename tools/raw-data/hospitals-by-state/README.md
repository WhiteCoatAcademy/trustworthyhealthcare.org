# Hospital Data

These are public domain data from the public CMS database at: http://dev.socrata.com/foundry/#/data.medicare.gov/xubh-q36u

A list of all Hospitals that have been registered with Medicare. The list includes addresses, phone numbers, and hospital type.

* Total Rows: 4,783
* Source Domain: data.medicare.gov
* Created: 5/14/2014, 8:51:24 AM
* Last Updated: 12/17/2014, 11:08:41 AM
* Category: Hospital Compare
* Owner: cms


Quickly verify these all exist, via: 

```
$ grep provider_id *.json | wc -l
4783 <--  Matches metadata provided at CMS site.
```
