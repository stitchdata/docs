---
content-type: "embed-form"
form-type: "source"
key: "source-form-properties-marketo-object"

title: "Marketo"
description: "A Marketo connection reads data from the Marketo API and corresponds to the source type of `platform.marketo`."

object-attributes:
  - name: "client_id"
    type: "string"
    description: "The user's Marketo client ID."

  - name: "client_secret"
    type: "string"
    description: "The user's Marketo client secret."

  - name: "frequency_in_minutes"
    type: "string"
    description: |
      Defines how often, in minutes, Stitch should attempt to replicate data from Marketo. Accepted values are:

      - `1`
      - `10`
      - `30`
      - `60`
      - `360`
      - `720`
      - `1440`

  - name: "endpoint"
    type: "string"
    description: "The user's Marketo REST endpoint URL. For example: `https://457-RFG-234.mktorest.com/rest`"

  - name: "identity"
    type: "string"
    description: "The user's Marketo REST identity URL. For example: `https://457-RFG-234.mktorest.com/identity`"

  - name: "max_daily_calls"
    type: "string"
    description: "The maximum number of daily API calls that Stitch may make to the Marketo API."

  - name: "start_date"
    type: "string"
    description: |
      The date from which Stitch should begin replicating data from HubSpot. Data from this date forward will be replicated.

      Data in this field must adhere to the `YYYY-MM-DDTHH:MM:SSZ` format. For example: `2018-01-01T11:59:59Z`

example: |
  {  
   "id":"<ID>",
   "type":"platform.marketo",
   "properties":{
      "client_id":"<CLIENT_ID>",
      "client_secret":"<CLIENT_SECRET>",
      "frequency_in_minutes":"1440",
      "endpoint":"https://457-RFG-234.mktorest.com/rest",
      "identity":"https://457-RFG-234.mktorest.com/identity",
      "max_daily_calls":"8,000",
      "start_date":"2018-01-10T00:00:00Z"
    }
  }
---