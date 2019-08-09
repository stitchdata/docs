---
tap: "bigcommerce"
version: "1.0"

name: "orders"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-bigcommerce/blob/master/tap_bigcommerce/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains info about the orders in your {{ integration.display_name }} store.

replication-method: "Key-based Incremental"
api-method:
  name: "Get all orders"
  doc-link: "https://developer.bigcommerce.com/api-reference/orders/orders-api/orders/getorders"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The order ID."
    # foreign-key-id: "order-id"

  - name: "date_modified"
    type: "date-time"
    replication-key: true
    description: "The date the order was last modified, in RFC 2822 format."

  - name: "base_handling_cost"
    type: "number"
    description: "The base handling cost."

  - name: "base_shipping_cost"
    type: "number"
    description: "The base shipping cost."

  - name: "base_wrapping_cost"
    type: "number"
    description: "The base wrapping cost."

  - name: "billing_address"
    type: "object"
    description: "The billing address for the customer who placed the order."
    address-type: "billing"
    subattributes:
      - name: "city"
        type: "string"
        description: &city "The city of the {{ attribute.address-type }} address."

      - name: "company"
        type: "string"
        description: &company "The company of the of the {{ attribute.address-type }} address."

      - name: "country"
        type: "string"
        description: &country "The country of the {{ attribute.address-type }} address."

      - name: "country_iso2"
        type: "string"
        description: &country-iso "The country code of the country associated with the {{ attribute.address-type }} address."

      - name: "email"
        type: "string"
        description: &email "The email address associated with the {{ attribute.address-type }} address."

      - name: "first_name"
        type: "string"
        description: &address-first-name "The first name associated with the {{ attribute.address-type }} address."

      - name: "form_fields"
        type: "array"
        description: "Details about the form fields associated with the {{ attribute.address-type }} address."
        subattributes: &form-fields
          - name: "name"
            type: "string"
            description: "The name of the form field."

          - name: "value"
            type: "string"
            description: "The value of the form field."

      - name: "last_name"
        type: "string"
        description: &address-last-name "The last name associated with the {{ attribute.address-type }} address."

      - name: "phone"
        type: "string"
        description: &phone "The phone number associated with the {{ attribute.address-type }} address."

      - name: "state"
        type: "string"
        description: &state "The state of the {{ attribute.address-type }} address."

      - name: "street_1"
        type: "string"
        description: &street-1 "The first line of the street associated with the {{ attribute.address-type }} address."

      - name: "street_2"
        type: "string"
        description: &street-2 "The second line of the street associated with the {{ attribute.address-type }} address."

      - name: "zip"
        type: "string"
        description: &zip "The zip code of the {{ attribute.address-type }} address."

  - name: "cart_id"
    type: "string"
    description: "The ID of the cart that the order originated from."

  - name: "channel_id"
    type: "integer"
    description: "Indicates where the order originated."

  - name: "coupon_discount"
    type: "number"
    description: "The value of the coupon discount applied to the order."

  - name: "coupons"
    type: "array"
    description: "Details about the coupons applied to the order."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The coupon code ID."
        foreign-key-id: "coupon-id"

      - name: "coupon_id"
        type: "integer"
        primary-key: true
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "amount"
        type: "number"
        description: |
          The discount to apply to an order as either an amount or a percentage. This field is determined by the coupon’s `type`.

          For example: If `type: percentage_discount`, this value would represent a percentage discount.

      - name: "code"
        type: "string"
        description: "The coupon code entered to receive the discount."

      - name: "discount"
        type: "number"
        description: "The discount amount applied to the order as a result of the coupon."

      - name: "order_id"
        type: "integer"
        description: "The ID of the order the coupon was applied to."
        foreign-key-id: "order-id"

      - name: "type"
        type: "string"
        description: |
          The type of coupon applied to the order. Possible values are:

          - `0` - `per_item_discount`
          - `1` - `percentage_discount`
          - `2` - `per_total_discount`
          - `3` - `shipping_discount`
          - `4` - `free_shipping`

  - name: "currency_code"
    type: "string"
    description: "The currency code of the currency used in the order."

  - name: "currency_exchange_rate"
    type: "number"
    description: "The exchange rate of the currency used in the order."

  - name: "currency_id"
    type: "integer"
    description: "The ID of the currency used in the order."

  - name: "custom_status"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer who placed the order."
    foreign-key-id: "customer-id"

  - name: "customer_message"
    type: "string"
    description: "The message the customer entered into the `Order Comments` box during checkout."

  - name: "date_created"
    type: "date-time"
    description: "The date the order was created, in RFC 2822 format."

  - name: "date_shipped"
    type: "date-time"
    description: "The date the order shipped, in RFC 2822 format."

  - name: "default_currency_code"
    type: "string"
    description: "The currency code of the default currency for this type of order."

  - name: "default_currency_id"
    type: "integer"
    description: "The ID of the default currency for this type of order."

  - name: "discount_amount"
    type: "string"
    description: "The amount of discount applied to the order."

  - name: "ebay_order_id"
    type: "string"
    description: "If the order was placed through eBay, this field will contain the eBay order number. Otherwise, the value will be `0`."

  - name: "external_id"
    type: "string"
    description: &external-id "The ID of the order in another system. For example: For Amazon orders, this field will contain the Amazon Order ID."

  - name: "external_merchant_id"
    type: "string"
    description: "The ID of the external merchant."

  - name: "external_source"
    type: "string"
    description: "The external source."

  - name: "form_fields"
    type: "array"
    description: "The form fields associated with the order."
    subattributes: *form-fields

  - name: "geoip_country"
    type: "string"
    description: "The full name of the country where the customer made the purchase, based on the customer's IP address."

  - name: "geoip_country_iso2"
    type: "string"
    description: "The country where the customer made the purchase, in ISO2 format, based on the customer's IP address."

  - name: "gift_certificate_amount"
    type: "number"
    description: "The gift certificate amount applied to the order."

  - name: "handling_cost_ex_tax"
    type: "number"
    description: "The handling cost, excluding tax."

  - name: "handling_cost_inc_tax"
    type: "number"
    description: "The handling cost, including tax."

  - name: "handling_cost_tax"
    type: "number"
    description: "The amount of tax associated with the handling cost."

  - name: "handling_cost_tax_class_id"
    type: "integer"
    description: "The ID of the tax class associated with the handling cost."

  - name: "ip_address"
    type: "string"
    description: "The IP address of the customer who placed the order, if known."

  - name: "is_deleted"
    type: "boolean"
    description: "Indicates whether the order was deleted (archived)."

  - name: "is_email_opt_in"
    type: "boolean"
    description: "Indicates whether the customer has selected an opt-in check box on the checkout page to receive emails."

  - name: "items_shipped"
    type: "integer"
    description: "The number of items that have been shipped."

  - name: "items_total"
    type: "integer"
    description: "The total number of items in the order."

  - name: "order_is_digital"
    type: "boolean"
    description: "Indicates if the order is for digital products."

  - name: "order_source"
    type: "string"
    description: "The source of the order. Orders submitted via the store's website will include a `www` value, while orders submitted via the API will be set to `external`."

  - name: "payment_method"
    type: "string"
    description: |
      The payment method for the order. Possible values include:

      - `Manual`
      - `Credit Card`
      - `Cash`
      - `Test Payment Gateway`

  - name: "payment_provider_id"
    type: "string"
    description: "If a payment provider was used, the transaction/payment ID in the order's payment provider's system."

  - name: "payment_status"
    type: "string"
    description: "The status of payment for the order."

  - name: "products"
    type: "array"
    description: "Details about the products in the order."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The product ID."
        foreign-key-id: "product-id"

      - name: "applied_discounts"
        type: "array"
        description: "Details about the discounts applied to the product."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the coupon applied to the order."
            foreign-key-id: "coupon-id"

          - name: "amount"
            type: "number"
            description: "The amount of the discount applied to the product."

          - name: "code"
            type: "string"
            description: "The code used to apply the discount to the product."

          - name: "name"
            type: "string"
            description: "The name of the coupon applied to the order."

          - name: "type"
            type: "string"
            description: "The type of coupon applied to the order."

      - name: "base_cost_price"
        type: "number"
        description: "The product's cost price."

      - name: "base_price"
        type: "number"
        description: "The product's base price."

      - name: "base_total"
        type: "number"
        description: "The product's total base price."

      - name: "base_wrapping_cost"
        type: "number"
        description: "The product's base wrapping cost."

      - name: "bin_picking_number"
        type: "string"
        description: "The BIN picking number for the product."

      - name: "cost_price_ex_tax"
        type: "number"
        description: "The cost price of the product, excluding tax."

      - name: "cost_price_inc_tax"
        type: "number"
        description: "The cost price of the product, including tax."

      - name: "cost_price_tax"
        type: "number"
        description: "The total tax applied to the product's cost price."

      - name: "depth"
        type: "string"
        description: "The depth of the product, which can be used when calculating shipping costs."

      - name: "ebay_item_id"
        type: "string"
        description: "The product's eBay item ID."

      - name: "ebay_transaction_id"
        type: "string"
        description: "The product's eBay transaction ID."

      - name: "event_date"
        type: "date-time"
        description: "The date of the product's promotional event/scheduled delivery."

      - name: "event_name"
        type: "string"
        description: "The name of the promotional event/delivery date."

      - name: "external_id"
        type: "integer"
        description: *external-id

      - name: "fixed_shipping_cost"
        type: "number"
        description: "The fixed shipping cost for the product."

      - name: "height"
        type: "string"
        description: "The height of the product, which can be used when calculating shipping costs."

      - name: "is_bundled_product"
        type: "boolean"
        description: "Indicates whether this product is bundled with other products."

      - name: "is_refunded"
        type: "boolean"
        description: "Indicates whether the product has been refunded."

      - name: "name"
        type: "string"
        description: "The name of the product."

      - name: "option_set_id"
        type: "integer"
        description: "The ID of the option set applied to the product."

      - name: "order_address_id"
        type: "integer"
        description: "The ID of the associated order address."

      - name: "order_id"
        type: "integer"
        description: "The ID of the order associated with the product."
        # foreign-key-id: "order-id"

      - name: "parent_order_product_id"
        type: "integer"
        description: "The ID of a parent product."
        foreign-key-id: "product-id"

      - name: "price_ex_tax"
        type: "number"
        description: "The price of the product, excluding tax."

      - name: "price_inc_tax"
        type: "number"
        description: "The price of the product, including tax."

      - name: "price_tax"
        type: "number"
        description: "The total tax amount based on the product's price."

      - name: "product_id"
        type: "integer"
        description: "The product ID."

      - name: "product_options"
        type: "array"
        description: "Details about the product options applied to the product."
        subattributes:
          - name: "id"
            type: "integer"
            primary-key: true
            description: "The product option ID."

          - name: "display_name"
            type: "string"
            description: "The product option's display name."

          - name: "display_style"
            type: "string"
            description: "Indicates how the product option is displayed on the storefront. For example: `drop down`"

          - name: "display_value"
            type: "string"
            description: "The name of the product option value as shown on the storefront."

          - name: "name"
            type: "string"
            description: "The name of the product option."

          - name: "option_id"
            type: "integer"
            description: "The option ID."

          - name: "order_product_id"
            type: "integer"
            description: "The order product ID."

          - name: "product_option_id"
            type: "integer"
            description: "The product option ID."

          - name: "type"
            type: "string"
            description: "The product option type."

          - name: "value"
            type: "number"
            description: ""

      - name: "quantity"
        type: "integer"
        description: "The quantity of the product included in the order."

      - name: "quantity_refunded"
        type: "integer"
        description: "The quantity of the product refunded for the order."

      - name: "quantity_shipped"
        type: "integer"
        description: "The quantity of the product that has been shipped."

      - name: "refund_amount"
        type: "number"
        description: "The amount refunded for the order."

      - name: "return_id"
        type: "integer"
        description: "The refund ID."
        # foreign-key-id: "refund-id"

      - name: "sku"
        type: "string"
        description: "The product SKU."

      - name: "total_ex_tax"
        type: "number"
        description: "The total amount for the product included in the order, excluding tax."

      - name: "total_inc_tax"
        type: "number"
        description: "The total amount for the product included in the order, including tax."

      - name: "total_tax"
        type: "number"
        description: "The total tax amount based on the product's price and quantity ordered."

      - name: "type"
        type: "string"
        description: "The type of product. Possible values are `physical` or `digital`."

      - name: "weight"
        type: "number"
        description: "The weight of the product, used to calculate shipping costs."

      - name: "width"
        type: "string"
        description: "The width of the product, used to calculate shipping costs."

      - name: "wrapping_cost_ex_tax"
        type: "number"
        description: "The total wrapping cost for the product included in the order, excluding tax."

      - name: "wrapping_cost_inc_tax"
        type: "number"
        description: "The total wrapping cost for the product included in the order, including tax."

      - name: "wrapping_cost_tax"
        type: "number"
        description: "The total tax amount for wrapping for the product included in the order."

      - name: "wrapping_message"
        type: "string"
        description: "The message to accompany the gift wrapping."

      - name: "wrapping_name"
        type: "string"
        description: "The name of the gift wrapping option."

  - name: "refunded_amount"
    type: "number"
    description: "The amount refunded from the order."

  - name: "shipping_address_count"
    type: "integer"
    description: "The number of shipping addresses associated with the transaction."

  - name: "shipping_addresses"
    type: "array"
    description: "The shipping addresses associated with the order."
    address-type: "shipping"
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: ""

      - name: "base_cost"
        type: "number"
        description: "The base value of the order's items."

      - name: "base_handling_cost"
        type: "number"
        description: "The base handling charge."

      - name: "city"
        type: "string"
        description: *city

      - name: "company"
        type: "string"
        description: *company

      - name: "cost_ex_tax"
        type: "number"
        description: "The value of the order's items, excluding tax."

      - name: "cost_inc_tax"
        type: "number"
        description: "The value of the order's items, including tax."

      - name: "cost_tax"
        type: "number"
        description: "The tax amount on the order."

      - name: "cost_tax_class_id"
        type: "integer"
        description: "The ID of the tax class applied to the order."

      - name: "country"
        type: "string"
        description: *country

      - name: "country_iso2"
        type: "string"
        description: *country-iso2

      - name: "email"
        type: "string"
        description: *email

      - name: "first_name"
        type: "string"
        description: *address-first-name

      - name: "form_fields"
        type: "array"
        description: ""
        subattributes: *form-fields

      - name: "handling_cost_ex_tax"
        type: "number"
        description: "The handling charge for the order, excluding tax."

      - name: "handling_cost_inc_tax"
        type: "number"
        description: "The handling charge for the order, including tax."

      - name: "handling_cost_tax"
        type: "number"
        description: "The tax amount for the order, based on the handling cost."

      - name: "handling_cost_tax_class_id"
        type: "integer"
        description: "The tax class ID associated with the handling cost."

      - name: "items_shipped"
        type: "integer"
        description: "The number of items that have been shipped."

      - name: "items_total"
        type: "integer"
        description: "The total number of items in the order."

      - name: "last_name"
        type: "string"
        description: *address-last-name

      - name: "order_id"
        type: "integer"
        description: "The order ID."
        foreign-key-id: "order-id"

      - name: "phone"
        type: "string"
        description: *phone

      - name: "shipping_method"
        type: "string"
        description: "The shipping method selected by the customer. For example: `Free Shipping`"

      - name: "shipping_zone_id"
        type: "integer"
        description: "The ID of the shipping zone."

      - name: "shipping_zone_name"
        type: "string"
        description: "The name of the shipping zone."

      - name: "state"
        type: "string"
        description: *state

      - name: "street_1"
        type: "string"
        description: *street-1

      - name: "street_2"
        type: "string"
        description: *street-2

      - name: "zip"
        type: "string"
        description: *zip

  - name: "shipping_cost_ex_tax"
    type: "number"
    description: "The cost of shipping for the order, excluding tax."

  - name: "shipping_cost_inc_tax"
    type: "number"
    description: "The cost of shipping for the order, including tax."

  - name: "shipping_cost_tax"
    type: "number"
    description: "The amount of tax associated with the shipping cost."

  - name: "shipping_cost_tax_class_id"
    type: "integer"
    description: "The ID of the tax class associated with the shipping."

  - name: "staff_notes"
    type: "string"
    description: "Additional notes for staff."

  - name: "status"
    type: "string"
    description: "The status of the order."

  - name: "status_id"
    type: "integer"
    description: "The ID of the order status."

  - name: "store_credit_amount"
    type: "number"
    description: "The amount of store credit applied to the order."

  - name: "subtotal_ex_tax"
    type: "number"
    description: "The order subtotal, excluding tax."

  - name: "subtotal_inc_tax"
    type: "number"
    description: "The order subtotal including tax."

  - name: "subtotal_tax"
    type: "number"
    description: "The total tax applied to the order subtotal."

  - name: "tax_provider_id"
    type: "string"
    description: |
      The ID of the tax provider associated with the order. Possible values are:

      - `BasicTaxProvider` - Tax is set to manual
      - `AvaTaxProvider` - Used for Avalara. Tax is set to automatic and the order was not created by the {{ integration.display_name }} API.
      - `""` (blank) - Tax provider is unknown 

  - name: "total_ex_tax"
    type: "number"
    description: "The order total, excluding tax."

  - name: "total_inc_tax"
    type: "number"
    description: "The order total, including tax."

  - name: "total_tax"
    type: "number"
    description: "The total tax applied to the order."

  - name: "wrapping_cost_ex_tax"
    type: "number"
    description: "The wrapping cost, excluding tax."

  - name: "wrapping_cost_inc_tax"
    type: "number"
    description: "The wrapping cost, including tax."

  - name: "wrapping_cost_tax"
    type: "number"
    description: "The total tax applied to the wrapping cost."

  - name: "wrapping_cost_tax_class_id"
    type: "integer"
    description: "The ID of the tax class associated with the wrapping cost."
---