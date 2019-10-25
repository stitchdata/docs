---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Amazon S3 Destination
permalink: /destinations/amazon-s3/
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3
summary: &summary "Amazon S3 is a simple, reliable, and cost-effective object store that provides nearly endless capacity to safely store data in the cloud. Its flexibility allows users the ability to not only persist data ranging from bytes to petabytes, but also consume it via a myriad of tools like Amazon Athena and Qubole."

content-type: "destination-overview"
key: "amazon-s3-reference"

toc: true
layout: general
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

this-version: "1.0"

# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/amazon-s3.yml for
## info about connection support, Stitch support,
## data limitations, etc.

## Resource links can be found in _data/destinations/links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: "{{ destination.summary | flatify }}"

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      {{ site.data.destinations.reference[destination.type]destination-details-info.pricing-details | flatify }}

      To learn more about pricing, refer to Amazon's S3 [pricing page]({{ site.data.destinations.resource-links[destination.type]pricing }}){:target="new"}. **Note**: Remember to select the correct region to view accurate pricing.

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

              #### Example: Key-based Incremental Replication

              Below is an example of how tables using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) will be loaded into {{ destination.display_name }}:

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
          {{ site.data.ui.destination-settings[destination.type]object-keys.default }}


          /* Example Object Keys */
            - {{ site.data.ui.destination-settings[destination.type]object-keys.example-1 }}
            - {{ site.data.ui.destination-settings[destination.type]object-keys.example-2 }}
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
---
{% assign destination = page %}
{% include misc/data-files.html %}