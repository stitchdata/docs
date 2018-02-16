---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Amazon Redshift Destination
permalink: /destinations/redshift/
layout: destination-overview
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, redshift etl, etl to redshift
summary: "Amazon Redshift is fully managed, cloud-based data warehouse. As Redshift is built for online analytic processing and business intelligence applications, it excels at executing large-scale analytical queries. For this reason, it exhibits far better performance than traditional, row-based relational databases like MySQL and PostgreSQL."
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
description: "Amazon Redshift is fully managed, cloud-based data warehouse. As Redshift is built for online analytic processing and business intelligence applications, it excels at executing large-scale analytical queries. For this reason, it exhibits far better performance than traditional, row-based relational databases like MySQL and PostgreSQL."
port: 5439
pricing_model: "Hourly" ## provider model
free_option: "Yes (plan & trial)"
fully-managed: false
pricing_notes: "Currently, Redshift bases their pricing on an hourly rate that varies depending on the type and number of nodes in a cluster. The type and number of nodes you choose when creating a cluster is dependent on your needs and data set, but you can scale up or down over time should your requirements change. "
icon: /images/destinations/icons/amazon-redshift.svg


# -------------------------- #
#           Support          #
# -------------------------- #
replication-methods: "All"
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
---
{% assign destination = page %}
{% include misc/data-files.html %}


{% contentfor intro %}
{{ destination.description }}

To learn more about transactional and analytic databases and how they compare, check out our [Data Strategy Guide](https://stitchdata.com/resources/guide/why-you-need-a-data-pipeline).

{{ destination.display_name}} is based on PostgreSQL 8.0.2 and while there are many similarities, Redshift differs in some key ways. **Before you spin up a cluster**, we recommend [checking out our destination comparison guide]({{ link.destinations.overviews.compatibility }}) to ensure you pick the best data warehouse for your needs.
{% endcontentfor %}


{% contentfor pricing %}
Currently, {{ destination.display_name}} bases their pricing on an hourly rate that varies depending on the type and number of nodes in a cluster. Check out their [Pricing page](https://aws.amazon.com/redshift/pricing/) for an in-depth look at their current plan offerings.

**So, what's a node?** A node is a single computer that participates in a cluster. Your Redshift cluster can have one to many nodes; the more nodes, the more data it can store and the faster it can process queries. Amazon currently offers four different types of nodes, each of which has its own CPU, RAM, storage capacity, and storage drive type.

The type and number of node(s) you choose when creating your cluster is dependent on your needs and dataset. **We do, however, recommend you set up a multi-node configuration to provide data redundancy.** 

For some guidance on choosing the right number of nodes for your cluster, check out Amazon's [Determining the Number of Nodes guide](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes).
{% endcontentfor %}



{% contentfor setup %}
Creating a {{ destination.display_name}} data warehouse for Stitch involves spinning up a cluster in Amazon Web Services and creating a database in the cluster.

- **[Create a new AWS account & Redshift cluster]({{ link.destinations.setup.redshift | prepend: site.baseurl }})**. If you're brand new to AWS, you can [sign up here](http://aws.amazon.com/) to create an AWS account and then use [this tutorial]() to connect your Redshift database.
- **[Connect a Redshift database via an SSH tunnel]({{ link.destinations.setup.redshift-ssh | prepend: site.baseurl }})**. If you want to use an SSH tunnel to connect Redshift to Stitch, there are some additional steps you'll need to complete to set up the connection.
- **Connect an existing Redshift instance**. If you already have an AWS account and a {{ destination.display_name}} cluster, you won't need to complete the initial cluster provisioning steps. You will, however, still need to:

   1. Create a database in the cluster for Stitch
   2. [Configure the firewall to grant access to Stitch]({{ link.destinations.setup.redshift | prepend: site.baseurl | append:"#configure-security-access-settings" }})
   3. [Create a database user for Stitch]({{ link.destinations.setup.redshift | prepend: site.baseurl | append:"#create-stitch-redshift-user" }})
   4. [Enter the connection info into Stitch]({{ link.destinations.setup.redshift | prepend: site.baseurl | append:"#step-6-connect-stitch" }})

### SSL Connections {#redshift-ssl-connections}

By default, Stitch will attempt to any Redshift destination using SSL. This doesn't require any configuration on your part.

{% endcontentfor %}



{% contentfor limitations %}
{% include destinations/overview-limitations.html %}
{% endcontentfor %}



{% contentfor replication %}
{% include destinations/overview-replication-process.html %}
{% endcontentfor %}



{% contentfor data-modeling %}
{% include destinations/overview-integration-schemas.html %}
{% endcontentfor %}

---

## Encodings, SORT, & DIST Keys

Want to improve your query performance? You can apply encodings, SORT, and DIST keys to Stitch-created tables in your Redshift data warehouse. Even when new data is replicated, your settings will remain intact.

[**Learn more about applying encodings & keys**]({{ site.baseurl }}/destinations/redshift/apply-encodings-sort-dist-keys-redshift)
