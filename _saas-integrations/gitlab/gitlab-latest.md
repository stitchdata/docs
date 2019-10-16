---
title: GitLab (v1.0)
permalink: /integrations/saas/gitlab
keywords: gitlab, integration, schema, etl gitlab, gitlab etl, gitlab schema
summary: "Connection instructions and schema details for Stitch's GitLab integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "gitlab"
display_name: "GitLab"

singer: true
repo-url: https://github.com/singer-io/tap-gitlab

this-version: "1.0"

api: |
  [GitLab REST API](https://docs.gitlab.com/ee/api/README.html){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://status.gitlab.com/

table-selection: false
column-selection: false

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to any projects you want to replicate data from.** Stitch will only be able to access the same projects as the user who creates the integration.

setup-steps:
  - title: "Create a {{ integration.display_name }} token"
    anchor: "create-access-token"
    content: |
      1. Sign into your GitLab account.
      2. Click the **user menu (your icon) > Settings**.
      3. Click the **Access Tokens** tab.
      4. In the **Name** field, enter `Stitch`. This will allow you to easily identify what application is using the token.
      5. In the **Scopes** section, check the **api** box. This will allow Stitch to access your API and replicate your GitLab data.
      6. Click **Create Personal Access Token**.
      7. The new Access Token will display at the top of the page. **Copy the token before navigating away from the page** - GitLab won't display it again.
  - title: "add integration"
    content: |
      4. In the **API URL** field, enter `https://gitlab.com/api/v3`
      5. In the **Private Token** field, paste the **Personal Access Token** you created in the previous section.
      6. In the **Projects to Track** field, enter the projects you want to track **separated by spaces**.

         For example: in an organization named `stitch`, there are two projects to track: `stitch-data` and `stitch-docs`. To track them, you'd enter them like this: `stitch/stitch-data stitch/stitch-docs`
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/gitlab
---
{% assign integration = page %}
{% include misc/data-files.html %}