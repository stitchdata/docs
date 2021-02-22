---
title: Google Cloud SQL PostgreSQL Support
content-type: "changelog-entry"
date: 2017-03-22
entry-type: new-feature
entry-category: connection
connections:
  - id: "postgres"
    type: "integration"
    version: ""

  - id: "postgres"
    type: "destination"
    version: "1"
---
todo: fix logic in here to account for integrations and destinations

We’re excited to report that Stitch supports the recently announced PostgreSQL flavor of the the Google CloudSQL service. It’s available as both an input [integration]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}) AND a [destination]({{ site.data.urls.destinations.postgres | prepend: site.baseurl | prepend: site.home }}) - a dual threat!