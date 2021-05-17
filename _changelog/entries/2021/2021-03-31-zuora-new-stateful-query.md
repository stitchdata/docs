---
title: "Zuora (v1): AQuA API CSV handling improvement"
content-type: "changelog-entry"
date: 2021-03-31
entry-type: improvement
entry-category: integration
connection-id: zuora
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zuora/pull/54"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how {{ this-connection.display_name }} (v{{ this-connection.this-version }})integrations handle truncated CSVs received from the {{ this-connection.display_name }} API.

For more info about this new feature, check out the [pull request in the tap-zuora repository]({{ item.pull-request }}){:target="new"}.