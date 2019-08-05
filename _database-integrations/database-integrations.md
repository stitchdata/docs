---
title: Stitch Database Integrations
keywords: database integration, etl database, database etl
layout: general
permalink: /integrations/databases/
summary: "With Stitch, you can consolidate data from a variety of databases into a single data warehouse. Learn more about setting up a database integration and how Stitch will replicate data from that specific database type."

toc: false
input: false
feedback: false

table-selection: true

display_name: "Any database"
row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: true
  lots-of-full-table: false

sections:
  - content: |
      With Stitch, you can consolidate data from a variety of databases into [a single destination]({{ site.baseurl }}/destinations).

  - title: "Database connection methods"
    anchor: "database-connection-methods"
    content: |
      The security and privacy of your data is of the utmost importance to us. To ensure your data stays private, we recommend using an SSH or SSL connection to connect your database and encrypt your data in transit.

      For more info on our security policies and recommended best practices, check out the [Security FAQ]({{ link.security.faq | prepend: site.baseurl }}).
    subsections:
      - title: "SSH and SSL connection support"
        anchor: "ssh-ssl-connection-support"
        content: |
          {% assign database-integrations = site.database-integrations | where:"input",true | sort:"title" %}

          The majority of our database integrations support connecting via an SSH Tunnel.

          Stitch supports SSL connections for these database integrations:

          {% for integration in database-integrations %}
          {% if integration.ssl == true %}
          - [{{ integration.title | remove: "(v1.0)" }}]({{ integration.url | prepend: site.baseurl }})
          {% endif %}
          {% endfor %}

      - title: "Advanced connectivity options"
        anchor: "advanced-connectivity-options"
        content: |
          Additional connection options can be included as part of an Enterprise plan. These options include reverse SSH tunnels, VPNs, and AWS Private Link. Reach out to [Stitch Sales]({{ site.sales }}){:target="new"} for more info.

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