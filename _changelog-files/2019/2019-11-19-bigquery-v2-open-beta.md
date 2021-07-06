---
title: "Google BigQuery destination in open beta"
content-type: "changelog-entry"
date: 2019-11-19
entry-type: "beta"
entry-category: destination
connection-id: "bigquery"
connection-version: 2
---

{{ site.data.changelog.metadata.single-destination | flatify }}

We've built a new {{ this-connection.display_name }} destination from the ground up to address feedback from our customers and take advantage of new features on the platform, including the ability to upsert data.

Some notable improvements include:

- The ability to choose between append only and upsert [loading behavior]({{ site.data.urls.destinations.storage.loading-behavior | prepend: site.baseurl | prepend: site.home }})

- Authentication using your own Google Service Account

- [Support for all existing Google regions]({{ site.data.urls.destinations.overviews.bigquery-v2 | prepend: site.baseurl | prepend: site.home | append: "#supported-gcs-regions" }})

It's available now - [check it out]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }})!