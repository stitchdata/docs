---
tap: "shopify"
version: "1.0"

name: "abandoned_checkouts"
doc-link: "https://help.shopify.com/en/api/reference/orders/abandoned_checkouts"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/abandoned_checkouts.json"
description: |
  The `{{ table.name }}` table contains info about abandoned checkouts. {{ integration.display_name }} considers a checkout to be abandoned when a customer has entered billing and shipping details, but hasn't completed the purchase.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve all abandoned checkouts"
    doc-link: "https://help.shopify.com/en/api/reference/orders/abandoned_checkouts"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The abandoned checkout ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","checkout" | replace: "[ACTION]","last updated" }}

  - name: "abandoned_checkout_url"
    type: "string"
    description: "The recovery URL that is sent to a customer so they can recover their checkout."

  - name: "billing_address"
    type: "object"
    description: "The customer's billing address details."
    object-properties:
      - name: "address1"
        type: "string"
        description: "The street address of the billing address."

      - name: "address2"
        type: "string"
        description: "An optional field for the street address of the billing address."

      - name: "city"
        type: "string"
        description: "The city of the billing address."

      - name: "company"
        type: "string"
        description: "The company of the person associated with the billing address."

      - name: "country"
        type: "string"
        description: "The name of the country of the billing address."

      - name: "country_code"
        type: "string"
        description: |
          The two letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"}) format for the country of the billing address.

      - name: "first_name"
        type: "string"
        description: "The first name of the person associated with the payment method."

      - name: "last_name"
        type: "string"
        description: "The last name of the person associated with the payment method."

      - name: "latitude"
        type: "number"
        description: "The latitude of the billing address."

      - name: "longitude"
        type: "number"
        description: "The longitude of the billing address."

      - name: "name"
        type: "string"
        description: "The full name of the person associated with the payment method."

      - name: "phone"
        type: "string"
        description: "The phone number at the billing address."

      - name: "province"
        type: "string"
        description: "The name of the state or province of the billing address."

      - name: "province_code"
        type: "string"
        description: "The two-letter abbreviation of the state or province of the billing address."

      - name: "zip"
        type: "string"
        description: "The zip or postal code of the billing address."

  - name: "buyer_accepts_marketing"
    type: "boolean"
    description: "Indicates whether the customer wants to receive email updates from the shop."

  - name: "cart_token"
    type: "string"
    description: "The ID of the cart that is attached to the checkout."

  - name: "closed_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","checkout" | replace: "[ACTION]","closed" }} If the checkout wasn't closed, this value will be `null`.

  - name: "completed_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","checkout" | replace: "[ACTION]","completed" }} For abandoned checkouts, this value will always be `null`.

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","checkout" | replace: "[ACTION]","created" }}

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} code of the shop's default currency at the time of checkout.

      For the currency the customer used at checkout, see `presentment_currency`.

  - name: "customer"
    type: "object"
    description: "Details about the customer associated with the abandoned checkout."
    object-properties:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The customer ID."
        foreign-key-id: "customer-id"
        
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
        description: |
          {{ table.date-time | replace: "[ITEM]","customer" | replace: "[ACTION]","last updated" }}

      - name: "verified_email"
        type: "boolean"
        description: "Indicates if the customer has verified their email address."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer associated with the abandoned checkout."

  - name: "customer_locale"
    type: "string"
    description: "The two or three-letter language code, optionally followed by a region modifier."

  - name: "device_id"
    type: "integer"
    description: "The ID of the Shopify POS device that created the checkout."

  - name: "discount_codes"
    type: "array"
    description: "The discount codees applied to the checkout."
    array-attributes:
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

  - name: "gateway"
    type: "string"
    description: "The payment gateway used by the checkout. For abandoned checkouts, this value will always be `null`."

  - name: "landing_site"
    type: "string"
    description: "The URL for the page where the customer entered the shop."

  - name: "line_items"
    type: "array"
    description: "A list of line items in the checkout."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The line item ID."

      - name: "applied_discount"
        type: "integer"
        description: "The amount of the discount applied to the line item."

      - name: "compare_at_price"
        type: "string"
        description: "The price of a line item before a sale or discount."

      - name: "destination_location"
        type: "object"
        description: "Details about the line item's destination location."
        object-properties: &address-fields
          - name: "address1"
            type: "string"
            description: "The street address."

          - name: "address2"
            type: "string"
            description: "An optional second line for the address."

          - name: "city"
            type: "string"
            description: "The city."

          - name: "country_code"
            type: "string"
            description: |
              The two letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"}) format for the country of the destination address.

          - name: "id"
            type: "integer"
            primary-key: true
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
        array-attributes:
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
        description: "The fulfillment service provider for the item."

      - name: "fulfillment_status"
        type: "string"
        description: |
          The status of the item's fulfillment. Possible values are:

          - `fulfilled`
          - `null`
          - `partial`

      - name: "gift_card"
        type: "boolean"
        description: "Indicates if the line item is a gift card."

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
        description: "The name of the line item."

      - name: "origin_location"
        type: "object"
        description: "Details about the line item's origin location."
        object-properties: *address-fields

      - name: "origin_location_id"
        type: "integer"
        description: "The ID of the origin location associated with the line item."

      - name: "pre_tax_price"
        type: "number"
        description: "The pre-tax price of the item."

      - name: "price"
        type: "number"
        description: "The price of the item before discounts were applied."

      - name: "product_exists"
        type: "boolean"
        description: "Indicates if the product exists."

      - name: "product_id"
        type: "integer"
        description: "The product ID of the item."
        foreign-key-id: "product-id"

      - name: "properties"
        type: "array"
        description: "Details about custom info for the item."
        array-attributes:
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
        array-attributes: &tax-lines
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
    description: "The ID of the physical location where the checkout was processed."

  - name: "name"
    type: "string"
    description: "The order name as represented by a number."

  - name: "note"
    type: "string"
    description: "An optional note attached to the order."

  - name: "phone"
    type: "string"
    description: "The customer's phone number."

  - name: "presentment_currency"
    type: "string"
    description: |
      The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} code of the currency that the customer used at checkout.

  - name: "referring_site"
    type: "string"
    description: "The website that referred the cusomter to the shop."

  - name: "shipping_address"
    type: "object"
    description: "Details about the shipping address associated with the checkout."
    object-properties:
      - name: "address1"
        type: "string"
        description: "The street address of the shipping address."

      - name: "address2"
        type: "string"
        description: "An optional field for the street address of the shipping address."

      - name: "city"
        type: "string"
        description: "The city of the shipping address."

      - name: "company"
        type: "string"
        description: "The company of the person associated with the shipping address."

      - name: "country"
        type: "string"
        description: "The name of the country of the shipping address."

      - name: "country_code"
        type: "string"
        description: |
          The two letter code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"}) format for the country of the shipping address.

      - name: "first_name"
        type: "string"
        description: "The first name of the person associated with the payment method."

      - name: "last_name"
        type: "string"
        description: "The last name of the person associated with the payment method."

      - name: "latitude"
        type: "number"
        description: "The latitude of the shipping address."

      - name: "longitude"
        type: "number"
        description: "The longitude of the shipping address."

      - name: "name"
        type: "string"
        description: "The full name of the person associated with the payment method."

      - name: "phone"
        type: "string"
        description: "The phone number at the shipping address."

      - name: "province"
        type: "string"
        description: "The name of the state or province of the shipping address."

      - name: "province_code"
        type: "string"
        description: "The two-letter abbreviation of the state or province of the shipping address."

      - name: "zip"
        type: "string"
        description: "The zip or postal code of the shipping address."

  - name: "shipping_lines"
    type: "array"
    description: "Details about the shipping methods associated with the order."
    array-attributes:
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

      - name: "markup"
        type: "string"
        description: ""

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
        description: "The channel where the checkout originated."

      - name: "tax_lines"
        type: "array"
        description: "Details about the shipping line's tax lines, each of which details a tax applicable to this shipping line."
        array-attributes: *tax-lines

      - name: "title"
        type: "string"
        description: "The title of the shipping method."

      - name: "validation_context"
        type: "string"
        description: ""

  - name: "source"
    type: "string"
    description: "The channel where the checkout originated."

  - name: "source_identifier"
    type: "string"
    description: ""

  - name: "source_name"
    type: "string"
    description: |
      Where the checkout originated. Possible values are:

      - `web`
      - `pos`
      - `iphone`
      - `android`

  - name: "source_url"
    type: "string"
    description: ""

  - name: "subtotal_price"
    type: "number"
    description: "The price of the checkout before shipping and taxes."

  - name: "tax_lines"
    type: "array"
    description: "Details about the taxes applicable to the checkout."
    array-attributes: *tax-lines

  - name: "taxes_included"
    type: "boolean"
    description: "Indicates if taxes are included in the price."

  - name: "token"
    type: "string"
    description: "A unique ID for the checkout."

  - name: "total_discounts"
    type: "number"
    description: "The total amount of discounts to be applied."

  - name: "total_line_items_price"
    type: "number"
    description: "The sum of the prices of all line items in the checkout."

  - name: "total_price"
    type: "number"
    description: "The sum of the prices of all line items in the checkout, discounts, shipping costs, and taxes"

  - name: "total_tax"
    type: "number"
    description: "The sum of all the taxes applied to the checkout."

  - name: "total_weight"
    type: "integer"
    description: "The sum of all the weights in grams of the line items in the checkout."

  - name: "user_id"
    type: "integer"
    description: "The ID of the user who created the checkout."
---