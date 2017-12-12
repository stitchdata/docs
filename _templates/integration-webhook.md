---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: WEBHOOK-INTEGRATION
permalink: /integrations/saas/webhook-integration
tags: [saas_integrations]
keywords: webhook-integration, integration, schema, etl webhook-integration, webhook-integration etl, webhook-integration schema

format: ## controls formatting options in template
  schema-list: true ## controls display of table list in Schema section
  table-desc: true ## controls display of default copy in table descriptions
  list: expand ## table is used for integrations with tons of tables, like NetSuite.


# -------------------------- #
#    Integration Details     #
# -------------------------- #

name: "webhook-integration"
display_name: "WEBHOOK-INTEGRATION"
author: "Stitch"
status: ""
type: "Webhook"
branded: true/false
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false     ## if we hard-code a PK, enter true & enter the name
  field: ""
tier: "Free"
status-url: 
icon: /images/integrations/icons/webhook-integration.svg


# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## uncomment section below if integration is compatible with all Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 


# -------------------------- #
#    Integration Schema      #
# -------------------------- #

tables:
## TABLE NAME
  - name: "data" ## data for v1 generic webhook integrations
    doc-link: 
    description: ""
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: ID (<code>id</code>)
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}

IF GENERIC WEBHOOK:
Connecting Stitch to WEBHOOK-INTEGRATION is a four-step process:

1. [Add WEBHOOK-INTEGRATION as a Stitch data source](#add-stitch-data-source)
2. [Define the Primary Key](#define-webhook-primary-key)
3. [Generate a Webhook URL](#generate-webhook-url)
4. [Set up webhooks in WEBHOOK-INTEGRATION](#setup-webhooks-in-app)

### Prerequisites
Before you dive into setting up your WEBHOOK-INTEGRATION integration, you need to:

{% include integrations/webhooks/webhook-setup.html %}

[in-app setup steps]
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}
{% endcontentfor %}