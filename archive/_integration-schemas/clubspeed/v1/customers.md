---
tap: "clubspeed"
version: "1"

name: "customers"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers for a location.
  
  {% capture replication-note %}
  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means updated customer data will only be selected for replication when the `{{ replication-keys | strip }}` value for the customer's record is updated.
  {% endcapture %}

  {% include note.html type="single-line" content=replication-note %}

replication-method: "Key-based Incremental"

attributes:
  - name: "customerId"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "lastVisited"
    type: "date-time"
    replication-key: true
    description: "The date on which the customer last visited."

  - name: "Address"
    type: "string"
    description: "The first address line for the customer."

  - name: "Address2"
    type: "string"
    description: "The second address line for the customer."

  - name: "City"
    type: "string"
    description: "The city of residence for the customer."

  - name: "Country"
    type: "string"
    description: "The country of residence for the customer."

  - name: "Custom1"
    type: "string"
    description: "Custom data holder 1."

  - name: "Custom2"
    type: "string"
    description: "Custom data holder 2."

  - name: "Custom3"
    type: "string"
    description: "Custom data holder 3."

  - name: "Custom4"
    type: "string"
    description: "Custom data holder 4."

  - name: "LicenseNumber"
    type: "string"
    description: "The license number for the customer."

  - name: "State"
    type: "string"
    description: "The state of residence for the customer."

  - name: "Zip"
    type: "string"
    description: "The post code for the address of the customer."

  - name: "accountCreated"
    type: "date-time"
    description: "The timestamp when the customer record was created."

  - name: "birthdate"
    type: "date-time"
    description: "The customer's birth date."

  - name: "cardId"
    type: "integer"
    description: "The membership card number for the customer."

  - name: "company"
    type: "string"
    description: "The company of the customer."

  - name: "creditLimit"
    type: "number"
    description: "The credit limit for the customer."

  - name: "creditOnHold"
    type: "boolean"
    description: "Indicates whether the customer's credit is on hold."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the customer has been soft deleted."

  - name: "donotemail"
    type: "boolean"
    description: "Indicates whether the customer wishes to receive emails."

  - name: "email"
    type: "string"
    description: "The email addresss of the customer."

  - name: "fax"
    type: "string"
    description: "The fax number of the customer."

  - name: "firstname"
    type: "string"
    description: "The customer's first name."

  - name: "gender"
    type: "integer"
    description: |
      The customer's gender. Possible values are:

      - `0` - Other/Unspecified
      - `1` - Male
      - `2` - Female

  - name: "generalNotes"
    type: "string"
    description: "Any notes about the customer."

  - name: "howdidyouhearaboutus"
    type: "integer"
    description: "The ID of the source for the customer."
    foreign-key-id: "source-id"

  - name: "ignoreDOB"
    type: "boolean"
    description: "Indicates whether the customer's birth date can be ignored."

  - name: "isEmployee"
    type: "boolean"
    description: "Indicates if the customer is also an employee."

  - name: "isGiftCard"
    type: "boolean"
    description: "Indicates if the customer record should be considered a gift card."

  - name: "lastname"
    type: "string"
    description: "The customer's last name."

  - name: "memberShipTextLong"
    type: "string"
    description: "Description of the membership for the customer."

  - name: "membershipStatus"
    type: "integer"
    description: "The customer's membership status."

  - name: "membershipText"
    type: "string"
    description: "Abbreviation of the membership for the customer."

  - name: "mobilephone"
    type: "string"
    description: "The mobile phone for the customer."

  - name: "originalId"
    type: "integer"
    description: ""

  - name: "phoneNumber"
    type: "string"
    description: "The phone number for the customer."

  - name: "phoneNumber2"
    type: "string"
    description: "The alternate phone number for the customer."

  - name: "priceLevel"
    type: "integer"
    description: "The price level that this customer's membership type grants to the customer."

  - name: "privacy1"
    type: "boolean"
    description: "Indicates whether the name of the customer should be hidden from race results."

  - name: "proskill"
    type: "integer"
    description: "The current proskill for the customer."

  - name: "racername"
    type: "string"
    description: "The nickname for the customer."

  - name: "status1"
    type: "integer"
    description: |
      Indicates a specific status. This is customizable per venue to handle indicators such as Customer added from POS, Customer added from Online Event Registration, Customer signed secondary waiver, etc.

  - name: "status2"
    type: "integer"
    description: "See `status1`."

  - name: "status3"
    type: "integer"
    description: "See `status1`."

  - name: "status4"
    type: "integer"
    description: "See `status1`."

  - name: "totalRaces"
    type: "integer"
    description: "The total number of times this customer has raced."

  - name: "totalVisits"
    type: "integer"
    description: "The total number of times this customer has visited."

  - name: "waiver"
    type: "integer"
    description: "Indicates the primary waiver the customer has signed."

  - name: "waiver2"
    type: "integer"
    description: "Indicates the secondary waiver the customer has signed."

  - name: "webUserName"
    type: "string"
    description: ""
---