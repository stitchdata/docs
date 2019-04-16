---
title: Stitch Database Integrations
keywords: database integration, etl database, database etl
layout: general
permalink: /integrations/databases/
summary: "With Stitch, you can consolidate data from a variety of databases into a single data warehouse. Learn more about setting up a database integration and how Stitch will replicate data from that specific database type."

toc: false
input: false
feedback: false

sections:
  - content: |
      With Stitch, you can consolidate data from a variety of databases into [a single destination]({{ site.baseurl }}/destinations).

  - title: "Database connection methods"
    anchor: "database-connection-methods"
    content: |
      The security and privacy of your data is of the utmost importance to us. For more info about Stitch's supported encryption options, refer to the [Data Encryption guide]({{ link.security.encryption | prepend: site.baseurl }}).

      For more info on our security policies and recommended best practices, check out the [Security FAQ]({{ link.security.faq | prepend: site.baseurl }}).

  - title: "All database integrations"
    anchor: "all-database-integrations"
    content: |
      Ready to connect your database to Stitch? For setup instructions and details on the queries Stitch runs to replicate data, check out the guides below.

      If you don't see what you're looking for in the list below, check out the Singer project. A simple, composable, open-source ETL standard, Singer allows you to extract data from any source. Check out the [Roadmap]({{ site.singer-roadmap }}){:target} or [GitHub repo]({{ site.singer-github }}){:target="new"} to see what's currently being worked on.

      {% include integrations/templates/integration-category-tiles.html type="where-is-integration" %}
    subsections:
      - content: |
          {% include integrations/templates/integration-category-tiles.html type="databases" %}

  - title: "Suggest an integration"
    anchor: "suggest-an-integration"
    content: |
      Don’t see your integration of choice listed here? We’d love to hear from you! [Reach out to us](mailto:{{ site.support }}) with your suggestion.
---
{% include misc/data-files.html %}