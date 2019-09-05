---
tap: "pipedrive"
version: "1.0"
key: "delete-log"

name: "delete_log"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/delete_log.json"
description: |
  The `{{ table.name }}` table contains a list of record IDs that have been deleted from {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "Get recent deletes"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the deleted record."
---