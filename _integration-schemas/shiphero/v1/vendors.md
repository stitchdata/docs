---
tap: "shiphero"
version: "1.0"

name: "vendors"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-shiphero/blob/master/tap_shiphero/schemas/vendors.json"
description: |
  The `{{ table.name }}` table contains info about the vendors in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
    name: "List vendors"
    doc-link: "https://shipheropublic.docs.apiary.io/#reference/vendors/list-vendors/list-vendors"

attributes:
  - name: "vendor_id"
    type: "integer"
    primary-key: true
    description: "The vendor ID."
    foreign-key-id: "vendor-id"

  - name: "email"
    type: "string"
    description: "The vendor email."

  - name: "name"
    type: "string"
    description: "The vendor name."
---