---
title: HubSpot (v2)
permalink: /integrations/saas/hubspot/v2
keywords: hubspot, integration, schema, etl hubspot, hubspot etl
summary: "Connection instructions and schema details for Stitch's HubSpot integration."
input: false
layout: singer
key: "hubspot-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "hubspot"
display_name: "HubSpot"

singer: true
repo-url: https://github.com/singer-io/tap-hubspot

this-version: "2"

api: |
  [{{ integration.display_name }} REST API](https://developers.hubspot.com/docs/overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "30 days"
frequency: "30 minutes"
tier: "Standard"
status-url: https://status.hubspot.com/

api-type: "platform.hubspot"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true
table-level-reset: true

extraction-logs: true
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## See the incompatibilities.yml files
## in _data/destinations for details.

has-incompatibilities: true

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
      **For HubSpot CRM or Marketing products:** Administrator permissions in HubSpot. **Note**: To replicate [email events](#email_events), you'll need to have **Super Admin** permissions in HubSpot.
  - item: "**For the HubSpot Sales product:** Sales Administrator permissions in HubSpot."

requirements-info: |
  More information about HubSpot user roles and permissions can be found in [HubSpot's documentation](https://knowledge.hubspot.com/articles/kcs_article/settings/hubspot-user-roles-guide){:target="new"}.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access HubSpot"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your HubSpot account.
      2. After you log into HubSpot, a screen with a list of your HubSpot accounts will display. Click the account you want to connect to Stitch.

         **Note that Stitch will only ever read your data**. Stitch will never modify or delete any data in your HubSpot account. 
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


removal-info: |
  To completely disconnect Stitch from your {{ page.display_name }} account, you need to delete the integration from Stitch, and uninstall the Stitch app from {{ page.display_name }}.
  
  Disconnecting {{ page.display_name }} from Stitch will stop the replication of {{ page.display_name }} data to your Stitch destination. There will be no impact to the {{ page.display_name }} data, as Stitch is a read-only integration with {{ page.display_name }}. All data that has already replicated to your Stitch destination will be maintained and under your control.

removal-steps:
  - title: "Deleting your {{ page.display_name }} integration"
    anchor: "delete-integration"
    content: |
      To delete your {{ page.display_name }} integration from your Stitch account:
      1. Log in to your Stitch account and open the **Integrations** tab.
      2. Click your {{ page.display_name }} integration and click **Settings**.
      3. Scroll down to the bottom of the page and click **Delete**.
      4. Click **Delete** to confirm.

  - title: "Uninstalling Stitch in your {{ page.display_name }} account"
    anchor: "uninstall-stitch"
    content: |
      To uninstall Stitch in your {{ page.display_name }} account:
      1. Log in to your {{ page.display_name }} account and click the **Marketplaces** account in the navigation bar.
      2. Under **Manage**, click **Connected apps**.
      3. Click the **Actions** drop-down menu in the **Stitch** app, and click **Uninstall**.
      4. In the dialog box that appears, enter `uninstall` in the text field and click **Uninstall** to confirm.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

## See this integration's folder in /_integration-schemas for details
## on the tables it contains.

schema-sections:
  - title: "Custom HubSpot field replication"
    anchor: "custom-field-replication"
    content: |
      Custom object properties, or fields, are supported by Stitch's {{ integration.display_name }} integration. Stitch will query the `properties` list for each object and, if custom fields are available through {{ integration.display_name }}'s API, replicate them to your destination.

      The data types of these fields will be the same as the data type in HubSpot. For example: A custom field containing `date` data will be a `date` field in your destination.

      This is applicable to any object that supports custom fields in {{ integration.display_name }}.

  - title: "HubSpot date/date-time values & UNIX timestamps"
    anchor: "datetime-unix-timestamps"
    content: |
      [{{ integration.display_name }} uses UNIX-formatted timestamps in milliseconds](https://developers.hubspot.com/docs/faq/how-should-timestamps-be-formatted-for-hubspots-apis){:target="new"} to store `date` and `datetime` data. Stitch doesn't perform any transformation during the replication process, meaning these values won't be converted to timestamps before they're loaded into your destination.

      To account for this, consider creating a user-defined function to perform the conversion or building views on top of the raw data.

---

{% include misc/data-files.html %}