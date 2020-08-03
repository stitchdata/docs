---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-location-map"

name: "item_location_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_location_map.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "atp_lead_time"
    type: "integer"
    description: ""

  - name: "available_count"
    type: "integer"
    description: ""

  - name: "average_cost"
    type: "number"
    description: ""

  - name: "backward_consumption_days"
    type: "integer"
    description: ""

  - name: "cost_0"
    type: "number"
    description: ""

  - name: "cost_accounting_status"
    type: "string"
    description: ""

  - name: "costing_lot_size"
    type: "integer"
    description: ""

  - name: "default_return_cost"
    type: "number"
    description: ""

  - name: "demand_source"
    type: "string"
    description: ""

  - name: "demand_time_fence"
    type: "integer"
    description: ""

  - name: "fixed_lot_size"
    type: "integer"
    description: ""

  - name: "forward_consumption_days"
    type: "integer"
    description: ""

  - name: "in_transit_count"
    type: "number"
    description: ""

  - name: "inventory_cost_template"
    type: "integer"
    description: ""

  - name: "invt_count_classification"
    type: "integer"
    description: ""

  - name: "invt_count_interval"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
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

  - name: "lot_sizing_method"
    type: "string"
    description: ""

  - name: "next_invt_count_date"
    type: "date-time"
    description: ""

  - name: "ns_lead_time"
    type: "integer"
    description: ""

  - name: "on_hand_count"
    type: "number"
    description: ""

  - name: "on_hand_value"
    type: "number"
    description: ""

  - name: "on_order_count"
    type: "number"
    description: ""

  - name: "periodic_lot_size_days"
    type: "integer"
    description: ""

  - name: "periodic_lot_size_type"
    type: "string"
    description: ""

  - name: "pref_stock_level"
    type: "integer"
    description: ""

  - name: "quantitybackordered"
    type: "integer"
    description: ""

  - name: "reorder_point"
    type: "number"
    description: ""

  - name: "reschedule_in_days"
    type: "integer"
    description: ""

  - name: "reschedule_out_days"
    type: "integer"
    description: ""

  - name: "safety_stock_level"
    type: "integer"
    description: ""

  - name: "supply_time_fence"
    type: "integer"
    description: ""

  - name: "supply_type"
    type: "string"
    description: ""

  - name: "wip"
    type: "string"
    description: ""
---