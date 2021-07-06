---
title: "Facebook Ads (v15-10-2015) integration: API upgrade to v2.9"
content-type: "changelog-entry"
date: 2017-12-13
entry-type: improvement
entry-category: integration
connection-id: facebook-ads
connection-version: "15-10-2015"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration to use a new version of the Facebook API. This update also provides access to a new table (`facebook_ads_insights_platform_and_device`), which contains fields allowing you to compare insights between platforms such as Facebok, Instagram, and Messenger, and positions such as feeds, instant articles, and stories.