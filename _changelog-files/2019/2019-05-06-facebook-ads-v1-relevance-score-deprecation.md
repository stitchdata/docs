---
title: "Facebook Ads (v1) integrations: Workaround relevance_score deprecation"
content-type: "changelog-entry"
date: 2019-05-06
entry-type: improvement
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/55"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Due to [Facebook prematurely deprecating `relevance_score` in their API](https://developers.facebook.com/support/bugs/2489592517771422){:target="new"}, we've added logging to notify you should this field cause an error during replication:

```shell
Due to a bug with Facebook prematurely deprecating 'relevance_score' that is not affecting all tap-facebook users in the same way, you need to deselect `relevance_score` from your Insights export. For further information, please see this Facebook bug report thread: https://developers.facebook.com/support/bugs/2489592517771422
```

Should you encounter this error in Stitch, de-select the `relevance_score` field from any `ads_insights_*` tables you have set to replicate.