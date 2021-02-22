---
title: "Google AdWords integration: New version (v1)"
content-type: "changelog-entry"
date: 2017-12-04
entry-type: new-feature
entry-category: integration
connection-id: google-ads 
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our Google AdWords integration is now available!

A few highlights include:

- Utilizing the AdWords API to replicate the most popular Google AdWords reports to Stitch
- Configurable fields in each of your selected Google AdWords reports 
- Connect multiple individual or MCC AdWords accounts in each Stitch integration
- Using a 30-day conversion/lookback window to update data over the past 30 days
- Loading report data using [Append-Only loading]({{ site.data.urls.destinations.storage.loading-behavior | prepend: site.baseurl }}) with an `_sdc_report_date` field so that users know when data was retrieved from the AdWords API

Learn more about the new version [in our documentation]({{ this-connection.url | prepend: site.baseurl }}).