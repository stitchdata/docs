---
tap: "google-ads"
version: "1"
name: "mobile_device_constant"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/MobileDeviceConstant
dependent-on: "campaign-criterion"
description: |
  The `{{ table.name }}` table contains info about mobile devices.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the [`{{ table.dependent-on }}`](#{{ table.dependent-on }}) stream.

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "type"
    type: "string"
    description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "manufacturer_name"
    type: "string"
    description: ""
    
  - name: "operating_system_name"
    type: "string"
    description: ""

---