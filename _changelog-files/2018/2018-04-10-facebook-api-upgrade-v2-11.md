---
title: "Facebook Ads (v1) integrations: API upgrade to v2.11"
content-type: "changelog-entry"
date: 2018-04-10
entry-type: updated-feature
entry-category: integration
connection-id: facebook-ads
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} integration to use the newest version of the Facebook Marketing API - version 2.11.

In addition, we've made the following improvements:

- Configurable attribution window when creating or editing a {{ this-connection.display_name }} integration. Choose between `1`, `7` or `28` days so that Stitch replicates historical data in alignment with the attribution window of your {{ this-connection.display_name }} account.

- A new table named `ads_insights_region`. View your data by the region (such as state or province) where people live or were located when they saw your ads, depending on how you set your location targeting. 

- Removed the `video_15_sec_watched_actions` attribute from relevant tables. Facebook deprecated this attribute in the 2.11 version of their API.