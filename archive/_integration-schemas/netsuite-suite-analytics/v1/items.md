---
tap: "netsuite-suite-analytics"
version: "1"
key: "item"

name: "items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "allow_drop_ship"
    type: "string"
    description: ""

  - name: "alt_demand_source_item_id"
    type: "integer"
    description: ""

  - name: "asset_account_id"
    type: "integer"
    description: ""

  - name: "atp_lead_time"
    type: "integer"
    description: ""

  - name: "atp_method"
    type: "string"
    description: ""

  - name: "available_to_partners"
    type: "string"
    description: ""

  - name: "averagecost"
    type: "number"
    description: ""

  - name: "backward_consumption_days"
    type: "integer"
    description: ""

  - name: "bill_exch_rate_var_account_id"
    type: "integer"
    description: ""

  - name: "bill_price_variance_account_id"
    type: "integer"
    description: ""

  - name: "bill_qty_variance_account_id"
    type: "integer"
    description: ""

  - name: "build_sub_assemblies"
    type: "string"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""

  - name: "consumption_unit_id"
    type: "integer"
    description: ""

  - name: "cost_0"
    type: "number"
    description: ""

  - name: "cost_category"
    type: "string"
    description: ""

  - name: "cost_estimate_type"
    type: "string"
    description: ""

  - name: "costing_method"
    type: "string"
    description: ""

  - name: "country_of_manufacture"
    type: "string"
    description: ""

  - name: "create_plan_on_event_type"
    type: "string"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "current_on_order_count"
    type: "number"
    description: ""

  - name: "custreturn_variance_account_id"
    type: "integer"
    description: ""

  - name: "date_of_last_transaction"
    type: "date-time"
    description: ""

  - name: "default_return_cost"
    type: "number"
    description: ""

  - name: "deferred_expense_account_id"
    type: "integer"
    description: ""

  - name: "deferred_revenue_account_id"
    type: "integer"
    description: ""

  - name: "demand_source"
    type: "string"
    description: ""

  - name: "demand_time_fence"
    type: "integer"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""

  - name: "deposit"
    type: "string"
    description: ""

  - name: "displayname"
    type: "string"
    description: ""

  - name: "distribution_category"
    type: "string"
    description: ""

  - name: "distribution_network"
    type: "string"
    description: ""

  - name: "dropship_expense_account_id"
    type: "integer"
    description: ""

  - name: "effective_bom_control_type"
    type: "string"
    description: ""

  - name: "expense_account_id"
    type: "integer"
    description: ""

  - name: "featureddescription"
    type: "string"
    description: ""

  - name: "featureditem"
    type: "string"
    description: ""

  - name: "fixed_lot_size"
    type: "integer"
    description: ""

  - name: "forward_consumption_days"
    type: "integer"
    description: ""

  - name: "fraud_risk"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "fx_adjustment_account_id"
    type: "integer"
    description: ""

  - name: "gain_loss_account_id"
    type: "integer"
    description: ""

  - name: "handling_cost"
    type: "number"
    description: ""

  - name: "hazmat"
    type: "string"
    description: ""

  - name: "hazmat_hazard_class"
    type: "string"
    description: ""

  - name: "hazmat_id"
    type: "string"
    description: ""

  - name: "hazmat_item_units"
    type: "string"
    description: ""

  - name: "hazmat_item_units_qty"
    type: "integer"
    description: ""

  - name: "hazmat_packing_group"
    type: "string"
    description: ""

  - name: "hazmat_shipping_name"
    type: "string"
    description: ""

  - name: "include_child_subsidiaries"
    type: "string"
    description: ""

  - name: "income_account_id"
    type: "integer"
    description: ""

  - name: "interco_expense_account_id"
    type: "integer"
    description: ""

  - name: "interco_income_account_id"
    type: "integer"
    description: ""

  - name: "invt_count_classification"
    type: "integer"
    description: ""

  - name: "invt_count_interval"
    type: "integer"
    description: ""

  - name: "is_cont_rev_handling"
    type: "string"
    description: ""

  - name: "is_enforce_min_qty_internally"
    type: "string"
    description: ""

  - name: "is_hold_rev_rec"
    type: "string"
    description: ""

  - name: "is_moss"
    type: "string"
    description: ""

  - name: "is_phantom"
    type: "string"
    description: ""

  - name: "is_special_order_item"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "istaxable"
    type: "string"
    description: ""

  - name: "item_defined_cost"
    type: "number"
    description: ""

  - name: "item_extid"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "item-id"

  - name: "item_revenue_category"
    type: "string"
    description: ""

  - name: "last_cogs_correction"
    type: "date-time"
    description: ""

  - name: "last_invt_count_date"
    type: "date-time"
    description: ""

  - name: "last_purchase_price"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "lot_numbered_item"
    type: "string"
    description: ""

  - name: "lot_sizing_method"
    type: "string"
    description: ""

  - name: "manufacturer"
    type: "string"
    description: ""

  - name: "manufacturing_charge_item"
    type: "string"
    description: ""

  - name: "match_bill_to_receipt"
    type: "string"
    description: ""

  - name: "matrix_type"
    type: "string"
    description: ""

  - name: "maximum_quantity"
    type: "integer"
    description: ""

  - name: "minimum_quantity"
    type: "integer"
    description: ""

  - name: "modified"
    type: "date-time"
    description: ""

  - name: "mpn"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "next_invt_count_date"
    type: "date-time"
    description: ""

  - name: "ns_lead_time"
    type: "integer"
    description: ""

  - name: "offersupport"
    type: "string"
    description: ""

  - name: "onspecial"
    type: "string"
    description: ""

  - name: "overhead_type"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "payment_method_id"
    type: "integer"
    description: ""

  - name: "periodic_lot_size_days"
    type: "integer"
    description: ""

  - name: "periodic_lot_size_type"
    type: "string"
    description: ""

  - name: "pref_purchase_tax_id"
    type: "integer"
    description: ""

  - name: "pref_sale_tax_id"
    type: "integer"
    description: ""

  - name: "pref_stock_level"
    type: "integer"
    description: ""

  - name: "prices_include_tax"
    type: "string"
    description: ""

  - name: "pricing_group_id"
    type: "integer"
    description: ""

  - name: "print_sub_items"
    type: "string"
    description: ""

  - name: "prod_price_var_account_id"
    type: "integer"
    description: ""

  - name: "prod_qty_var_account_id"
    type: "integer"
    description: ""

  - name: "purchase_price_var_account_id"
    type: "integer"
    description: ""

  - name: "purchase_unit_id"
    type: "integer"
    description: ""

  - name: "purchasedescription"
    type: "string"
    description: ""

  - name: "purchaseorderamount"
    type: "number"
    description: ""

  - name: "purchaseorderquantity"
    type: "number"
    description: ""

  - name: "purchaseorderquantitydiff"
    type: "number"
    description: ""

  - name: "quantityavailable"
    type: "integer"
    description: ""

  - name: "quantitybackordered"
    type: "integer"
    description: ""

  - name: "quantityonhand"
    type: "number"
    description: ""

  - name: "receiptamount"
    type: "number"
    description: ""

  - name: "receiptquantity"
    type: "number"
    description: ""

  - name: "receiptquantitydiff"
    type: "number"
    description: ""

  - name: "reorder_multiple"
    type: "integer"
    description: ""

  - name: "reorderpoint"
    type: "number"
    description: ""

  - name: "replenishment_method"
    type: "string"
    description: ""

  - name: "resalable"
    type: "string"
    description: ""

  - name: "reschedule_in_days"
    type: "integer"
    description: ""

  - name: "reschedule_out_days"
    type: "integer"
    description: ""

  - name: "rev_rec_forecast_rule_id"
    type: "integer"
    description: ""

  - name: "rev_rec_rule_id"
    type: "integer"
    description: ""

  - name: "revenue_allocation_group"
    type: "string"
    description: ""

  - name: "round_up_as_component"
    type: "string"
    description: ""

  - name: "safety_stock_days"
    type: "integer"
    description: ""

  - name: "safety_stock_level"
    type: "integer"
    description: ""

  - name: "sale_unit_id"
    type: "integer"
    description: ""

  - name: "salesdescription"
    type: "string"
    description: ""

  - name: "salesprice"
    type: "string"
    description: ""

  - name: "scrap_account_id"
    type: "integer"
    description: ""

  - name: "serialized_item"
    type: "string"
    description: ""

  - name: "shippingcost"
    type: "number"
    description: ""

  - name: "special_work_order_item"
    type: "string"
    description: ""

  - name: "specialsdescription"
    type: "string"
    description: ""

  - name: "stock_unit_id"
    type: "integer"
    description: ""

  - name: "storedescription"
    type: "string"
    description: ""

  - name: "storedetaileddescription"
    type: "string"
    description: ""

  - name: "storedisplayname"
    type: "string"
    description: ""

  - name: "subtype"
    type: "string"
    description: ""

  - name: "supply_time_fence"
    type: "integer"
    description: ""

  - name: "supply_type"
    type: "string"
    description: ""

  - name: "tax_item_id"
    type: "integer"
    description: ""

  - name: "totalvalue"
    type: "number"
    description: ""

  - name: "transferprice"
    type: "number"
    description: ""

  - name: "type_name"
    type: "string"
    description: ""

  - name: "unbuild_variance_account_id"
    type: "integer"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""

  - name: "upc_code"
    type: "string"
    description: ""

  - name: "use_component_yield"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""

  - name: "vendorname"
    type: "string"
    description: ""

  - name: "vendreturn_variance_account_id"
    type: "integer"
    description: ""

  - name: "vsoe_deferral"
    type: "string"
    description: ""

  - name: "vsoe_delivered"
    type: "string"
    description: ""

  - name: "vsoe_discount"
    type: "string"
    description: ""

  - name: "vsoe_price"
    type: "number"
    description: ""

  - name: "weight"
    type: "number"
    description: ""

  - name: "weight_in_user_defined_unit"
    type: "integer"
    description: ""

  - name: "weight_unit_index"
    type: "integer"
    description: ""

  - name: "wip_account_id"
    type: "integer"
    description: ""

  - name: "wip_cost_variance_account_id"
    type: "integer"
    description: ""

  - name: "work_order_lead_time"
    type: "integer"
    description: ""
---