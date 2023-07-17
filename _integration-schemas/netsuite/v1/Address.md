---
tap: "netsuite"
version: "1"

name: "Address"
doc-link: ""
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Address.json"
description: |
  The `{{ table.name }}` table contains info about the custom address forms in your {{ integration.display_name }} account.

  Custom address forms can apply to entity, transaction, subsidiary, company information, location, and workplace records in {{ integration.display_name }}. As custom address forms inherit the permissions set on the parent record, the permissions required for the parent record are required to access custom address data.

  For example: To get custom address data for a location, the user must have the permission for accessing location data.

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "address"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "address-id"

  - name: "addr1"
    type: "string"
    description: ""

  - name: "addr2"
    type: "string"
    description: ""

  - name: "addr3"
    type: "string"
    description: ""

  - name: "addrPhone"
    type: "string"
    description: ""

  - name: "addrText"
    type: "string"
    description: ""

  - name: "addressee"
    type: "string"
    description: ""

  - name: "attention"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "override"
    type: "boolean, string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---