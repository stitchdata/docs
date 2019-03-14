---
tap: "shopify"
version: "1.0"

name: "orders"
doc-link: "https://help.shopify.com/en/api/reference/orders"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains info about a shop's completed orders.

  #### Order metafield data

  To replicate order metafield data, you must set this table and the [`metafields`](#metafields) table to replicate.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of orders"
    doc-link: "https://help.shopify.com/en/api/reference/orders/order#index"

attributes:
  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "id"
    type: "integer"
    primary-key: true
    description: "The order ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","order" | replace: "[ACTION]","last updated" }}

  - name: "app_id"
    type: "integer"
    description: "The ID of the app that created the order."

  - name: "billing_address"
    type: "object"
    description: "Details about the mailing address associated with the payment method. This address is an optional field that won't be available on orders that don't require a payment method."
    object-type: "billing address"
    subattributes: &address-fields
      - name: "address1"
        type: "string"
        description: "The street address of the {{ attribute.object-type }}."

      - name: "address2"
        type: "string"
        description: "An optional additional field for the street address of the of the {{ attribute.object-type }}."

      - name: "city"
        type: "string"
        description: "The city, town or village of the {{ attribute.object-type }}."

      - name: "company"
        type: "string"
        description: "The company of the person associated with the {{ attribute.object-type }}."

      - name: "country"
        type: "string"
        description: "The name of the country of the {{ attribute.object-type }}."

      - name: "country_code"
        type: "string"
        description: &country-code
          The two-letter [ISO 3166-1 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"} for the country of the {{ attribute.object-type }}.

      - name: "first_name"
        type: "string"
        description: "The first name of the person associated with the payment method."

      - name: "last_name"
        type: "string"
        description: "The last name of the person associated with the payment method."

      - name: "latitude"
        type: "number"
        description: "The latitude of the {{ attribute.object-type }}."

      - name: "longitude"
        type: "number"
        description: "The longitude of the {{ attribute.object-type }}."

      - name: "name"
        type: "string"
        description: "The full name of the person associated with the payment method."

      - name: "phone"
        type: "string"
        description: "The phone number at the {{ attribute.object-type }}."

      - name: "province"
        type: "string"
        description: "The name of the region of the {{ attribute.object-type }}."

      - name: "province_code"
        type: "string"
        description: "The two-letter of the region of the {{ attribute.object-type }}."

      - name: "zip"
        type: "string"
        description: "The postal code of the {{ attribute.object-type }}."

  - name: "browser_ip"
    type: "string"
    description: "The IP address of the browser used by the customer when they placed the order."

  - name: "buyer_accepts_marketing"
    type: "boolean"
    description: "Indicates whether the customer consented to receive email updates from the shop."

  - name: "cancel_reason"
    type: "string"
    description: |
      The reason why the order was canceled. Possible values are:

      - `customer` - The customer canceled the order.
      - `fraud` - The order was fraudulent.
      - `inventory` - Items in the order weren't in inventory.
      - `declined` - The payment was declined.
      - `other` - A reason not in this list.

  - name: "cancelled_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","order" | replace: "[ACTION]","cancelled" }}

  - name: "cart_token"
    type: "string"
    description: "The ID for the cart associated with the order."

  - name: "checkout_id"
    type: "integer"
    description: "The checkout ID associated with the order."

  - name: "checkout_token"
    type: "string"
    description: "The checkout token associated with the order."

  - name: "client_details"
    type: "object"
    description: "Details about the browser the customer used when the order was placed."
    subattributes:
      - name: "accept_language"
        type: "string"
        description: "The languages and locales that the browser understands."

      - name: "browser_height"
        type: "integer"
        description: "The browser's screen height in pixels."

      - name: "browser_ip"
        type: "string"
        description: "The browser's IP address."

      - name: "browser_width"
        type: "integer"
        description: "The browser's screen width in pixels."

      - name: "session_hash"
        type: "string"
        description: "A hash of the session."

      - name: "user_agent"
        type: "string"
        description: "Details of the browsing client, including software and operating versions."

  - name: "closed_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","order" | replace: "[ACTION]","closed" }}

  - name: "confirmed"
    type: "boolean"
    description: "Indicates if the order has been confirmed."

  - name: "contact_email"
    type: "string"
    description: "The contact email associated with the order."

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","order" | replace: "[ACTION]","created" }}

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} code for the currency used for the payment.

  - name: "customer"
    type: "object"
    description: "Details about the customer associated with the abandoned checkout."
    object-properties:
      - name: "accepts_marketing"
        type: "boolean"
        description: "Indicates the customer has consented to receive marketing material via email."

      # - name: "admin_graphql_api_id"
      #   type: "string"
      #   description: ""

      - name: "created_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","customer" | replace: "[ACTION]","created" }}

      - name: "default_address"
        type: "object"
        description: "Details about the customer's default address."
        object-properties:
          - name: "address1"
            type: "string"
            description: "The street address of the customer's address."

          - name: "address2"
            type: "string"
            description: "An optional field for the street address of the customer's address."

          - name: "city"
            type: "string"
            description: "The city of the customer's address."

          - name: "company"
            type: "string"
            description: "The company of the person associated with the customer's address."

          - name: "country"
            type: "string"
            description: "The name of the country of the customer's address."

          - name: "country_code"
            type: "string"
            description: |
              The two letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"}) format for the country of the customer's address.

          - name: "country_name"
            type: "string"
            description: "The customer's normalized country name."

          - name: "customer_id"
            type: "integer"
            description: "The customer's ID."
            foreign-key-id: "customer-id"

          - name: "default"
            type: "boolean"
            description: "Indicates if this is the customer's default address."

          - name: "first_name"
            type: "string"
            description: "The first name of the customer."

          - name: "id"
            type: "integer"
            description: "The address ID."

          - name: "last_name"
            type: "string"
            description: "The last name of the customer."

          - name: "name"
            type: "string"
            description: "The customer's first and last name."

          - name: "phone"
            type: "string"
            description: "The customer's phone number at this address."

          - name: "province"
            type: "string"
            description: "The customer's region name."

          - name: "province_code"
            type: "string"
            description: "The two-letter province code for the customer's region."

          - name: "zip"
            type: "string"
            description: "The customer's postal or zip code."

      - name: "email"
        type: "string"
        description: "The customer's email address."

      - name: "first_name"
        type: "string"
        description: "The first name of the customer."

      - name: "id"
        type: "integer"
        description: "The customer ID."
        foreign-key-id: "customer-id"

      - name: "last_name"
        type: "string"
        description: "The last name of the customer."

      - name: "last_order_id"
        type: "integer"
        description: "The ID of the customer's last order."
        foreign-key-id: "order-id"

      - name: "last_order_name"
        type: "string"
        description: |
          The name of the customer's last order. This is related to the `name` field in the [`orders` table](#orders).

      - name: "multipass_identifier"
        type: "string"
        description: "The customer's Multipass login ID."

      - name: "note"
        type: "string"
        description: "A note about the customer."

      - name: "orders_count"
        type: "integer"
        description: "The number of orders associated with the customer."

      - name: "phone"
        type: "string"
        description: |
          The phone number for the customer, in [E.164 format](https://en.wikipedia.org/wiki/E.164){:target="new"}.

      - name: "state"
        type: "string"
        description: |
          The state of the customer's account with a shop. Possible values are:

          - `disabled` - The customer doesn't have an active account.
          - `invited` - The customer has received an email invite to create an account.
          - `enabled` - The customer has created an account.
          - `declined` - The customer has declined the eamil invite to create an account.

      - name: "tags"
        type: "string"
        description: "Tags that the shop owner has attached to the customer."

      - name: "tax_exempt"
        type: "boolean"
        description: |
          Indicates if the customer is exempt from paying taxes on their order. If `true`, taxes will not be applied to an order at checkout.

      - name: "total_spent"
        type: "string"
        description: "The total amount of money that the customer has spent across their order history."

      - name: "updated_at"
        type: "date-time"
        description: "The last time the customer was updated."

      - name: "verified_email"
        type: "boolean"
        description: "Indicates if the customer has verified their email address."

  - name: "customer_locale"
    type: "string"
    description: "The two or three-letter language code, optionally followed by a region modifier."

  - name: "device_id"
    type: "integer"
    description: "The ID of the Shopify POS device that created the order."

  - name: "discount_applications"
    type: "array"
    description: "Details about the discount applications associated with the order."
    subattributes:
      - name: "allocation_method"
        type: "string"
        description: "The method used to allocate the discount application."

      - name: "code"
        type: "string"
        description: "The discount code."

      - name: "description"
        type: "string"
        description: "A description of the discount."

      - name: "target_selection"
        type: "string"
        description: |
          Indicates how a discount selects line items in the cart to be discounted. Possible values are:

          - `all` - The discount applies to all line items.
          - `entitled` - The discount applies to a particular subset of line items, often defined by a condition.
          - `explicit` - The discount applies to a specifically selected line item or shipping line.

      - name: "target_type"
        type: "string"
        description: |
          Indicates the type of item that a discount applies to. Possible values are:

          - `line_item`
          - `shipping_line`

      - name: "title"
        type: "string"
        description: "The customer-facing name of the discount."

      - name: "type"
        type: "string"
        description: |
          The type of the discount. Possible values are:

          - `automatic`
          - `discount_code`
          - `manual`
          - `script`

      - name: "value"
        type: "number"
        description: "The value of the discount. This value is in the customer's local (presentment) currency."

      - name: "value_type"
        type: "string"
        description: |
          The value type of the discount. Possible values are:

          - `fixed_amount`
          - `percentage`

  - name: "discount_codes"
    type: "array"
    description: "The discount codees applied to the checkout."
    subattributes:
      - name: "amount"
        type: "number"
        description: "The amount of the discount."

      - name: "code"
        type: "string"
        description: "The discount code."

      - name: "type"
        type: "string"
        description: |
          The type of discount. Possible values are:

          - `percentage`
          - `shipping`
          - `fixed_amount`

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "financial_status"
    type: "string"
    description: |
      The order's financial status. Possible falues are:

      - `authorized`
      - `pending`
      - `paid`
      - `partially_paid`
      - `refunded`
      - `voided`
      - `partially_refunded`
      - `unpaid`

  - name: "fulfillment_status"
    type: "string"
    description: |
      The order's fulfillment status. Possible values are:

      - `shipped`
      - `partial`
      - `unshipped`

  - name: "fulfillments"
    type: "array"
    description: "Details about the fulfillments associated with the order."
    subattributes:
      # - name: "admin_graphql_api_id"
      #   type: "string"
      #   description: ""

      - name: "id"
        type: "integer"
        primary-key: true
        description: "The fulfillment ID."

      - name: "created_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","fulfillment" | replace: "[ACTION]","created" }}

      - name: "line_items"
        type: "array"
        description: "Details about the line items associated with the fulfillment."
        subattributes: &line-items
          # - name: "admin_graphql_api_id"
          #   type: "string"
          #   description: ""

          - name: "applied_discount"
            type: "integer"
            description: "The discount applied to the line item, if applicable."

          - name: "compare_at_price"
            type: "string"
            description: "The line item's _compare at_ price."

          - name: "destination_location"
            type: "object"
            description: "Details about the line item's destination location."
            subattributes: &default-address-fields
              - name: "address1"
                type: "string"
                description: "The street address."

              - name: "address2"
                type: "string"
                description: "An optional second address line."

              - name: "city"
                type: "string"
                description: "The city."

              - name: "country_code"
                type: "string"
                description: |
                  The two letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"}) format for the country.

              - name: "id"
                type: "integer"
                description: "The address ID."

              - name: "name"
                type: "string"
                description: "The first and last name of the person associated with the address."

              - name: "province_code"
                type: "string"
                description: "The two-letter province code for the region associated with the address."

              - name: "zip"
                type: "string"
                description: "The postal or zip code associated with the address."

          - name: "destination_location_id"
            type: "integer"
            description: "The ID of the destination location."

          - name: "discount_allocations"
            type: "array"
            description: "An ordered list of amounts allocated by discount applications. Each discount allocation is associated to a particular appliction."
            subattributes: &discount-allocations
              - name: "amount"
                type: "number"
                description: "The discount amount allocated to the line."

              - name: "discount_application_index"
                type: "integer"
                description: "The index of the associated discount application in the order's `discount_allocations` list."

          - name: "fulfillable_quantity"
            type: "integer"
            description: |
              The amount available to fulfill, calculated as follows:

              _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

          - name: "fulfillment_service"
            type: "string"
            description: "The service provider that fulfilled the item. Possible values are `manual` or the name of the provider, such as `amazon` or `shipwire`"

          - name: "fulfillment_status"
            type: "string"
            description: |
              Indicates how far along an order is in terms of line items fulfilled. Possible values are:

              - `null`
              - `fulfilled`
              - `partial`
              - `not_eligible`

          - name: "gift_card"
            type: "boolean"
            description: "Indicates whether the line item is a gift card."

          - name: "grams"
            type: "integer"
            description: "The weight of the item in grams."

          - name: "key"
            type: "string"
            description: "A unique identifier for the line item, constructed from the line item's `variant_id` plus a hash of the line item's `properties`, even if the item has no additional properties."

          - name: "line_price"
            type: "string"
            description: "**This field has been deprecated by {{ integration.display_name }}**."

          - name: "name"
            type: "string"
            description: "The name of the product variant."

          - name: "origin_location"
            type: "object"
            description: "Details about the origin location associated with the refund line item."
            subattributes: *default-address-fields

          - name: "origin_location_id"
            type: "integer"
            description: "The ID of the origin location associated with the refund line item."

          - name: "pre_tax_price"
            type: "number"
            description: "The pre-tax price of the item."

          - name: "price"
            type: "number"
            description: "The price of the item before discounts were applied."

          - name: "product_exists"
            type: "boolean"
            description: "Indicates whether the product exists."

          - name: "product_id"
            type: "integer"
            description: "The product ID."
            foreign-key-id: "product-id"

          - name: "properties"
            type: "array"
            description: "Details about custom info for the item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "quantity"
            type: "integer"
            description: "The number of items purchased."

          - name: "requires_shipping"
            type: "boolean"
            description: "Indicates if the item requires shipping."

          - name: "sku"
            type: "string"
            description: "The item's SKU."

          - name: "tax_code"
            type: "string"
            description: ""

          - name: "tax_lines"
            type: "array"
            description: "Details about the line item's tax lines, each of which details a tax applicable to this line item."
            subattributes: &tax-lines
              - name: "compare_at"
                type: "string"
                description: ""

              - name: "position"
                type: "integer"
                description: ""

              - name: "price"
                type: "number"
                description: "The amount of tax to be charged."

              - name: "rate"
                type: "number"
                description: "The rate of tax to be applied."

              - name: "source"
                type: "string"
                description: ""

              - name: "title"
                type: "string"
                description: "The name of the tax."

              - name: "zone"
                type: "string"
                description: ""

          - name: "taxable"
            type: "boolean"
            description: "Indicates if the item is taxable."

          - name: "title"
            type: "string"
            description: "The title of the product."

          - name: "total_discount"
            type: "number"
            description: "The total of any discounts applied to the line item."

          - name: "variant_id"
            type: "integer"
            description: "The product variant ID."

          - name: "variant_inventory_management"
            type: "string"
            description: "The name of the inventory management system."

          - name: "variant_title"
            type: "string"
            description: "The title of the product variant."

          - name: "vendor"
            type: "string"
            description: "The name of the item's supplier."

      - name: "location_id"
        type: "integer"
        description: "The ID of the physical location where the fulfillment was processed."

      - name: "name"
        type: "string"
        description: "The fulfillment name as represented by a number."

      - name: "receipt"
        type: "object"
        description: ""
        subattributes:
          - name: "authorization"
            type: "string"
            description: ""

          - name: "testcase"
            type: "boolean"
            description: ""

      - name: "service"
        type: "string"
        description: ""

      - name: "shipment_status"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "tracking_company"
        type: "string"
        description: "The name of the service performing the fulfillment."

      - name: "tracking_number"
        type: "string"
        description: "The tracking number of a fulfillment, if it exists."

      - name: "tracking_numbers"
        type: "array"
        description: "A list of the fulfillment's tracking numbers."
        subattributes:
          - name: "value"
            type: "string"
            description: "The fulfillment's tracking number."

      - name: "tracking_url"
        type: "string"
        description: "The URL for a tracking number."

      - name: "tracking_urls"
        type: "array"
        description: "A list of URLs for the fulfillment's tracking numbers."
        subattributes:
          - name: "value"
            type: "string"
            description: "The URL for a tracking number."

      - name: "updated_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","fulfillment" | replace: "[ACTION]","last updated" }}

  - name: "gateway"
    type: "string"
    description: "The payment gateway used by the checkout."

  - name: "landing_site"
    type: "string"
    description: "The URL for the page where the customer entered the shop."

  # - name: "landing_site_ref"
  #   type: "string"
  #   description: ""

  - name: "line_items"
    type: "array"
    description: "Details about the line items in the order."
    subattributes: *line-items

  - name: "location_id"
    type: "integer"
    description: "The ID of the physical location where the order was processed."

  - name: "name"
    type: "string"
    description: "The order name as represented by a number."

  - name: "note"
    type: "string"
    description: "An optional note the shop owner attached to the order."

  - name: "note_attributes"
    type: "array"
    description: "Additional info added to the order, as it appears in the **Additional details** section of an order page."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "number"
    type: "integer"
    description: "An identifier unique to the shop. Numbers are sequential and start at `1000`."

  - name: "order_adjustments"
    type: "array"
    description: "A list of order adjustments attached to the order."
    subattributes: &order-adjustments
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The order adjustment ID."

      - name: "order_id"
        type: "integer"
        primary-key: true
        description: "The ID of the order associated with the order adjustment."
        foreign-key-id: "order-id"

      - name: "refund_id"
        type: "integer"
        description: "The ID of the refund associated with the order adjustment."
        primary-key: true
        foreign-key-id: "order-refund-id"

      - name: "amount"
        type: "number"
        description: "The value of the discrepancy between the calculated refund and the actual refund. If the `kind` attribute's value is `shipping_refund`, then `amount` is the value of shipping charges refunded to the customer."

      - name: "kind"
        type: "string"
        description: |
          The order adjustment type. Possible values are:

          - `shipping_refund`
          - `refund_discrepancy`

      - name: "reason"
        type: "string"
        description: "The reason for the order adjustment."

      - name: "tax_amount"
        type: "number"
        description: "The tax amount of the order adjustment in shop and presentment currencies."

  - name: "order_number"
    type: "integer"
    description: "A unique identifier for the order, used by the shop owner and customer. This is different from the `id` attribute."

  - name: "order_status_url"
    type: "string"
    description: "The URL of the order's status page."

  - name: "payment_details"
    type: "object"
    description: "Details about the payment used for the order."
    object-properties:
      - name: "avs_result_code"
        type: "string"
        description: |
          The response code from the [address verification system](https://en.wikipedia.org/wiki/Address_Verification_System){:target="new"}. Refer to [Electronic Merchant System's documentation](http://www.emsecommerce.net/avs_cvv2_response_codes.htm){:target="new"} for a list of possible codes and definitions.

      - name: "credit_card_bin"
        type: "string"
        description: |
          The [issuer identification number](https://en.wikipedia.org/wiki/ISO/IEC_7812){:target="new"} (IIN), formerly known as bank identification number (BIN) of the customer's credit card. This is made up of the first few digits of the credit card number.

      - name: "credit_card_company"
        type: "string"
        description: "The name of the company that issued the customer's credit card."

      - name: "credit_card_number"
        type: "string"
        description: "The customer's credit card number, **with most of the leading digits redacted**."

      - name: "cvv_result_code"
        type: "string"
        description: |
          The response code from the credit card company indicating whether the customer entered the card security code or card verification value (CVV) correctly. Refer to [Electronic Merchant System's documentation](http://www.emsecommerce.net/avs_cvv2_response_codes.htm){:target="new"} for a list of possible codes and defintions.

  - name: "payment_gateway_names"
    type: "array"
    description: "The list of payment gateways used for the order."
    subattributes:
      - name: "value"
        type: "string"
        description: "The payment gateway used for the order."

  - name: "phone"
    type: "string"
    description: "The customer's phone number."

  - name: "processed_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","order" | replace: "[ACTION]","processed" }}

  - name: "processing_method"
    type: "string"
    description: |
      Indicates how the payment was processed. Possible values are:

      - `checkout`
      - `direct`
      - `manual`
      - `offsite`
      - `express`

  - name: "reference"
    type: "string"
    description: ""

  - name: "referring_site"
    type: "string"
    description: "The website where the customer clicked a link to the shop."

  - name: "refunds"
    type: "array"
    description: "A list of refunds applied to the order."
    subattributes:
      # - name: "admin_graphql_api_id"
      #   type: "string"
      #   description: ""

      - name: "id"
        type: "integer"
        primary-key: true
        description: ""
        foreign-key-id: "order-refund-id"

      - name: "created_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","refund" | replace: "[ACTION]","created" }}

      - name: "note"
        type: "string"
        description: "An optional note attached to a refund."

      - name: "order_adjustments"
        type: "array"
        description: "A list of order adjustments attached to the refund. Order adjustments are generated to account for refunded shipping costs and differences between calculated and actual refund amounts."
        subattributes: *order-adjustments

      - name: "processed_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","refund" | replace: "[ACTION]","last imported" }}

      - name: "refund_line_items"
        type: "array"
        description: "A list of refunded line items."
        subattributes:
          - name: "id"
            type: "integer"
            primary-key: true
            description: "The refund line item ID."

          - name: "line_item"
            type: "object"
            description: "Details about the refund line item."
            subattributes: *line-items

          - name: "line_item_id"
            type: "integer"
            description: "The ID of the related line item in the order."

          - name: "location_id"
            type: "integer"
            description: "The ID of the location where the items will be restocked."

          - name: "quantity"
            type: "integer"
            description: "The quantity of the associated line item that was returned."

          - name: "restock_type"
            type: "string"
            description: |
              Indicates how the refund line item affects inventory levels. Possible values are:

              - `no_restock` - Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example, a refund payment can be issued but no items will be returned or made available for sale again.

              - `cancel` - The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.

              - `return` - The items were already delivered, and will be returned to the merchant. The returned quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.

              - `legacy_restock` - The deprecated restock property was used for this refund. These items were made available for sale again.

          - name: "subtotal"
            type: "number"
            description: "The subtotal of the refund line item."

          - name: "total_tax"
            type: "number"
            description: "The total tax on the refund line item."

      - name: "restock"
        type: "boolean"
        description: "Indicates if the line items will be added back to the store's inventory."

      - name: "user_id"
        type: "integer"
        description: "The ID of the user who performed the refund."

  - name: "shipping_address"
    type: "object"
    description: "Details about the shipping address associated with the order."
    object-type: "shipping address"
    subattributes: *address-fields

  - name: "shipping_lines"
    type: "array"
    description: "Details about the shipping methods associated with the order."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The shipping line ID."

      - name: "carrier_identifier"
        type: "string"
        description: "The shipping carrier's identifier."

      - name: "code"
        type: "string"
        description: "A reference to the shipping method."

      - name: "delivery_category"
        type: "string"
        description: ""

      - name: "discount_allocations"
        type: "array"
        description: "An ordered list of amounts allocated by discount applications. Each discount allocation is associated to a particular appliction."
        subattributes: *discount-allocations

      - name: "discounted_price"
        type: "number"
        description: "The price of the shipping method after discounts."

      - name: "phone"
        type: "string"
        description: "The phone number associated with the shipping method."

      - name: "price"
        type: "number"
        description: "The price of the shipping method."

      - name: "requested_fulfillment_service_id"
        type: "string"
        description: "A reference to the fulfillment service being requested for the shipping method. Present if the shipping method requires processing by a third party fulfillment service; `null` otherwise."

      - name: "source"
        type: "string"
        description: "The source of the shipping method."

      - name: "tax_lines"
        type: "array"
        description: "Details about the shipping line's tax lines, each of which details a tax applicable to this shipping line."
        subattributes: *tax-lines

      - name: "title"
        type: "string"
        description: "The title of the shipping method."

  - name: "source_identifier"
    type: "string"
    description: ""

  - name: "source_name"
    type: "string"
    description: "Where the order originated."

  - name: "source_url"
    type: "string"
    description: "The URL where the order originated."

  - name: "subtotal_price"
    type: "number"
    description: "The price of the order after discounts but before shipping, taxes, and tips."

  - name: "tags"
    type: "string"
    description: "Tags attached to the order."

  - name: "tax_lines"
    type: "array"
    description: "Details about the order's tax lines, each of which is a tax applicable to the order."
    subattributes: *tax-lines

  - name: "taxes_included"
    type: "boolean"
    description: "Indicates if taxes are included in the order subtotal."

  - name: "test"
    type: "boolean"
    description: "Indicates if the order is a test order."

  - name: "token"
    type: "string"
    description: "A unique identifier for the order."

  - name: "total_discounts"
    type: "number"
    description: "The total discounts applied to the price of the order."

  - name: "total_line_items_price"
    type: "number"
    description: "The sum of all line item prices."

  - name: "total_price"
    type: "number"
    description: "The sum of all line item prices, discounts, shipping, taxes, and tips."

  - name: "total_price_usd"
    type: "number"
    description: "The sum of all line item prices, discounts, shipping, taxes, and tips in USD."

  - name: "total_tax"
    type: "number"
    description: "The sum of all the taxes applied to the order."

  - name: "total_tip_received"
    type: "string"
    description: "The sum of all the tips in the order."

  - name: "total_weight"
    type: "integer"
    description: "The sum of all line item weights, in grams."

  - name: "user_id"
    type: "integer"
    description: "The ID of th euser logged into the {{ integration.display_name }} POS that processed the order, if applicable."
---