---
title: "PostgreSQL (v15-10-2015) integrations: ARRAY and JSONB data type support"
content-type: "changelog-entry"
date: 2016-08-05
entry-type: new-feature
entry-category: integration
connection-id: postgres
connection-version: "15-10-2015"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

All {{ this-connection.display_name }} fields of type `JSONB` and `ARRAY` may now be tracked from the **Integrations** page. These fields will be converted to strings in Amazon Redshift.