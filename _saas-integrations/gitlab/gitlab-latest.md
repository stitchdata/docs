---
title: GitLab (v1)
permalink: /integrations/saas/gitlab
keywords: gitlab, integration, schema, etl gitlab, gitlab etl, gitlab schema
summary: "Connection instructions and schema details for Stitch's GitLab integration."
layout: singer

key: "gitlab-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "gitlab"
display_name: "GitLab"

singer: true
repo-url: https://github.com/singer-io/tap-gitlab

this-version: "1"

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

api-type: "platform.gitlab"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false

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
      6. In the **Projects** and **Groups to Track** fields, you'll enter the projects and/or groups you want to track as a **space-separated** list.

         For example: `stitchdata/group-a`, or `stitchdata/project-a stitchdata/project-b`

         **Note**: A value for one of these fields must be provided. Additionally, the way you define these settings determines how some data is replicated:

         - If **groups** are provided but **projects** aren't, all group projects will be replicated.
         - If **groups** and **projects** are provided, the selected projects of the listed groups will be replicated.
         - If **projects** are provided but **groups** aren't, all listed projects will be replicated.

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