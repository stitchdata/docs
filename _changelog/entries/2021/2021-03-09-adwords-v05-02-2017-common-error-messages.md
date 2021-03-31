---
title: "Google Ads (v1) improvement: New custom messages for common errors"
content-type: "changelog-entry"
date: 2021-03-09
entry-type: improvement
entry-category: "integration"
connection-id: "google-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-adwords/pull/77"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration to return actionable messages when Stitch encounters errors during Extraction. These messages now include the cause of the error, ensuring you can take action to resolve it.
