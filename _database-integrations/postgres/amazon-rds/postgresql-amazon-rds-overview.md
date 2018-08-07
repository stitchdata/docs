---
title: Amazon PostgreSQL RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-postgresql
summary: "Connect and replicate data from your Amazon RDS database using Stitch's RDS integration."
layout: general
input: false

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "postgresql-rds"
display_name: "PostgreSQL RDS"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include integrations/templates/versioning/integration-version-tiles.html %}

  - title: "Version history"
    anchor: "version-history"
    content: |
      {% include integrations/templates/versioning/integration-history-and-changelog.html %}
  - title: "Version features"
    anchor: "version-features"
    content: |
      {% capture logical-replication-limitations %}
      On August 6, 2018, we discovered some limitations with {{ integration.display_name }} Log-based Replication. Currently, Log-based Replication requires:

      - **PostgreSQL databases running PostgreSQL versions 9.4.x-9.9.x.** If your database is running PostgreSQL 10 or greater, Log-based Replication will not work. Some of the functions Stitch uses to replicate data were renamed in PostgreSQL 10.

         We are working on adding support for logical replication - which is what Stitch uses to perform Log-based Replication - to the integration. In the meantime, use Key-based Incremental Replication.

      - **A connection to the master instance.** Log-based Replication will not work on read replicas. When PostgreSQL initially released logical replication, support for replicating from read replicas wasn't implemented.

         [Based on their forums](https://commitfest.postgresql.org/12/788/){:target="new"}, PostgreSQL is working on adding this feature to a future version. Until this feature is released, you can connect Stitch to the master instance and use Log-based Replication, **or** connect to a read replica and use Key-based Incremental Replication.
      {% endcapture %}

      {% include important.html first-line="**Log-based Replication requirements**" content=logical-replication-limitations %}

      In this section:

      - [Supported features](#supported-features)
      - [Supported data types](#supported-data-types)
    subsections:
      - content: |
          {% include integrations/templates/versioning/integration-supported-features.html feature-type="databases" %}
      - content: |
          {% include replication/templates/data-types/integration-specific-data-types.html %}

---
{% include misc/data-files.html %}