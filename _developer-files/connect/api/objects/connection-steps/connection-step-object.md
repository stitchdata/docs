---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "connection-step-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Connection Step"
description: "{{ api.data-structures.connection-steps.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "type"
    type: "string"
    description: |
      The type of step. Possible values are:

      - `form` - The first step in every source's creation.
      - `oauth` - If required, the OAuth step for the source's creation. **Note**: OAuth properties may be provided alongside `form` properties in a single `POST` or `PUT` request. A separate request isn't necessary.
      - `profile` - If required, the profile selection step. For example: Selecting a Facebook Ads profile.
      - `discover_schema` - The step in which Stitch performs a [structure sync]({{ api.terms }}) to detect the streams and fields available in the source.
      - `field_selection` - The step in which streams and fields are selected for replication.
      - `fully_configured` - Achieved when the source has a successful connection and `field_selection` is complete.

  - name: "properties"
    type: "array"
    description: "An array of [Properties objects]({{ api.data-structures.properties.section }})."


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

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