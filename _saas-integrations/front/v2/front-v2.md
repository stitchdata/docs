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

title: Front (v2)
permalink: /integrations/saas/front
keywords: front, integration, schema, etl front, front etl, front schema
summary: "Connection instructions, replication info, and schema details for Stitch's Front integration."
layout: singer
# input: false

key: "frontapp-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "frontapp"
display_name: "Front"

singer: true 
tap-name: "FrontApp"
repo-url: https://github.com/singer-io/tap-frontapp

this-version: "2"

api: |
  [Front API](https://dev.frontapp.com/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://www.frontstatus.com/"

api-type: "platform.frontapp"

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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Premium or Enterprise {{ integration.display_name }} plan**. These plans include API access, which is required to use Stitch's {{ integration.display_name }} integration. Refer to [{{ integration.display_name }}'s pricing page for more info](https://frontapp.com/pricing){:target="new"}.

setup-steps:
  - title: "Generate a {{ integration.display_name }} API token"
    anchor: "generate-front-api-token"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/front-create-api-token.png" alt="The New API token page in Front" max-width="550px" %}

      1. Sign into your [{{ integration.display_name }} account](https://app.frontapp.com/){:target="new"}.
      2. Click the user menu (your icon) in the top left corner of the page.
      3. Click **Settings**.
      4. In the **Company** section on the left side of the page, click **Plugins & API**.
      5. On the page that displays, click **API**.
      6. Click the **New Token** button.
      7. On the **New Token** page, click the **Select Scopes** dropdown and select the type of resources you want to replicate data from.
      8. Click **Create** to create the API token.

      Keep the token handy - you'll need it in the next step to complete the setup.

# Per FrontApp support on 12/18/18:
# If you use the shared namespace, you will get analytics for all shared inboxes across all teams. If you use the private namespace, you will get analytics for private inboxes that users have marked accessible to the public API (is an individual user setting).
# I'm not sure how this works with the Get Analtyics endpoint, since this metric seems to be team-focused.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Token** field, paste the {{ integration.display_name }} API token you generated in [Step 1](#generate-front-api-token).
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/front
---
{% assign integration = page %}
{% include misc/data-files.html %}