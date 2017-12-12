---
title: PostgreSQL Data Types Stored as Strings
keywords: troubleshooting, integration, database integration, trouble, issue, help, postgres, postgresql, strings
permalink: /troubleshooting/postgres-data-types-stored-as-strings
tags: [data_discrepancy, database_integrations]

summary: "When certain Postgres data types are replicated, they'll be stored as `strings` in your data warehouse."
type: "discrepancy, database-integration"
promote: "false"
---
{% include misc/data-files.html %}

When certain data types are replicated from a PostgreSQL database (**input**) integration, they'll display as `OTHER` in {{ app.page-names.int-details }} page.

When replicated into your data warehouse, the following data types will be stored as `strings:`

{% for data-type in stitch.supported-data-types.data-types %}
{% if data-type.supported-by == "postgresql" %}
- `{{ data-type.name }}`
{% endif %}
{% endfor %}