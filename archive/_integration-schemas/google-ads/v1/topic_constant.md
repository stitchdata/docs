---
tap: "google-ads"
version: "1"
name: "topic_constant"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/TopicConstant
dependent-on: "campaign_criterion|ad_group_criterion"
description: |
  The `{{ table.name }}` table contains info about topics.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the following streams:

  {% assign dependents = table.dependent-on | split: "|" %}
  
  {% for dependent in dependents %}
  - [`{{ dependent }}`](#{{ dependent | replace:'_','-'}})
  {% endfor %}

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "path"
    type: "array"
    description: ""
    subattributes:
      - name: "item"
        type: "string"
        description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "topic_constant_parent"
    type: "string"
    description: ""

---