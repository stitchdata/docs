---
tap: "activecampaign"
version: "0.4"
key: ""

name: "contact_deals"
doc-link: "https://developers.activecampaign.com/reference#secondary-contacts"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_deals.json"
description: |
  The `{{ table.name }}` contains information about secondary contacts associated with a deal in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all secondary contacts"
    doc-link: "https://developers.activecampaign.com/reference#list-all-secondary-contacts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The secondary contact ID."
    #foreign-key-id: "contact-deal-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the secondary contact was last updated."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "deal"
    type: "integer"
    description: "The deal ID."
    foreign-key-id: "deal-id"
  
  - name: "role"
    type: "string"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""

---
