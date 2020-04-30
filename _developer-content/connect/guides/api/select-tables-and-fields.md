---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Select Streams and Fields with the Connect API
permalink: /developers/stitch-connect/guides/select-streams-and-fields-with-connect-api
redirect_from: /stitch-connect/guides/select-streams-and-fields-with-connect-api
summary: "Using the Stitch Connect API, select a source's streams and fields for replication using this step-by-step tutorial."

product-type: "connect"
content-type: "guide"
content-id: "select-streams-and-fields"
topics: "basics, data selection"

key: "connect-select-data"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: table-selection
order: 4

description: "Select streams and fields for replication."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"

  - title: "Create and configure a source with Connect"
    link: "{{ link.connect.guides.create-configure-a-source | prepend: site.baseurl }}"

  - title: "Field selection and compatibility rules"
    link: "{{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }}

  **Note**: While this guide will walk you through creating, configuring, and advancing a new source to its `field_selection` [connection step]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.connection-steps.section | flatify }}), the steps are still applicable to existing `fully_configured` sources if their Report Cards have a `field_selection` step. You may only select streams and fields when a source's `current_step` is `field_selection` or `fully_configured`.


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch Enterprise feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.
  - item: |
      **Access to a source with a `field_selection` connection step**. This guide will use a [Shopify SaaS source]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.data-structures.source-form-properties.section |  append: "-shopify-object" }}) as an example, but any source type with a `field_selection` step will work.

         Refer to the [Source Form Properties documentation]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.data-structures.source-form-properties.section }}) for the sources supported by Connect. To determine if a source has a `field_selection` step, [retrieve its Report Card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.source-types.get.anchor | flatify }}).


# -------------------------- #
#         GUIDE STEPS        #
# -------------------------- #

steps:
  - title: "Create and configure the source"
    anchor: "configure-the-source"
    content: |
      {% assign api = site.data.connect.api %}
      {% assign right-bracket = "}" %}
      {% assign source-id = "122635" %}
      {% assign stream-id = "2288758" %}
      {% assign tap-stream-id = "custom_collections" %}

      Create and configure a source. Refer to the [Quick start guide]({{ link.connect.guides.create-configure-a-source | flatify | prepend: site.baseurl }}) for instructions.
  
  - title: "Wait for a successful connection check and discovery"
    anchor: "successful-connection-check-discovery"
    content: |
      After the [Source API]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create.anchor }}) reports that the source's `current_step` is equal to the `discover_schema` connection step, Stitch will automatically kick off a connection check. {{ site.data.tooltips.connection-check | replace:"A test","This is a test" | replace:"parameters.","parameters" }} and discovers the streams and fields available for the source.

      {% include developers/api-tutorial-step-table.html item=step item-list=step.substeps %}

    substeps:
      - title: "Get the source's last connection check"
        anchor: "get-sources-connection-check"
        endpoint: "GET {{ site.data.connect.core-objects.connection-checks.get-source.name }}"
        content: |
          To view the results of the source's [last connection check]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.core-objects.connection-checks.object }}), make a request to [GET {{ site.data.connect.core-objects.connection-checks.get-source.name | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.connection-checks.get-source.anchor | prepend: site.baseurl }}), replacing `{source_id}` with the source's ID:

          {% assign example-url = site.data.connect.core-objects.connection-checks.get-source.name %}
          {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

          {% assign description = substep.endpoint %}

          {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

          A successful connection check and discovery will have a `status` of `succeeded` and a `discovery_exit_status` of `0`:

          {% capture code %}{{ site.data.connect.code-examples.connection-checks.successful | rstrip }}
          {% endcapture %}

          {% assign description = "Response for " | append: substep.endpoint %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

          When the connection check completes, the source's `current_step` will advance to `field_selection`.
        
      - title: "Verify the current connection step"
        anchor: "verify-current-connection-step"
        endpoint: "GET {{ site.data.connect.core-objects.sources.retrieve.name | flatify }}"
        content: |
          Next, you'll verify that the source has advanced to the `field_selection` step. This step indicates that available streams and fields can be selected for replication.

          To get the source's `current_step`, make a request to [GET {{ site.data.connect.core-objects.sources.retrieve.name | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.sources.retrieve.anchor | prepend: site.baseurl }}), replacing `{source_id}` with the source's ID:

          {% assign example-url = site.data.connect.core-objects.sources.retrieve.name %}
          {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

          {% assign description = substep.endpoint %}

          {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

          The response will be the source's [`report_card` object]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.data-structures.report-cards.source.section }}). In this example, the `current_step` is `4`, which corresponds to the `field_selection` step:

          {% capture code %}{{ site.data.connect.code-examples.source-report-cards.shopify | replace: "<STEP_NUMBER>","4" }}
          {% endcapture %}

          {% assign description = "Response for " | append: substep.endpoint %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

  - title: "Get the source's available streams"
    anchor: "get-available-streams"
    content: |
      When the [Source API]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.core-objects.sources.retrieve.anchor }}) reports that the source's `current_step` is equal to `field_selection`, you can retrieve a list of the streams available for the source.

      {% include note.html type="single-line" content="**Note**: If a source has a `field_selection` step in its report card but its `current_step` is `fully_configured`, you can still select additional streams and fields. Selection may only occur during `field_selection` and `fully_configured` steps." %}

      In general, a stream is:

      - A unique table or database view in a data source, or
      - An API endpoint in a data source

      To return the streams available for selection, make a request to [GET {{ site.data.connect.core-objects.streams.list.name | flatify }}]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.list.anchor | flatify }}), replacing `{source_id}` with the source's ID:

      {% assign example-url = site.data.connect.core-objects.streams.list.name %}
      {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

      {% assign description = "GET " | append: example-url %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be an array of [Stream objects]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: api.core-objects.streams.object }}), each object corresponding to a stream available for selection:

      {% capture code %}{{ site.data.connect.code-examples.streams.saas-streams | rstrip }}
      {% endcapture %}

      {% assign description = "Response for GET " | append: example-url %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

  - title: "Understand and retrieve the stream's schema"
    anchor: "understand-retrieve-stream-metadata"
    content: |
      {% include developers/api-tutorial-step-table.html item=step item-list=step.substeps %}
    substeps:
      - title: "Understand field metadata"
        anchor: "understand-field-metadata"
        endpoint: ""
        content: |
          Before you retrieve the stream's schema, we'll touch on the properties the [Stream Schema object]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.data-structures.stream-schemas.section | flatify }}) contains. You'll eventually use this data to select streams and fields, and if applicable, configure the stream's Replication Method.

          The Stream Schema object contains three root properties:

          - `schema` - The JSON schema describing the stream's fields.
          - `metadata` - An array of [Metadata]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.top-level.section | flatify }}) objects, each object referring to a field in the stream.
          - `non-discoverable-metadata-keys` - A list of `metadata` keys that can be modified.

          Each `metadata` object in the response corresponds to a field in the stream, or a `breadcrumb`. The `breadcrumb` is a path into the schema that describes the part of the schema associated with the metadata.

          Consider this schema:

          {% capture code %}{
            "schema":{"properties":{"id":{"type":["null","integer"]},"name":{"type":["null","string"]},"updated":{"format":"date-time","type":["null","string"]}}
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          For this example, there would be four different breadcrumb values:

          1. `[]` - Refers to the entire schema, or stream
          2. `["properties":"id"]` - Refers to `properties.id`, or a field named `id`
          3. `["properties":"name"]` - Refers to `properties.name`, or a field named `name`
          4. `["properties":"updated"]` - Refers to `properties.name`, or a field named `updated`

          Below is what the Stream Schema object for this stream might look like:

          {% capture code %}{{ site.data.connect.code-examples.streams.breadcrumb-explanation }}
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

      - title: "Get the stream's schema"
        anchor: "get-stream-schema"
        endpoint: "GET {{ site.data.connect.core-objects.streams.retrieve-schema.name | flatify }}"
        content: |
          Next, you'll retrieve the schema for each stream you want to select for replication. The stream schema is a list of fields the stream contains.

          To retrieve a stream's schema, make a request to [GET {{ site.data.connect.core-objects.streams.retrieve-schema.name | flatify }}]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.retrieve-schema.anchor | flatify }}), replacing `{source_id}` and `{stream_id}` with the source ID and stream ID, respectively.

          In this example, we'll get the schema for the `custom_collections` table (`stream_id: {{ stream-id }}`):

          {% assign example-url = site.data.connect.core-objects.streams.retrieve-schema.name %}
          {% assign request-url = example-url | flatify | replace: "{source_id",source-id | replace: "{stream_id",stream-id | remove: right-bracket | strip_newlines %}

          {% assign description = substep.endpoint %}

          {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

          The response will be a single [Stream Schema object]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.data-structures.stream-schemas.section | flatify }}):

          {% capture code %}{{ site.data.connect.code-examples.streams.saas-stream-schema | rstrip }}
          {% endcapture %}

          {% assign description = "Response for " | append: substep.endpoint %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

  - title: "Select and configure a stream"
    anchor: "select-configure-a-stream"
    content: |
      {% include developers/api-tutorial-step-table.html item=step item-list=step.substeps %}
    substeps:
      - title: "Create the request body"
        anchor: "create-the-request-body"
        content: |
          {% capture quote %}'{% endcapture %}
          To select a stream, you'll make a request to [POST {{ site.data.connect.core-objects.streams.update.name | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.streams.update.anchor | prepend: site.baseurl }}) with a request body that contains:

          1. The stream's `tap_stream_id`. **Note** This is different than the `stream_id`, which is always numeric.

             For example: In the examples in this guide, the `stream_id` for the `custom_collections` table is `{{ stream-id }}` while its `tap_stream_id` is `{{ tap-stream-id }}`.
          2. A [Metadata object]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | append:"--arguments" | flatify }}) with a `breadcrumb` property that refers to the entire schema, and
          3. A [Stream-level Metadata object]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.stream-level.section | flatify }}) with a `selected` property with a `true` value. This is ultimately what will select the stream.

          This is an example of what the request body will look like:

          {% capture code %}{{ site.data.connect.code-examples.streams.request-bodies.blank-stream | prepend: quote | rstrip | append: quote }}
          {% endcapture %}

          {% assign description = "Example request body to update a stream's metadata" %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

          **Note**: Multiple streams in a source can be updated in a single request, but for clarity, this guide will focus on selecting a single stream. Refer to the [Update a Stream endpoint documentation]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | append:"--returns" | flatify }}) for examples.

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

          {% capture code %}{{ site.data.connect.code-examples.streams.request-bodies.database | rstrip | prepend: quote | append: quote }}
          {% endcapture %}

          {% assign description = "Example request body for a stream with a configurable Replication Method" %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

          **Note**: When `replication-method` is set to `INCREMENTAL`, the value of the `replication-key` property must be one of the following:

          1. One of the fields in the `valid-replication-keys` property, if provided. **Note**: If using this method, you must set the `replication-key` value using one of these fields. Selecting a field in the `valid-replication-keys` property for replication will not automatically set it as the stream's Replication Key.
          2. The name of an `integer`, `date-time`, or `timestamp` field in the stream. Refer to the [Replication Keys documentation]({{ link.replication.rep-keys | prepend: site.baseurl }}) for more info. 

          #### Streams with forced Replication Methods {#streams-forced-replication}

          In cases where a stream can only be replicated using one method, the stream's metadata may indicate the method it will use via the `forced-replication-method` property:

          {% capture code %}{{ site.data.connect.code-examples.streams.saas-stream | rstrip }}
          {% endcapture %}

          {% assign description = "Example metadata for a stream with a forced Replication Method" %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

          When the stream's metadata contains the `forced-replication-method` property, its Replication Method cannot be changed. If selected, the stream will use the `forced-replication-method` and the field in `valid-replication-keys` as a Replication Key, if applicable.

          Your request to select the stream will not need to include a `replication-method` property:

          {% capture code %}{{ site.data.connect.code-examples.streams.request-bodies.saas | rstrip | prepend: quote | append: quote }}
          {% endcapture %}

          {% assign description = "Example request body for a stream with a forced Replication Method" %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

      - title: "Submit the request"
        anchor: "submit-stream-request"
        endpoint: "PUT {{ site.data.connect.core-objects.streams.update.name | flatify }}"
        content: |
          To select a stream, make a request to [PUT {{ site.data.connect.core-objects.streams.update.name | flatify }}]({{ site.data.connect.api.section | prepend: site.baseurl | append: site.data.connect.core-objects.streams.update.anchor | flatify }}), replacing `{source_id}` with the source ID. The request body must contain with the [appropriate request body metadata properties](#configure-stream-replication):

          {% assign example-url = site.data.connect.core-objects.streams.update.name %}
          {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

          {% assign description = substep.endpoint %}

          {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.put.with-body request-url=request-url code=code%}

          {% capture code %}'{
             "streams":[
                {
                   "tap_stream_id":"custom_collections",
                   "metadata":[
                      {
                         "breadcrumb":[

                         ],
                         "metadata":{
                            "selected":true
                         }
                      }
                   ]
                }
             ]
          }'
          {% endcapture %}

  - title: "Select fields in a stream"
    anchor: "select-fields-in-a-stream"
    endpoint: "PUT {{ site.data.connect.core-objects.streams.update.name | flatify }}"
    content: |
      {% capture field-selection-rules %}
      Before selecting fields, refer to the [Field selection and compatibility rules guide]({{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}) to ensure the combinations of fields you select are valid for replication.
      {% endcapture %}
      {% include important.html type="single-line" content=field-selection-rules %}

      After stream selection, field selection can be used to select which fields are replicated from the source stream. The request to select a field is analogous to the request to select a stream, except that the `breadcrumb` should point to the field’s path in the schema.

      For example: This request selects the `id` field in the `custom_collections` stream:

      {% assign example-url = site.data.connect.core-objects.streams.update.name | strip_newlines %}
      {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

      {% assign description = "Selecting a single field via " | append: step.endpoint %}

      {% capture code %}{{ site.data.connect.code-examples.field-metadata.request-bodies.saas-field | rstrip | prepend: quote | append: quote }} 
      {% endcapture %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.put.with-body request-url=request-url code=code %}

      Multiple fields in a stream can be submitted as part of the same request. For each field included in the request body, include a `metadata` object referencing the field.

      For example: This request selects the `id`, `published_at`, `title`, and `handle` fields in the `custom_collections` stream:

      {% capture code %}{{ site.data.connect.code-examples.field-metadata.request-bodies.saas-fields | rstrip | prepend: quote | append: quote }} 
      {% endcapture %}

      {% assign description = "Selecting multiple fields via " | append: step.endpoint %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.put.with-body request-url=request-url code=code %}

      **Note**: Fields with metadata properties of `inclusion: automatic` or `selected-by-default: true` don't need to be explicitly selected through a request. These fields will be automatically selected for replication regardless of their `selected` value. Refer to the [Field selection and compatibility rules guide]({{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}) for more info.


# -------------------------- #
#         NEXT STEPS         #
# -------------------------- #

next-steps: |
  Stream and field selection may occur any time when a source's `current_step` is `field_selection` or `fully_configured`, as long as the source's report card has a `field_selection` step. To select additional streams and fields, follow steps 3 - 6 of this guide.
---