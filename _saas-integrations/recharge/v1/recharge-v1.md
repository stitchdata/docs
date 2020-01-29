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

title: ReCharge
permalink: /integrations/saas/recharge
keywords: recharge, integration, schema, etl recharge, recharge etl, recharge schema
layout: singer
# input: false

key: "recharge-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "recharge"
display_name: "ReCharge"

singer: true
status-url: ""

tap-name: "recharge"
repo-url: https://github.com/singer-io/tap-recharge

this-version: "1.0"

api: |
  [ReCharge Payments API](https://developer.rechargepayments.com/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. To access the {{ integration.display_name }} API documentation, you will need [your API key](#obtain-api-key). Refer to the [Schema](#schema) section for a list of objects available for replication.



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
  - item: "**A Shopify Account**. You need this to access your {{ integration.display_name }} information."

setup-steps:
  - title: "Obtain Your {{ integration.display_name }} API Key"
    anchor: "obtain-api-key"
    content: |
      1. Log into your Shopify account, select `Apps`, and then click on your {{ integration.display_name }} application.
         {% include layout/image.html file="/integrations/recharge-apps-screen.png" alt="Shopify Apps page." enlarge=true max-width="550" %}
      {:start="2"}
      2. In the application, click on the `EXPLORE {{ integration.display_name }}` option.
         {% include layout/image.html file="/integrations/recharge-explore-button.png" alt="EXPLORE ReCharge button." enlarge=true max-width="250" %}
      {:start="3"}
      3. Click on the `Integrations` tab, and then click `API tokens...`.
         {% include layout/image.html file="/integrations/recharge-integrations-api-tokens.png" alt="Integrations page with API token link." enlarge=true max-width="550" %}
      {:start="4"}   
      4. Click on `Create an API token` and fill out the `Details` and `Permission`. In the `Permission` section, select `Read Access` from the dropdown menu for each item. Save to obtain your API key and keep it readily available to set up the inegration.
         {% include layout/image.html file="/integrations/recharge-api-token.png" alt="The API key creation page." enlarge=true max-width="550" %}
  - title: "add integration"
    content: |
      4. In the `API Key` field, enter the API key you obtained in the [previous step](#obtain-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/recharge


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}