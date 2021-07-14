---
title: "Klaviyo (v1) update: New campaigns table!"
content-type: "changelog-entry"
date: 2021-05-28
entry-type: updated-feature
entry-category: integration
connection-id: klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/40"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new `campaigns` table has been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration! This table contains info about the campaigns in your {{ this-connection.display_name }} account.

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.baseurl | append: "#campaigns" }}).