---
tap: "twilio"
version: "1"
key: ""

name: "usage_triggers"
doc-link: "https://www.twilio.com/docs/usage/api/usage-trigger#read-multiple-usagetrigger-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/usage_triggers.json
description: |
  The **{{ table.name }}** table returns list of usage triggers in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple UsageTrigger resources"
    doc-link: "https://www.twilio.com/docs/usage/api/usage-trigger?code-sample=code-read-multiple-usagetrigger-resources&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the UsageTrigger resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."  

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that the trigger monitors."

  - name: "api_version"
    type: "string"
    description: "The API version used to create the resource."

  - name: "callback_method"
    type: "string"
    description: "The HTTP method we use to call callback_url. Can be: GET or POST."

  - name: "callback_url"
    type: "string"
    description: "The URL we call using the callback_method when the trigger fires."

  - name: "current_value"
    type: "number"
    description: "The current value of the field the trigger is watching."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "date_fired"
    type: "date-time"
    description: "The date and time in GMT that the trigger was last fired specified in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "The string that you assigned to describe the trigger."

  - name: "recurring"
    type: "string"
    description: "The frequency of a recurring UsageTrigger. Can be: daily, monthly, or yearly for recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in GMT."

  - name: "trigger_by"
    type: "string"
    description: "The field in the UsageRecord resource that fires the trigger. Can be: count, usage, or price."

  - name: "trigger_value"
    type: "number"
    description: "The value at which the trigger will fire. Must be a positive, numeric value."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."

  - name: "usage_category"
    type: "string"
    description: "The usage category the trigger watches."

  - name: "usage_record_uri"
    type: "string"
    description: "The URI of the UsageRecord resource this trigger watches, relative to https://api.twilio.com."
---