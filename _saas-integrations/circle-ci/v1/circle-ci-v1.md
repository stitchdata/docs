---
title: CircleCI (v1)
permalink: /integrations/saas/circle-ci ## Add if there are multiple versions: /vVERSION
keywords: circle-ci, integration, schema, etl circle-ci, circle-ci etl, circle-ci schema
layout: singer
# input: false

key: "circle-ci-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "circle-ci"
display_name: "CircleCI"

singer: true
status-url: "https://status.circleci.com/"

tap-name: "CircleCI" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-circle-ci

this-version: "1"

api: |
  [CircleCI API v2](https://circleci.com/docs/api/v2/index.html){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.circle-ci"

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
  - title: "Create {{ integration.display_name }} API token"
    anchor: "create-api-token"
    content: |
      1. Log into your {{ integration.display_name }} application.
      2. Go to your **User settings**.
      3. Click **Personal API Tokens**.
      4. Click the **Create New Token** button.
      5. The the **Token name** field, type in a name you will remember - like `Stitch Integration`.
      6. Click the **Add API Token** button.
      7. Copy your new API token and paste it in a safe location, as you will not be able to view it in the application again.

  - title: "Create your project slugs"
    anchor: "create-your-project-slugs"
    content: |
      A project slug is a triplet of the componenets:
        - **Project type** - which can either be `github` or `bitbucket`
        - **Organization** - the name of your organization on GitHub or Bitbucket
        - **Repository** - the name of the repository
      
      The project slug takes the form of `<project_type>/<org_name>/<repo_name>`. For example, the project slug for this {{ integration.display_name }} Singer tap is `github/singer-io/circle-ci`.

      Determine which repositories you would like to include in your Stitch {{ integration.display_name }} integration and list them, separated by spaces, in the project slug format. Keep this list in a safe location.


  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Project Slugs** field, paste the list of project slugs you created in [step 2](#create-your-project-slugs).
      5. In the **Token** field, paste the API token you created in [step 1](#create-api-token).

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/circle-ci


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}