---
title: "Salesforce (v1) update: Increased request timeout"
content-type: "changelog-entry"
date: 2021-10-28
entry-type: improvement
entry-category: integration
connection-id: "salesforce"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-salesforce/pull/126"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to increase the request timeout from 30 seconds to five minutes.

With this change, the integration can support objects that take longer than 30 seconds to return.