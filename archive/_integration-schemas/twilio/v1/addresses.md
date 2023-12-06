---
tap: "twilio"
version: "1"
key: ""

name: "addresses"
doc-link: "https://www.twilio.com/docs/usage/api/address#read-multiple-address-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/addresses.json
description: |
  The **{{ table.name }}** table returns a list of address resource representations, each representing an address within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Address resources"
    doc-link: "https://www.twilio.com/docs/usage/api/address?code-sample=code-show-all-addresses&code-language=curl&code-sdk-version=json"


attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the Address resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."  

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that is responsible for the Address resource"

  - name: "city"
    type: "string"
    description: "The city in which the address is located."

  - name: "customer_name"
    type: "string"
    description: "The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte characters."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "emergency_enabled"
    type: "boolean"
    description: "Whether emergency calling has been enabled on this number."

  - name: "friendly_name"
    type: "string"
    description: "The string that you assigned to describe the resource."

  - name: "iso_country"
    type: "string"
    description: "The ISO country code of the address."

  - name: "postal_code"
    type: "string"
    description: "The postal code of the address."

  - name: "region"
    type: "string"
    description: "The state or region of the address."

  - name: "street"
    type: "string"
    description: "The number and street address of the address."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com"

  - name: "validated"
    type: "boolean"
    description: "Whether the address has been validated to comply with local regulation. In countries that require valid addresses, an invalid address will not be accepted. true indicates the Address has been validated. false indicate the country doesn't require validation or the Address is not valid."

  - name: "verified"
    type: "boolean"
    description: "Whether the address has been verified to comply with regulation. In countries that require valid addresses, an invalid address will not be accepted. true indicates the Address has been verified. false indicate the country doesn't require verified or the Address is not valid."
---