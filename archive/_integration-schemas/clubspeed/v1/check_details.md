---
tap: "clubspeed"
version: "1"

name: "check_details"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/check_details.json"
description: |
  The `{{ table.name }}` table contains info about line items and quantity info attached to [`checks`](#checks).

  {% capture replication-tip %}
  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means that check details will be selected for replication only when they are initially created. Any subsequent updates made to the check detail will not be detected, as the `{{ replication-keys | strip }}` value will not be updated. Refer to the [Key-based Incremental Replication documentation]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) for more info and examples.
  {% endcapture %}

  {% include note.html type="single-line" content=replication-tip %}

replication-method: "Key-based Incremental"

attributes:
  - name: "checkDetailId"
    type: "integer"
    primary-key: true
    description: "The check detail ID."
    foreign-key-id: "check-detail-id"

  - name: "createdDate"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the check detail was created."

  - name: "calculateType"
    type: "integer"
    description: "The type of application for an applied discount."

  - name: "checkId"
    type: "integer"
    description: "The ID of the parent check for the check detail."
    foreign-key-id: "checks"

  - name: "discountApplied"
    type: "number"
    description: "The amount of the discount applied to the check detail."

  - name: "discountDesc"
    type: "string"
    description: "The description of the applied discount."

  - name: "discountId"
    type: "integer"
    description: "The ID of the applied discount."
    foreign-key-id: "discount-id"

  - name: "discountNotes"
    type: "string"
    description: "Notes about the discount application."

  - name: "discountUserId"
    type: "integer"
    description: "The ID of the user who applied the discount."
    foreign-key-id: "user-id"

  - name: "g_CustId"
    type: "integer"
    description: "The ID of the customer on which to apply points on purchase. **Note**: This may reference a gift card."
    foreign-key-id: "customer-id"

  - name: "g_Points"
    type: "number"
    description: "The amount of money to be given to the customer (`g_CustId`) at purchase or check finalization."

  - name: "gst"
    type: "number"
    description: "The percent of the tax to be applied as GST."

  - name: "m_DaysAdded"
    type: "integer"
    description: ""

  - name: "p_CustId"
    type: "integer"
    description: "The ID of the customer on which to apply points on purchase."
    foreign-key-id: "customer-id"

  - name: "p_Points"
    type: "integer"
    description: "The number of points to be applied on purchase."

  - name: "productId"
    type: "integer"
    description: "The ID of the product on the check detail."
    foreign-key-id: "product-id"

  - name: "productName"
    type: "string"
    description: "The name of the product on the check detail."

  - name: "qty"
    type: "integer"
    description: "The quantity of the product on the check detail."

  - name: "r_Points"
    type: "integer"
    description: "The number of reservation points to be applied on purchase."

  - name: "s_CustId"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "s_NoOfLapsOrSeconds"
    type: "integer"
    description: ""

  - name: "s_SaleBy"
    type: "integer"
    description: ""

  - name: "s_Vol"
    type: "integer"
    description: ""

  - name: "status"
    type: "integer"
    description: |
      The status of the check detail. Possible values are:

      - `1` (New)
      - `2` (Voided)
      - `3` (Permanent)

  - name: "taxId"
    type: "integer"
    description: "The ID of the tax to be applied to the check detail."
    foreign-key-id: "tax-id"

  - name: "taxPercent"
    type: "number"
    description: "The percent of tax to be applied."

  - name: "type"
    type: "integer"
    description: |
      The type of the product. Possible values are:

      - `1` - Regular
      - `2` - Point
      - `3` - Food
      - `4` - Reservation
      - `5` - GameCard
      - `6` - Membership
      - `7` - Gift Card
      - `8` - Entitle

  - name: "unitPrice"
    type: "number"
    description: "The unit price of the product."

  - name: "unitPrice2"
    type: "number"
    description: "The unit price of the product."

  - name: "voidNotes"
    type: "string"
    description: "Notes added while voiding the check detail."
---