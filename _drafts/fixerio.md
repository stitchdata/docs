---
title: Fixer.io
permalink: /integrations/saas/fixerio
tags: [saas_integrations]
keywords: fixerio, integration, schema, etl fixerio, fixerio etl, fixerio schema

name: "fixerio"
display_name: "Fixer.io"
author: "Stitch"
author-url: https://www.stitchdata.com
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://fixer.io/
repo-url: https://github.com/singer-io/tap-fixerio
icon:
whitelist:
  tables: "No"
  columns: "No"

format: 
  schema-list: true
  table-desc: true
  list: expand

tables:
## Exchange Rate
  - name: "exchange_rate"
    doc-link: 
    description: "info about daily exchange rates,  "
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: base
      - name: date
      - name: rates
---

{% contentfor setup %}
Connecting Stitch to Fixer.io is a **-step process:

1. [Steps]
2. [Add Fixer.io as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)



## Prerequisites


{% include custom/integrations/setup/connection-setup.html %}
[remaining steps]

{% include custom/integrations/setup/historical-sync.html %}

{% include custom/integrations/setup/replication-frequency.html %}
{% endcontentfor %}



{% contentfor replication-notes %}


{% endcontentfor %}



{% contentfor schema-notes %}


{% endcontentfor %}