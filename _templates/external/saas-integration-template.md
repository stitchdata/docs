---
title: INTEGRATION NAME
permalink: /integrations/saas/integration_name ## use find/replace on 'integration_name' to insert the integration name
tags: [saas_integrations]
keywords: integration_name, schema, etl integration_name, integration_name etl, integration_name schema

## used as a key; never changes. Use underscores for spaces.
name: "integration_name"

## integration name as it should be displayed.
display_name: "INTEGRATION NAME"

## leave as-is - indicates integration is built on Singer platform
singer: true

## who built this awesomeness?
author: ""

## link to your site
author-url: 

## Stitch release status - leave as-is
status: "Open Beta"

## default historical sync
historical: "1 year"

## default Replication Frequency
frequency: "30 minutes"

## Stitch pricing tier required to use integration
tier: "Free"

## URL of integration's status page
status-url: 

## URL of GitHub repo in Singer.io org
repo-url:

## Stitch to complete this - leave blank 
icon: 

## indicates ability to select individual tables & columns for replication
whitelist:
  tables: "No" ## can the user whitelist tables?
  columns: "No" ## can the user whitelist columns?

## API Usage Limits
## Does the integration's API have usage limits that may impact the
## speed of replication or ability to replicate at all? 
## If yes, set to true.
## For example: Salesforce enforces a daily quota - once it's reached,
## Stitch is unable to replicate data until more quota is available.

enforces-api-limits: true/false

## Querying Strategy
## Some services have attribution windows where data can be updated during
## default attribution windows.
## Ex: Google Analytics' replication is always for the last 15 days due to
## GA's attribution window. This accounts for updates & prevents stale (false)
## data, but can result in a high number of rep[licated rows.

attribution-window: "# days"

tables:
## every table Stitch will create needs to have a section 
## created for it, using the template below.

## Entity/Object Name (ex: Customers)

  ## name of table as it will appear in data warehouse
  - name: "table_name" 

    ## link to external docs, if there are any. 
    ## Ex: API docs that list out fields & descriptions.
    doc-link: 

    ## brief description of what the table is/what's in it
    description: "" 

    ## info / things of note about the table. 
    ## Ex: how to account for deletes, how the table replicates, etc.
    notes: 

    ## how Stitch will replicate the table. This is different 
    ## than how data is requested from an API. As Stitch charges 
    ## by the number of replicated rows, we care about the rows that 
    ## are **persisted** to a data warehouse.
    replication-method: "Full Table / Incremental / Append-Only (Incremental)"

    ## If this table is affected by an attribution window, leave this as-is.
    ## Otherwise, remove.
    ## For an example, see Intercom: /docs/integrations/saas/intercom#replication
    attribution-window: true

    ## table's Primary Key column(s). If composite, use colons 
    ## to separate. Ex: id : user_id
    primary-key: ""

    ## change to true only if the endpoint contains nested **arrays**. 
    nested-structures: false

    ## list each attribute in the table, listing Primary Key columns first.
    attributes:
      - name: primary_key 
      - name: column_name
      - name: column_name
      - name: column_name
---

{% contentfor setup %}
### Prerequisites
- Is there anything that's absolutely required to use this integration or set it up? Ex: certain permission levels, certain plan tier, etc.

### Setup
- What setup, if any, must users complete outside of Stitch to use the integration?
{% endcontentfor %}



{% contentfor replication-notes %}
- If there's anything of note about replication or how Stitch queries, note it here.

- We include info that impacts the number of rows replicated (such as only being able to query by day, thus potentially re-replicating data) or will explain why a sync may take awhile.
{% endcontentfor %}



{% contentfor schema-notes %}
- If there's anything of note about the table(s) in this integration, note them here.
 
- Ex: columns Stitch inserts or syncs by default, such as the new Google AdWords integration. `start_date` and `end_date` columns were added to account for the daily pagination of data & tie rows to specific days.
{% endcontentfor %}