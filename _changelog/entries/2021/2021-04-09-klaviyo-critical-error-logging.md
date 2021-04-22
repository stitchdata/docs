---
title: "Klaviyo (v1) improvement: Error logging improvement"
content-type: "changelog-entry"
date: 2021-04-09
entry-type: improvement
entry-category: integration
connection-id: klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/24"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Error messages to be prioritized for exception handling will now be logged as `CRITICAL`.