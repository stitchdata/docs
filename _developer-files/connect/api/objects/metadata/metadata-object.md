---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "metadata-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Metadata"
description: |
  {% include misc/data-files.html %}
  {{ api.data-structures.metadata.top-level.description | flatify }}

  Refer to the [Select streams and fields guide]({{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}) for instructions on selecting streams and fields.

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "breadcrumbs"
    type: "array"
    description: |
      An array of strings describing a path into the schema. For example:

      - A value of `[]` refers to the entire schema, or stream
      - A value of `["properties", "<FIELD_NAME>"]` refers to the `properties.<FIELD_NAME>` portion of the schema. For example: `["properties", "id"]` would refer to a field named `id`

  - name: "metadata"
    type: "object"
    description: |
      An object containing metadata associated with the `breadcrumb`. The type of metadata object depends on the `breadcrumb`:

       - For the entire schema (`breadcrumb: []`), this will be a [Stream-level Metadata object]({{ api.data-structures.metadata.stream-level.section }})
       - For an individual field (`breadcrumb: ["properties", "<FIELD_NAME>"]`), this will be a [Field-level Metadata object]({{ api.data-structures.metadata.field-level.section }})

sub-structures:
  - key: "field-level-metadata-object"
  - key: "stream-level-metadata-object"

examples:
  - type: "Database source"
    code: |
      {
         "metadata":[
            {
               "breadcrumb":[],
               "metadata":{
                  "database-name":"demni2mf59dt10",
                  "is-view":false,
                  "row-count":90849,
                  "schema-name":"products",
                  "table-key-properties":[
                     "id"
                  ]
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "collection_id"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected-by-default":true,
                  "sql-datatype":"bigint"
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "id"
               ],
               "metadata":{
                  "inclusion":"automatic",
                  "selected-by-default":true,
                  "sql-datatype":"bigint"
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "updated_at"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected-by-default":true,
                  "sql-datatype":"timestamp with time zone"
               }
            }
         ]
      }


  - type: "SaaS source"
    code: |
      {
         "metadata":[
            {
               "breadcrumb":[],
               "metadata":{
                  "forced-replication-method":"INCREMENTAL",
                  "selected":true,
                  "table-key-properties":[
                     "id"
                  ],
                  "valid-replication-keys":[
                     "updated_at"
                  ]
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "collection_id"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":true
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "created_at"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "featured"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "id"
               ],
               "metadata":{
                  "inclusion":"automatic",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "position"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "product_id"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "sort_value"
               ],
               "metadata":{
                  "inclusion":"available",
                  "selected":false
               }
            },
            {
               "breadcrumb":[
                  "properties",
                  "updated_at"
               ],
               "metadata":{
                  "inclusion":"automatic",
                  "selected":false
               }
            }
         ]
      }

---