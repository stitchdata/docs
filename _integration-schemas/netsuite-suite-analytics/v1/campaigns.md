---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaign.html"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your NetSuite account. Campaigns are used to manage marketing initiatives.

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the campaign was last modified."

  - name: "campaign_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The campaign ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "campaign-id"

  - name: "audience_id"
    type: "integer"
    description: "The audience associated with the campaign."
    foreign-key-id: "campaign-audience-id"

  - name: "campaign_extid"
    type: "integer"
    description: "The external ID of the campaign."

  - name: "category_id"
    type: "integer"
    description: "The campaign category associated with the campaign."
    foreign-key-id: "campaign-category-id"

  - name: "cost_0"
    type: "number"
    description: "The campaign cost."

  - name: "date_created"
    type: "date-time"
    description: "The date the campaign was created."

  - name: "end_date"
    type: "date-time"
    description: "The end date of the campaign."

  - name: "expectedrevenue"
    type: "number"
    description: "The expected revenue of the campaign."

  - name: "family_id"
    type: "integer"
    description: "The campaign family associated with the campaign."
    foreign-key-id: "campaign-family-id"

  - name: "is_inactive"
    type: "string"
    description: "Whether the campaign is inactive."

  - name: "is_sales_campaign"
    type: "string"
    description: "Whether the campaign is sales or marketing."

  - name: "keyword"
    type: "string"
    description: "The campaign keyword."

  - name: "last_modified_date"
    type: "date-time"
    description: "The date the campaign was last modified."

  - name: "message"
    type: "string"
    description: "The campaign message."

  - name: "number_0"
    type: "string"
    description: ""

  - name: "offer_id"
    type: "integer"
    description: "The offer associated with the campaign."
    foreign-key-id: "campaign-offer-id"

  - name: "organizer_id"
    type: "integer"
    description: "The organizer of the campaign."
    foreign-key-id: "entity-id"

  - name: "search_engine_id"
    type: "integer"
    description: "The search engine associated with the campaign."
    foreign-key-id: "search-engine-id"

  - name: "start_date"
    type: "date-time"
    description: "The start date of the campaign."

  - name: "time_zone_0"
    type: "string"
    description: "The time zone of the campaign."

  - name: "title"
    type: "string"
    description: "The title of the campaign."

  - name: "url"
    type: "string"
    description: "The URL of the campaign."

  - name: "vertical_id"
    type: "integer"
    description: "The vertical associated with the campaign."
    foreign-key-id: "campaign-vertical-id"
---