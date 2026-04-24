---
title: "Mambu (v2) bug fix: Corrected handling for lists of custom fields"
content-type: "changelog-entry"
date: 2021-06-03
entry-type: bug-fix
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/47"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration to correctly handle lists of custom fields. Previously, the integration would drop lists (arrays) of custom fields. Lists of custom fields will now be correctly saved and replicated.