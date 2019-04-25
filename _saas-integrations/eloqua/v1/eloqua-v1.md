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

title: Eloqua
permalink: /integrations/saas/eloqua
keywords: eloqua, integration, schema, etl eloqua, eloqua etl, eloqua schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "eloqua"
display_name: "Eloqua"

singer: true 
tap-name: "Eloqua"
repo-url: https://github.com/singer-io/tap-eloqua

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://community.oracle.com/community/topliners/eloqua-system-status"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account. Click **Sign In** to sign in.
      2. Enter your {{ integration.display_name }} credentials and click **Sign In** again.
      3. The next page will display the application (`Stitch`) requesting access to {{ integration.display_name }}. Click **Sign In** to continue.
      4. The next page will display the company and user you are currently logged into {{ integration.display_name }} as. Click **Accept**.
      5. After the authorization process is successfully completed, you'll be directed back to Stitch.
      6. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/eloqua
---
{% assign integration = page %}
{% include misc/data-files.html %}