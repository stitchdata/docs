---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

# Need some help?

# See this how-to for instructions on filling out the template:
#     

# See this reference guide for more info on the parameters in this template:
# 


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: WEBHOOK-INTEGRATION
permalink: /integrations/saas/webhook-integration
tags: [saas_integrations]
keywords: webhook-integration, integration, schema, etl webhook-integration, webhook-integration etl, webhook-integration schema

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "webhook-integration"
display_name: "WEBHOOK-INTEGRATION"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta/Closed Beta/Released/Deprecated"
certified: 

type: "Webhook"
branded: true/false

historical: "Webhook"
frequency: "Continuous"
tier: "Free/Premium"
status-url: ""
icon: /images/integrations/icons/webhook-integration.svg

whitelist:
  tables: false
  columns: false
primary-key:
  defined: false
  field: ""

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#     Incompatibilities      #
# -------------------------- #

## uncomment section below if integration is compatible with all Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

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