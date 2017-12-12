---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Panoply.io Destination
permalink: /destinations/panoply/
layout: destination-overview
tags: [panoply_destination]
keywords: panoply, panoply.io, panoply data warehouse, panoply etl, etl to panoply
summary: "Panoply is a fully managed data warehouse service that will spin up a Redshift instance in just a few clicks. With Panoply, you can use your favorite analysis, SQL, and visualization tools just like you would if you were creating a Redshift data warehouse on your own."
toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "Panoply"
type: "panoply"
db-type: "Analytic"
pricing_tier: "standard" ## for Stitch
status: "Released"
description: "Panoply is a fully managed data warehouse service that will spin up a Redshift instance in just a few clicks. With Panoply, you can use your favorite analysis, SQL, and visualization tools just like you would if you were creating a Redshift data warehouse on your own."
port: 5439
pricing_model: "Storage" ## provider model
free_option: "Yes (trial)"
fully-managed: true
pricing_notes: "Panoply charges based on the amount of data stored and offers several plan options for your needs. [Refer to their pricing page for more information](https://panoply.io/pricing/)."
icon: /images/destinations/icons/panoply.svg


# -------------------------- #
#           Support          #
# -------------------------- #
replication-methods: "All"
connection-methods: "SSL"
supported-versions: "n/a"

nested-structure-support: false
case: "Case Insensitive"
table-name-limit: "127" ## # of characters
column-name-limit: "115" ## # of characters
column-limit: "1,600"
timestamp-range: "4713 BC to 294276 AD"
timestamp-data: "Converted to UTC & <br>`TIMESTAMP WITHOUT TIME ZONE`"
varchar-limit: "65K"
integer-limit: "-9223372036854775808 to 9223372036854775807" # http://docs.aws.amazon.com/redshift/latest/dg/r_Numeric_types201.html#r_Numeric_types201-integer-types
decimal-limit: "38 numbers, or places"
decimal-range: "6 numbers after the decimal"
reserved-words: "http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html"


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 1
## MongoDB
## Sometimes Incompatible
## Deeply nested data in tables may exceed the 1,600 column limit.


# -------------------------- #
#            Links           #
# -------------------------- #
main-site: http://www.panoply.io/
contact: http://panoply.io/contact/
pricing: https://panoply.io/pricing/
documentation: http://panoply.io/documentation/
status-url: "https://twitter.com/panoplyio?lang=en"
---
{% assign destination = page %}
{% include misc/data-files.html %}


{% contentfor intro %}
{{ destination.description }}

If you're looking for a cost-effective, no-effort way to test out Stitch or get started consolidating your data, {{ destination.display_name }} is your best bet.
{% endcontentfor %}



{% contentfor pricing %}
In just a few minutes, you can create a {{ destination.display_name }} account and spin up your own Redshift data warehouse. 

Pricing varies from plan to plan, but every {{ destination.display_name }} plan includes:

- Unlimited queries
- Unlimited user accounts
- Automatic maintenance, vacuuming, and backups

To learn more about each of {{ destination.display_name }}'s plans, [check out their pricing page]({{ destination.pricing }}).
{% endcontentfor %}



{% contentfor limitations %}
{% include destinations/overview-limitations.html %}
{% endcontentfor %}



{% contentfor setup %}
With just a few clicks, you can [connect a new]({{ link.destinations.setup.panoply-new | prepend: site.baseurl }}) or [an existing {{ destination.display_name }} data warehouse to Stitch]({{ link.destinations.setup.panoply-ex | prepend: site.baseurl }}).
{% endcontentfor %}



{% contentfor data-modeling %}
{% include destinations/overview-integration-schemas.html %}
{% endcontentfor %}



{% contentfor replication %}
{% include destinations/overview-replication-process.html %}
{% endcontentfor %}