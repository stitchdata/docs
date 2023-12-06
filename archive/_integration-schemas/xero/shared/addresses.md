---
tap-reference: "xero"
version: "1"

name: "addresses"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/addresses.json
doc-link: https://developer.xero.com/documentation/api/types#Addresses

attributes:
  - name: "Region"
    type: "string"
    description: "The region associated with the address."

  - name: "AddressType"
    type: "string"
    description: |
      The address type. Possible values are:

      - `POBOX`
      - `STREET`
      - `DELIVERY` - **Note**: This address type is not valid for `contacts`.

  - name: "AddressLine1"
    type: "string"
    description: "The first line of the address."

  - name: "AddressLine2"
    type: "string"
    description: "The second line of the address."

  - name: "AddressLine3"
    type: "string"
    description: "The third line of the address."

  - name: "AddressLine4" 
    type: "string"
    description: "The fourth line of the address."

  - name: "AttentionTo" 
    type: "string"
    description: "The name of the addressee."

  - name: "City" 
    type: "string"
    description: "The city associated with the address."

  - name: "PostalCode" 
    type: "string"
    description: "The postal code associated with the address."

  - name: "Country"
    type: "string"
    description: "The country associated with the address."
---