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

title: Toggl (v1.0)
permalink: /integrations/saas/toggl
tags: [saas_integrations]
keywords: toggl, integration, schema, etl toggl, toggl etl, toggl schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "toggl"
display_name: "Toggl"

singer: true 
tap-name: "Toggl"
repo-url: https://github.com/singer-io/tap-toggl

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
#status-url: "" # None available

# TODO: Add toggl.svg
icon: /images/integrations/icons/singer.svg

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

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API token"
    anchor: "retrieve-toggl-api-token"
    content: |
      1. [Sign into your {{ integration.display_name }} account](https://toggl.com/login/){:target="new"}.
      2. Click the **Workspace** menu in the lower left corner.
      3. Click **Profile settings**.
      4. Locate the **API token** field, which is highlighted in the image below:

         ![The API token field, highlighted in the Toggl Profile Settings page]({{ site.baseurl }}/images/integrations/toggl-profile-settings-api-token.png)

      5. Copy the API token.

      Keep this handy - you'll need it to complete the next step.

  - title: "add integration"
    content: |
      4. In the **API Token** field, paste the API token you retrieve in [Step 1](#retrieve-toggl-api-token).
      5. In the **Trailing Days** field, 

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/toggl
---
{% assign integration = page %}
{% include misc/data-files.html %}