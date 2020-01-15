---
tap: "netsuite"
version: "1.0"

name: "Nexus"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/nexus.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Nexus.json"
description: |
  The `{{ table.name }}` table contains info about the tax jurisdictions - or nexus - in your {{ integration.display_name }} account. A nexus is a tax jurisdiction, usually defined at the country level. 

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "nexus"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "nexus-id"

  - name: "country"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parentNexus"
    type: "varies"
    description: ""

  - name: "state"
    type: "varies"
    description: ""

  - name: "taxAgency"
    type: "varies"
    description: ""

  - name: "taxAgencyPst"
    type: "varies"
    description: ""

  - name: "taxCode"
    type: "varies"
    description: ""
---