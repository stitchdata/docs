---
title: "New integration: Bing Ads"
content-type: "changelog-entry"
date: 2018-05-07
entry-type: new-feature
entry-category: integration
connection-id: bing-ads
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new Bing Ads integration is now available!

Stitch's Bing Ads integration lets you replicate data from Microsoft's search advertising platform to the Stitch destination of your choice.

A few highlights from the integration include:

- Replication from eight of the most popular Bing Ads reports
- Configurable fields in each of your selected reports
- Connection to multiple ads accounts in each Stitch integration
- [Append-Only loading behavior]({{ site.data.urls.destinations.storage.loading-behavior | prepend: site.baseurl | prepend: site.home }}, enabling you to see report changes over time
- A new `_sdc_report_date` field, allowing you to see when data was retrieved from Bing Ads 

Get started by creating a new Bing Ads integration or learning more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).