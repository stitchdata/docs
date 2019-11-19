---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Panoply.io Destination Reference
permalink: /destinations/panoply/reference
keywords: panoply, panoply.io, panoply data warehouse, panoply etl, etl to panoply
summary: "Reference documentation for Stitch's Panoply.io destination, including info about Stitch features, replication, and transformations."

content-type: "destination-overview"
key: "panoply-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a new {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.panoply-new | prepend: site.baseurl }}"

  - title: "Connect an existing {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.panoply-ex | prepend: site.baseurl }}"

  - title: "Loading nested structures in {{ page.display_name }}"
    link: "{{ link.destinations.storage.nested-structures | prepend: site.baseurl }}"

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Panoply"
type: "panoply"

this-version: "2"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/panoply for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in
## _data/destinations/panoply/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.panoply.destination-details.description | flatify }}

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

      - title: "Pricing"
        anchor: "pricing"
        content: |
          Pricing varies from plan to plan, but every {{ destination.display_name }} plan includes:

          - Unlimited queries
          - Unlimited user accounts
          - Automatic maintenance, vacuuming, and backups

          {{ site.data.destinations.panoply.destination-details.pricing-details | flatify | markdownify }}

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
          {% assign version = destination.this-version | prepend: "v" %} 
          By default, Stitch will use **{{ site.data.destinations[destination.type][version]replication.default-loading-behavior }} loading** when loading data into {{ destination.display_name }}.

          If the conditions for Upsert loading aren't met, data will be loaded using Append-Only loading.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

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

# Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.
      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          {{ destination.display_name }} destinations don't have native support for nested data structures. To ensure nested data can be loaded, Stitch will flatten objects and arrays into columns and subtables, respectively. For more info and examples, refer to the [Handling nested data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.panoply.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.redshift.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          {{ destination.display_name }} will store the value as `TIMESTAMP WITHOUT TIMEZONE`. In {{ destination.display_name }}, this data is stored without timezone information and expressed as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}