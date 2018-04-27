---
tap: "jira"
version: "1.0"

name: "resolutions"
doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/resolution-getResolutions
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/resolutions.json
description: |
  The `resolutions` table contains info about the resolutions in your JIRA account.

replication-method: "Full Table"

api-method:
  name: getResolutions
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/resolution-getResolutions

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the resolution."

  - name: "self"
    type: "string"
    description: "The URL associated with the resolution."

  - name: "description"
    type: "string"
    description: "The description of the resolution."

  - name: "iconUrl"
    type: "string"
    description: "The URL of the icon associated with the resolution."

  - name: "name"
    type: "string"
    description: "The name of the resolution."

---