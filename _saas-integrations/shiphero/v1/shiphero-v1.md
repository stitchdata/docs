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

title: ShipHero (v1.0)
permalink: /integrations/saas/shiphero
keywords: shiphero, integration, schema, etl shiphero, shiphero etl, shiphero schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "shiphero"
display_name: "ShipHero"

singer: true 
tap-name: "ShipHero"
repo-url: https://github.com/singer-io/tap-shiphero

use-default-icon: true

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.shiphero.com/"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

#https://help.shiphero.com/article/32-where-can-i-get-my-api-credentials
# It looks like API tokens are tied to a single store in ShipHero.
# this means one store per integration in Stitch.

setup-steps:
  - title: "Generate a {{ integration.display_name }} API token"
    anchor: "generate-{{ integration.name }}-api-token"
    content: |
      1. Sign into your [{{ integration.display_name }} account](https://signin.shiphero.com/){:target="new"}.
      2. Using the top menu in {{ integration.display_name }}, click **My Account > Settings > API**.
      3. On the **API Credentials** page, click into the **Shop Name** field and enter the name of the shop you want to use.
      4. Click the **Add** button to generate the API credentials.

      The **API Key** on this page is what you'll need to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} Token** field, paste the value from the **API Key** field in {{ integration.display_name }}.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/shiphero

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}