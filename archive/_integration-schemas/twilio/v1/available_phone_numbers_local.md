---
tap: "twilio"
version: "1"
key: ""

name: "available_phone_numbers_local"
doc-link: "https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource#read-multiple-availablephonenumberlocal-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/available_phone_numbers_local.json
description: |
  The **{{ table.name }}** table returns a list of available phone numbers for local resources for your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Read multiple AvailablePhoneNumberLocal resources"
    doc-link: "https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource#read-multiple-availablephonenumberlocal-resources"

attributes:
  - name: "iso_country"
    type: "string"
    primary-key: true
    description: "The ISO country code of this phone number."

  - name: "phone_number"
    type: "string"
    primary-key: true
    description: "The phone number in E.164 format, which consists of a + followed by the country code and subscriber number."

  - name: "address_requirements"
    type: "string"
    description: "The type of Address resource the phone number requires. Can be: none, any, local, or foreign. none means no address is required. any means an address is required, but it can be anywhere in the world. local means an address in the phone number's country is required. foreign means an address outside of the phone number's country is required."

  - name: "beta"
    type: "boolean"
    description: "Whether the phone number is new to the Twilio platform. Can be: true or false."

  - name: "capabilities"
    type: "object"
    description: "The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities are: Voice, SMS, and MMS and each capability can be: true or false."
    subattributes:
    - name: "voice"
      type: "boolean"
      description: ""

    - name: "SMS"
      type: "boolean"
      description: ""

    - name: "MMS"
      type: "boolean"
      description: ""

    - name: "fax"
      type: "boolean"
      description: ""

  - name: "friendly_name"
    type: "string"
    description: "A formatted version of the phone number."

  - name: "lata"
    type: "string"
    description: "The LATA of this phone number. Available for only phone numbers from the US and Canada."

  - name: "latitude"
    type: "string"
    description: "The longitude of this phone number's location. Available for only phone numbers from the US and Canada."

  - name: "locality"
    type: "string"
    description: "The locality or city of this phone number's location."

  - name: "longitude"
    type: "string"
    description: "The longitude of this phone number's location. Available for only phone numbers from the US and Canada."

  - name: "postal_code"
    type: "string"
    description: "The postal or ZIP code of this phone number's location. Available for only phone numbers from the US and Canada."

  - name: "rate_center"
    type: "string"
    description: "The rate center of this phone number. Available for only phone numbers from the US and Canada."

  - name: "region"
    type: "string"
    description: "The two-letter state or province abbreviation of this phone number's location. Available for only phone numbers from the US and Canada."
---