---
title: "LinkedIn Ads (v1) update: Access token configurations"
content-type: "changelog-entry"
date: 2022-06-23
entry-type: updated-feature
entry-category: integration
connection-id: linkedin-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/43"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

You can now provide an access token for existing connections and generate new access tokens for new connections using refresh tokens in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.