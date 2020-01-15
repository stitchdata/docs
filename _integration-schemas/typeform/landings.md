---
tap: "typeform"
version: "1"

name: "landings"
doc-link: "https://developer.typeform.com/responses/reference/retrieve-responses"
singer-schema: "https://github.com/singer-io/tap-typeform/blob/master/tap_typeform/schemas/landings.json"
description: |
  The `{{ table.name }}` table contains info about form landings. Depending on the [**Incremental Range**]() setting defined in the {{ app.page-names.int-settings }} page, data may be aggregated on a daily or hourly basis.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve responses"
    doc-link: "https://developer.typeform.com/responses/reference/retrieve-responses"

attributes:
  - name: "landing_id"
    type: "string"
    primary-key: true
    description: "The landing ID."
    foreign-key-id: "landing-id"

  - name: "submitted_at"
    type: "date-time"
    replication-key: true
    description: |
      The time that the form response was submitted in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} format, UTC time.

  - name: "browser"
    type: "string"
    description: "The browser used in the landing."
    
  - name: "hidden"
    type: "string"
    description: ""
    
  - name: "landed_at"
    type: "date-time"
    description: |
      The time of the form landing in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} format, UTC time.
    
  - name: "network_id"
    type: "string"
    description: "The IP address of the client."
    
  - name: "platform"
    type: "string"
    description: "The platform used in the landing, derived from `user_agent`."
    
  - name: "referer"
    type: "string"
    description: "If applicable, the referrer used in the landing."
    
  - name: "token"
    type: "string"
    description: ""
    
  - name: "user_agent"
    type: "string"
    description: "The user agent used in the landing."
---