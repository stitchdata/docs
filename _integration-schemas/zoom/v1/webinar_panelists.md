---
tap: "zoom"
version: "1"
key: "webinar-panelist"

name: "webinar_panelists"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpanelists"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_panelists.json"
description: |
  The `{{ table.name }}` table contains information about your {{ integration.display_name}} webinar panelists. 

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, a Pro plan or higher with with the webinar add-on enabled is required to retrieve this data.

replication-method: "Full Table"

api-method:
  name: "Get webinar panelists"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpanelists"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The panelist ID."
    # foreign-key-id: "panelist-id"

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