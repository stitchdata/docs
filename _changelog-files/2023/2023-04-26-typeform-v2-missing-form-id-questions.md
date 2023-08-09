---
title: "Typeform (v2) update: Handle missing form ID and form questions"
content-type: "changelog-entry"
date: 2023-04-26
entry-type: improvement
entry-category: integration
connection-id: typeform
connection-version: 2
pull-request: "https://github.com/singer-io/tap-typeform/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to:
- Sync data for all forms if no form ID is provided.
- Continue syncing data instead of failing when a form doesn't contain any questions.