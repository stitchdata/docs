---
tap: "3plcentral"
version: "1.0"

name: "customers"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/customers.json"
description: "This table contains information about customers."

replication-method: "Full Table"

api-method:
    name: "Get customers"
    doc-link: "http://api.3plcentral.com/rels/customers/customers"
attributes:
  - name: "customer_id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"
    
  - name: "company_info"
    type: "object"
    description: |
      Details about the company associated with the customer.

      When identifying an existing contact, the lookup order is: 

      1. `id`
      2. `code`, if no other fields are present
      3. All fields except `id`

      If `contact_id` is not specified and other fields do not match an existing contact for the relevant customer, a new contact is created.
    subattributes:
      - name: "address1"
        type: "string"
        description: ""
      - name: "address2"
        type: "string"
        description: ""
      
      - &address_status
        name: "address_status"
        type: "integer"
        description: |
          The confirmation status. Possible values are: 

          - `0` - Unconfirmed
          - `1` - Confirmed
          - `2` - UserAccepted
      
      - name: "city"
        type: "string"
        description: ""
      
      - &code
        name: "code"
        type: "string"
        description: "The company code. This is used an identifier. If known, only this field is used. If other fields are specified, then the code is not used as the identifier."
      
      - name: "company_name"
        type: "string"
        description: ""
      
      - &contact_id
        name: "contact_id"
        type: "integer"
        description: "The contact ID. If the contact ID is known, then other fields are ignored."
      
      - name: "country"
        type: "string"
        description: ""
      - name: "dept"
        type: "string"
        description: ""
      - name: "email_address"
        type: "string"
        description: ""
      - name: "fax"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "phone_number"
        type: "string"
        description: ""
      - name: "state"
        type: "string"
        description: ""
      - name: "title"
        type: "string"
        description: ""
      - name: "zip"
        type: "string"
        description: ""

  - name: "creation_date"
    type: "date-time"
    description: "The date the customer was created."

  - name: "deactivated"
    type: "boolean"
    description: ""

  - name: "external_id"
    type: "string"
    description: "The ID of the customer on another system."

  - name: "facilities"
    type: "array"
    description: "The list of facilities the customer's items are stored in. The first in the list is the primary facility."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: "The facility ID."
        foreign-key-id: "facility-id"   

  - name: "groups"
    type: "string"
    description: "The list of groups this customer belongs to."

  - name: "options"
    type: "object"
    description: "The customer's preferences."
    subattributes:
      - name: "alerts"
        type: "object"
        description: ""
        subattributes:
          - name: "expiration_notification_threshold"
            type: "integer"
            description: ""
          - name: "from_email_address"
            type: "string"
            description: ""
          - name: "notify_ship_to"
            type: "boolean"
            description: ""
      - name: "edi"
        type: "object"
        description: ""
        subattributes:
          - name: "customer_interchange_id"
            type: "string"
            description: ""
          - name: "customer_interchange_id_qual"
            type: "string"
            description: ""
          - name: "threepl_interchange_id"
            type: "string"
            description: ""
          - name: "threepl_interchange_id_qual"
            type: "string"
            description: ""
          - name: "trading_partner_id"
            type: "string"
            description: ""
      - name: "other_system_behaviors"
        type: "object"
        description: ""
        subattributes:
          - name: "flex_fields"
            type: "boolean"
            description: ""
          - name: "require_attached_documents"
            type: "boolean"
            description: ""
      - name: "packaging"
        type: "object"
        description: ""
        subattributes:
          - name: "small_parcel_create_packages_on_find"
            type: "boolean"
            description: ""
          - name: "small_parcel_customize_duties"
            type: "boolean"
            description: ""
          - name: "small_parcel_duties_and_taxes"
            type: "string"
            description: ""
          - name: "small_parcel_duty_billing_type"
            type: "string"
            description: ""
          - name: "small_parcel_high_volume_default_checked"
            type: "boolean"
            description: ""
          - name: "small_parcel_high_volume_zpl_batched"
            type: "boolean"
            description: ""
          - name: "small_parcel_rate_shopping_carrier_ids"
            type: "string"
            description: ""
          - name: "small_parcel_rate_shopping_logic"
            type: "string"
            description: ""
          - name: "small_parcel_references"
            type: "string"
            description: ""
          - name: "small_parcel_return_default_checked"
            type: "boolean"
            description: ""
          - name: "small_parcel_return_fed_ex_service"
            type: "string"
            description: ""
          - name: "small_parcel_return_shipping_cost"
            type: "boolean"
            description: ""
          - name: "small_parcel_return_ups_service"
            type: "string"
            description: ""
          - name: "small_parcel_usps_3rd_party"
            type: "string"
            description: ""
          - name: "small_parcel_usps_return_type"
            type: "string"
            description: ""
          - name: "sps_close_on_update"
            type: "boolean"
            description: ""
          - name: "ucc128_manufacturers_id"
            type: "integer"
            description: ""
          - name: "use_vendor_id_on_bol"
            type: "boolean"
            description: ""
      - name: "receivers"
        type: "object"
        description: ""
        subattributes:
          - name: "defs"
            type: "null"
            description: ""
          - name: "item_defs"
            type: "null"
            description: ""
      - name: "receiving"
        type: "object"
        description: ""
        subattributes:
          - name: "autofill_track_bys"
            type: "boolean"
            description: ""
          - name: "create_multiple_mus"
            type: "boolean"
            description: ""
          - name: "inherit_original_receipt_date_on_transfer"
            type: "boolean"
            description: ""
          - name: "purchase_orders"
            type: "boolean"
            description: ""
          - name: "receive_against_asns"
            type: "integer"
            description: &receiving-values |
              Possible values are: 
              - `0` - Disabled
              - `1` - Enabled
              - `2` - Blind
          - name: "require_scac_for_asn"
            type: "boolean"
            description: ""
          - name: "suggest_put_away_enabled"
            type: "boolean"
            description: ""
          - name: "track_location"
            type: "integer"
            description: &track-values |
              Possible vlaues are:

              - `0` - Disallow
              - `1` - Allow
              - `2` - Require

          - name: "track_pallets"
            type: "integer"
            description: *track-values
          - name: "track_supplier"
            type: "integer"
            description: *track-values
      - name: "saved_elements"
        type: "object"
        description: ""
        subattributes:
          - name: "orders"
            type: "object"
            description: ""
            subattributes:
              - name: "defs"
                type: "array"
                description: ""
                subattributes:
                  - name: "name"
                    type: "string"
                    description: ""
                  - name: "required"
                    type: "boolean"
                    description: ""   
              - name: "item_defs"
                type: "array"
                description: ""
                subattributes:
                  - name: "name"
                    type: "string"
                    description: ""
                  - name: "required"
                    type: "boolean"
                    description: ""  
      - name: "shipping"
        type: "object"
        description: ""
        subattributes:
          - name: "auto_confirm_order_on_tracking_update"
            type: "boolean"
            description: ""
          - name: "bol_num_as_trans_num"
            type: "boolean"
            description: ""
          - name: "fed_ex_account_number"
            type: "string"
            description: ""
          - name: "fulfillment_invoicing"
            type: "integer"
            description: &fulfillment-values |
              Possible values are:
              - `0` - Disabled
              - `1` - Enabled
              - `2` - Prepoulated
          - name: "next_master_bol_id"
            type: "integer"
            description: ""
          - name: "next_master_bol_id_override"
            type: "integer"
            description: ""
          - name: "order_queue"
            type: "boolean"
            description: ""
          - name: "packing_list_footer_url"
            type: "string"
            description: ""
          - name: "packing_list_logo_url"
            type: "string"
            description: ""
          - name: "prepopulate_carrier_info"
            type: "integer"
            description: &prepopulate-carrier-values |
              Possible values are:

              - `0` - Off
              - `1` - On
              - `2` - PrepaidOnly
              - `3` - ThirdPartyOnly

          - name: "require_tracking_number"
            type: "boolean"
            description: ""
          - name: "roundupto_full_mu"
            type: "boolean"
            description: ""
          - name: "ups_account_number"
            type: "string"
            description: ""
          - name: "ups_account_zip"
            type: "string"
            description: ""
      - name: "storage"
        type: "object"
        description: ""
        subattributes:
          - name: "accounting_customer_name"
            type: "string"
            description: ""
          - name: "autofill_charges_on_confirm"
            type: "boolean"
            description: ""
          - name: "fuel_surcharge"
            type: "number"
            description: "This value is a positive integer percentage."
          - name: "set_invoice_date_to_xaction_confirm_date"
            type: "boolean"
            description: ""
      - name: "user_interface"
        type: "object"
        description: ""
        subattributes:
          - name: "auto_check_auto_reallocate_on_receive"
            type: "boolean"
            description: ""
          - name: "branding_image_id"
            type: "integer"
            description: ""
          - name: "dashboard"
            type: "boolean"
            description: ""
          - name: "exclude_location_with_zero_inventory"
            type: "boolean"
            description: ""
          - name: "hide_location_selected_list"
            type: "boolean"
            description: ""
          - name: "mobile_receipt_quantity_one_default"
            type: "boolean"
            description: ""
          - name: "reallocate_at_pick_time"
            type: "boolean"
            description: ""
          - name: "transaction_confirm_invoice_create_default"
            type: "integer"
            description: &transaction-confirm-values |
              Possible values are:

              - `0` - Off
              - `1` - On
              - `2` - ReceiversOnly
              - `3` - OrdersOnly

  - name: "other_contacts"
    type: "object"
    description: "Customer contacts where the contact type is other than primary."
    subattributes:
      - name: "type"
        type: "integer"
        description: &contact-type-values |
          The customer contact type. Possible values are:

          - `2` - Invoicing
          - `3` - Additional
          - `4` - For753
          - `5` - SmallParcelReturnLabel

      - name: "address1"
        type: "string"
        description: ""
      - name: "address2"
        type: "string"
        description: ""
      - *address_status
      - name: "city"
        type: "string"
        description: ""
      - *code
      - name: "company_name"
        type: "string"
        description: ""
      - *contact_id
      - name: "country"
        type: "string"
        description: ""
      - name: "dept"
        type: "string"
        description: ""
      - name: "email_address"
        type: "string"
        description: ""
      - name: "fax"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "phone_number"
        type: "string"
        description: ""
      - name: "state"
        type: "string"
        description: ""
      - name: "title"
        type: "string"
        description: ""
      - name: "zip"
        type: "string"
        description: ""

  - name: "primary_contact"
    type: "object"
    description: ""
    subattributes:
      - name: "address1"
        type: "string"
        description: ""
      - name: "address2"
        type: "string"
        description: ""
      - *address_status
      - name: "city"
        type: "string"
        description: ""
      - *code
      - name: "company_name"
        type: "string"
        description: ""
      - *contact_id
      - name: "country"
        type: "string"
        description: ""
      - name: "dept"
        type: "string"
        description: ""
      - name: "email_address"
        type: "string"
        description: ""
      - name: "fax"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "phone_number"
        type: "string"
        description: ""
      - name: "state"
        type: "string"
        description: ""
      - name: "title"
        type: "string"
        description: ""
      - name: "zip"
        type: "string"
        description: ""

  - name: "primary_facility_identifier"
    type: "object"
    description: "The primary facility."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The facility ID."
        foreign-key-id: "facility-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "website"
    type: "string"
    description: "The customer's business website."
---