---
title: Square
permalink: /integrations/saas/square
keywords: square, integration, schema, etl square, square etl, square schema
summary: "Connection instructions and schema details for Stitch's Square integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

key: "square-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "square"
display_name: "Square"

singer: false
status-url: "http://issquareup.com/"

this-version: "04-05-2016"

api: |
  [{{ integration.display_name }} Connect v1 API](https://developer.squareup.com/docs/api/connect/v1#navsection-v1endpoints){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: false
  lots-of-full-table: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Bank Accounts
  - name: "square_bank_accounts"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-bankaccount
    description: "non-confidential info - this means no full bank account numbers - about a location’s associated bank accounts."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Bank Account ID (<code>id</code>)
      - name: location_id
      - name: merchant_id
      - name: bank_name
      - name: name
      - name: type
      - name: routing_number
      - name: account_number_suffix
      - name: currency_code

## Cash Drawer Shifts
  - name: "square_cash_drawer_shifts"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-cashdrawershift
    description: "the details for all of a location’s cash drawer shifts."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Cash Drawer Shift ID (<code>id</code>)
      - name: location_id
      - name: cash_drawer_state
      - name: opened_at
      - name: ended_at
      - name: closed_at
      - name: employee_ids
      - name: opening_employee_id
      - name: ending_employee_id
      - name: closing_employee_id
      - name: description
      - name: starting_cash_money
      - name: cash_payment_money
      - name: cash_refunds_money
      - name: cash_paid_in_money
      - name: cash_paid_out_money
      - name: expected_cash_money
      - name: closed_cash_money
      - name: device
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-cashdrawerevent" target="new">events</a><code>*</code>


## Categories
  - name: "square_categories"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-category
    description: "info about a location’s item categories."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Category ID (<code>id</code>)
      - name: name
      - name: location_id


## Discounts
  - name: "square_discounts"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-discount
    description: "info about a location’s discounts."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Discount ID (<code>id</code>)
      - name: location_id
      - name: name
      - name: rate
      - name: amount_money
      - name: discount_type
      - name: pin_required
      - name: color


## Employees
  - name: "square_employees"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-employee
    description: "summary info for all of a business’s employees."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Employee ID (<code>id</code>)
      - name: first_name
      - name: last_name
      - name: role_ids
      - name: authorized_location_ids
      - name: email
      - name: status
      - name: external_id
      - name: created_at
      - name: updated_at


## Fees
  - name: "square_fees"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-fee
    description: "info on a location’s fees, or tax items."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Fee ID (<code>id</code>)
      - name: location_id
      - name: name
      - name: rate
      - name: calculation_phase
      - name: adjustment_type
      - name: applies_to_custom_amounts
      - name: enabled
      - name: inclusion_type
      - name: type


## Inventory
  - name: "square_inventory"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-inventoryentry
    description: "inventory info for all of a merchant’s inventory-enabled variations."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Variation ID (<code>id</code>)
      - name: location_id
      - name: quantity_on_hand


## Items
  - name: "square_items"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-item
    description: "info about a location’s items."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Item ID (<code>id</code>)
      - name: location_id
      - name: name
      - name: description
      - name: type
      - name: abbreviation
      - name: color
      - name: visibility
      - name: available_online
      - name: master_image
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-itemvariation target="new">variations</a><code>*</code>
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-modifierlist" target="new">modifier_lists</a><code>*</code>
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-fee" target="new">fees</a><code>*</code>
      - name: taxable


## Location
  - name: "square_location"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#get-locations
    description: "details for a business’s locations."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Location ID (<code>id</code>)
      - name: name
      - name: email
      - name: country_code
      - name: currency_code
      - name: business_name
      - name: business_address__address_line_1
      - name: business_address__locality
      - name: business_address__administrative_district_level_1
      - name: business_address__postal_code
      - name: business_phone__calling_code
      - name: business_phone__number
      - name: business_type
      - name: shipping_address__address_line_1
      - name: shipping_address__locality
      - name: shipping_address__administrative_district_level_1
      - name: shipping_address__postal_code
      - name: account_type
      - name: location_details__nickname
      - name: market_url
      - name: account_capabilities<code>*</code>


## Modifier Lists
  - name: "square_modifier_lists"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-modifierlist
    description: "info about modifications for specific items."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Modifier ID (<code>id</code>)
      - name: name
      - name: selection_type
      - name: modifier_options<code>*</code>


## Orders
  - name: "square_orders"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-order
    description: "summary information for a merchant’s online store orders."
    notes: |
      <h4 id="purchased-items">Purchased Items & Orders</h4>
      <p><strong>This table does not contain purchased items data</strong>. To view order data alongside purchased items data, use the <code>payment_id</code> column in this table to join it to the <code>payments</code> table.</p>
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Order ID (<code>id</code>)
      - name: state
      - name: buyer_email
      - name: recipient_name
      - name: recipient_phone_number
      - name: shipping_address
      - name: subtotal_money
      - name: total_shipping_money
      - name: total_price_money
      - name: total_discount_money
      - name: created_at
      - name: updated_at
      - name: expires_at
      - name: payment_id
      - name: buyer_note
      - name: completed_note
      - name: refunded_note
      - name: canceled_note
      - name: tender
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-orderhistoryentry" target="new">order_history</a><code>*</code>
      - name: promo_code
      - name: btc_receive_address
      - name: btc_price_satoshi


## Pages
  - name: "square_pages"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-page
    description: "info about favorites pages created in the iPad version of Square Register."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Page ID (<code>id</code>)
      - name: name
      - name: page_index
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-pagecell" target="new">cells</a><code>*</code>


## Payments
  - name: "square_payments"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-payment
    description: "summary info - including itemizations - for all payments taken by a merchant or the merchant’s mobile staff. <strong>Note that Square doesn't always include itemizations in payments when the payment amount is zero.</strong>"
    notes: |
      ### Payment Amounts & Itemizations
      Square doesn't always include itemizations in payments when the payment amount is zero. If you're missing itzemization data, check the corresponding payment amounts to see if they're greater than zero.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: PaymentID (<code>id</code>)
      - name: merchant_id
      - name: created_at
      - name: creator_id
      - name: device
      - name: payment_url
      - name: receipt_url
      - name: inclusive_tax_money
      - name: additive_tax_money
      - name: tax_money
      - name: tip_money
      - name: discount_money
      - name: total_collected_money
      - name: processing_fee_money
      - name: net_total_money
      - name: refunded_money
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-paymenttax" target="new">inclusive_tax</a><code>*</code>
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-paymenttax" target="new">additive_tax</a><code>*</code>
      - name: tender<code>*</code>
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-refund" target="new">refunds</a><code>*</code>
      - name: <a href="https://docs.connect.squareup.com/api/connect/v1/#datatype-paymentitemization" target="new">itemizations</a><code>*</code>



## Refunds
  - name: "square_refunds"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-refund
    description: "the details for all refunds initiated by a merchant or any of the merchant’s mobile staff."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "payment_id:created_at"
    nested-structures: false
    attributes:
      - name: payment_id
      - name: created_at
      - name: type
      - name: reason
      - name: refunded_money
      - name: processed_at


## Roles
  - name: "square_roles"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-employeerole
    description: "summary info for all of a business’s employee roles."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Role ID (<code>id</code>)
      - name: name
      - name: permissions<code>*</code>
      - name: is_owner
      - name: created_at
      - name: updated_at


## Settlements
  - name: "square_square_settlements"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#get-settlements
    description: "summary information for all deposits and withdraws initiated by Square to a merchant’s bank account. <strong>This table does not contain entry data</strong>, which lists the individual transactions that contribute to the settlement total."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Settlement ID (<code>id</code>)
      - name: status
      - name: bank_account_id
      - name: initiated_at
      - name: total_money__amount
      - name: total_money__currency_code


## Timecards
  - name: "square_square_timecards"
    doc-link: https://docs.connect.squareup.com/api/connect/v1/#datatype-timecard
    description: "summary info for all of a business’s employee timecards."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Timecard ID (<code>id</code>)
      - name: employee_id
      - name: deleted
      - name: clockin_time
      - name: clockout_time
      - name: clockin_location_id
      - name: clockout_location_id
      - name: created_at
      - name: updated_at
---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your Square data to Stitch a four-step process:

1. [Add Square as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)
5. [Authorize Stitch to access Square](#authorize-stitch)

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorizing Stitch to Access Square {#authorize-stitch}

Lastly, you'll be directed to Square's website to complete the setup.

1. Enter your Square credentials and click **Login**.
2. After the authorization process successfully completes, you'll be redirected back to Stitch.
3. Click {{ app.buttons.finish-int-setup }}.

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
