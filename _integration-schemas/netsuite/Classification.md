---
tap: "netsuite"
version: "1.0"

name: "Classification"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/classification.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Classification.json"
description: |
  The `{{ table.name }}` table contains info about the classifications in your {{ integration.display_name }} account.

  As classifications inherit the permissions set on the parent record, the permissions required for the parent record are required to access classification data.

  For example: To get classification data for a location, the user must have the permission for accessing location data.

permission:
  tab: "Lists"
  name: "<Parent Record Permission>"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "classification-id"

  - name: "classTranslationList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "includeChildren"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""
---