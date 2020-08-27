---
tap: "zoom"
version: "1"
key: "webinar-tracking-source"

name: "webinar_tracking_sources"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/gettrackingsources"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_tracking_sources.json"
description: |
  The `{{ table.name }}` lists all information about tracking sources in your {{ integration.display_name }} account. Only webinars where registration is required will be included in this table.

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, the following requirements must be met to retrieve this data:

  - A {{ integration.display_name }} [webinar license](https://zoom.us/webinar){:target="new"}
  - An authentication app with the `webinar:read:admin` and `webinar:read` scopes

replication-method: "Full Table"

api-method:
  name: "Get webinar tracking sources"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/gettrackingsources"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The tracking source ID."
    # foreign-key-id: "tracking-source-id"

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