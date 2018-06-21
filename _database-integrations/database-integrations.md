---
title: Stitch Database Integrations
keywords: database integration, etl database, database etl
layout: integration-category
permalink: /integrations/databases/
summary: "With Stitch, you can consolidate data from a variety of databases into a single data warehouse. Learn more about setting up a database integration and how Stitch will replicate data from that specific database type."

toc: false
input: false
integration-type: "database"
feedback: false
---
{% include misc/data-files.html %}
{% assign database-integrations = site.database-integrations | where:"input",true | sort:"title" %}


{% contentfor intro %}
With Stitch, you can consolidate data from a variety of databases into [a single data warehouse]({{ site.baseurl }}/destinations).
{% endcontentfor %}


{% contentfor more-info %}
## Connecting databases to Stitch

To connect a database integration to Stitch, you'll need to create a database user for us and grant the appropriate permissions. Note that we will only ever read your data.

The security and privacy of your data is of the utmost importance to us. To ensure your data stays private, we recommend using an SSH or SSL connection to connect your database encrypt your data in transit.

For more info on our security policies and recommended best practices, check out the [Security FAQ]({{ link.account.security-faq | prepend: site.baseurl }}).

### SSH & SSL connection support

The majority of our database integrations support connecting via an SSH Tunnel.

Stitch supports SSL connections for these database integrations:

{% for integration in database-integrations %}
{% if integration.ssl == true %}
- [{{ integration.title }}]({{ integration.url | prepend: site.baseurl }})
{% endif %}
{% endfor %}

### VPN connection support

At this time, Stitch does not support VPN connections for any of our database integrations.
{% endcontentfor %}