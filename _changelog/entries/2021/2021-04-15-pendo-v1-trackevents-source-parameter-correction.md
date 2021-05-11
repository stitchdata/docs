---
title: "Pendo (v1) bug fix: Corrected  `trackEvents` source parameter"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: bug-fix
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This bug fix resolves the 400 error for the {{ this-connection.display_name }} integration:
  `bad pipeline: bad source: bad parameters for source type trackEvents: unexpected parameters`.

We corrected the source parameter for the `trackEvents` source from `trackId` to `trackTypeId`.