---
tap: "pardot"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: "http://developer.pardot.com/kb/object-field-references/#campaign"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Query campaigns"
  doc-link: "http://developer.pardot.com/kb/api-version-3/campaigns/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "cost"
    type: "integer"
    description: "The cost associated to the campaign."
---