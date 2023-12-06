---
tap-reference: "xero"
version: "1"

name: "phones"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/phones.json

attributes:
  - name: "PhoneNumber"
    type: "string"
    description: "The phone number."

  - name: "PhoneAreaCode"
    type: "string"
    description: "The area code associated with the phone number."

  - name: "PhoneCountryCode"
    type: "string"
    description: "The country code associated with the phone number."

  - name: "PhoneType"
    type: "string"
    description: |
      The type of phone number. Possible values are:

      - `DEFAULT`
      - `DDI`
      - `MOBILE`
      - `FAX`
---