---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "destinations"
key: "list-destinations"
version: "3"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List destinations"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.list.short }}"
description: "{{ api.core-objects.destinations.list.description | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array (of length zero or one) of [Destination objects]({{ api.core-objects.destinations.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json" 
  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1
      
      [
        {  
          "id":"<DESTINATION_ID>",
          "type":"redshift",
          "created_at":"2018-02-06T15:36:36Z",
          "updated_at":"2018-02-06T15:36:36Z",
          "connection": {  
              "host":"<HOST>",
              "port":5439,
              "username":"<USERNAME>",
              "database":"<DATABASE>",
              "password":"<PASSWORD>",
              "ssl":false
          },
          "last_check":{
            "error": false,
            "started_at":"2018-02-06T16:15:19Z",
            "completed_at":"2018-02-06T16:16:21Z"
          }
        }
      ]
---

