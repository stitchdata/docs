---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: PostgreSQL Destination
permalink: /destinations/postgresql/
keywords: postgres, postgresql, postgres data warehouse, postgres etl, etl to postgres, postgresql data warehouse, etl to postgresql
summary: "An open-source relational database, PostgreSQL is a powerful and well-known system that has received recognition from both its users and the industry at large. Unlike some other database systems, PostgreSQL is completely customizable and yours to do with as you please (assuming, of course, that your instance is self-hosted)."

content-type: "destination-overview"
key: "postgresql-reference"

toc: true
layout: general
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "PostgreSQL"
type: "postgres"

this-version: "1"

# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/postgres.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in _data/destinations/links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ destination.summary | flatify | markdownify }}

  For a more in-depth look at {{ destination.display_name }}, [click here]({{ site.data.destinations.postgres.resource-links.main-site }}).
  
sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Pricing for {{ destination.display_name }} depends on where your instance is hosted.

      - **Self-hosted:** {{ destination.display_name }} is open-source, meaning you don't need to pay an upfront cost to obtain the necessary software. You may, however, have hosting and maintenance costs associated with the server housing the instance. You may have to do a little bit of internal number crunching to figure out these potential costs. 
      - **Heroku:** Heroku has a [variety of plans to choose from](https://www.heroku.com/pricing), and [a guide to help you select the right plan](https://devcenter.heroku.com/articles/heroku-postgres-plans) for you or your company.
      - **Amazon Aurora and RDS:** Amazon offers [a variety of plans](https://aws.amazon.com/rds/postgresql/pricing/) for both on-demand instances and Multi-AZ Deployment. To get an estimate of what your monthly bill might look like, check out their [monthly calculator]({{ site.data.destinations[destination.type]resource-links.aws-calculator }}).
      - **Google CloudSQL PostgreSQL:** Unlike many other cloud-based data warehouse solutions, [Google's pricing model]({{ site.data.destinations.postgres.resource-links.cloudsql-pricing }}) is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

         Before fully committing yourself to using Google CloudSQL PostgreSQL as your data warehouse, we recommend familiarizing yourself with Google's pricing model and [using their pricing calculator to estimate your potential costs]({{ site.data.destinations.postgres.resource-links.price-calculator }}).

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