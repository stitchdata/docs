---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-fulfillment"

name: "item_fulfillments"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemfulfillment.html"
description: ""

replication-method: ""

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "accounting_period_id"
    type: "integer"
    description: ""

  - name: "ancillary_endorsement"
    type: "string"
    description: ""

  - name: "b13a_filling_option"
    type: "string"
    description: ""

  - name: "b13a_statement_data"
    type: "string"
    description: ""

  - name: "backup_ship_notification_email"
    type: "string"
    description: ""

  - name: "billaddress"
    type: "string"
    description: ""

  - name: "booking_confirmation_number"
    type: "string"
    description: ""

  - name: "carrier_identification_code"
    type: "string"
    description: ""

  - name: "created_by_id"
    type: "integer"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "date_blanket_period_end"
    type: "date-time"
    description: ""

  - name: "date_blanket_period_start"
    type: "date-time"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_future_shipping"
    type: "date-time"
    description: ""

  - name: "date_home_delivery"
    type: "date-time"
    description: ""

  - name: "date_license"
    type: "date-time"
    description: ""

  - name: "date_sales_effective"
    type: "date-time"
    description: ""

  - name: "date_transaction"
    type: "date-time"
    description: ""

  - name: "delivery_instructions"
    type: "string"
    description: ""

  - name: "eccn"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "entry_number"
    type: "string"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "export_type"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "fedex_ship_alert"
    type: "string"
    description: ""

  - name: "fob"
    type: "string"
    description: ""

  - name: "handling_cost"
    type: "integer"
    description: ""

  - name: "has_cert_of_origin"
    type: "string"
    description: ""

  - name: "has_commercial_invoice"
    type: "string"
    description: ""

  - name: "has_nafta_cert_of_origin"
    type: "string"
    description: ""

  - name: "has_pro_forma_invoice"
    type: "string"
    description: ""

  - name: "hold_at_location_address_one"
    type: "string"
    description: ""

  - name: "hold_at_location_address_three"
    type: "string"
    description: ""

  - name: "hold_at_location_address_two"
    type: "string"
    description: ""

  - name: "hold_at_location_city"
    type: "string"
    description: ""

  - name: "hold_at_location_country"
    type: "string"
    description: ""

  - name: "hold_at_location_loc_phone"
    type: "string"
    description: ""

  - name: "hold_at_location_phone"
    type: "string"
    description: ""

  - name: "hold_at_location_state"
    type: "string"
    description: ""

  - name: "hold_at_location_zip"
    type: "string"
    description: ""

  - name: "home_delivery_type"
    type: "string"
    description: ""

  - name: "in_bond_code"
    type: "string"
    description: ""

  - name: "international_exemption_number"
    type: "string"
    description: ""

  - name: "is_certified_mail"
    type: "string"
    description: ""

  - name: "is_fdx_signature_home_delivery"
    type: "string"
    description: ""

  - name: "is_held_at_location"
    type: "string"
    description: ""

  - name: "is_holiday_delivery"
    type: "string"
    description: ""

  - name: "is_inside_delivery"
    type: "string"
    description: ""

  - name: "is_inside_pickup"
    type: "string"
    description: ""

  - name: "is_intercompany"
    type: "string"
    description: ""

  - name: "is_memorized"
    type: "string"
    description: ""

  - name: "is_online_bill_pay"
    type: "string"
    description: ""

  - name: "is_related_parties_transaction"
    type: "string"
    description: ""

  - name: "is_routed_export_transaction"
    type: "string"
    description: ""

  - name: "is_saturday_delivery"
    type: "string"
    description: ""

  - name: "is_saturday_pickup"
    type: "string"
    description: ""

  - name: "is_saturday_service"
    type: "string"
    description: ""

  - name: "is_tax_reg_override"
    type: "string"
    description: ""

  - name: "is_visible_in_customer_center"
    type: "string"
    description: ""

  - name: "is_weekend_delivery"
    type: "string"
    description: ""

  - name: "license_exception"
    type: "string"
    description: ""

  - name: "license_number"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "method_of_transport"
    type: "string"
    description: ""

  - name: "needs_bill"
    type: "string"
    description: ""

  - name: "notification_email_message"
    type: "string"
    description: ""

  - name: "promotion_code_id"
    type: "integer"
    description: ""

  - name: "reason_for_export"
    type: "string"
    description: ""

  - name: "recipient_customs_id"
    type: "string"
    description: ""

  - name: "recipient_customs_id_type"
    type: "string"
    description: ""

  - name: "recipient_tax_id"
    type: "string"
    description: ""

  - name: "related_tranid"
    type: "string"
    description: ""

  - name: "return_type"
    type: "string"
    description: ""

  - name: "return_type_description"
    type: "string"
    description: ""

  - name: "ship_notification_email"
    type: "string"
    description: ""

  - name: "ship_notification_email_two"
    type: "string"
    description: ""

  - name: "shipaddress"
    type: "string"
    description: ""

  - name: "shipping_cost"
    type: "integer"
    description: ""

  - name: "shipping_item_id"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_reg_id"
    type: "integer"
    description: ""

  - name: "terms_freight_charge"
    type: "integer"
    description: ""

  - name: "terms_insurance_charge"
    type: "integer"
    description: ""

  - name: "terms_of_sale"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "total_package_weight_in_lbs"
    type: "integer"
    description: ""

  - name: "tranid"
    type: "string"
    description: ""

  - name: "transaction_extid"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "transfer_location_id"
    type: "integer"
    description: ""

  - name: "use_backup_email"
    type: "string"
    description: ""

  - name: "use_fedex_ship_alert"
    type: "string"
    description: ""

  - name: "use_ship_notification_email"
    type: "string"
    description: ""
---