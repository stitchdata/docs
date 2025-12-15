---
title: "HubSpot (v4): Retry the API requests for all the errors"
content-type: "changelog-entry"
date: 2025-12-09
entry-type: NOT FOUND
entry-category: integration
connection-id: hubspot
connection-version: 4
pull-request: "https://github.com/singer-io/tap-hubspot/pull/282"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to retry the API requests for all the errors.