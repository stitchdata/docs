---
title: Xero (v1.0)
permalink: /integrations/saas/xero
keywords: xero, integration, schema, etl xero, xero etl, xero schema
summary: "Connection instructions and schema details for Stitch's Xero integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "xero"
display_name: "Xero"

singer: true
status-url: "https://status.xero.com"
repo-url: "https://github.com/singer-io/tap-xero"

this-version: "1.0"

api: |
  [{{ integration.display_name }} Accounting API](https://developer.xero.com/documentation/api/api-overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "1 hour"
tier: "Paid"
icon: /images/integrations/icons/xero.svg

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
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
  - title: "track data"

# -------------------------- #
#    Replication Details     #
# -------------------------- #

# replication-sections:
#   - title: ""
#     anchor: ""
#     content: |
#       Xero has a daily limit of 5,000 calls in a rolling 24 hour window, and will return a 503 Service Unavailable error if exceeded. This is on a per organization basis.


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