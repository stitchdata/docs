---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Amazon Redshift Destination
permalink: /destinations/redshift/
keywords: redshift, amazon redshift, redshift data warehouse, redshift etl, etl to redshift
summary: "Amazon Redshift is a fully managed, cloud-based data warehouse. As Redshift is built for online analytic processing and business intelligence applications, it excels at executing large-scale analytical queries. For this reason, it exhibits far better performance than traditional, row-based relational databases like MySQL and PostgreSQL."

content-type: "destination-overview"

toc: true
layout: general
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Redshift"
type: "redshift"
port: 5439


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/redshift.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in _data/destinations/links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ destination.summary | flatify | markdownify }}

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Currently, {{ destination.display_name}} pricing is based on an hourly rate that varies depending on the type and number of nodes in a cluster. Check out Amazon's [pricing page]({{ site.data.destinations.resource-links[destination.type]pricing }}){:target="new"} for an in-depth look at their current plan offerings.

      **So, what's a node?** A node is a single computer that participates in a cluster. Your {{ destination.display_name }} cluster can have one to many nodes; the more nodes, the more data it can store and the faster it can process queries. Amazon currently offers four different types of nodes, each of which has its own CPU, RAM, storage capacity, and storage drive type.

      The type and number of node(s) you choose when creating your cluster is dependent on your needs and dataset. We do, however, recommend you set up a multi-node configuration to provide data redundancy.

      For some guidance on choosing the right number of nodes for your cluster, check out Amazon's [Determining the Number of Nodes guide](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes){:target="new"}.

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