---
title: Responsys
permalink: /integrations/saas/responsys
tags: [saas_integrations]
keywords: responsys, integration, schema, etl responsys, responsys etl, responsys schema

name: "responsys"
display_name: "Responsys"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://status.goshippo.com/
repo-url: https://github.com/singer-io/tap-responsys
icon: /images/integrations/icons/responsys.svg
whitelist:
  tables: "No"
  columns: "No"

format: ## controls formatting options in template
  schema-list: true ## controls display of table list in Schema section
  table-desc: true ## controls display of default copy in table descriptions
  list: expand ## table is used for integrations with tons of tables, like NetSuite.

tables:
## 
  - name: ""
    doc-link: 
    description: ""
    notes: 
    replication-method: "Incremental"
    primary-key: ""
    nested-structures: true
    attribute-notes: 
    attributes:
      - name: 



---

{% contentfor setup %}
Connecting Stitch to Responsys is a four-step process:

1. [](#retrieve-app-creds)
2. [Add Responsys as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)


### 


{% include integrations/shared-setup/connection-setup.html %}


{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}
{% endcontentfor %}



{% contentfor replication-notes %}

{% endcontentfor %}



{% contentfor schema-notes %}


{% endcontentfor %}