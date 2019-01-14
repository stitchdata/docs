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

title: FrontApp (v1.0)
permalink: /integrations/saas/frontapp
tags: [saas_integrations]
keywords: frontapp, integration, schema, etl frontapp, frontapp etl, frontapp schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "frontapp"
display_name: "FrontApp"

singer: true 
tap-name: "FrontApp"
repo-url: https://github.com/singer-io/tap-frontapp

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://www.frontstatus.com/"
icon: /images/integrations/icons/frontapp.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Premium or Enterprise {{ integration.display_name }} plan**. These plans include API access, which is required to use Stitch's {{ integration.display_name }} integration. Refer to [{{ integration.display_name }}'s pricing page for more info](https://frontapp.com/pricing){:target="new"}.

setup-steps:
  - title: "Generate a {{ integration.display_name }} API token"
    anchor: "generate-frontapp-api-token"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/frontapp-create-api-token.png" alt="The New API token page in FrontApp" max-width="550px" %}

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

  - title: "add integration"
    content: |
      4. In the **API Token** field, paste the {{ integration.display_name }} API token you generated in [Step 1](#generate-frontapp-api-token).
      5. From the **Incremental Range** dropdown, select one of the following options:
         - **Daily** - Data will be aggregated on a daily basis.
         - **Hourly** - Data will be aggregated on an hourly basis.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/frontapp
---
{% assign integration = page %}
{% include misc/data-files.html %}