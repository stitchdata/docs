---
title: Segment
permalink: /integrations/webhooks/segment
redirect_from: /integrations/saas/segment
layout: saas  ## this uses the SaaS layout b/c it's more SaaS than webhook. The setup is very different.

keywords: segment, integration, schema, etl segment, segment etl, segment schema
summary: "Connection instructions, replication info, and schema details for Stitch's Segment integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "segment"
display_name: "Segment"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "Webhook"
frequency: "Continuous"
tier: "Free"
status-url: "https://twitter.com/segmentstatus"
icon: /images/integrations/icons/segment.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## incompatible:
##  bigquery: "sometimes"
##  reason: "Segment sometimes sends records that contain multiple data types. BigQuery only allows `FLOAT` and `DOUBLE` data types in the same column; otherwise, the field will be rejected."

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Group
  - name: "group"
    doc-link: https://segment.com/docs/spec/track/
    description: "info about groups, which is how individual users are associated with companies, accounts, projects, teams, and so on."
    notes: 
    replication-method: "Incremental (Webhook)"
    primary-key: "message_id"
    nested-structures: false
    attributes:
      - name: Message ID (<code>message_id</code>)
      - name: <a href="https://segment.com/docs/spec/group/#traits" target="blank">Group Traits</a>
      - name: &spec <a href="https://segment.com/docs/spec/common/">Common Fields</a>

## Identify
  - name: "identify"
    doc-link: https://segment.com/docs/spec/identify/
    description: "all user info."
    notes: 
    replication-method: "Incremental (Webhook)"
    primary-key: "message_id"
    nested-structures: false
    attributes:
      - name: Message ID (<code>message_id</code>)
      - name: <a href="https://segment.com/docs/spec/identify/#traits" target="blank">Customer Traits</a>
      - name: *spec

## Page
  - name: "page"
    doc-link: https://segment.com/docs/spec/page/
    description: "info about page events, along with any data about page properties."
    notes: 
    replication-method: "Incremental (Webhook)"
    primary-key: "message_id"
    nested-structures: false
    attributes:
      - name: Message ID (<code>message_id</code>)
      - name: <a href="https://segment.com/docs/spec/page#name" target="blank">Page Name</a>
      - name: <a href="https://segment.com/docs/spec/page#properties" target="blank">Page Properties</a>
      - name: *spec

## Screen
  - name: "screen"
    doc-link: https://segment.com/docs/spec/screen/
    description: "info about screen events, along with any data about screen properties."
    notes: 
    replication-method: "Incremental (Webhook)"
    primary-key: "message_id"
    nested-structures: false
    attributes:
      - name: Message ID (<code>message_id</code>)
      - name: <a href="https://segment.com/docs/spec/screen#name" target="blank">Screen Name</a>
      - name: <a href="https://segment.com/docs/spec/screen#properties" target="blank">Screen Properties</a>
      - name: *spec

## Track
  - name: "track"
    doc-link: https://segment.com/docs/spec/track/
    description: "user action info."
    notes: |
      ### Semantic & Standardized Events
      For info on semantic events - or Segment's standardized event names and properties - [check out their docs](https://segment.com/docs/spec/semantic/).
    replication-method: "Incremental (Webhook)"
    primary-key: "message_id"
    nested-structures: false
    attributes:
      - name: Message ID (<code>message_id</code>)
      - name: <a href="https://segment.com/docs/spec/track#name" target="blank">Event Name</a>
      - name: <a href="https://segment.com/docs/spec/track#properties" target="blank">Event Properties</a>
      - name: *spec
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Segment data to Stitch is a three-step process:

1. [Add Stitch as a selective integration](#stitch-selective-integration)
2. [Add Segment as a Stitch data source](#add-stitch-data-source)
3. [Authorizing Stitch to access Segment](#authorize-stitch)

### Add Stitch as a Selective Integration {#stitch-selective-integration}
{% include integrations/saas/segment-selective-integration.html %}

{% include integrations/shared-setup/connection-setup.html %}
4. Click {{ app.buttons.segment }}.

### Authorize Stitch to Access Segment {#authorize-stitch}

Lastly, you'll be directed to Segment's website to complete the setup.

1. Enter your Segment credentials and click **Login**.
2. From the dropdown menu, select the **Source** you want to send data from. **Note that Stitch will only ever read your data.**
3. Click **Send Data.**
4. After the authorization process successfully completes, you'll be redirected back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.
{% endcontentfor %}



{% contentfor replication-notes %}
Stitch uses what is called a [direct integration](https://segment.com/docs/partners/direct-integration/) to integrate with Segment. This is a webhook-based method of sending your Segment data to integrations. Unlike REST or SOAP APIs, **webhooks deliver data as it happens in real-time**.

In the event that our webhook service experiences downtime, you may notice some lag between an event occurring and the data appearing in your data warehouse.
{% endcontentfor %}



{% contentfor schema-notes %}
Each of Segment's endpoints contains a set of fields unique to that endpoint along with a set of common fields. Common fields are the same across all of Segment's endpoints.

Common fields describe user identity, timestamping, device, network, and so on. For a full list of these fields, check out Segment's [Common Fields](https://segment.com/docs/spec/common/) Spec.
{% endcontentfor %}
