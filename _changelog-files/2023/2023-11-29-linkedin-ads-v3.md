---
title: "LinkedIn Ads integration: New version (v3) now available!"
content-type: "changelog-entry"
date: 2023-11-29
entry-type: new-feature
entry-category: integration
connection-id: linkedin-ads
connection-version: 3
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/64"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available!

We've upgraded the {{ this-connection.display_name }} API from `202302` to `202309`. This upgrade bring some updates to the `video_ads` stream, including a new Primary Key and a new Replication Key.