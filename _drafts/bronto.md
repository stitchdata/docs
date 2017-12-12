---
title: Bronto
permalink: /integrations/saas/bronto
tags: [saas_integrations]
keywords: bronto, integration, schema, etl bronto, bronto etl, bronto schema

name: "Bronto"
display_name: "bronto"
author: "Stitch"
author-url: https://www.stitchdata.com
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://twitter.com/Bronto
repo-url: https://github.com/singer-io/tap-bronto
icon:
whitelist:
  tables: "No"
  columns: "No"

format: ## controls formatting options in template
  schema-list: true ## controls display of table list in Schema section
  table-desc: true ## controls display of default copy in table descriptions
  list: expand ## table is used for integrations with tons of tables, like NetSuite.

tables:
## TABLE NAME
  - name: ""
    doc-link: 
    description: ""
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: ID (<code>id</code>)
---

{% contentfor setup %}
Connecting Stitch to Bronto is a **-step process:

1. [Steps]
2. [Add Bronto as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)



## Prerequisites


{% include integrations/shared-setup/connection-setup.html %}
[remaining steps]

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}
{% endcontentfor %}



{% contentfor replication-notes %}

{% endcontentfor %}



{% contentfor schema-notes %}

{% endcontentfor %}