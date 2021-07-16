---
title: "Chargebee (v1) update: restrictive properties removed"
content-type: "changelog-entry"
date: 2021-06-30
entry-type: updated-feature
entry-category: "integration"
connection-id: "chargebee"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-chargebee/pull/45"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've removed all `minimum/maximum` and `minLength/maxLength` restrictive properties from all {{ this-connection.display_name }} tables so that the integration can continue to sync with the evolving {{ this-connection.display_name }} API.