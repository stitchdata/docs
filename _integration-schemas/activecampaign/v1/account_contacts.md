---
tap: "activecampaign"
version: "0.4"
key: ""

name: "account_contacts"
doc-link: "https://developers.activecampaign.com/reference#account-contacts"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/account_contacts.json"
description: |
  The `{{ table.name }}` table contains information about contacts in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all associations"
    doc-link: "https://developers.activecampaign.com/reference#list-all-associations-1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The account contact ID."
    #foreign-key-id: "account-contact-id"
  
  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the contact was last updated."
    replication-key: true

  - name: "account"
    type: "integer"
    description: "The account ID."
    foreign-key-id: "account-id"
  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
    
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  
  - name: "job_title"
    type: "string"
    description: ""
---
