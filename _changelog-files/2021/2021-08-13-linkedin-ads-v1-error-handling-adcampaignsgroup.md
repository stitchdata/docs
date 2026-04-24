---
title: "LinkedIn Ads (v1) update: Improved handling of 4xx errors"
content-type: "changelog-entry"
date: 2021-08-13
entry-type: improvement
entry-category: integration
connection-id: linkedin-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/28"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles 4xx errors for the `adCampaignGroup` stream by returning custom messages and handling JSON decoding errors.