---
title: "Mambu (v2) update: Continued refactoring, new fields added"
content-type: "changelog-entry"
date: 2022-03-04
entry-type: updated-feature
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/70"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made many updates to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. See the list below for changes:

- Refactored `centres`, `clients` and `branches` streams
- Added `assignedBranchKey` field to `clients` stream