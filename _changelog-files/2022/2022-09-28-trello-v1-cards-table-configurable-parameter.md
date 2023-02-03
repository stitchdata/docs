---
title: "Trello (v1) update: Added configurable parameter to cards table"
content-type: "changelog-entry"
date: 2022-09-28
entry-type: updated-feature
entry-category: integration
connection-id: trello
connection-version: 1
pull-request: "https://github.com/singer-io/tap-trello/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the configurable parameter `cards_respoonse_file` to the `cards` table of our {{ this-connection.display_name }} integration. The default value is `1000`.