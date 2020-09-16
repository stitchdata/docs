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

title: Kustomer (v1)
permalink: /integrations/saas/kustomer
keywords: kustomer, integration, schema, etl kustomer, kustomer etl, kustomer schema
layout: singer
# input: false

key: "kustomer-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "kustomer"
display_name: "Kustomer"

singer: true
status-url: ""

tap-name: "Kustomer"
repo-url: https://github.com/singer-io/tap-kustomer

this-version: "1"

api: |
  [Kustomer REST API v1](https://apidocs.kustomer.com/?version=latest){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.kustomer"

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
  - item: |
      **A {{ integration.display_name }} admin role**. Admin permissions or a role with **read** and **write** security permissions are required to create an API key in {{ integration.display_name }}.

setup-steps:
  - title: "Create a {{ integration.display_name }} API key"
    anchor: "obtain-api-key"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Navigate to **Settings > API Keys**
      3. Click **New API Key**.
      4. Select the roles that can have access to the API key.
      5. **Leave the API expriation options blank.** If you set an expiration date, the API key will expire and break the connection to Stitch. In the event that this happens, you'll need to re-generate the API key in {{ integration.display_name }} and enter the new key into Stitch.
      6. Click **Create**.
      7. Copy the API key and keep it readily available for the next step.

      **Note**: {{ integration.display_name }} will only display the key once, so save it somewhere secure for future reference.
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the API key you obtained in [Step 1](#obtain-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/kustomer/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}

