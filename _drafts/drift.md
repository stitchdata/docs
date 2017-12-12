---
title: Drift
permalink: /integrations/saas/drift
tags: [saas_integrations]
keywords: drift, integration, schema, etl drift, drift etl, drift schema

name: "drift"
display_name: "Drift"
author: "Stitch"
author-url: https://www.stitchdata.com
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://drift.com
repo-url: https://github.com/singer-io/tap-drift
icon: 
whitelist:
  tables: "No"
  columns: "No"

format: 
  schema-list: true
  table-desc: true
  list: expand

tables:
## Conversations
  - name: "conversations"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: Conversation ID (<code>id</code>)

## Campaign Members
  - name: "campaign_members"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "resultid"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: resultid

## Campaigns
  - name: "campaigns"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: Conversation ID (<code>id</code>)

## Inboxes
  - name: "inboxes"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: Inbox ID (<code>id</code>)

## Messages
  - name: "messages"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Full Table Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: Message ID (<code>id</code>)
---

{% contentfor setup %}
Connecting Stitch to Drift is a **-step process:

1. [Steps]
2. [Add Drift as a Stitch data source](#add-stitch-data-source)
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