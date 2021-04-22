---
title: "Zuora"
content-type: "changelog-entry"
date: 2021-03-31
entry-type: new-feature
entry-category: integration
connection-id: zuora
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zuora/pull/54"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

When we encounter a truncated {{ this-connection.display_name }} CSV file, the integration will get a new stateful query session.

For more context behind this new feature, be sure to click the `TAP-ZUORA #54` button to the left of the header of this changelog entry.