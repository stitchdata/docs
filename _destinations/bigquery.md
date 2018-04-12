---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Google BigQuery Destination
permalink: /destinations/bigquery/
layout: destination-overview
tags: [bigquery_destination]
keywords: bigquery, google bigquery, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."
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
incremental-replication: "Append-Only"
connection-methods: "SSL"
supported-versions: "n/a"

nested-structure-support: true ## if true, natively supports nested structures
case: "Case Insensitive"
table-name-limit: "1,024" ## max # of characters
column-name-limit: "128" ## max # of characters
column-limit: "10,000" ## max # of columns allowed in tables
timestamp-range: "Long/MIN_Value(292269055-12-02T16:47:04.192-00:00)<br>AND<br>Long/MAX_LONG (292278994-08-17T07:12:55.807-00:00)"
timezones:
  supported: false
  storage: "No support for timezones."
varchar-limit: "None" ## max width for varchars
integer-limit: "-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807" # https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types
decimal-limit: "38 numbers, or places"
decimal-range: "Not applicable"
reserved-words: "https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved_keywords"


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
  - title: "pricing"
    content: |
      Unlike many other cloud-based data warehouse solutions, {{ destination.display_name }}'s pricing model is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

      Before fully committing yourself to using {{ destination.display_name }} as your data warehouse, we recommend familiarizing yourself with the {{ destination.display_name }} pricing model and how using Stitch may impact your costs.

      **[Learn more about Stitch & {{ destination.display_name }} pricing]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }})**

  - title: "setup"
    content: |
      To set up {{ destination.display_name }}, Stitch requires:

      1. **A user with access to an existing [Google Cloud Platform project within {{ destination.display_name }}]({{ destination.setup-project }}){:target="_blank"}**. Stitch won't be able to create one for you.
      2. **Admin permissions for BigQuery and Google Cloud Storage (GCS)**. This includes the BigQuery Admin and Storage Admin permissions.
      2. **Access to a project where [billing is enabled]({{ destination.enable-billing }}){:target="_blank"} and a credit card is attached**. Even if you're using BigQuery's free trial, billing must still be enabled for Stitch to load data.

      **[Spin up a {{ destination.display_name }} data warehouse]({{ link.destinations.setup.bigquery | prepend: site.baseurl }})**

  - title: "limitations"
    include: |
      {% include destinations/overviews/limitations.html %}

  - title: "replication"
    include: |
      {% include destinations/overviews/replication-process.html %}

  - title: "schema"
    include: |
      {% include destinations/overviews/integration-schemas.html %}

---
{% assign destination = page %}
{% include misc/data-files.html %}