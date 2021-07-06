---
title: "Facebook Ads (v1) integrations: AdLabel data is now available!"
content-type: "changelog-entry"
date: 2017-10-27
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/27"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `adlabels` fields to the `adsets` and `campaigns` tables for our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl }}).