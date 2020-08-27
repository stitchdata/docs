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

title: Slack (v1)
permalink: /integrations/saas/slack ## Add if there are multiple versions: /vVERSION
keywords: slack, integration, schema, etl slack, slack etl, slack schema
layout: singer
# input: false

key: "slack-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "slack"
display_name: "Slack"

singer: true
status-url: "https://status.slack.com/"

tap-name: "Slack"
repo-url: https://github.com/singer-io/tap-slack

this-version: "1"

api: |
  [{{ integration.display_name }} Web API](https://api.slack.com/web){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.slack"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

attribution-window: "14 days"
attribution-is-configurable: false

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from a single {{ integration.display_name }} workspace using the {{ integration.api | flatify | strip }}. To replicate data from multiple workspaces, create an additional {{ integration.display_name }} integration for each workspace.

  Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Create a {{ integration.display_name }} app and retrieve a verification token"
    anchor: "create-slack-app"
    content: |
      {% capture multiple-workspaces %}
      **Connecting multiple workspaces?** You'll need to create a new {{ integration.display_name }} app and Stitch {{ integration.display_name }} integration for each workspace. Follow this guide in its entirety for each workspace you want to replicate data from.
      {% endcapture %}

      {% include note.html type="single-line" content=multiple-workspaces %}

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Create the app"
        anchor: "create-the-app"
        content: |
          1. Navigate to the [{{ integration.display_name }} App site](https://api.slack.com/apps){:target="new"}.
          2. Click **Create an App**.
          3. Enter a name for the app and select the workspace you want to replicate data from.
          4. Click **Create App**.
  
      - title: "Grant relevant scopes to the app"
        anchor: "assign-scopes"
        content: |
          Next, you'll grant the required permissions to the app you created in [the previous step](#create-the-app).

          {% include layout/inline_image.html type="right" alt="The add permission by scope or API method menu, expanded, in the Bot Token Scopes section of the Slack App Scopes page" file="integrations/slack-bot-token-scopes.png" max-width="450px" %}

          1. The app you created should be selected in the drop-down menu near the top-left corner of the page. If it isn't, select it.
          2. Click **Features > OAuth & Permissions** in the left side menu.
          3. Scroll to the **Scopes** section.
          4. In the **Bot Token Scopes** section, click the **Add an OAuth Scope** button.
          5. In the field that appears, search for the following scopes:
              - `channels:history`
              - `channels:join`
              - `channels:read`
              - `files:read`
              - `groups:read`
              - `links:read`
              - `reactions:read`
              - `remote_files:read`
              - `remote_files:write`
              - `team:read`
              - `useergroups:read`
              - `users.profile:read`
              - `users:read`

              {{ integration.display_name }} will automatically save the changes each time a scope is added.
          6. Repeat steps 4 and 5 until all the scopes have been added.

      - title: "Install the app to your workspace"
        anchor: "install-app-workspace"
        content: |
          {% capture install-approval %}
          **If app approval is enabled for your workspace** and you don't have the required permissions to install apps, you may need to contact a  Workspace Owner or App Manager in your workspace to complete this step. Refer to [{{ integration.display_name }}'s documentation](https://slack.com/help/articles/222386767-Manage-app-installation-settings-for-your-workspace){:target="new"} for more info.
          {% endcapture %}

          {% include note.html type="single-line" content=install-approval %}

          After the [required scopes](#assign-scopes) are added to the app, you'll need to install it to your {{ integration.display_name }} workspace. This is required to successfully connect to Stitch.

          1. Scroll up to the **OAuth Tokens & Redirect URLs** section of the **OAuth & Permissions** page.
          2. In this section, click the **Install App to Workspace** button.
          3. Complete the steps that follow to install the app or submit a request to your Workspace Owner(s) for approval.

      - title: "Retrieve the app's bot user OAuth access token"
        anchor: "bot-user-oauth-access-token"
        content: |
          After the app is successfully installed to your {{ integration.display_name }} workspace, a **Tokens for Your Workspace** section containing a **Bot User OAuth Access Token** field will display on the page:

          ![The Bot User OAuth Access Token in the Tokens for Your Workspace section of the OAuth Tokens & Redirect URLs App page in Slack]({{ site.baseurl }}/images/integrations/slack-bot-oauth-access-token.png)

          Keep the token readily available for the next step.
  
  - title: "add integration"
    content: |
      4. In the **Token** field, paste the bot user OAuth access token you copied from [Step 1.4](#bot-user-oauth-access-token).
      5. Check the **Join public channels** box if you'd like to replicate data for all public channels in the workspace you're connecting. Otherwise, only data for channels you've personally joined will be replicated.
      6. Check the **Include private channels** box if you'd like to replicate data for private channels in the workspace.
      7. Check the **Exclude archived channels** box if you don't want to replicate data from archived channels.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
- title: "Workspace replication"
  anchor: "workspace-replication"
  content: |
    Stitch can only replicate data from one {{ integration.display_name }} workspace at a time. In order to replicate multiple workspaces, you will need to create integrations for each workspace.

# - title: "Lookback windows and data extraction"
#   anchor: "lookback-windows-extraction"
#   content: |
#     {% include note.html type="single-line" content="The info in this section only applies to tables using Key-based Incremental Replication. Tables using Full Table Replication replicate fully during each replication job and don't use lookback windows." %}

#     When Stitch runs a replication job for {{ integration.display_name }}, it will use a 14-day lookback period to query for and extract data for your `files` and `remote_files` tables. A lookback window is a period of time for attributing shared files and the lookback period after those actions occur.

#     While Stitch replicates data in this way to account for updates to records made during the lookback window, it can have a [substantial impact on your overall row usage](#lookback-window-row-count-impact).

#     In the sections below are examples of how lookback windows impact how Stitch extracts data during historical and ongoing replication jobs.

#     {% include integrations/saas/ads-append-only-replication.html %}
#     {% include integrations/saas/attribution-window-examples.html %}

#   subsections:
#     - title: "Lookback windows and row count impact"
#       anchor: "lookback-window-row-count-impact"
#       content: |
#         Due to the Lookback Window, a high Replication Frequency may not be necessary. Because Stitch will replicate data from the past **14 days** during every replication job, recent data will be re-replicated and count towards your row quota.
        
#         To reduce your row usage and replicating redundant data, consider setting the integration to replicate less frequently. For example: every 12 or 24 hours.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/slack/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}