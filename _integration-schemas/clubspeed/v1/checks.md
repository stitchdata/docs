---
tap: "clubspeed"
version: "1"

name: "checks"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/checks.json"
description: |
  The `{{ table.name }}` table contains info about checks, or financial invoices, that have been closed.
  
  {% capture replication-note %}
  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means that checks will not be selected for replication until the record has a `{{ replication-keys | strip }}` value, which should occur when the check has a `status` of `closed`.
  {% endcapture %}

  {% include note.html type="single-line" content=replication-note %}

replication-method: "Key-based Incremental"

attributes:
  - name: "checkId"
    type: "integer"
    primary-key: true
    description: "The check ID."
    foreign-key-id: "check-id"
  
  - name: "closedDate"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the check was closed."
    
  - name: "broker"
    type: "string"
    description: "The name of the check broker."

  - name: "customerId"
    type: "integer"
    description: "The ID of the customer for the check."
    foreign-key-id: "customer-id"

  - name: "discount"
    type: "number"
    description: "The discount applied to the entire check."

  - name: "discountId"
    type: "integer"
    description: "The ID of the discount applied to the check."
    foreign-key-id: "discount-id"

  - name: "discountNotes"
    type: "string"
    description: "Notes about the discount applied to the check."

  - name: "discountUserId"
    type: "integer"
    description: "The ID of the user who applied the discount."
    foreign-key-id: "user-id"

  - name: "fee"
    type: "number"
    description: "The additional fee to be applied to the entire check."

  - name: "gratuity"
    type: "number"
    description: "The gratuity to be applied to the whole check."

  - name: "invoiceDate"
    type: "date-time"
    description: "The timestamp on which the invoice was handled."

  - name: "isTaxExempt"
    type: "boolean"
    description: "Indicates if the entire check is exempt from taxation."

  - name: "name"
    type: "string"
    description: "The name of the check."

  - name: "notes"
    type: "string"
    description: "Any notes about the check."

  - name: "openedDate"
    type: "date-time"
    description: "The timestamp on which the check was opened."

  - name: "status"
    type: "integer"
    description: |
      The status of the check. Possible values are:

      - `0` - Open
      - `1` - Closed

  - name: "total"
    type: "number"
    description: "The applied total for the check. This includes all underlying check details, taxes, discounts, fees, and gratuity."

  - name: "type"
    type: "integer"
    description: |
      The type of the check. Possible values are:

      - `1` - Regular
      - `2` - Event

  - name: "userId"
    type: "integer"
    description: "The ID of the user who created the check."
    foreign-key-id: "user-id"
---