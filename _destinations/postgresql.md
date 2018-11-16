---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: PostgreSQL Destination
permalink: /destinations/postgresql/
layout: destination
tags: [postgresql_destination]
keywords: postgres, postgresql, postgres data warehouse, postgres etl, etl to postgres, postgresql data warehouse, etl to postgresql
summary: "An open-source relational database, PostgreSQL is a powerful and well-known system that has received recognition from both its users and the industry at large. Unlike some other database systems, PostgreSQL is completely customizable and yours to do with as you please (assuming, of course, that your instance is self-hosted)."

content-type: "destination-overview"

toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "PostgreSQL"
type: "postgres"
db-type: "Transactional"
pricing_tier: "standard" ## for Stitch
status: "Released"
description: "An open-source relational database, PostgreSQL is a powerful and well-known system that has received recognition from both its users and the industry at large. Unlike some other database systems, PostgreSQL is completely customizable and yours to do with as you please (assuming, of course, that your instance is self-hosted)."
port: 5432
pricing_model: "Varies" ## provider model
free_option: "Yes (self-hosted)"
fully-managed: "Depends"
pricing_notes: "The software for hosting your own PostgreSQL instance is open-source, meaning it's free. Heroku and Amazon RDS have a variety of plans to choose from."
icon: /images/destinations/icons/postgresql.svg


# -------------------------- #
#           Support          #
# -------------------------- #

ssl: true
ssh: true

incremental-upsert-support: true
connection-methods: "SSH, SSL"
supported-versions: "9.3+" ## if Stitch supports certain versions


nested-structure-support: false ## if true, natively supports nested structures
case: "Case Sensitive"
table-name-limit: "63" ## max # of characters
column-name-limit: "59" ## max # of characters
column-limit: "250-1,600" ## max # of columns allowed in tables
timestamp-range: "4713 BC to 294276 AD"
timezones:
  supported: false ## if false, no support for timezones
  storage: "Converted to UTC & <br>`TIMESTAMP WITHOUT TIME ZONE`" ## what happens to data with timezone info
timestamp-data: "Converted to UTC & <br>`TIMESTAMP WITHOUT TIME ZONE`"
varchar-limit: "None" ## max width for varchars
decimal-limit: "> 131,072 digits before the decimal or > 16,383 digits after"
decimal-range: "Stored without precision"
reserved-words: "https://www.postgresql.org/docs/9.6/static/sql-keywords-appendix.html"


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 2
## Facebook Ads
## Always Incompatible
## Subtables created from de-nesting exceed the 59 character limit for table names. 

# -------------------------- #
#            Links           #
# -------------------------- #
aws-calculator: http://calculator.s3.amazonaws.com/calc5.html
pricing: "/docs/destinations/postgresql#pricing"
main-site: https://www.postgresql.org/about/
documentation: https://www.postgresql.org

## Google CloudSQL Postgres Links
cloudsql-pricing: https://cloud.google.com/bigquery/pricing
price-calculator: https://cloud.google.com/products/calculator/

# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description | flatify | markdownify }}

  For a more in-depth look at {{ destination.display_name }}, [click here]({{ destination.main-site }}).
sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Pricing for {{ destination.display_name }} depends on where your instance is hosted.

      - **Self-hosted:** {{ destination.display_name }} is open-source, meaning you don't need to pay an upfront cost to obtain the necessary software. You may, however, have hosting and maintenance costs associated with the server housing the instance. You may have to do a little bit of internal number crunching to figure out these potential costs. 
      - **Heroku:** Heroku has a [variety of plans to choose from](https://www.heroku.com/pricing), and [a guide to help you select the right plan](https://devcenter.heroku.com/articles/heroku-postgres-plans) for you or your company.
      - **Amazon RDS:** Amazon offers [a variety of plans](https://aws.amazon.com/rds/postgresql/pricing/) for both on-demand instances and Multi-AZ Deployment. To get an estimate of what your monthly bill might look like, check out their [monthly calculator]({{ destination.aws-calculator }}).
      - **Google CloudSQL PostgreSQL:** Unlike many other cloud-based data warehouse solutions, [Google's pricing model]({{ destination.cloudsql-pricing }}) is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

         Before fully committing yourself to using Google CloudSQL PostgreSQL as your data warehouse, we recommend familiarizing yourself with Google's pricing model and [using their pricing calculator to estimate your potential costs]({{ destination.price-calculator }}).

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