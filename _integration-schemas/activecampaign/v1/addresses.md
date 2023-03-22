---
tap: "activecampaign"
version: "1"
key: ""

name: "addresses"
doc-link: "https://developers.activecampaign.com/reference#address"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/addresses.json"
description: |
  The `{{ table.name }}` table contains information about addresses in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all addresses"
    doc-link: "https://developers.activecampaign.com/reference#list-all-addresses"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The address ID."
    foreign-key-id: "address-id"

  - name: "address1"
    type: "string"
    description: ""
  - name: "address2"
    type: "string"
    description: ""
  - name: "allgroup"
    type: "integer"
    description: ""
  - name: "city"
    type: "string"
    description: ""
  - name: "company_name"
    type: "string"
    description: ""
  - name: "country"
    type: "string"
    description: ""
  - name: "district"
    type: "string"
    description: ""
  
  - name: "is_default"
    type: "boolean"
    description: ""
  - name: "state"
    type: "string"
    description: ""
  - name: "zip"
    type: "string"
    description: ""
---
