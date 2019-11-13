---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Snowflake Destination
permalink: /destinations/snowflake/
layout: destination
tags: [snowflake_destination]
keywords: snowflake, snowflake destination, snowflake data warehouse, snowflake etl, etl to snowflake
summary: "Snowflake is a SQL data warehouse built from the ground up for the cloud, designed with a patented new architecture to handle today’s and tomorrow’s data and analytics."

content-type: "destination-overview"
key: "snowflake-reference"

toc: true
layout: general
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Snowflake"
type: "snowflake"

this-version: "1"

# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/snowflake.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in _data/destinations/links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #
intro: |
  {{ destination.description }}

  A fully-managed SaaS data warehouse solution, Snowflake runs on [Amazon Web Services](http://aws.amazon.com/){:target="new"} cloud infrastructure: AWS EC2 virtual compute instances are used for compute needs, while S3 is utilized for persistent data storage.

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      {{ site.data.destinations.reference[destination.type]destination-details-info.pricing-details | flatify }}
    subsections:
      - title: "Snowflake warehouse sizes"
        anchor: "warehouse-sizes"
        content: |
          Snowflake data warehouses can be different sizes - X-Small, Large, and 3X-Large, for example - which defines how many servers will comprise each cluster in a warehouse.

          While the size of a warehouse can impact the time required to execute queries, bigger doesn't always mean better. Warehouse size is directly tied to the number of credits used, which will directly impact your Snowflake costs. [Learn more about Snowflake warehouse sizes here](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html){:target="_blank"}.

          To help you select the warehouse size that fits your needs and budget, check out [Snowflake's Warehouse Considerations guide](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html){:target="_blank"} before getting started.

      - title: "Automated warehouse management"
        anchor: "automated-warehouse-management"
        content: |
          To reduce usage, you can elect to automate the management of your Snowflake warehouse. This means that you can elect to suspend the warehouse when there's no activity after a specified period of time, and then automatically resume when there is. Note that these settings apply to the entire warehouse and not individual clusters.

          Enabling these settings depends on your workload and availability needs. [Learn more about the Auto Suspend and Auto Resume features here](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html#automating-warehouse-management){:target="_blank"}.

          **Note**: Stitch will only ever impact your Snowflake usage when loading data.

  - title: "Setup"
    anchor: "stitch-details-setup-info"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="stitch-details" %}

  - title: "Replication"
    anchor: "replication"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="replication" %}

      {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

  - title: "Limitations"
    anchor: "limitations"
    content: |
      In this section:

      {% assign list-items = "object-name-limits|data-limits|column-naming" | split: "|" %}

      {% for item in list-items %}
      {% for category in reference-categories[item] %}
      - [**{{ category.name }}**](#{{ item }}) - {{ category.description | flatify }}
      {% endfor %}
      {% endfor %}

    subsections:
      - title: "Object name limits"
        anchor: "object-name-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="object-name-limits" %}

      - title: "Data limits"
        anchor: "data-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="data-limits" %}

      - title: "Column naming"
        anchor: "column-naming"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="column-naming" %}

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}