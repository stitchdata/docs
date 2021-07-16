---
title: "Facebook Ads (v1) update: Fixed composite primary key for the `ads_insights_country` table"
content-type: "changelog-entry"
date: 2021-06-28
entry-type: bug-fix
entry-category: "integration"
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/154"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed the `ads_insights_country` composite primary key. The `country` field had previously been erroneously excluded.

The composite primary key is now: `campaign_id", "adset_id", "ad_id", "date_start", "country"`.

This is a breaking change and communiation from Stitch support has been emailed to affected users.

If you are not already including the `country` field in downstream processes that identify uniqueness of records in the files loaded to S3 for this table, this field will need to be added into those processes.

You may also wish to reset this table to have historical data re-replicated and more accurately portrayed in S3, in which case you should:

  1. Contact our support team to implement a courtesy row-usage exemption for your Facebook Ads integration.
  2. Within Stitch, navigate to the ads_insights_country table's Table Settings page.
  3. Use the Reset Table button to queue this table's reset.

If you have any questions about the change or this process, please reach out to Stitch support via in-app chat.