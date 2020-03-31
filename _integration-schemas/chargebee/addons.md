---
tap: "chargebee"
version: "1"
key: "addon"

name: "addons"
doc-link: "https://apidocs.chargebee.com/docs/api/addons"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/addons.json"
description: |
  The `{{ table.name }}` table contains info about the addons in your {{ integration.display_name }} account. Addons are additional charges applied to subscriptions apart from base charges.

replication-method: "Key-based Incremental"

api-method:
    name: "List addons"
    doc-link: "https://apidocs.chargebee.com/docs/api/addons#list_addons"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The addon ID."
    foreign-key-id: "addon-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the addon was last updated. **Note**: This attribute will be present only if the resource has been updated after 2016-09-28."

  - name: "accounting_code"
    type: "string"
    description: "The accounting code used by the addon."

  - name: "accouting_category1"
    type: "string"
    description: |
      The name of the category of your product in Xero. If you've integrated with QuickBooks, this will be the `Class`.

  - name: "accouting_category2"
    type: "string"
    description: |
      The name of the category of your product in Xero.

  - name: "archived_at"
    type: "date-time"
    description: "The time at which the plan was moved to archived status."

  - name: "avalara_sale_type"
    type: "string"
    description: |
      **Applicable only if you use {{ integration.display_name }}'s AvaTax for Communications integration**. The type of sale carried out. Possible values are:

      - `wholesale`
      - `retail`
      - `consumed`
      - `vendor_use`

  - name: "avalara_service_type"
    type: "integer"
    description: "**Applicable only if you use {{ integration.display_name }}'s AvaTax for Communications integration**. The type of service for the product to be taxed."

  - name: "avalara_transaction_type"
    type: "integer"
    description: "**Applicable only if you use {{ integration.display_name }}'s AvaTax for Communications integration**. The type of product to be taxed."

  - name: "charge_type"
    type: "string"
    description: |
      The type of charge. Possible values are:

      - `recurring`: Charges are automatically applied in sync with the billing frequency of the subscription.
      - `non_recurring`: Charged immediately and only once every time it's applied.

  - name: "currency_code"
    type: "string"
    description: "The currency code (ISO 4217 format) of the addon."

  - name: "custom_fields"
    type: "string"
    description: "" 

  - name: "description"
    type: "string"
    description: "Description about the addon to show in the hosted pages and customer portal."

  - name: "enabled_in_portal"
    type: "boolean"
    description: "Indicates if the addon is available to customers to add in the 'Change Subscription' option in the customer portal."

  - name: "invoice_name"
    type: "string"
    description: "The display name used in invoices."

  - name: "invoice_notes"
    type: "string"
    description: "The invoice notes for the addon."

  - name: "is_shippable"
    type: "boolean"
    description: "Indicates whether the addon can be added to orders."

  - name: "meta_data"
    type: "string"
    description: "Additional info about the addon."

  - name: "name"
    type: "string"
    description: "The display name used in web interface for identifying the addon."

  - name: "object"
    type: "string"
    description: ""

  - name: "period"
    type: "integer"
    description: "Applicable only for `charge_type: recurring`. Along with `period_unit`, this determines the term-price of the addon."

  - name: "period_unit"
    type: "string"
    description: |
      Applicable only for `charge_type: recurring`. Along with `period`, this determines the term-price of the addon. Possible values are:

      - `week`: Charge based on week(s)
      - `month`:  Charge based on month(s)
      - `year`: Charge based on year(s)
      - `not_applicable`: Not applicable for the addon

  - name: "price"
    type: "integer"
    description: "The addon price. Addon price is calculated based on the addon type and charge type."
    doc-link: "https://www.chargebee.com/docs/addons.html#charge-type-and-pricing"

  - name: "pricing_model"
    type: "string"
    description: |
      Indicates how the charges for the addon are calculated. Possible values are:

      - `flat_fee`: Charges single price on a recurring basis.
      - `per_unit`: Charges the price for each unit of the plan for the subscription on a recurring basis.
      - `tiered`: Charges different per unit price for the quantity purchased from every tier.
      - `volume`: Charges the per unit price for the total quantity purchased based on the tier under which it falls.
      - `stairstep`: Charges a price for a range.

  - name: "resource_version"
    type: "integer"
    description: "The version number of the addon. Each update of the addon results in an incremental change of this value. **Note**: This attribute will be present only if the resource has been updated after 2016-09-28."

  - name: "shipping_frequency_period"
    type: "integer"
    description: "Defines the shipping frequency in conjunction with `shipping_frequency_period_unit`. For example: If `shipping_frequency_period_unit: week` and this value is `2`, the customer would be billed every two weeks."

  - name: "shipping_frequency_period_unit"
    type: "string"
    description: |
      Defines the shipping frequency in conjunction with  `shipping_frequency_period`. Possible values are:

      - `year`
      - `month`
      - `week`

  - name: "sku"
    type: "string"
    description: "The field is used as Product name/code in your third party accounting application. {{ integration.display_name }} will use it as an alternate name in your accounting application"

  - name: "status"
    type: "string"
    description: |
      The status of the addon. Possible values are:

      - `active`
      - `archived`

  - name: "tax_code"
    type: "string"
    description: "The Avalara tax codes to which items are mapped to should be provided here. Applicable only if you use {{ integration.display_name }}'s AvaTax for Sales integration."

  - name: "tax_profile_id"
    type: "string"
    description: "The tax profile of the addon."

  - name: "taxable"
    type: "boolean"
    description: "Indicates whether the addon is taxable or not."

  - name: "tiers"
    type: "array"
    description: "Applicable only if the addon uses tiered, volume, or stairstep pricing. The list of tiers for the addon."
    subattributes:
      - name: "ending_unit"
        type: "integer"
        description: "The upper limit of a range of units for the tier."

      - name: "price "
        type: "integer"
        description: "The price of the tier if the charge model is stairstep pricing, or the price of each unit in the tier if the charge model is tiered/volume pricing."

      - name: "starting_unit"
        type: "integer"
        description: "The lower limit of a range of units for the tier."

  - name: "type"
    type: "string"
    description: ""

  - name: "unit"
    type: "string"
    description: |
      Applicable only for quantity type addons. This specifies the type of quantity. For example: If the addon price is `$10` and `agent` is the unit, it will be displayed as `$10/agent`.   
---