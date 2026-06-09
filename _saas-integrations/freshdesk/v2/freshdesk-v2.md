---
title: Freshdesk (v2)
permalink: /integrations/saas/freshdesk
keywords: freshdesk, integration, schema, etl freshdesk, freshdesk etl, freshdesk schema
summary: "Connection instructions and schema details for Stitch's Freshdesk integration."
layout: singer

key: "freshdesk-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "freshdesk"
display_name: "Freshdesk"

singer: true
repo-url: https://github.com/singer-io/tap-freshdesk

this-version: "2"

api: |
  [{{ integration.display_name }} REST API v2](https://developers.freshdesk.com/api/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: https://status.freshdesk.com/

api-type: "platform.freshdesk"

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

# Release date for this version
release-date: "February 12, 2026"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

# -------------------------- #
#      What's New in v2      #
# -------------------------- #

whats-new: |
  
  **Version 2.0 of the {{ integration.display_name }} integration includes the following updates:**
  
  - **Discovery support**: You can now select which tables to replicate in Stitch's interface.
  - **Improved replication methods**: Some tables now use Full Table replication for more reliable synchronization.
  - **API v2 support**: The integration now uses {{ integration.display_name }}'s API v2, providing access to current endpoints and functionality.
  - **Enhanced parent-child relationships**: Improved handling of dependent objects (conversations, satisfaction ratings, time entries).
  - **Updated dependencies**: Singer Python upgraded to v6.1.0 for improved compatibility and performance.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in Freshdesk.** As Stitch will only be able to replicate data that the authorizing user has access to, we recommend that someone with these permissions complete the setup. For example: if the authorizing user only has access to a handful of tickets, Stitch will only be able to access and replicate the data for those tickets.

      Having a Freshdesk administrator create the integration will ensure that Stitch is able to replicate all the data in your Freshdesk account.

setup-steps:
  - title: "Retrieve your Freshdesk API Key"
    anchor: "retrieve-api-credentials"
    content: |
      1. Sign into your Freshdesk account.
      2. Click the **user menu (your icon) > Profile Settings**.
      3. Your API Key will display under the **Change Password** section of your profile page. Copy this key.

      Leave this page open for now - you'll need it to wrap things up in Stitch.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/saas/setup/table-selection.html %}

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/freshdesk/v2

---
{% assign integration = page %}
{% include misc/data-files.html %}
