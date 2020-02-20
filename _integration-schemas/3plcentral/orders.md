---
tap: "3plcentral"
version: "1"

name: "orders"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/orders.json"
description: "This table contains information about orders."

replication-method: "Key-based Incremental"

api-method:
    name: "Get orders"
    doc-link: "http://api.3plcentral.com/rels/orders/orders"

attributes:
  - name: "order_id"
    type: "integer"
    primary-key: true
    description: "The order ID."
    #foreign-key-id: "order-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The time the order was last modified."
    replication-key: true  

  - name: "add_freight_to_cod"
    type: "boolean"
    description: ""

  - name: "asn_candidate"
    type: "integer"
    description: ""

  - name: "asn_number"
    type: "string"
    description: ""

  - name: "asn_sent"
    type: "boolean"
    description: ""

  - name: "asn_sent_date"
    type: "date-time"
    description: ""

  - name: "batch_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "name_key"
        type: "object"
        description: ""
        subattributes:
          - name: "customer_identifier"
            type: "object"
            description: ""
            subattributes: &customer-identifier
              - name: "external_id"
                type: "string"
                description: ""

              - name: "id"
                type: "integer"
                description: "The customer ID."
                foreign-key-id: "customer-id"

              - name: "name"
                type: "string"
                description: ""

          - name: "name"
            type: "string"
            description: ""

  - name: "bill_to"
    type: "object"
    description: ""
    subattributes: &bill-to
      - name: "address1"
        type: "string"
        description: ""
        
      - name: "address2"
        type: "string"
        description: ""

      - name: "address_status"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "code"
        type: "string"
        description: ""

      - name: "company_name"
        type: "string"
        description: ""

      - name: "contact_id"
        type: "integer"
        description: ""

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

      - name: "is_quick_lookup"
        type: "boolean"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phone_number"
        type: "string"
        description: ""

      - name: "retailer_id"
        type: "integer"
        description: ""

      - name: "same_as"
        type: "integer"
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

  - name: "billing"
    type: "object"
    description: ""
    subattributes:
      - name: "billing_charges"
        type: "array"
        description: ""
        subattributes:
          - name: "charge_label"
            type: "string"
            description: ""

          - name: "charge_per_unit"
            type: "number"
            description: ""

          - name: "gl_acct_num"
            type: "string"
            description: ""

          - name: "num_units"
            type: "number"
            description: ""

          - name: "pt_ar_acct"
            type: "string"
            description: ""

          - name: "pt_item"
            type: "string"
            description: ""

          - name: "pt_item_description"
            type: "string"
            description: ""

          - name: "sku"
            type: "string"
            description: ""

          - name: "system_generated"
            type: "boolean"
            description: ""

          - name: "unit_description"
            type: "string"
            description: ""

          - name: "warehouse_transaction_price_calc_id"
            type: "integer"
            description: ""

  - name: "billing_code"
    type: "string"
    description: ""

  - name: "created_by_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "customer_identifier"
    type: "object"
    description: "Details about the customer associated with the order."
    subattributes: *customer-identifier

  - name: "defer_notification"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "earliest_ship_date"
    type: "date-time"
    description: ""

  - name: "export_channel_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "export_module_ids"
    type: "string"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "facility_identifier"
    type: "object"
    description: ""
    subattributes: &facility-identifier
      - name: "id"
        type: "integer"
        description: "The facility ID."
        foreign-key-id: "facility-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "fulfill_inv_info"
    type: "object"
    description: ""
    subattributes:
      - name: "fulfill_inv_amount"
        type: "number"
        description: ""

      - name: "fulfill_inv_discount_code"
        type: "string"
        description: ""

      - name: "fulfill_inv_message"
        type: "string"
        description: ""

      - name: "fulfill_inv_shipping_and_handling"
        type: "number"
        description: ""

      - name: "fulfill_inv_tax"
        type: "number"
        description: ""

  - name: "fully_allocated"
    type: "boolean"
    description: ""

  - name: "import_channel_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "invoice_delivered_date"
    type: "date-time"
    description: ""

  - name: "invoice_exported_date"
    type: "date-time"
    description: ""

  - name: "invoice_number"
    type: "string"
    description: ""

  - name: "is_closed"
    type: "boolean"
    description: ""

  - name: "labels_exported"
    type: "boolean"
    description: ""

  - name: "last_modified_by_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "load_out_done_date"
    type: "date-time"
    description: ""

  - name: "loaded_state"
    type: "integer"
    description: ""

  - name: "master_billing_of_lading_id"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "num_units"
    type: "number"
    description: ""

  - name: "order_items"
    type: "null"
    description: ""

  - name: "outbound_serial_numbers"
    type: "null"
    description: ""

  - name: "pack_done_date"
    type: "date-time"
    description: ""

  - name: "packages"
    type: "null"
    description: ""

  - name: "parcel_label_type"
    type: "integer"
    description: ""

  - name: "pick_done_date"
    type: "date-time"
    description: ""

  - name: "pick_ticket_print_date"
    type: "date-time"
    description: ""

  - name: "pkgs_exported"
    type: "boolean"
    description: ""

  - name: "po_num"
    type: "string"
    description: ""

  - name: "process_date"
    type: "date-time"
    description: ""

  - name: "reallocated_after_pick_ticket_date"
    type: "date-time"
    description: ""

  - name: "reference_num"
    type: "string"
    description: ""

  - name: "route_candidate"
    type: "integer"
    description: ""

  - name: "route_pickup_date"
    type: "date-time"
    description: ""

  - name: "route_sent"
    type: "boolean"
    description: ""

  - name: "routing_info"
    type: "object"
    description: ""
    subattributes:
      - name: "account"
        type: "string"
        description: ""
      - name: "bill_of_lading"
        type: "string"
        description: ""
      - name: "capacity_identifier"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""
          - name: "name"
            type: "string"
            description: ""
      - name: "carrier"
        type: "string"
        description: ""
      - name: "door_number"
        type: "string"
        description: ""
      - name: "is_cod"
        type: "boolean"
        description: ""
      - name: "is_insurance"
        type: "boolean"
        description: ""
      - name: "load_number"
        type: "string"
        description: ""
      - name: "mode"
        type: "string"
        description: ""
      - name: "pickup_date"
        type: "date-time"
        description: ""
      - name: "required_delivery_conf"
        type: "boolean"
        description: ""
      - name: "required_return_receipt"
        type: "boolean"
        description: ""
      - name: "scac_code"
        type: "string"
        description: ""
      - name: "seal_number"
        type: "string"
        description: ""
      - name: "ship_point_zip"
        type: "string"
        description: ""
      - name: "tracking_number"
        type: "string"
        description: ""
      - name: "trailer_number"
        type: "string"
        description: ""

  - name: "saved_elements"
    type: "null"
    description: ""

  - name: "ship_cancel_date"
    type: "date-time"
    description: ""

  - name: "ship_to"
    type: "object"
    description: ""
    subattributes:
      - name: "address1"
        type: "string"
        description: ""
      - name: "address2"
        type: "string"
        description: ""
      - name: "address_status"
        type: "string"
        description: ""
      - name: "city"
        type: "string"
        description: ""
      - name: "code"
        type: "string"
        description: ""
      - name: "company_name"
        type: "string"
        description: ""
      - name: "contact_id"
        type: "integer"
        description: ""
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
      - name: "is_quick_lookup"
        type: "boolean"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "phone_number"
        type: "string"
        description: ""
      - name: "retailer_id"
        type: "integer"
        description: ""
      - name: "retailer_info"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""

          - name: "name_key"
            type: "object"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "customer_identifier"
                type: "object"
                description: ""
                anchor-id: 1
                subattributes: *customer-identifier

              - name: "name"
                type: "string"
                description: ""

              - name: "number"
                type: "string"
                description: ""

      - name: "same_as"
        type: "integer"
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

  - name: "shipping_notes"
    type: "string"
    description: ""

  - name: "sold_to"
    type: "object"
    description: ""
    subattributes: *bill-to

  - name: "status"
    type: "integer"
    description: ""

  - name: "total_volume"
    type: "number"
    description: ""

  - name: "total_weight"
    type: "number"
    description: ""

  - name: "transaction_entry_type"
    type: "integer"
    description: ""

  - name: "unit2_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "up_service_option_charge"
    type: "number"
    description: ""

  - name: "up_transportation_charge"
    type: "number"
    description: ""

  - name: "ups_is_residential"
    type: "number"
    description: ""

  - name: "warehouse_transaction_source_type"
    type: "integer"
    description: ""
---