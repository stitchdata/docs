---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "audit-trail"

name: "audit_trail"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/audit_trail.json"
description: |
  This table contains information about activities that have been performed in the Mambu Core Banking system.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get a list of events"
  doc-link: "https://support.mambu.com/docs/audit-trail"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "event_source"
    type: "string"
    description: "The category of the event: `API` or `UI`."

  - name: "request_uri"
    type: "string"
    description: "The part of the request's URL after the base URL and up to the query string."

  - name: "request_method"
    type: "string"
    description: "The HTTP request method."

  - name: "request_payload"
    type: "string"
    description: "The raw request data as a string, with sensitive information removed."

  - name: "user_agent"
    type: "string"
    description: "The value of HTTP user agent header."

  - name: "resource"
    type: "string"
    description: "The resource on which the event occurred."

  - name: "resource_fragment"
    type: "string"
    description: "The request URI or raw URL hash."

  - name: "username"
    type: "string"
    description: "The user who carried out the action or the name of the API consumer."

  - name: "client_ip"
    type: "string"
    description: "The IP address from the HTTP request or the `X_FORWARDED_FOR` header."

  - name: "response_code"
    type: "number"
    description: "The HTTP response code."


  - name: "occurred_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the event occurred."

  - name: "response_payload"
    type: "string"
    description: "The raw response payload with sensitive information removed."
---