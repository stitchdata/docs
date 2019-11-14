---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Amazon S3 Destination Reference
permalink: /destinations/amazon-s3/v1/reference
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3
summary: "Reference documentation for Stitch's Amazon S3 destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "amazon-s3-reference"

layout: general
sidebar: on-page
toc: false

data-loading: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect an {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.amazon-s3 | prepend: site.baseurl }}"

  - title: "All {{ page.display_name }} docs"
    link: "{{ site.baseurl }}/destinations/amazon-s3"


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Amazon S3"
type: "amazon-s3"

this-version: "1"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/bigquery and 
## _data/destinations/amazon-s3 for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in:
## _data/destinations/amazon-s3/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ destination.summary | flatify }}

  This guide serves as a reference for version {{ destination.this-version }} of Stitch's {{ destination.display_name }} destination.

sections:
  - title: "Details and features"
    anchor: "details-and-features"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Stitch features"
        anchor: "stitch-features"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="stitch-details" %}

      - title: "Destination details"
        anchor: "destination-details"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="destination-details" %}

      - title: "Amazon S3 pricing"
        anchor: "pricing"
        content: |
          {{ site.data.destinations.reference[destination.type]destination-details-info.pricing-details | flatify }}

          To learn more about pricing, refer to Amazon's S3 [pricing page]({{ site.data.destinations[destination.type]resource-links.pricing }}){:target="new"}. **Note**: Remember to select the correct region to view accurate pricing.

  - title: "Replication"
    anchor: "replication"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Replication process overview"
        anchor: "replication-process-overview"
        content: |
          A Stitch replication job consists of three stages:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Step 1: Data extraction"
            anchor: "replication--data-extraction"
            content: |
              {% include replication/replication-process-phases.html phase="data-extraction" %}

          - title: "Step 2: Preparation"
            anchor: "replication--stitch-internal-pipeline"
            content: |
              {{ site.data.tooltips.prepare }} Refer to the [System overview guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture--preparing" }}) for a more detailed explanation of the Preparation phase.

          - title: "Step 3: Loading"
            anchor: "replication--loading"
            content: |
              {{ site.data.tooltips.load }} For {{ destination.display_name }} destinations, data is loaded in an Append-Only fashion into the file format (`.csv` or `.jsonl`) you select during destination setup. Refer to the [Loading behavior](#loading-behavior) section for more info and examples.

              **Note**: The transformations Stitch performs when loading data into {{ destination.display_name }} depends on the data storage format selected during destination setup. Refer to the [Transformations](#transformations) section for more info.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          When data is loaded into an {{ destination.display_name }} destination, it will be loaded in an Append-Only fashion. This means that:

          - A new CSV or JSON file for every table replicated is created during each load. A single table in the source will correspond to multiple files in the destination.
          - Existing records - that is, records in files already in the destination - are never updated
          - Data will not be de-duped, meaning that multiple versions of the same record may exist across multiple files in the data warehouse

          Because of this loading strategy, querying may require a different approach than usual. Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time. Refer to the [Querying Append-Only Tables documentation]({{ link.replication.append-only | prepend: site.baseurl }}) for more info.

        sub-subsections:
          - title: "Example: Key-based Incremental Replication"
            anchor: "loading-behavior--example"
            content: |
              Below is an example of how tables using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) will be loaded into {{ destination.display_name }}:

              ![Example {{ destination.display_name }} data loading diagram]({{ site.baseurl }}/images/destinations/append-only-s3.png)

      - title: "File structure"
        anchor: "schema"
        content: |
          The file structure of your integrations' data in your {{ destination.display_name }} bucket depends on two destination parameters:

          1. The definition of the Object Key, and
          2. The selected data storage format (CSV or JSON)
        sub-subsections:
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

          - title: "Data storage formats"
            anchor: "data-storage-formats"
            content: |
              Stitch will store replicated data in the format you select during the initial setup of {{ destination.display_name }}. Currently Stitch supports storing data in CSV or JSON format for {{ destination.display_name }} destinations.

              The tabs below contain an example of raw source data and how it would be stored in {{ destination.display_name }} for each data storage format type.

              {% capture csv-top-level-example %}
              **Top-level Table**
              
              In {{ destination.display_name }}, this data would create a file named `{{ stitch.sample-data.table-name | append: "/" | append: "1_[timestamp].csv" }}`, which would look like this:
              {% endcapture %}

              {% capture csv-sub-level-example %}
              While objects (like `phone_numbers`) will be flattened into the table, arrays are handled differently.

              **Subfiles**

              Arrays will be de-nested and flattened into subfiles. In this example, the name of the file would be `{{ stitch.sample-data.table-name | append: "/" | append: stitch.sample-data.subtable-name | append: "/" | append: "1_[timestamp].csv" }}`:
              {% endcapture %}

              {% capture csv-guide-copy %}
              For more info and examples on how Stitch flattens nested data structures, refer to the [Nested Data Structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).
              {% endcapture %}

              {% capture json-example %}
              With the exception of the `{{ system-column.prefix }}` columns, Stitch will store replicated data intact as `.jsonl` files. In this example, the name of the file would be `{{ stitch.sample-data.table-name | append: "/" | append: "1_[timestamp].jsonl" }}`:

              {{ stitch.sample-data.json-stored | flatify | markdownify }}
              {% endcapture %}

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
              {{ csv-top-level-example | flatify | markdownify }}

              {% include destinations/overviews/data-storage-examples.html type="top-level-table" %}

              {{ csv-sub-level-example | flatify | markdownify }}

              {% include destinations/overviews/data-storage-examples.html type="sub-table" %}

              {{ csv-guide-copy | flatify | markdownify }}
              </div>

              <div role="tabpanel" class="tab-pane" id="json">
              {{ json-example | flatify | markdownify }}
              </div>
              </div>

      - title: "Incompatible sources"
        anchor: "replication--incompatible-sources"
        content: |
          {% include shared/incompatibilities/destination-version-incompatibilities.html %}

  - title: "Transformations"
    anchor: "transformations"
    content: |
      **Note**: Aside from these transformations, the data loaded into {{ destination.display_name }} is in its raw form.

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "System tables and columns"
        anchor: "transformations--system-tables-columns"
        content: |
          **Note**: This applies to all [data storage formats](#data-storage-formats).

          For every integration you connect, an `{{ stitch.system-tables.sdc-rejected.name }}` folder will be created in the integration's directory in {{ destination.display_name }}. For every load where a rejection occurs, a `.jsonl` file containing data about the rejection will be placed in the `{{ stitch.system-tables.sdc-rejected.name }}` folder. **Note**: These files will be `.jsonl`, even if `.csv` is selected as the file format during destination setup.

          Additionally, Stitch will insert [system columns]({{ link.destinations.storage.system-tables-and-columns | prepend: site.baseurl }}) (prepended with `{{ system-column.prefix }}`) into each file (`.csv` or `.jsonl`) created for each table.

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          How JSON structures are stored in {{ destination.display_name }} destinations depends on the [data storage format](#data-storage-formats) selected during destination setup:

          - **CSV**: Nested JSON structures will be flattened into relational objects. This means that nested maps (JSON objects) will be flattened into the CSV file, and nested records (JSON arrays) will be de-nested into subfiles.

          - **JSON**: Nested JSON structures are stored as-is, as all data is stored in JSON files.

          Refer to the [Data storage formats](#data-storage-formats) section for examples of how nested data will be stored for each data storage format.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}