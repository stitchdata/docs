---
title: Xero (v1)
permalink: /integrations/saas/xero
keywords: xero, integration, schema, etl xero, xero etl, xero schema
summary: "Connection instructions and schema details for Stitch's Xero integration."
layout: singer

key: "xero-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "xero"
display_name: "Xero"

singer: true
status-url: "https://status.xero.com"
repo-url: "https://github.com/singer-io/tap-xero"

this-version: "1"

api: |
  [{{ integration.display_name }} Accounting API](https://developer.xero.com/documentation/api/api-overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.xero"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

extraction-logs: true
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To enable Single Sign-On (SSO) authentication in your Stitch account.** For more information, see [Enabling SSO](https://www.stitchdata.com/docs/account-security/single-sign-on#enable-sso).

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. **Optional**: Check **Include archived contacts** to have Stitch replicate records for archived contacts. If left unchecked, only records for active contacts will be replicated.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Next, you'll be directed to {{ integration.display_name }}'s website to complete the setup.

      1. Enter your {{ integration.display_name }} credentials and click **Login**.
      2. A screen asking for authorization to {{ integration.display_name }} will display. **Note that Stitch will only ever read your data.**
      3. From the dropdown menu, select the company you want to connect to Stitch.
      3. Click **Authorise.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.
  
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/xero

subtable-note: |
  {% assign subtable-name = table.name | append: "__" | append: attribute.name %}
  **Note**: This is an array that may be flattened into a subtable. This table would be named `{{ subtable-name }}`; records in this table may be joined to their parent by following [these instructions]({{ link.destinations.storage.nested-structures | prepend: site.baseurl | append: "#connecting-subtables-to-top-level-records" }}).

  Refer to the [`table_name`](#table_name) table for a list of attributes this subtable may contain.

subsubtable-note: |
  {% assign subtable-name = table.name | append: "__" | append: attribute.name | append: "__" | append: subattribute.name %}
  **Note**: This is an array that may be flattened into a subtable. This table would be named `{{ subtable-name }}`; records in this table may be joined to their parent by following [these instructions]({{ link.destinations.storage.nested-structures | prepend: site.baseurl | append: "#connecting-subtables-to-top-level-records" }}).

  Refer to the [`table_name`](#table_name) table for a list of attributes this subtable may contain.
---
{% assign integration = page %}
{% include misc/data-files.html %}