---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Panoply.io Destination
permalink: /destinations/panoply/
layout: destination
tags: [panoply_destination]
keywords: panoply, panoply.io, panoply data warehouse, panoply etl, etl to panoply
summary: "Panoply is a fully managed data warehouse service that will spin up a Redshift instance in just a few clicks. With Panoply, you can use your favorite analysis, SQL, and visualization tools just like you would if you were creating a Redshift data warehouse on your own."

content-type: "destination-overview"
key: "panoply-reference"

toc: true
layout: general
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Panoply"
type: "panoply"
port: 5439

this-version: "2.0"

# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/amazon-s3.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in _data/destinations/links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ destination.summary | flatify | markdownify }}

  If you're looking for a cost-effective, no-effort way to test out Stitch or get started consolidating your data, {{ destination.display_name }} is your best bet.

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Pricing varies from plan to plan, but every {{ destination.display_name }} plan includes:

      - Unlimited queries
      - Unlimited user accounts
      - Automatic maintenance, vacuuming, and backups

      {{ site.data.destinations.reference[destination.type]destination-details-info.pricing-details | flatify | markdownify }}

  - title: "Setup"
    anchor: "stitch-details-setup-info"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="stitch-details" %}

  - title: "Replication"
    anchor: "replication"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="replication" %}

  - title: "Limitations"
    anchor: "limitations"
    content: |
      In this section:

      {% assign list-items = "object-name-limits|table-limits|data-limits|column-naming" | split: "|" %}

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

      - title: "Table limits"
        anchor: "table-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="table-limits" %}

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