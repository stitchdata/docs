---
title: "Outreach (v1) update: New tables and foreign key documentation"
content-type: "changelog-entry"
date: 2021-06-10
entry-type: updated-feature
entry-category: "integration, documentation"
connection-id: "outreach"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-outreach/pull/12"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added some new tables to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:

- `sequence_states`
- `sequence_steps`
- `sequence_templates`
- `sequences`

We've also updated the {{ this-connection.display_name }} table documentation to include info about foreign keys and how tables related to each other. Check it out [here]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).