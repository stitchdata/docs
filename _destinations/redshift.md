---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Amazon Redshift Destination
permalink: /destinations/redshift/
layout: destination-overview
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, redshift etl, etl to redshift
summary: &summary "Amazon Redshift is a fully managed, cloud-based data warehouse. As Redshift is built for online analytic processing and business intelligence applications, it excels at executing large-scale analytical queries. For this reason, it exhibits far better performance than traditional, row-based relational databases like MySQL and PostgreSQL."
toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "Redshift"
type: "redshift"
db-type: "Analytic"
pricing_tier: "standard" ## for Stitch
status: "Released"
description: *summary
port: 5439
pricing_model: "Hourly" ## provider model
free_option: "Yes (plan & trial)"
fully-managed: false
pricing_notes: "Currently, Redshift bases their pricing on an hourly rate that varies depending on the type and number of nodes in a cluster. The type and number of nodes you choose when creating a cluster is dependent on your needs and data set, but you can scale up or down over time should your requirements change. "
icon: /images/destinations/icons/amazon-redshift.svg


# -------------------------- #
#           Support          #
# -------------------------- #

ssl: true
ssh: false

incremental-replication: "Upserts, Append-Only"
connection-methods: "SSH, SSL"
supported-versions: "n/a"

nested-structure-support: false
case: "Case Insensitive"
table-name-limit: "127" ## # of characters
column-name-limit: "115" ## # of characters
column-limit: "1,600"
timezones:
  supported: false
  storage: "Converted to UTC & <br>`TIMESTAMP WITHOUT TIME ZONE`"
timestamp-range: "4713 BC to 294276 AD"
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
main-site: http://aws.amazon.com/
pricing: https://aws.amazon.com/redshift/pricing/
status-url: https://status.aws.amazon.com/
documentation: https://aws.amazon.com/documentation/redshift/
redshift-vs-postgres: http://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html



# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description | flatify | markdownify }}

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Currently, {{ destination.display_name}} bases their pricing on an hourly rate that varies depending on the type and number of nodes in a cluster. Check out their [Pricing page](https://aws.amazon.com/redshift/pricing/) for an in-depth look at their current plan offerings.

      **So, what's a node?** A node is a single computer that participates in a cluster. Your Redshift cluster can have one to many nodes; the more nodes, the more data it can store and the faster it can process queries. Amazon currently offers four different types of nodes, each of which has its own CPU, RAM, storage capacity, and storage drive type.

      The type and number of node(s) you choose when creating your cluster is dependent on your needs and dataset. **We do, however, recommend you set up a multi-node configuration to provide data redundancy.** 

      For some guidance on choosing the right number of nodes for your cluster, check out Amazon's [Determining the Number of Nodes guide](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes).

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
      {% for category in reference-defaults[item] %}
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
