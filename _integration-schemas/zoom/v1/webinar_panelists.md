---
tap: "zoom"
version: "1"
key: ""

name: "webinar_panelists"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpanelists"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_panelists.json"
description: ""

replication-method: "Full Table"

api-method:
    name: "getWebinarPanelists"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpanelists"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The panelist ID."
    foreign-key-id: "panelist-id"

  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"

  - name: "email"
    type: "string"
    description: ""
  - name: "join_url"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  
---
