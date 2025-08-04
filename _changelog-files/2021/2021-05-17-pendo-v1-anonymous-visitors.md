---
title: "Pendo (v1) update: New setting for including anonymous visitor data"
content-type: "changelog-entry"
date: 2021-05-17
entry-type: improvement
entry-category: integration
connection-id: "pendo"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-pendo/pull/32"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new setting to our {{ this-connection.display_name }} integration: **Include Anonymous Visitors**

When checked, Stitch will replicate data attributed to anonymous visitors.

Learn more in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}). 