---
tap: "twilio"
version: "1"
key: ""

name: "usage_records"
doc-link: "https://www.twilio.com/docs/usage/api/usage-record#read-multiple-usagerecord-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/usage_records.json
description: |
  The **{{ table.name }}** table returns a list of usage records in your {{ integration.display_name }} account.
  
replication-method: "Key-based Incremental"

api-method:
    name: "Usage Records"
    doc-link: "https://www.twilio.com/docs/usage/api/usage-record?code-sample=code-all-time-usage-all-usage-categories&code-language=curl&code-sdk-version=json"

attributes:
  - name: "account_sid"
    type: "string"
    primary-key: true
    description: "The SID of the Account that accrued the usage."

  - name: "category"
    type: "string"
    primary-key: true
    description: "The category of usage."  

  - name: "start_date"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as YYYY-MM-DD."  

  - name: "api_version"
    type: "string"
    description: "The API version used to create the resource."

  - name: "as_of"
    type: "date-time"
    description: "Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in GMT"

  - name: "count"
    type: "string, integer"
    description: "The number of usage events, such as the number of calls."

  - name: "count_unit"
    type: "string"
    description: "The units in which count is measured, such as calls for calls or messages for SMS."

  - name: "description"
    type: "string"
    description: "A plain-language description of the usage category."

  - name: "end_date"
    type: "date-time"
    description: "The last date for which usage is included in the UsageRecord. The date is specified in GMT and formatted as YYYY-MM-DD."

  - name: "price"
    type: "number"
    description: "The total price of the usage in the currency specified in price_unit and associated with the account."

  - name: "price_unit"
    type: "string"
    description: "The currency in which price is measured, in ISO 4127 format, such as usd, eur, and jpy."

  - name: "subresource_uris"
    type: "array"
    description: "A list of related resources identified by their URIs."
    subattributes:
    - name: "subresource"
      type: "string"
      description: ""

    - name: "uri"
      type: "string"
      description: ""

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."

  - name: "usage"
    type: "number, string"
    description: "The amount used to bill usage and measured in units described in usage_unit."

  - name: "usage_unit"
    type: "string"
    description: "The units in which usage is measured, such as minutes for calls or messages for SMS."
---