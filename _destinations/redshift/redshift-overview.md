---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Amazon Redshift Destination
permalink: /destinations/amazon-redshift/v2/reference
keywords: redshift, amazon redshift, redshift data warehouse, redshift etl, etl to redshift
summary: "Reference documentation for Stitch's Amazon Redshift destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "redshift-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.bigquery | prepend: site.baseurl }}"

  - title: "Loading nested structures in {{ page.display_name }}"
    link: "{{ link.destinations.storage.bigquery-nested-structures | prepend: site.baseurl }}"

  - title: "TODO: All {{ page.display_name }} docs"
    link: ""


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Amazon Redshift"
type: "redshift"

this-version: "2"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/redshift for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in 
## _data/destinations/redshift/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.redshift.destination-details.description | flatify }}

  This guide serves as a reference for version {{ destination.this-version }} of Stitch's {{ destination.display_name }} destination.

sections:
  - title: "Details and features"
    anchor: "details-and-features"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
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

      - title: "Encodings, SORT, and DIST keys"
        anchor: "encodings-sort-dist-keys"
        content: |
          To improve your query performance, you can apply encodings, SORT, and DIST keys to Stitch-created tables in your {{ destination.display_name }} destination. Your settings will remain intact even when new data is loaded.

          Refer to the [Encodings, SORT, and DIST Keys guide]({{ link.destinations.storage.redshift-encodings | prepend: site.baseurl }}) for application instructions.

      - title: "{{ page.display_name }} pricing"
        anchor: "pricing"
        content: |
          Currently, {{ destination.display_name}} pricing is based on an hourly rate that varies depending on the type and number of nodes in a cluster. Check out Amazon's [pricing page]({{ site.data.destinations[destination.type]resource-links.pricing }}){:target="new"} for an in-depth look at their current plan offerings.

          **So, what's a node?** A node is a single computer that participates in a cluster. Your {{ destination.display_name }} cluster can have one to many nodes; the more nodes, the more data it can store and the faster it can process queries. Amazon currently offers four different types of nodes, each of which has its own CPU, RAM, storage capacity, and storage drive type.

          The type and number of node(s) you choose when creating your cluster is dependent on your needs and dataset. We do, however, recommend you set up a multi-node configuration to provide data redundancy.

          For some guidance on choosing the right number of nodes for your cluster, check out Amazon's [Determining the Number of Nodes guide](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes){:target="new"}.

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
              Stitch loads the data into {{ destination.display_name }}.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          When data is loaded into {{ destination.display_name }}, Stitch will upsert the data. This means that existing rows are updated in tables with [defined Primary Keys](#replication--primary-keys). A single version of a row will exist in the table.

          If a table doesn't have defined Primary Keys, data will be loaded in an Append-Only fashion. New rows and modifications to existing rows will be appended at the end of the table. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

          [TODO - Add link to loading behavior guide]

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          Stitch requires Primary Keys to de-dupe incrementally replicated data. To ensure Primary Key data is available, Stitch creates a `primary_keys` [table comment](https://docs.aws.amazon.com/redshift/latest/dg/r_COMMENT.html){:target="new"}. The comment is an array of strings that contain the names of the Primary Key columns for the table. 

          For example: A table comment for a table with a single Primary Key:

          ```json
          '{"primary_keys":["id"]}'
          ```

          And a table comment for a table with a composite Primary Key:

          ```json
          '{"primary_keys":["event_id","created_at"]}'
          ```

          **Note**: Removing or incorrectly altering Primary Key table comments can lead to replication issues.

      - title: "Incompatible sources"
        anchor: "replication--incompatible-sources"
        content: |
          {% include shared/incompatibilities/destination-version-incompatibilities.html %}

  - title: "Transformations"
    anchor: "transformations"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "System tables and columns"
        anchor: "transformations--system-tables-columns"
        content: |
          Stitch will create the following tables in each integration's dataset:

          - [{{ stitch.system-tables.sdc-rejected.name }}]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }})

          Additionally, Stitch will insert [system columns]({{ link.destinations.storage.system-tables-and-columns | prepend: site.baseurl }}) (prepended with `{{ system-column.prefix }}`) into each table.

      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          {{ destination.display_name }} destinations don't have native support for nested data structures. To ensure nested data can be loaded, Stitch will flatten objects and arrays into columns and subtables, respectively. For more info and examples, refer to the [Handling nested data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.redshift.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.redshift.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          [TODO]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#timezones" }})

          {{ destination.display_name }} will store the value as `TIMESTAMP WITHOUT TIMEZONE`. In {{ destination.display_name }}, this data is stored without timezone information and expressed as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}