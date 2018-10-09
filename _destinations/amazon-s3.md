---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Amazon S3 Destination
permalink: /destinations/amazon-s3/
layout: destination
tags: [bigquery_destination]
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3
summary: &summary "Amazon S3 is a simple, reliable, and cost-effective object store that provides nearly endless capacity to safely store data in the cloud. Its flexibility allows users the ability to not only persist data ranging from bytes to petabytes, but also consume it via a myriad of tools like Amazon Athena and Qubole."
toc: true
destination: true
data-loading: false


enterprise-cta:
  title: "Need loading notifications?"
  url: "?utm_medium=docs&utm_campaign=s3-webhook-notifications"
  copy: |
    As part of an Enterprise plan, you can set up configurable webhooks to notify you when fresh data has finished loading into your destination. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Amazon S3"
type: "amazon-s3"
db-type: "s3"
pricing_tier: "standard"
status: "Released"
description: *summary
pricing_model: "Storage"
free_option: "Yes (plan & trial)"
fully-managed: false
pricing_notes: "{{ destination.display_name }} pricing is based on two factors: the amount of data stored in and location (region) of your {{ destination.display_name }} bucket."
icon: /images/destinations/icons/amazon-s3.svg


# -------------------------- #
#           Support          #
# -------------------------- #
incremental-replication: "Append-Only"
connection-methods: "n/a"
supported-versions: "n/a"

nested-structure-support: true
case: "Case Insensitive"
table-name-limit: "n/a"
column-name-limit: "n/a"
column-limit: "n/a"
timestamp-range: "n/a"
timezones:
  supported: false
  storage: "n/a"
varchar-limit: "None"
decimal-limit: "n/a"
decimal-range: "n/a"
reserved-words: "None"


# -------------------------- #
#    Object Key Elements     #
# -------------------------- #
key-elements:
  - name: "integration_name"
    required: true
  - name: "table_name"
    required: true
  - name: "table_version"
    required: true
  - name: "timestamp_loaded"
    required: true
    description: " - <strong>Note</strong>: This is a Unix timestamp."
  - name: "year_loaded"
    required: false
  - name: "day_loaded"
    required: false
  - name: "month_loaded"
    required: false
  - name: "hour_loaded"
    required: false
  - name: "Arbitrary text"
    required: false

default-key: "[integration_name]/[table_name]/[table_version]_[timestamp_loaded].[csv|jsonl]"
example-key-1: "salesforce-prod/account/1_1519235654474.[csv|jsonl]"
example-key-2: "salesforce-prod/opportunity/1_1519327555000.[csv|jsonl]"

# -------------------------- #
#    Required Permissions    #
# -------------------------- #
permissions:
  - name: "s3:PutObject"
    operations:
      - name: "PUT Object"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUT.html"
        description: "Allows the addition of objects to a bucket."

      - name: "POST Object"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html"
        description: "An alternate form of `PUT Ojbect`, this allows the addition of objects to a bucket using HTML forms."

      - name: "Initiate Multipart Upload"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html"
        description: "Allows a multipart upload and return of an upload ID."

      - name: "Upload Part"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadUploadPart.html"
        description: "Allows for the upload of a part in a multipart upload."

      - name: "Complete Multipart Upload"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html"
        description: "Allows for the completion of a multipart upload by assembling previously uploaded parts."

      - name: "PUT Object - Copy"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadUploadPartCopy.html"
        description: "Allows for the upload of a part by copying data from an existing object as the data source."
  - name: "s3:GetObject"
    operations:
      - name: "GET Object"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html"
        description: "Allows for the retrieval of objects from {{ destination.display_name }}."

      - name: "HEAD Object"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectHEAD.html"
        description: "Allows for the retrieval of metadata from an object without returning the object itself."
  - name: "s3:ListBucket"
    operations:
      - name: "GET Bucket (List Objects)"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/v2-RESTBucketGET.html"
        description: "Allows for the return of some or all (up to 1,000) of the objects in a bucket."

      - name: "HEAD Bucket"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketHEAD.html"
        description: "Used to determine if a bucket exists and access is allowed."


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0

# -------------------------- #
#            Links           #
# -------------------------- #
status-url: https://status.aws.amazon.com/
sign-up: https://aws.amazon.com/s3/
documentation: https://aws.amazon.com/documentation/s3/
pricing: https://aws.amazon.com/s3/pricing/
price-calculator: http://aws.amazon.com/calculator/


# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: "{{ destination.description | flatify }}"

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      {{ destination.pricing_notes | flatify }}

      To learn more about pricing, refer to Amazon's S3 [pricing page]({{ destination.pricing }}). **Note**: Remember to select the correct region to view accurate pricing.

  - title: "Setup info"
    anchor: "stitch-details-setup-info"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="stitch-details" %}

  - title: "Replication"
    anchor: "replication"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="replication" %}

    subsections:
      - title: "Replication process overview"
        anchor: "replication-process-overview"
        content: |
          A Stitch replication job consists of three stages: Extraction, Preparation, and Loading.
        sub-subsections:
          - title: "Data extraction"
            anchor: "extraction"
            content: |
              During the **Extraction** phase, Stitch will check for structural changes to your data, query for data according to the integration's replication settings, and extract the appropriate data.

              Replication settings include the integration's [Replication Schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}), the [data set to replicate]({{ link.replication.syncing | prepend: site.baseurl }}), and the selected tables' [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}).

              **Note**: Because Stitch's Incremental Replication Method is inclusive, a single row will be replicated for every Incremental table even if there's no new or updated data. Refer to the [Replication Methods documentation]({{ link.replication.rep-methods | prepend: site.baseurl }}) for an explanation and examples.

          - title: "Data preparation/transformations for {{ destination.display_name }}"
            anchor: "preparation"
            content: |
              During the **Preparation** phase, Stitch applies some light transformations to the extracted data to ensure compatibility with the destination.

              The transformations Stitch performs depends on the selected data storage format (CSV or JSON). Aside from these transformations, the data loaded into {{ destination.display_name }} is in its raw form. Refer to the [Schema](#schema) section for more info and examples.

              <table class="attribute-list">
              <tr>
              <th width="50%; fixed">CSV</th>
              <th>JSON</th>
              </tr>
              <tr>
              <td>
              <ul>
              <li>
              <a href="{{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}">
              Stitch (<code>_sdc</code>) system columns</a>
              are inserted into every table</li>
              <li>Nested data structures are <a href="{{ link.destinations.storage.nested-structures | prepend: site.baseurl }}">flattened into relational objects</a>. Refer to the <a href="#data-storage-formats">Data Storage Formats</a> section below for an example.</li>
              </ul>
              </td>
              <td>
              <ul>
              <li>Stitch (<code>_sdc</code>) system columns are inserted into every table</li>
              </ul></td>
              </tr>
              </table>

          - title: "Loading data into {{ destination.display_name }}"
            anchor: "loading"
            content: |
              During **Loading**, Stitch loads the extracted data into the destination. For {{ destination.display_name }} destinations, data is loaded in an Append-Only fashion.

              This means that:

              - A new CSV or JSON file for every table replicated is created during each load
              - Existing records - that is, records already in the bucket - are never updated
              - Data will not be de-duped, meaning that multiple versions of the same record may exist in the data warehouse

              Because of this loading strategy, querying may require a different strategy than usual. Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time. Refer to the [Querying Append-Only Tables documentation]({{ link.replication.append-only | prepend: site.baseurl }}) for more info.

              #### Example: Incremental Replication

              Below is an example of how [incrementally replicated tables]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication"}}) will be loaded into {{ destination.display_name }}:

              ![Example {{ destination.display_name }} data loading diagram]({{ site.baseurl }}/images/destinations/append-only-s3.png)

  - title: "Schema"
    anchor: "schema"
    content: |
      The file structure of your integrations' data in your {{ destination.display_name }} bucket depends on two destination parameters:

      1. The definition of the Object Key, and
      2. The selected data storage format (CSV or JSON)

    subsections:
      - title: "Object Keys and file structure"
        anchor: "object-keys-file-structure"
        content: |
          {{ destination.display_name }} uses what is called an Object Key to uniquely identify objects in a bucket. During the Stitch setup process, you have the option of using our default Object Key or defining your own using a handful of Stitch-approved elements. Refer to the [{{ destination.display_name }} Setup instructions]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#define-s3-object-key" }}) for more info on the available elements.

          The S3 Key setting determines the convention Stitch uses to create Object Keys when it writes to your bucket. It also defines the folder structure of Stitch-replicated data.

          Below is the default Key and two examples of an Object Key that an integration named `salesforce-prod` might produce:

          ```shell
          /* Default Key */
          {{ destination.default-key }}


          /* Example Object Keys */
            - {{ destination.example-key-1 }}
            - {{ destination.example-key-2 }}
          ```

          As previously mentioned, the S3 Key also determines the folder structure of replicated data. In the AWS console, the folder structure for the `salesforce-prod` integration would look like the following:

          ```shell
          .
          └── salesforce-prod
              └── account
              |   └── 1_1519235654474.[csv|jsonl]
              └── opportunity
              |   └── 1_1519327555000.[csv|jsonl]
              └── {{ rejected-records.name }}
                  └── 1_[timestamp].jsonl
                  └── 1_[timestamp].jsonl
          ```

          #### {{ rejected-records.name }}

          For every integration you connect, an `{{ rejected-records.name }}` folder will be created in the integration's directory in {{ destination.display_name }}. `{{ rejected-records.name }}` acts as a [log for records rejected during the loading process]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}). For every load where a rejection occurs, a `.jsonl` file containing data about the rejection will be placed in the `{{ rejected-records.name }}` folder.

      - title: "Data storage formats"
        anchor: "data-storage-formats"
        content: |
          Stitch will store replicated data in the format you select during the initial setup of {{ destination.display_name }}. Currently Stitch supports storing data in CSV or JSON format for {{ destination.display_name }} destinations.

          The tabs below contain an example of raw source data and how it would be stored in {{ destination.display_name }} for each data storage format type.

          <ul id="profileTabs" class="nav nav-tabs">
              <li class="active">
                <a href="#original-data" data-toggle="tab">Raw Source Data</a>
              </li>
              <li>
                <a href="#csv-quoted" data-toggle="tab">CSV</a>
              </li>
              <li>
                <a href="#json" data-toggle="tab">JSON</a>
              </li>
          </ul>
          <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="original-data">
                {{ stitch.sample-data.json-original | markdownify }}
              </div>

              <div role="tabpanel" class="tab-pane" id="csv-quoted">
                <p><strong>Top-level Table</strong></p>
                <p>In {{ destination.display_name }}, this data would create a file named <code>{{ stitch.sample-data.table-name | append: "/" | append: "1_[timestamp].csv" }}</code>, which would look like this:</p>
                {% include destinations/overviews/data-storage-examples.html type="top-level-table" %}

                <p>While objects (like <code>phone_numbers</code>) will be flattened into the table, arrays are handled differently.</P>

                <p><strong>Subtables</strong></p>

                <p>Arrays will be de-nested and flattened into subtables. In this example, the name of the file would be <code>{{ stitch.sample-data.table-name | append: "/" | append: stitch.sample-data.subtable-name | append: "/" | append: "1_[timestamp].csv" }}</code>:</p>

                {% include destinations/overviews/data-storage-examples.html type="sub-table" %}

                <p>For more info and examples on how Stitch flattens nested data structures, refer to the <a href="{{ link.destinations.storage.nested-structures | prepend: site.baseurl }}">Nested Data Structures guide</a>.</p>
              </div>

              <div role="tabpanel" class="tab-pane" id="json">
                <p>With the exception of the <code>{{ system-column.prefix }}</code> columns, Stitch will store replicated data intact as <code>.jsonl</code> files. In this example, the name of the file would be <code>{{ stitch.sample-data.table-name | append: "/" | append: "1_[timestamp].jsonl" }}</code>:</p>

                {{ stitch.sample-data.json-stored | flatify | markdownify }}
              </div>
          </div>

  - title: "Limitations"
    anchor: "limitations"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="data-limits" %}

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.

  # - title: "Webhook loading notifications"
  #   anchor: "webhook-loading-notifications"
  #   content: |
  #     {% include enterprise-cta.html %}
  #     Webhooks allow external services to be notified when an event happens. If you choose, you can configure a webhook for Stitch to notify you when data is successfully loaded into your bucket.

  #     Webhook notifications are sent on a per-integration basis. This means that every time Stitch successfully loads data for an integration, a summary webhook will be sent to the URL you define.

  #   subsections:
  #     - title: "Sample use cases"
  #       anchor: "webhook-notification-sample-use-cases"
  #       content: |
  #         Enabling loading notifications ensures that you and your team are alerted when fresh data is available in {{ destination.display_name }}. For example, you could:

  #         - Set up a webhook Zap in Zapier that sends a Slack notification whenever data is loaded for a specific integration
  #         - Use loading notifications to kick off an internal process, such as [DBT](https://www.getdbt.com/) or a script

  #     - title: "Webhook request body"
  #       anchor: "webhook-body"
  #       content: |
  #         {% include destinations/overviews/webhook-loading-notification.html type="request-body" %}

  #     - title: "Webhook request body fields"
  #       anchor: "webhook-request-body-fields"
  #       content: |
  #         {% include destinations/overviews/webhook-loading-notification.html type="request-body-fields" %}
---
{% assign destination = page %}
{% include misc/data-files.html %}
