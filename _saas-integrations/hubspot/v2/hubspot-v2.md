---
title: HubSpot (v2)
permalink: /integrations/saas/hubspot
keywords: hubspot, integration, schema, etl hubspot, hubspot etl
summary: "Connection instructions and schema details for Stitch's HubSpot integration."

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
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access HubSpot"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your HubSpot account.
      2. After you log into HubSpot, a screen with a list of your HubSpot accounts will display. Click the account you want to connect to Stitch.

         **Note that Stitch will only ever read your data**. Stitch will never modify or delete any data in your HubSpot account. 
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


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