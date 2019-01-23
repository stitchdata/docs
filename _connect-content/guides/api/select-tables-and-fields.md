---
title: Select tables and fields with the Connect API
content-type: "guide"
content-id: "select-tables-and-fields"

sidebar: guide
layout: connect

permalink: /stitch-connect/guides/select-tables-and-fields-with-connect-api

toc: false
summary: false
feedback: false

intro: |
  {% include misc/data-files.html %}

sections:
  - title: "Create and configure the source"
    anchor: "configure-the-source"
    content: |
      Create and configure a source. Refer to the [Create and configure a source guide]({{ guide.create-a-source | flatify }}) for instructions, including how to configure an OAuth source.
  
  - title: "Wait for a successful connection check and discovery"
    anchor: "successful-connection-check-discovery"
    content: |
      After the [Source API]({{ api.section | flatify | prepend: site.baseurl | append: api.core-objects.sources.create.anchor }}) reports that the source's `current_step` is equal to the `discover_schema` connection step, Stitch will automatically kick off a connection check. {{ site.data.tooltips.connection-check | replace:"A test","This is a test" | replace:"parameters.","parameters" }} and discovers the streams and fields available for the source.

    subsections:
      - title: "Get the source's last connection check"
        anchor: "get-sources-connection-check"
        content: |
          {% assign right-bracket = "}" %}

          To view the results of the source's [last connection check]({{ api.section | flatify | prepend: site.baseurl | append: api.core-objects.connection-checks.object }}), make a request to `GET {{ api.core-objects.connection-checks.get-source.name | flatify }}`, replacing `{source_id}` with the source's ID:

          ```json
          curl -X GET {{ api.base-url | strip_newlines }}{{ api.core-objects.connection-checks.get-source.name | flatify | replace: "{source_id","122635" | remove: right-bracket | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <API_TOKEN>'
          ```

          A successful connection check and discovery will have a `status` of `succeeded` and a `discovery_exit_status` of `0`:

          ```json
          {{ site.data.connect.code-examples.connection-checks.successful | rstrip }}
          ```

          When the connection check completes, the source's `current_step` will advance to `field_selection`.
        
      - title: "Verify the current connection step"
        anchor: "verify-current-connection-step"
        content: |
          Next, you'll verify that the source has advanced to the `field_selection` step. This step indicates that available streams and fields can be selected for replication.

          To get the source's `current_step`, make a request to `GET {{ api.core-objects.sources.retrieve.name | flatify }}`, replacing `{source_id}` with the source's ID:

          ```json
          curl -X GET {{ api.base-url | strip_newlines }}{{ api.core-objects.sources.retrieve.name | flatify | replace: "{source_id","122635" | remove: right-bracket | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <API_TOKEN>'
          ```

          The response will be the source's [`report_card` object]({{ api.section | flatify | prepend: site.baseurl | append: api.data-structures.report-cards.source.section }}). In this example, the `current_step` is `3`, which corresponds to the `field_selection` step:

          ```json
          {{ site.data.connect.code-examples.source-report-cards.toggl | replace: "<STEP_NUMBER>","3" }}
          ```

  - title: "Get the source's available streams"
    anchor: "get-available-streams"
    content: |
      When the [Source API]({{ api.section | flatify | prepend: site.baseurl | append: api.core-objects.sources.retrieve.anchor }}) reports that the source's `current_step` is equal to `field_selection`, you can retrieve a list of the streams available for the source.

      In general, a stream is:

      - A unique table or database view in a data source, or
      - An API endpoint in a data source

      [To return the streams available for selection]({{ api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.list.anchor | flatify }}), make a request to `GET {{ api.core-objects.streams.list.name | flatify }}`, replacing `{source_id}` with the source's ID:

      ```json
      curl -X GET {{ api.base-url | strip_newlines }}{{ api.core-objects.streams.list.name | flatify | replace: "{source_id","122635" | remove: right-bracket | strip_newlines }}
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <API_TOKEN>'
      ```

      The response will be an array of [Stream objects]({{ api.section | flatify | prepend: site.baseurl | append: api.core-objects.streams.object }}), each object corresponding to a stream available for selection:

      ```json
      {{ site.data.connect.code-examples.streams.saas-streams }}
      ```

  - title: "Understand and retrieve the stream's schema"
    anchor: "get-stream-schema"
    endpoint-resource: "GET {{ site.data.connect.core-objects.streams.retrieve-schema.name | flatify }}"
    endpoint-name: "title"
    endpoint-doc-link: "anchor"
    object: "stream-schema"
    request: |
      ```json
      curl -X GET {{ api.base-url | strip_newlines }}{{ api.core-objects.streams.retrieve-schema.name | flatify | replace: "{source_id","122635" | replace: "{stream_id","2394777" | remove: right-bracket | strip_newlines }}
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <API_TOKEN>'
      ```
    response: |
      ```json
      {{ site.data.connect.code-examples.streams.saas-stream-schema | rstrip }}
      ```
    content: |
      HOLD
    subsections:
      - title: "Understand field metadata"
        anchor: "understand-field-metadata"
        content: |
          Before you retrieve the stream's schema, we'll touch on the properties the [Stream Schema object]() contains. You'll eventually use this data to select streams and fields, and if applicable, configure the stream's Replication Method.

          The Stream Schema object contains three root properties:

          - `schema` - The JSON schema describing the stream's fields.
          - `metadata` - An array of [Metadata]() objects, each object referring to a field in the stream.
          - `non-discoverable-metadata-keys` - A list of `metadata` keys that can be modified.

          Each `metadata` object in the response corresponds to a field in the stream, or a `breadcrumb`. The `breadcrumb` is a path into the schema that describes the part of the schema associated with the metadata.

          Consider this schema: 

          ```json
          {
            "schema":{"properties":{"id":{"type":["null","integer"]},"name":{"type":["null","string"]},"updated":{"format":"date-time","type":["null","string"]}}
          }
          ```

          For this example, there would be four different breadcrumb values:

          1. `[]` - Refers to the entire schema, or stream
          2. `["properties":"id"]` - Refers to `properties.id`, or a field named `id`
          3. `["properties":"name"]` - Refers to `properties.name`, or a field named `name`
          4. `["properties":"updated"]` - Refers to `properties.name`, or a field named `updated`

          Below is what the Stream Schema object for this stream would look like:

          ```json
          {{ site.data.connect.code-examples.streams.breadcrumb-explanation }}
          ```

      - title: "Get the stream's schema"
        anchor: "get-stream-schema"
        content: |
          Next, you'll retrieve the schema for each stream you want to select for replication. The stream schema is a list of fields the stream contains.

          [To retrieve a stream's schema]({{ api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.retrieve-schema.anchor | flatify }}), make a call to `{{ section.endpoint-resource | flatify }}`, replacing `{source_id}` and `{stream_id}` with the source ID and stream ID, respectively.

          In this example, we'll get the schema for the `time_entries` table (`stream_id: 2394777`):

          {{ section.request | flatify | markdownify }}

          The response will be a single [Stream Schema object]():

          {{ section.response | flatify | markdownify | rstrip }}

  - title: "Select and configure a stream"
    anchor: "select-configure-a-stream"
    content: |
      HOLD

    subsections:
      - title: "Create the request body"
        anchor: "create-the-request-body"
        content: |
          {% capture quote %}"{% endcapture %}
          The selection of streams is controlled through the `selected` metadata property.

          When you select a stream, you'll `POST` to `{{ site.data.connect.core-objects.streams.update.name | flatify }}` with a request body containing the `tap_stream_id` and other [required arguments]({{ api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | append:"--arguments" | flatify }}):

          ```json
          {{ site.data.connect.code-examples.streams.blank-stream-selection | prepend: quote | append: quote }}
          ```

          **Note**: Multiple streams in a source can be updated in a single request, but for clarity, this guide will focus on selecting a single stream. Refer to the [Update a Stream endpoint documentation]({{ api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | append:"--returns" | flatify }}) for examples.

      - title: "Configure stream replication"
        anchor: "configure-stream-replication"
        content: |
          Stitch uses one of three [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) to replicate data from selected streams:

          - [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}) - {{ site.data.tooltips.full-table-rep }}
          - [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) - {{ site.data.tooltips.key-based-incremental-rep }}
          - [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) - {{ site.data.tooltips.log-based-incremental-rep }} **Note**: This Replication Method is only available to [select database integrations]({{ link.replication.log-based-incremental | prepend: site.baseurl | append: "#limitation-1--availability" }}) and requires additional configuration steps when setting up the source. Refer to the [documentation for the database]({{ site.baseurl }}/integrations/databases) for more info.

          #### Streams with configurable Replication Methods {#streams-configurable-replication}

          For some sources - mainly databases and Salesforce -  you can configure how a stream is replicated by Stitch by providing the method via the `replication-method` metadata property. Accepted values are `FULL_TABLE`, `INCREMENTAL`, and `LOG_BASED`.

          In this request body example, the `demni2mf59dt10-public-customers` stream is set to use `INCREMENTAL` replication with `updated_at` as the `replication-key`:

          ```json
          {{ site.data.connect.code-examples.streams.request-bodies.database | rstrip | prepend: quote | append: quote }}
          ```

          **Note**: When `replication-method` is set to `INCREMENTAL`, the value of the `replication-key` property must be:

          1. If provided, one of the fields in the `valid-replication-keys` property, or
          2. The name of an `integer`, `date-time`, or `timestamp` field in the stream. Refer to the [Replication Keys documentation]({{ link.replication.rep-keys | prepend: site.baseurl }}) for more info. 

          #### Streams with forced Replication Methods {#streams-forced-replication}

          In cases where a stream can only be replicated using one method, the stream's metadata may indicate the method it will use via the `forced-replication-method` property:

          ```json
          {{ site.data.connect.code-examples.streams.saas-stream | rstrip }}
          ```

          When the stream's metadata contains the `forced-replication-method` property, its Replication Method cannot be changed. If selected, the stream will use the `forced-replication-method` and the field in `valid-replication-keys` as a Replication Key, if applicable.

          Your request to select the stream will not need to include a `replication-method` property:

          ```json
          {{ site.data.connect.code-examples.streams.request-bodies.saas | rstrip | prepend: quote | append: quote }}
          ```



# When this is true, the `replication-method` metadata will be returned at the [stream level](#get-available-streams). For example: This is a stream from a database source:

# ```json
# {{ site.data.connect.code-examples.streams.database-stream | rstrip }}
# ```
        # sub-subsections:
        #   - title: "SaaS sources"
        #     anchor: "configure-saas-sources"
        #     content: |

        #   - title: "Salesforce sources"
        #     anchor: "configure-salesforce-sources"
        #     content: |

        #   - title: "Database sources"
        #     anchor: "configure-database-sources"
        #     content: |

        #   - 

      - title: "Submit the request"
        anchor: "submit-stream-request"
        content: |
          [To select a stream]({{ api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | flatify }}), make a request to `PUT {{ site.data.connect.core-objects.streams.update.name | flatify }}` with the [appropriate request body metadata properties](#configure-stream-replication) replacing `{source_id}` with the source ID:

          {% capture put-stream-request %}
          curl -X GET {{ api.base-url | strip_newlines }}{{ api.core-objects.streams.update.name | flatify | replace: "{source_id","122635" | remove: right-bracket | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <API_TOKEN>'
               -d $
          {% endcapture %}

          ```json
          {{ put-stream-request | flatify | lstrip | rstrip }}
          {{ site.data.connect.code-examples.streams.request-bodies.saas | rstrip | prepend: quote | append: quote }} 
          ```
          
          **Note**: The request body must contain the stream's `tap_stream_id` property, which is an alphanumeric value. This is different than the `stream_id`, which is numeric.

          For example: In the examples in this guide, the `stream_id` for the `time_entries` table is `2394777` while its `tap_stream_id` is `time_entries`.
      
  - title: "Select fields in a stream"
    anchor: "select-fields-in-a-stream"
    content: |
      {% capture field-selection-rules %}
      Before selecting fields, refer to the [Field selection and compatibility rules guide]({{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}) to ensure the combinations of fields you select are valid for replication.
      {% endcapture %}
      {% include important.html type="single-line" content=field-selection-rules %}

      After stream selection, field selection can be used to select which fields are replicated from the source stream. The request to select a field is analogous to the request to select a stream, except that the `breadcrumb` should point to the field’s path in the schema.

      For example: This request selects the `id` field in the `time_entries` stream:

      ```json
      {{ put-stream-request | flatify | lstrip | rstrip }}
      {{ site.data.connect.code-examples.field-metadata.request-bodies.saas-field | rstrip | prepend: quote | append: quote }} 
      ```

      Multiple fields in a stream can be submitted as part of the same request. For each field included in the request body, include a `metadata` object referencing the field.

      For example: This request selects the `id`, `published_at`, `project`, and `client` fields in the `time_entries` stream: 

      ```json
      {{ put-stream-request | flatify | lstrip | rstrip }}
      {{ site.data.connect.code-examples.field-metadata.request-bodies.saas-fields | rstrip | prepend: quote | append: quote }} 
      ```

      **Note**: Fields with metadata properties of `inclusion: automatic` or `selected-by-default: true` don't need to be explicitly selected through a request. These fields will be automatically selected for replication regardless of their `selected` value. Refer to the [Field selection and compatibility rules guide]({{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}) for more info.
---