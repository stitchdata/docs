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
  [Slack Web API](https://api.slack.com/web){:target="new"}


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

# attribution-window: "# days"
# attribution-is-configurable: 

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
      1. Go to the [{{ integration.display_name }} App site](api.slack.com/apps).
      2. Click **Create and App**.
      3. Enter a name for your App and select the workspace you want to replicate data from, then click **Create App**.
      4. In the left-side menu panel, click **Install App**.
      5. Click **Request to Install**, to install your app. The app must be installed so that you're allowed you to connect to Stitch.
  
  - title: "Assign relevant scopes"
    anchor: "assign-scopes"
    content: |
      1. Log into your {{ integration.display_name }} app.
      2. In the left-side menu panel, click **OAuth & Permissions**.
      3. Scroll down to the **Scopes**.
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
    content: |
      4. In the **Token** field, paste the verification token you copied from [step 3](#verification-token).
      5. Check the **Join public channels** box if you'd like to sync all public channels in the workspace you're replicating, and not just the channels you've personally joined.
      4. Check the **Include private channels** box if you'd like to sync privatee channels in the workspace.
      4. Check the **Exclude archived channels** box if you don't want to sync data from archived channels.

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