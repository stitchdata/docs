---
title: "Zendesk (v15-10-2015) integrations: New group membership table"
content-type: "changelog-entry"
date: 2016-09-07
entry-type: updated-feature
entry-category: integration
connection-id: zendesk
connection-version: "15-10-2015"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The {{ this-connection.display_name }} integration now includes a `zendesk_group_memberships` table, which contains information about the groups your {{ this-connection.display_name }} agents are members of. Fields in this table include:

- Group membership ID (`id`)
- URL
- Name
- Deletion flag
- `created_at`
- `updated_at`