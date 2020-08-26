---
tap: "zoom"
version: "1"
key: ""

name: "webinar_tracking_sources"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/gettrackingsources"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_tracking_sources.json"
description: |
  The `{{ table.name }}` lists all information about tracking sources in your {{ integration.display_name }} account. To retrieve this information you must have a webinar license, a **Rate Limit Label** value of `Medium`, and the following scopes: `webinar:read:admin`, `webinar:read`. Registration is also required for the webinar.

replication-method: "Full Table"

api-method:
    name: "getWebinarTrackingSources"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/gettrackingsources"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The tracking source ID."
    foreign-key-id: "tracking-source-id"

  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"

  - name: "registration_count"
    type: "integer"
    description: ""
  - name: "source_name"
    type: "string"
    description: ""
  - name: "tracking_url"
    type: "string"
    description: ""
  - name: "visitor_count"
    type: "integer"
    description: ""
---
