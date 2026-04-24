---
title: "Klaviyo (v1) update: New campaigns table and field selection support!"
content-type: "changelog-entry"
date: 2021-05-28
entry-type: improvement
entry-category: integration
connection-id: klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/40"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made some updates to our {{ this-connection.display_name }} integration:

- **Field selection is now supported!** Select only the fields you want to replicate in the **Tables to Replicate** tab.
- **New `campaigns` table**. This table contains info about the campaigns in your {{ this-connection.display_name }} account.

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.baseurl }}).