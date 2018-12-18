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

title: FrontApp
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
tap-name: "frontapp"
repo-url: https://github.com/singer-io/tap-frontapp

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true 

historical: "1 year"
frequency: "30 minutes"
tier: "Free/Paid"
status-url: ""
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
      1. Sign into your {{ integration.display_name }} account.
      2. Click the user menu (your icon) in the top left corner of the page.
      3. Click **Settings**.
      4. In the **Company** section on the left side of the page, click **Plugins & API**.
      5. On the page that displays, click **API**.
      6. Click the **New Token** button.

  - title: "add integration"
    content: |
      4. In the **API Token** field, paste the {{ integration.display_name }} API token you generated in [Step 1](#generate-frontapp-api-token).
      5. In the **Metric** field,
      6. In the **Incremental Range** field, 
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/frontapp

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}