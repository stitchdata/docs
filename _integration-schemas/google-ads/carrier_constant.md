---
tap: "google-ads"
version: "1"
name: "carrier_constant"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/CarrierConstant
dependent-on: "campaign_criterion"
description: |
  The `{{ table.name }}` table contains info about carrier criteria that can be used in campaign targeting.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the [`{{ table.dependent-on }}`](#{{ table.dependent-on | replace:'_','-'}}) stream.

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "country_code"
    type: "string"
    description: ""

---