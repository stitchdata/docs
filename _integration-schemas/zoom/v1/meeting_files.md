---
tap: "zoom"
version: "1"
key: ""

name: "meeting_files"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_files.json"
description: |
  The `{{ table.name }}` table contains information about files shared in-meeting in your {{ integration.display_name }} account. The files are deleted after 24 hours fo the meeting completion time.

replication-method: "Full Table"

api-method:
    name: "getMeetingFiles"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/listpastmeetingfiles"

attributes:
  - name: "meeting_uuid"
    type: "string"
    primary-key: true
    description: "The meeting UUID."
    foreign-key-id: "meeting-uuid"
  - name: "file_name"
    type: "string"
    primary-key: true
    description: "The name of the file."
    foreign-key-id: "meeting-files"
      
  - name: "download_url"
    type: "string"
    description: ""
  - name: "file_size"
    type: "integer"
    description: ""
---
