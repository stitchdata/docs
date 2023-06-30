---
tap: "google-ads"
version: "1"
name: "operating_system_verison_constant"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/OperatingSystemVersionConstant
dependent-on: "campaign-criterion"
description: |
  The `{{ table.name }}` table contains info about mobile operating system versions.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the [`{{ table.dependent-on }}`](#{{ table.dependent-on }}) stream.

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "operator_type"
    type: "string"
    description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "os_major_version"
    type: "integer"
    description: ""
    
  - name: "os_minor_version"
    type: "integer"
    description: ""

---