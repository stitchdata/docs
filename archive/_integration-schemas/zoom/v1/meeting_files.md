---
tap: "zoom"
version: "1"
key: "meeting-file"

name: "meeting_files"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/listpastmeetingfiles"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_files.json"
description: |
  The `{{ table.name }}` table contains information about files shared during meetings in your {{ integration.display_name }} account. **Note**:{{ integration.display_name }} deletes these files 24 hours after completion of the meeting.

replication-method: "Full Table"

api-method:
  name: "Get meeting files"
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
      
  - name: "download_url"
    type: "string"
    description: ""

  - name: "file_size"
    type: "integer"
    description: ""
---