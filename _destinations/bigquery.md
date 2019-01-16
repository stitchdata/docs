---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Google BigQuery Destination
permalink: /destinations/bigquery/
layout: destination
tags: [bigquery_destination]
keywords: bigquery, google bigquery, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."

content-type: "destination-overview"

toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "BigQuery"
type: "bigquery"
db-type: "Analytic"
pricing_tier: "standard" ## for Stitch
status: "Released"
description: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."
pricing_model: "Usage" ## provider model
free_option: "No"
fully-managed: true
pricing_notes: "BigQuery's pricing isn't based on a fixed rate, meaning your bill can vary over time."
icon: /images/destinations/icons/google-bigquery.svg


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/bigquery.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0


# -------------------------- #
#            Links           #
# -------------------------- #
status-url: https://status.cloud.google.com/
sign-up: https://goo.gl/KSnUR2
documentation: https://cloud.google.com/bigquery/docs/
pricing: https://cloud.google.com/bigquery/pricing
storage-pricing: https://cloud.google.com/storage/pricing
price-calculator: https://cloud.google.com/products/calculator/
what-is-bq: https://cloud.google.com/bigquery/what-is-bigquery
setup-project: https://support.google.com/cloud/answer/6251787
cost-control: https://cloud.google.com/bigquery/cost-controls
enable-billing: https://support.google.com/cloud/answer/6288653?hl=en


# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description }}

  For more information, check out [Google's {{ destination.display_name }} overview]({{ destination.what-is-bq }}).

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Unlike many other cloud-based data warehouse solutions, {{ destination.display_name }}'s pricing model is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

      Before fully committing yourself to using {{ destination.display_name }} as your data warehouse, we recommend familiarizing yourself with the {{ destination.display_name }} pricing model and how using Stitch may impact your costs.

      **[Learn more about Stitch & {{ destination.display_name }} pricing]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }})**

  - title: "Setup info"
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