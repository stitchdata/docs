---
title: "Klaviyo (v1) improvement: Error logging improvements"
content-type: "changelog-entry"
date: 2021-04-09
entry-type: improvement
entry-category: integration
connection-id: klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/24"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Errors that stop Extraction will now display in the Extraction Logs. Previously, these errors wouldn't be included, resulting in confusion about the cause of the error.