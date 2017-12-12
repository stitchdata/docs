---
title: Twitter Ads
permalink: /integrations/saas/twitter ads
tags: [saas_integrations]
keywords: twitter ads, integration, schema, etl twitter ads, twitter ads etl, twitter ads schema

name: "twitter-ads"
display_name: "Twitter Ads"
author: "Stitch"
## singer: true
author-url: https://www.stitchdata.com
status: "Coming Soon"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: ""
icon: /images/integrations/icons/twitter-ads.svg
whitelist:
  tables: "No"
  columns: "No"

## Twitter's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

attribution-window: "30 days"

format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

tables:
## TABLE NAME
  - name: "twitter_ads_"
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

{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/saas/attribution-windows.html %}
{% endcontentfor %}



{% contentfor schema-notes %}

{% endcontentfor %}