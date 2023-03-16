---
title: "Facebook Ads (v1) integrations: Ads, AdSets, and Campaigns now replicate incrementally!"
content-type: "changelog-entry"
date: 2017-11-02
entry-type: improvement
entry-category: "integration"
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/29"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Big news: The following {{ this-connection.display_name }} integration tables, which previously replicated in full, now use [Key-based Incremental Replication]({{ site.data.urls.replication.key-based-incremental | prepend: site.baseurl }}):

- `ads`
- `adsets`
- `campaigns`

These tables use `updated_time` as Replication Keys, ensuring you're only replicating records that have been updated. You can learn more about these tables in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl }}). 