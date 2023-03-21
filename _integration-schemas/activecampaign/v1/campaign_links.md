---
tap: "activecampaign"
version: "0.4"
key: ""

name: "campaign_links"
doc-link: "https://developers.activecampaign.com/reference#test-1"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/campaign_links.json"
description: |
  The `{{ table.name }}` table contains information about the links attached to your campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve links associated to campaign"
    doc-link: "https://developers.activecampaign.com/reference#retrieve-links-associated-campaign"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign link ID."
    #foreign-key-id: "campaign-link-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the campaign link was last updated."
    replication-key: true

  - name: "campaign"
    type: "integer"
    description: ""
  - name: "campaignid"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  
  - name: "link"
    type: "string"
    description: ""
  - name: "linkclicks"
    type: "integer"
    description: ""
  - name: "message"
    type: "string"
    description: ""
  - name: "messageid"
    type: "integer"
    description: "The message ID."
    foreign-key-id: "message-id"
  - name: "name"
    type: "string"
    description: ""
  - name: "ref"
    type: "string"
    description: ""
  - name: "tracked"
    type: "integer"
    description: ""
  - name: "uniquelinkclicks"
    type: "integer"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
---
