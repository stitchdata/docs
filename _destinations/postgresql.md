---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: PostgreSQL Destination
permalink: /destinations/postgresql/
layout: destination-overview
tags: [postgresql_destination]
keywords: postgres, postgresql, postgres data warehouse, postgres etl, etl to postgres, postgresql data warehouse, etl to postgresql
summary: "An open-source relational database, PostgreSQL is a powerful and well-known system that has received recognition from both its users and the industry at large. Unlike some other database systems, PostgreSQL is completely customizable and yours to do with as you please (assuming, of course, that your instance is self-hosted)."
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
replication-methods: "All"
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
  - title: "pricing"
    content: |
      Pricing for {{ destination.display_name }} depends entirely on where your instance is hosted.

      - **Self-hosted:** {{ destination.display_name }} is open-source, meaning you don't need to pay an upfront cost to obtain the necessary software. You may, however, have hosting and maintenance costs associated with the server housing the instance. You may have to do a little bit of internal number crunching to figure out these potential costs. 
      - **Heroku:** Heroku has a [variety of plans to choose from](https://www.heroku.com/pricing), and [a guide to help you select the right plan](https://devcenter.heroku.com/articles/heroku-postgres-plans) for you or your company.
      - **Amazon RDS:** Amazon offers [a variety of plans](https://aws.amazon.com/rds/postgresql/pricing/) for both on-demand instances and Multi-AZ Deployment. To get an estimate of what your monthly bill might look like, check out their [monthly calculator]({{ destination.aws-calculator }}).
      - **Google CloudSQL PostgreSQL:** Unlike many other cloud-based data warehouse solutions, [Google's pricing model]({{ destination.cloudsql-pricing }}) is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

         Before fully committing yourself to using Google CloudSQL PostgreSQL as your data warehouse, we recommend familiarizing yourself with Google's pricing model and [using their pricing calculator to estimate your potential costs]({{ destination.price-calculator }}).

  - title: "setup"
    content: |
      When it comes to setting up, hosting, and connecting a {{ destination.display_name }} data warehouse to Stitch, you have a few options:

      - [Connect a self-hosted {{ destination.display_name }} database]({{ link.destinations.setup.self-hosted-postgres | prepend: site.baseurl }}). If you currently use {{ destination.display_name }}, you can create a database for Stitch within the instance and connect it.
      - [Connect a Heroku-{{ destination.display_name }} database]({{ link.destinations.setup.heroku-postgres | prepend: site.baseurl }}). Heroku offers a managed {{ destination.display_name }}-based database service, which is easy to set up and connect to Stitch. No technical expertise is required to create the database or connect it to Stitch.
      - [Connect an Amazon {{ destination.display_name }}-RDS database]({{ link.destinations.setup.postgres-rds | prepend: site.baseurl }}). Amazon Web Services' RDS service allows you to create and connect a {{ destination.display_name }} database to Stitch.
      - [Connect a Google CloudSQL PostgreSQL database]({{ link.destinations.setup.cloudsql-postgres | prepend: site.baseurl }}). Google's fully-managed CloudSQL database service takes only minutes to set up and provision. While no technical expertise is required to set up a simple instance, additional configuration options - such as assigning specific database permissions - is available for more advanced users.

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