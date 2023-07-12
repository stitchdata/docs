---
tap: "zoom"
version: "1"
key: "webinar-file"

name: "webinar_files"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_files.json"
description: |
  The `{{ table.name }}` table contains information about files shared in-meeting in your {{ integration.display_name }} account. 

  **Note**: {{ integration.display_name }} deletes these files 24 hours after completion of the webinar.

replication-method: "Full Table"

api-method:
  name: "Get webinar files"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarfiles"

attributes:
  - name: "webinar_uuid"
    type: "string"
    primary-key: true
    description: "The webinar UUID."
    foreign-key-id: "webinar-uuid"

  - name: "file_name"
    type: "string"
    primary-key: true
    description: "The name of the file shared during the webinar."

  - name: "download_url"
    type: "string"
    description: ""

  - name: "file_size"
    type: "integer"
    description: ""
---