---
content-type: "embed-endpoint"
endpoint: "sources"
key: "create-a-source"
version: "4"
order: 1


title: "Create a source"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  Creates a data source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed.

  The configuration process is unique for each type of source. Use the source's `report_card` object's `current_step` attribute to identify the current `step` in configuring the source.

  The `report_card` object's `current_step_hints` attribute will assist you in guiding the user to [Stitch.js](#stitch-js) to complete the current step.


arguments:
  - name: "display_name"
    required: true
    description: "A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into."

  - name: "properties"
    required: false
    description: "A source properties object corresponding to the value of `type`."

  - name: "type"
    required: true
    description: "The source type. For example: `platform.marketo` or `platform.hubspot`."


returns: "A source object with a `report_card` property, which contains the report card object for the source's configuration status."


examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                   "type":"platform.hubspot",
                   "display_name":"Hubspot",
                   "properties":{
                      "start_date":"2018-01-01 00:00:00",
                      "customFrequencyInMinutes":"360"
                   }
                }"
  # - type: "response"
  #   language: ""
  #   code: |

---