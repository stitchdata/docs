---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: eBay (v1)
permalink: /integrations/saas/ebay ## Add if there are multiple versions: /vVERSION
keywords: ebay, integration, schema, etl ebay, ebay etl, ebay schema
layout: singer
# input: false

key: "ebay-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ebay"
display_name: "eBay"

singer: true
status-url: "https://www.ebay.com/sts"

tap-name: "eBay" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-ebay

this-version: "1"

api: |
  [{{ integration.display_name }} Fulfillment API](https://developer.ebay.com/api-docs/sell/fulfillment/static/overview.html){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.ebay"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**An {{ integration.display_name }} seller account**. This account owns the sales data."
  - item: "**An {{ integration.display_name }} developer account** to allow Stitch to access the sales data."

requirements-info:

setup-steps:
  - title: "Obtain your App and Cert IDs"
    anchor: "obtain-ids"
    content: |
      1. Login to your {{ integration.display_name }} developer account.
      2. Click on the dropdown menu at the top of the page titled with your username.
      3. Select **Application Access Keys**.
      4. Locate the app you want to use for the integration. If you don't have an app, click **Create a keyset** to make one.
      5. Copy your **App ID** and **Cert ID**. You will need these to setup the Stitch integration.

  - title: "Grant your {{ integration.display_name }} developer account access to your {{ integration.display_name }} seller account and obtain your refresh token"
    anchor: "grant-access"
    content: |
      1. Next to your **App ID** you obtained in [step 1](#obtain-ids), click **User Tokens**.
      2. In the **User Tokens ({{ integration.display_name }} Sign-in)** section, make sure **Auth'n'Auth** is selected, and then click **Sign in to Production**.
      3. Sign in using your {{ integration.display_name }} seller account.
      4. A page will open asking you to grant your {{ integration.display_name }} application access to your {{ integration.display_name }} seller data. Click **Agree**.
      4. You will be redirected back to the **User Tokens ({{ integration.display_name }} Sign-in)** section. Underneath the **Sign in to Production** button is your refresh token. Copy the token and also keep note of the expiration date. You will need to update the refresh token in the Stitch integration setup anytime it expires.


  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Client ID** field, paste the App ID you obtained in [step 1](#obtain-ids).
      5. In the **Client Secret** field, paste the Cert ID you obtained in [step 1](#obtain-ids).
      6. In the **Refresh Token** field, paste the token you obtained in [step 2](#grant-access).
      7. In the **Scope** field, enter `sell.fulfillment.readonly`.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/ebay


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}