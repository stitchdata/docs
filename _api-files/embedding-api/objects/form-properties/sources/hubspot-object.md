---
content-type: "embed-form"
form-type: "source"
key: "source-form-properties-hubspot-object"

title: "HubSpot"
description: "A Hubspot connection reads data from the Hubspot API and corresponds to the source type of `platform.hubspot`."

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    description: |
      Defines how often, in minutes, Stitch should attempt to replicate data from HubSpot. Accepted values are:

      - `1`
      - `10`
      - `30`
      - `60`
      - `360`
      - `720`
      - `1440`

  - name: "start_date"
    type: "string"
    description: "The date from which Stitch should begin replicating data from HubSpot. Data from this date forward will be replicated."

example: |
  {  
   "id":"<ID>",
   "type":"platform.hubspot",
   "properties":{  
      "frequency_in_minutes":"30",
      "start_date":"2018-01-10 00:00:00"
    }
  }
---