---
tap: "twilio"
version: "1"
key: ""

name: "available_phone_number_countries"
doc-link: "https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#read-a-list-of-countries"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/available_phone_number_countries.json
description: |
  The **{{ table.name }}** table returns a list of countries that have phone numbers to purchase for your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Read a list of countries"
    doc-link: "https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource?code-sample=code-read-a-list-of-countries&code-language=curl&code-sdk-version=json"

attributes:
  - name: "country_code"
    type: "string"
    primary-key: true
    description: "The ISO-3166-1 country code of the country."

  - name: "beta"
    type: "boolean"
    description: "Whether all phone numbers available in the country are new to the Twilio platform. true if they are and false if all numbers are not in the Twilio Phone Number Beta program."

  - name: "country"
    type: "string"
    description: "The name of the country."

  - name: "subresource_uris"
    type: "array"
    description: "A list of related AvailablePhoneNumber resources identified by their URIs relative to https://api.twilio.com"
    subattributes:
    - name: "subresource"
      type: "string"
      description: "Subresource type"

    - name: "uri"
      type: "string"
      description: "URI for the subresource, relative to https://api.twilio.com"

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com"
---
