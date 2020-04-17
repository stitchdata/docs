---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Structuring Data for the Stitch Import API
permalink: /developers/import-api/guides/structure-data-for-the-import-api
summary: &summary "Best practices and tips for structuring data in Import API requests."

doc-type: "concept"

product-type: "import-api"
content-type: "guide"
content-id: "structure-data"

key: "import-api-structure-data"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /import-api/guides page.
icon: json
order: 3

display-title: "Structuring and typing Import API data"
description: *summary


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "Sequencing data for the Import API"
    link: "{{ link.import-api.guides.sequence-data | prepend: site.baseurl }}"

  - title: "Understanding loading behavior"
    link: "{{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}"



# -------------------------- #
#            INTRO           #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% include tip.html content="**Set up a test Import API integration!** We recommend setting up a test Import API integration while developing your script. This ensures that you can try different structuring and typing approaches while figuring out what works for you." %}

  Stitch’s Import API allows you to push arbitrary data from a source to your Stitch account. 

  In this guide, we'll cover what you need to know about structuring and typing the data you send to the Import API:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

# -------------------------- #
#           CONTENT          #
# -------------------------- #

sections:
  - title: "Endpoints in this guide"
    anchor: "endpoints"
    summary: "The endpoints in this guide"
    content: |
      {% include misc/icons.html %}
      The Import API has two endpoints that accept and persist data to your Stitch destination:

      {% assign endpoint = site.data.import-api.core-objects %}
      {% assign types = "batch|push" | split:"|" %}
      {% assign comparison-attributes = "accepts-multiple-records|accepts-multiple-tables|enforces-data-types|requires-primary-keys" | split:"|" %}

      <table>
      <tr>
      <td class="attribute-name"></td>
      {% for type in types %}
      <td width="35%; fixed">
      <strong>{{ endpoint[type]name }}</strong>
      </td>
      {% endfor %}
      </tr>
      <tr>
      <td class="attribute-name"><strong>Resource URL</strong></td>
      {% for type in types %}
      <td>
      <a href="{{ link.import-api.api | prepend: site.baseurl | append: endpoint[type]anchor }}">{{ endpoint[type]url }}</a>
      </td>
      {% endfor %}
      </tr>
      {% for attribute in comparison-attributes %}
      <tr>
      <td class="attribute-name">
      <strong>
      {{ attribute | replace:"-"," " | capitalize | replace:"primary keys","Primary Keys" }}
      </strong>
      </td>
      {% for type in types %}
      <td>
      {% case endpoint[type]comparison[attribute]support %}
      {% when true %}
      <p><strong>{{ supported | replace:"TOOLTIP","Supported" }} Supported</strong></p>
      {% when false %}
      <p><strong>{{ not-supported | replace:"TOOLTIP","Not supported"}} Unsupported</strong></p>
      {% else %}
      {{ endpoint[type]comparison[attribute]support | flatify | markdownify }}
      {% endcase %}
      {{ endpoint[type]comparison[attribute]note | flatify | markdownify }}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

      **Note**: We recommend using the Batch endpoint for sending data to the Import API. The Push endpoint is mentioned only as a comparison to the Batch endpoint and as a reference for existing Import API scripts.

  - title: "Structuring guidelines"
    anchor: "structuring-guidelines"
    summary: "Some general guidelines for structuring Import API data"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "General guidelines"
        anchor: "general-guidelines"
        content: |
          When developing your Import API script, you should keep these general guidelines in mind:

          - **Field names shouldn't include reserved words**. This includes the keywords [reserved by Stitch]({{ link.destinations.storage.reserved-keywords.overview | prepend: site.baseurl }}) and by [your destination]({{ link.destinations.storage.reserved-keywords.overview | prepend: site.baseurl | append: "#destination-reserved-keywords" }}). For example: Fields shouldn't contain `{{ system-column.prefix }}`, a Stitch system prefix.

          - **Fields should contain one data type per field.** This affects not only how data is typed in your destination, but the resulting structure of destination tables. Refer to the [Data typing section](#changed-data-type-handling) for more info.

      - title: "Guidelines for request bodies"
        anchor: "request-body-requirements"
        content: |
          We recommend using the Batch endpoint to send data to the Import API. As such, this section only contains the request body requirements for the Batch endpoint.

          Request bodies sent to the Batch endpoint must be valid JSON and adhere to the following: 

          {% assign common-request-requirements = site.data.import-api.general.request-body-requirements.common %}
          {% assign batch-request-requirements = site.data.import-api.general.request-body-requirements.batch %}

          {% assign all-request-requirements = batch-request-requirements | concat: common-request-requirements %}

          {% assign batch-requirements = link.import-api.api | prepend: site.baseurl | append: "#batch-data--arguments" %}

          {% for requirement in all-request-requirements %}
          - {{ requirement | replace:"#[NAME]-data--arguments",batch-requirements | flatify | markdownify }}
          {% endfor %}
      
  - title: "Defining tables and Primary Keys"
    anchor: "tables-and-primary-keys"
    summary: "How to define tables and Primary Keys"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Tables"
        anchor: "tables"
        content: |
          Tables are dynamically generated based on the `table_name` specified in Import API requests. All tables pushed using the same API access token will be created in the same schema in your destination. You can find the name of [the schema for your Import API integration]({{ 
          link.destinations.storage.stitch-schema | prepend: site.baseurl | append:"#integration-schema-names" }}) by logging into Stitch.

          Generally, we recommend creating one table for each type of record you want to push to the Import API. For example: If you have customer and product data, you should create two tables - one for `customers` and one for `products`.

          Every record pushed to a table should have the same structure. For example: If a `customers` table contains `customer_id`, `name`, and `email` fields, every customer record pushed into this table should contain those fields.

          **Note**: The Import API doesn't support methods for specifically creating or deleting a table. If you need to delete a table, you should drop it in your destination and prevent any new data for the table from being pushed to the Import API. Any data accepted by Stitch will still be processed, even if the destination table has been dropped.

      - title: "Primary Keys"
        anchor: "primary-keys"
        content: |
          While Primary Keys are optional when using the [Batch endpoint]({{ site.data.import-api.core-objects.batch.anchor | prepend: link.import-api.api | prepend: site.baseurl }}), they will determine how Stitch loads data for the table:

          - **For tables with Primary Keys**, Stitch will use Primary Key columns to de-dupe data during the Loading phase of the replication process. This ensures that only the most recent version of a record is loaded into the destination.

          - **If a table doesn't have a Primary Key, or if the destination only supports Append-Only loading**, records will be appended to the end of the table as new rows. Existing rows will not be updated. Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

          A table's Primary Keys are defined using the `key_names` property in the [Batch endpoint]({{ site.data.import-api.core-objects.batch.anchor | prepend: link.import-api.api | prepend: site.baseurl }}). For example:

          {% capture code %}{
            "key_names":[
                "id"
             ],
             "table_name":"customers",
             "schema":{
                "properties":{
                   "id":{
                      "type":"integer"
                   },
                   "name":{
                      "type":"string"
                   },
                   "age":{
                      "type":"integer"
                   },
                   "has_magic":{
                      "type":"boolean"
                   }
                }
             },
             "messages":[
                {
                   "action":"upsert",
                   "sequence":1565880017,
                   "data":{
                      "id":1,
                      "name":"Finn",
                      "age":15,
                      "has_magic":false
                   }
                }
             ]
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          If you choose to define Primary Keys, keep the following in mind:

          - Every record in a table must have a Primary Key.
          - Primary Key columns should only contain a single data type.
          - Primary Keys cannot be null.
          - Primary Key values must be unique. For composite keys, the value of all combined values must be unique across all records in the table.

            For example: Let's assume that `event_id`, `app_id`, and `created_at` are the Primary Keys for the table containing these records:

          {% capture code %}
          [
             {
                "event_id":1,
                "app_id":1,
                "created_at":"2019-08-20T00:00:00+00:00"
             },
             {
                "event_id":2,
                "app_id":1,
                "created_at":"2019-08-20T00:00:00+00:00"
             }
          ]
          {% endcapture %}

             {% include layout/code-snippet.html use-code-block=false language="json" code=code %}

             ```json
          {{ code | lstrip | rstrip }}
             ```

            While `app_id` and `created_at` have two identical values between these records, the `event_id` makes the records unique.

          - Every column in the `key_names` property must be present in both the request's Schema object and in every record for the table. For example:

          {% capture code %}
          {
             "key_names":[
                "id",
                "created_at"
             ]
          }
          {% endcapture %}

             {% include layout/code-snippet.html use-code-block=false language="json" code=code %}

             ```json
          {{ code | lstrip | rstrip }}
             ```

            In this case, the Schema object must contain `id` and `created_at` properties. Every record must contain also contain these properties or the Import API will return the following error:

            {% capture code %}
            {
               "error":"Record is missing key property <KEY_NAME>"
            }
            {% endcapture %}

             {% include layout/code-snippet.html use-code-block=false language="json" code=code %}

             ```json
          {{ code | lstrip | rstrip }}
             ```

  - title: "Data typing"
    anchor: "data-typing"
    summary: "How data typing works in the Import API"
    content: |
      How data is typed depends on what endpoint you're using to push data to the Import API:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify | remove: " data typing" }}](#{{ subsection.anchor }})
      {% endfor %}

      **Note**: We recommend using the Batch endpoint for sending data to the Import API. The Push endpoint is mentioned only as a comparison to the Batch endpoint and as a reference for existing Import API scripts.

    subsections:
      - title: "Batch ({{ site.data.import-api.core-objects.batch.url }}) endpoint data typing"
        anchor: "create-a-batch-endpoint-data-typing"
        content: |
          When using the Batch endpoint, Stitch will assign data types based on the JSON schema in the [Schema object]({{ site.data.import-api.data-structures.schema.section | prepend: link.import-api.api | prepend: site.baseurl }}) in the request.

          For example: This is the schema for a table named `customers`:

          {% capture code %}{
             "schema":{
                "properties":{
                   "id":{
                      "type":"integer"
                   },
                   "name":{
                      "type":"string"
                   },
                   "age":{
                      "type":"number"
                   },
                   "has_magic":{
                      "type":"boolean"
                   }
                }
             }
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          A record sent to the Import API for the `customers` table could look like this:

          {% capture code %}{
             "action":"upsert",
             "sequence":1565880017,
             "data":{
                "id":1,
                "name":"Finn",
                "age":15,
                "has_magic":false
             }
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          This data point would create a table similar to the following, depending on the data types used by your destination:

          | id (integer) | name (string)  | age (integer) | has_magic (boolean) |
          |--------------+----------------+---------------+---------------------|
          | 1            | Finn           | 15            | false               |
          
          
          Records sent to the Import API must adhere to the JSON schema for the table that contains them, or the API will return a `400` response and an error similar to the following:

          {% capture code %}{
            "error": "Record 0 did not conform to schema: #/<FIELD_NAME>: expected: <DATA_TYPE>, found: <DATA_TYPE>"
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          Refer to the **Errors** in the [Batch endpoint documentation]({{ site.data.import-api.core-objects.batch.anchor | append:"--returns" | prepend: link.import-api.api | prepend: site.baseurl }}) for a list of errors and their causes.

        sub-subsections:
          - title: "JSON schemas in the Batch endpoint"
            anchor: "json-schemas-batch-endpoint"
            content: |
              The schema specified in a request's Schema object must be a valid JSON schema. The Batch endpoint uses [jsonschema 2.6.0]({{ site.data.import-api.resources.jsonschema.docs }}){:target="new"}, a JSON Schema implementation for Python, to validate JSON schemas.

              Walking through creating a JSON schema is outside the scope of this guide, but [the official Understanding JSON Schema reference]({{ site.data.import-api.resources.jsonschema.reference }}){:target="new"} is a good resource for getting started. When you're ready, you can use [jsonschema.net](https://jsonschema.net/){:target="new"} to test and validate your own schemas.

      - title: "Push ({{ site.data.import-api.core-objects.push.url }}) endpoint data typing"
        anchor: "push-data-endpoint-data-typing"
        content: |
          {% include note.html type="single-line" content="**Use the Batch endpoint for the best data typing experience.** The Push endpoint doesn't allow you to specify or enforce data types, which may lead to inconsistencies when data types change. The [Batch endpoint](#create-a-batch-endpoint-data-typing) allows this via a JSON schema you supply." %}

          When using the Push endpoint, Stitch will type the data based on the value's JSON data type. The Import API doesn't infer data types on its own.

          As JSON doesn't explicitly enforce data types, all data typing needs to be handled withing your data source and Import API script.

          For example:

          {% capture code %}{
             "id":1,
             "cost":3.14,
             "tax":"1.00"
             "modified_at":"2019-08-13T21:25:03+0000"
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          This data point would create a table similar to the following, depending on the data types used by your destination:

          | id (integer) | cost (double)  | tax (string) | modified_at (string)     |
          |--------------+----------------+--------------+--------------------------|
          | 1            | 3.14           | 1.00         | 2019-08-13T21:25:03+0000 |


          Consider the `modified_at` field in the example. Even though this field contains an ISO 8601 formatted timestamp, the Import API won't type this column as a `timestamp` in the destination. This is because it's being sent as a JSON string.

          While JSON doesn't allow for defining data types, you can use the [Batch endpoint](#create-a-batch-endpoint-data-typing) instead. This endpoint accepts a JSON schema and will enforce the data types it declares for each field.
        sub-subsections:
          - title: "Changed data type handling in the Push endpoint"
            anchor: "changed-data-type-handling-push-endpoint"
            content: |
              The Push endpoint considers data types on a record-by-record basis. If a field's data type changes from one record to the next, all data types received via the Push endpoint will be used when the data is loaded. In the destination, this will look like a field's values have been "split" between columns.

              For example: Consider the `cost` values for each of the following records:

              {% capture code %}
              {
                 "id":1,
                 "cost":3.14,         // number
                 "tax":"1.00"
                 "modified_at":"2019-08-13T21:25:03+0000"
              },
              {
                 "id":2,
                 "cost":10,           // integer
                 "tax":"2.45"
                 "modified_at":"2019-08-13T21:34:14+0000"
              },
              {
                 "id":3,
                 "cost":5.61,         // number
                 "tax":".55"
                 "modified_at":"2019-08-13T21:35:04+0000"
              }
              {% endcapture %}

              {% include layout/code-snippet.html language="json" code=code %}

              As a result of the `cost` values changing between records, the destination table would look like this:

              | id (integer) | cost (double)  | cost__it (integer) | tax (string) | modified_at (string)     |
              |--------------+----------------+--------------------+--------------+--------------------------|
              | 1            | 3.14           | _null_             | 1.00         | 2019-08-13T21:25:03+0000 |
              | 2            | _null_         | 10                 | 2.45         | 2019-08-13T21:34:14+0000 |
              | 3            | 5.61           | _null_             |  .55         | 2019-08-13T21:35:04+0000 |

              To prevent this from occurring, each field should only ever contain a single data type. You can resolve column splits by:

              1. Using a view in your destination to coerce the data types
              2. Fixing the issue in the source, [enforcing data typing](#enforcing-data-types-in-push-endpoint), dropping the destination table, and re-pushing all historical data to Stitch. The table will be re-created with the correct data types.

          - title: "Enforcing data types in the Push endpoint"
            anchor: "enforcing-data-types-in-push-endpoint"
            content: |
              The only way to enforce data types using the Push endpoint is to use [Transit]({{ site.data.import-api.resources.transit.url }}){:target="new"}, as JSON on its own doesn't allow for defining data types. You can use Transit libraries in your Import API script to specify data types for various fields.

              Otherwise, we recommend using the [Batch endpoint](#create-a-batch-endpoint-data-typing). This endpoint accepts a JSON schema and will enforce the data types it declares for each field.
---