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

tap-name: "Slack" ## Ex: Intercom, not intercom
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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication. For this integration, you will need to create a new integration for each individual {{ integration.display_name }} workspace you want to replicate data from.


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

setup-steps:
  - title: "Create a Slack App"
    anchor: "slack-app"
    content: |
      1. Go to the [{{ integration.display_name }} App site](https://api.slack.com/apps){:target="new"}.
      2. Click **Create an App**.
      3. Enter a name for your App and select the workspace you want to replicate data from, then click **Create App**.
      4. In the left-side menu panel, click **Install App**.
      5. Click **Request to Install** to install your app. The app must be installed to be allowed to connect to Stitch.
  
  - title: "Assign relevant scopes"
    anchor: "assign-scopes"
    content: |
      1. Log into your {{ integration.display_name }} app.
      2. In the left-side menu panel, click **OAuth & Permissions**.
       3. Scroll down to the **Scopes** section.
      4. For this integration to work, there are a minimum amount of required scopes that need to be added in the **Bot Token Scopes** catecory. They are:
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

  - title: "Retrieve verification token"
    anchor: "verification-token"
    content: |
      1. Log into your {{ integration.display_name }} app.
      2. In the left-side menu panel, click **Basic Information**.
      3. Scroll down to the **App Credentials** section and copy the **Verification Token**. Keep the token readily available for the next step.
  
  - title: "add integration"
    anchor: "add-integration"
    content: |
      4. In the **Token** field, paste the verification token you copied from [step 3](#verification-token).
      5. Check the **Join public channels** box if you'd like to replicate all public channels in the workspace you're replicating, and not just the channels you've personally joined.
      6. Check the **Include private channels** box if you'd like to replicate private channels in the workspace.
      7. Check the **Exclude archived channels** box if you don't want to replicate data from archived channels.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection



# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
- title: "Workspace replication"
  anchor: "workspace-replication"
  content: |
    Stitch can only replicate data from one {{ integration.display_name }} workspace at a time. In order to replicate multiple workspaces, you will need to create integrations for each workspace.

- title: "Lookback windows and data extraction"
  anchor: "lookback-windows-extraction"
  content: |
    {% include note.html type="single-line" content="The info in this section only applies to tables using Key-based Incremental Replication. Tables using Full Table Replication replicate fully during each replication job and don't use lookback windows." %}

    When Stitch runs a replication job for {{ integration.display_name }}, it will use a 14-day lookback period to query for and extract data for your `files` and `remote_files` tables. A lookback window is a period of time for attributing shared files and the lookback period after those actions occur.

    While Stitch replicates data in this way to account for updates to records made during the lookback window, it can have a [substantial impact on your overall row usage](#lookback-window-row-count-impact).

    In the sections below are examples of how lookback windows impact how Stitch extracts data during historical and ongoing replication jobs.

    {% include integrations/saas/ads-append-only-replication.html %}
    {% include integrations/saas/attribution-window-examples.html %}

  subsections:
    - title: "Lookback windows and row count impact"
      anchor: "lookback-window-row-count-impact"
      content: |
        Due to the Lookback Window, a high Replication Frequency may not be necessary. Because Stitch will replicate data from the past `14` days during every replication job, recent data will be re-replicated and count towards your row quota.
        
        To reduce your row usage and replicating redundant data, consider setting the integration to replicate less frequently. For example: every 12 or 24 hours.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/slack


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}