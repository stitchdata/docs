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

requirements-list:
  - item: |
      **Admin access to the workspaces you want to replicate time entry data from, if replicating from multiple workspaces.** Stitch is only able to access the same data as the user whose API token is used to authenticate the integration. {{ integration.display_name }}'s API limits retrieving time entry data to the user's own time entries and the time entries in a workspace where they are also an Admin.


setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API token"
    anchor: "retrieve-toggl-api-token"
    content: |
      {% capture toggl-api-tokens %}
      Your {{ integration.display_name }} API token is specific to you. When replicating data, Stitch will only be able to access the same data as you in Toggl.

      To replicate time entry data from multiple workspaces, you must be an Admin in the workspace you want to replicate data from. Verify that you have this permission in {{ integration.display_name }} before proceeding.
      {% endcapture %}

      {% include note.html first-line="**Verify your Toggl workspace permissions:**" content=toggl-api-tokens %}

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
      5. In the **Trailing Days** field, enter the number of days Stitch should use as an attribution window when replicating time entry data. **Note**: This is only applicable to the `time_entries` table.

         For example: If this value is `5`, Stitch will replicate the past five days' worth of data for the `time_entries` table during every replication job.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Replicating time entry data"
    anchor: "replicating-time-entry-data"
    content: |
      The `time_entries` table uses the **Trailing Days** setting as an attribution window during replication. This means that the number entered into the **Trailing Days** field in the {{ app.page-names.int-settings }} page is the number of days Stitch will query time entry data for during every replication job.

      For example: If you set **Trailing Days** to `5`, Stitch will query for and replicate the past five days' worth of data during every replication job for the `time_entries` table.

      While `time_entries` is replicated incrementally - in that only data from the number of trailing days is replicated during each job - a high number of days being used as the attribution window can increase your row usage.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/toggl
---
{% assign integration = page %}
{% include misc/data-files.html %}