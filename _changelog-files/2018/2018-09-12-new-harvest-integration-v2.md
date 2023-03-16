---
title: "Harvest integration: New version (v2)"
content-type: "changelog-entry"
date: 2018-09-12
entry-type: new-feature
entry-category: integration
connection-id: harvest 
connection-version: 2
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available!

Changes in this version include:

- Upgrading to V2 of the {{ this-connection.display_name }} API
- [Many new tables](https://www.stitchdata.com/docs/integrations/saas/harvest#schema)
- Schema modifications to align with the {{ this-connection.display_name }} API
- The `people` table was renamed to `users`, as per new {{ this-connection.display_name }} API endpoints

Full details can be found on the pull request against the open sourced integration [here](https://github.com/singer-io/tap-harvest/pull/20). Stitch docs for the version 2 of the {{ this-connection.display_name }} integration can be found [here]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).