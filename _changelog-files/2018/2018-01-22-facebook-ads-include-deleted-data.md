---
title: "Facebook Ads (v1) integrations: Include deleted ads, adsets, and campaigns"
content-type: "changelog-entry"
date: 2018-01-22
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/34"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new setting for {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations that enables you to replicate records for deleted ads, adsets, and campaigns:

![]({{ site.baseurl }}/images/changelog/facebook-ads-include-deleted-data.png)

When checked, Stitch will query for and extract data for deleted ads, adsets, and campaigns from your {{ this-connection.display_name }} account. Relevant records will be included in the `ads`, `adcreatives`, `adsets`, and `campaigns` tables, if selected for replication.

Learn more in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl }}). 