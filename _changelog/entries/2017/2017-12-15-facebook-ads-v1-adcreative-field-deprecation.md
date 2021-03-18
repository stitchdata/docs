---
title: "Facebook Ads (v1) integrations: use_page_actor_override field deprecation"
content-type: "changelog-entry"
date: 2017-12-15
entry-type: deprecation
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/32"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Due to issues with querying and a [bug in Facebook's API](https://developers.facebook.com/support/bugs/262625957597388/){:target="new"}, we're removing support for the `adcreative.use_page_actor_override` column. As a result, this column will no longer display in Stitch as available for replication.