---
title: "Hubspot (v2) bug fix: Retrieval of contacts to company"
content-type: "changelog-entry"
date: 2024-01-23
entry-type: bug-fix
entry-category: integration
connection-id: hubspot
connection-version: 2
pull-request: "https://github.com/singer-io/tap-hubspot/pull/250"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue when retrieving `contacts_by_company` per `company_id` with a large number of company IDs. 