---
content-type: "api-structure"
key: "connection-step-object"

title: "Connection Steps"
description: "Contained in the Report Card object, the Connection Steps object contains the steps necessary to configure a data source or destination."

object-attributes:
  - name: "type"
    type: "string"
    description: |
      The type of step. Possible values are:

      - `form` - The first step in every source's creation.
      - `oauth` - If required, the OAuth step for the source's creation.
      - `profile` - 
      - `discover_schema` - The step in which Stitch performs a [structure sync](#terminology) to detect the tables and attributes available in the source.
      - `field_selection` - The step in which tables and columns are selected for replication.
      - `fully_configured` - Achieved when the source has a successful connection and `field_selection` is complete.

  - name: "properties"
    type: "array"
    url: "{{ page.anchors.data-structures.properties }}"
    description: "An array of [Properties objects]({{ page.anchors.data-structures.properties }})."

examples:
  - code: |
      {  
         "report_card":{  
            "type":"platform.hubspot",
            "current_step":2,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[]
               },
               {  
                  "type":"oauth",
                  "properties":[]
               },
               {  
                  "type":"discover_schema",
                  "properties":[]
               },
               {  
                  "type":"field_selection",
                  "properties":[]
               },
               {  
                  "type":"fully_configured",
                  "properties":[]
               }
            ]
         }
      }

---