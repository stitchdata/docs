---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-sub-structure"
key: "stream-level-metadata-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stream-level Metadata"
description: |
  {% include misc/data-files.html %}
  {{ api.data-structures.metadata.stream-level.description | flatify }}


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "database-name"
    type: "string"
    description: "**For database sources only**. The name of the database containing the stream."
    modifiable: false
    applies-to: "mysql, oracle, postgres"
    value: |
      <DATABASE_NAME>

  - name: "forced-replication-method"
    type: "string"
    description: |
      Indicates which Replication Method is required for the stream. Possible values are:

      - `FULL_TABLE` - The stream is using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }})
      - `INCREMENTAL` - The stream is using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }})
      - `LOG_BASED` - The stream is using [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}).
    modifiable: false
    applies-to: "xero, salesforce, shopify, zendesk, hubspot, uservoice"
    value: |
      INCREMENTAL

  - name: "is-view"
    type: "boolean"
    description: "**For database sources only.** Indicates if the stream is a database view."
    modifiable: false
    applies-to: ""
    value: |
      false

  - name: "replication-key"
    type: "string"
    description: "Indicates the field being used as the stream's [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }})."
    modifiable: true
    applies-to: "mysql, oracle, salesforce, db2, postgres"
    value: |
      updated_at

  - name: "replication-method"
    type: "string"
    description: |
      The Replication Method the stream uses to replicate data. Accepted values are:

      - `FULL_TABLE` - The stream is using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }})
      - `INCREMENTAL` - The stream is using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }})
      - `LOG_BASED` - The stream is using [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}). **Note**: This method is only available for certain database sources, and requires additional setup to use.
    modifiable: true
    applies-to: "xero, shopify, salesforce, zendesk, hubspot"
    value: |
      INCREMENTAL

  - name: "row-count"
    type: "integer"
    description: "**For database sources only.** The number of rows (records) in the stream."
    modifiable: false
    applies-to: "oracle, mysql"
    value: |
      55

  - name: "schema-name"
    type: "string"
    description: "**For database sources only.** The name of the schema containing the stream."
    modifiable: false
    applies-to: "oracle, postgres"
    value: |
      <SCHEMA_NAME>

  - name: "selected"
    type: "boolean"
    description: |
      Indicates whether a stream should be set to replicate. Accepted values are:

      - `true` - The stream is selected and data for selected fields will be replicated
      - `false` - The stream is not selected and no data will be replicated
    modifiable: true
    applies-to: "all"
    value: |
      true

  - name: "table-key-properties"
    type: "array"
    description: |
      An array of strings listing the fields that make up the key properties of the table. These are the table's defined Primary Keys.
    modifiable: false
    applies-to: "all"
    value: |
      id, created_at

  - name: "valid-replication-keys"
    type: "array"
    description: |
      An array of strings indicating the fields valid for use as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) in [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) (`replication-method: INCREMENTAL`).

      **Note**: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.
    modifiable: false
    applies-to: "bronto, hubspot, harvest-forecast, db2, shopify, salesforce, xero"
    value: |
      updated_at

  - name: "view-key-properties"
    type: "array"
    description: "**For database sources only.** An array of strings listing the fields that make up the key properties of the view."
    modifiable: false 
    applies-to: "oracle, postgres, mysql, db2"
    value: |
      <TODO>

examples:
  - type: "Database source (non-view)"
    code: |
      {
        "metadata": {
          "database-name": "demni2mf59dt10",
          "selected": true,
          "is-view": false,
          "replication-method": "FULL_TABLE",
          "row-count": 13,
          "schema-name": "public",
          "table-key-properties": [
            "id"
          ]
        }
      }

  - type: "Database source (view)"
    code: |
      {
        "metadata": {
          "database-name": "demni2mf59dt10",
          "selected": true,
          "replication-method":"INCREMENTAL",
          "replication-key":"updated_at",
          "is-view": true,
          "row-count": 156,
          "schema-name": "heroku",
          "view-key-properties": [
            "customer_id"
          ]
        }
      }

  - type: "SaaS source"
    code: |
      {
        "metadata": {
          "forced-replication-method": "INCREMENTAL",
          "selected": true,
          "table-key-properties": [
            "id"
          ],
          "valid-replication-keys": [
            "updated_at"
          ]
        }
      }
---