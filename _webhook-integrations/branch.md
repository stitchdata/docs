---
title: Branch
permalink: /integrations/webhooks/branch
redirect_from: /integrations/saas/branch
## Some users may experience a blip while the redirect works - it's normal.

keywords: branch, integration, schema, etl branch, branch etl, branch schema, stitch webhooks
summary: "Connect your Branch data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "branch"
display_name: "Branch"

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "Webhook"
branded: true
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false
  field: 
tier: "Standard"
status-url: http://status.branch.io/
icon: /images/integrations/icons/branch.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://branch.com/docs/api/webhooks
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: true
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: ID (<code>id</code>)
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

For additional info on Branch webhooks, check out [Branch's webhooks documentation](https://dev.branch.io/getting-started/webhooks/guide/).

1. Sign into your Branch account.
2. In the side nav, click the [webhooks](https://dashboard.branch.io/webhook) option.
3. Click **Add a new webhook**. 
4. In the window that displays:
   - Paste your Stitch-generated webhook URL in the URL field.
   - Leave the method (`POST`) as-is.
   - Set the notification frequency using the drop-down menu. You can choose to receive a webhook for every single event occurrence or only for the first time that event is triggered for a unique user.
   - Set the [**event trigger**](https://dev.branch.io/getting-started/webhooks/guide/#event-trigger) using the drop-down menu.
5. When finished, click the **Add webhook** button.
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}
{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}