---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: GitHub (v1.0)
permalink: /integrations/saas/github
keywords: github, integration, schema, etl github, github etl, github schema
summary: "Connection instructions, replication info, and schema details for Stitch's GitHub integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "github"
display_name: "GitHub"

singer: true
repo-url: https://github.com/singer-io/tap-github

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: https://status.github.com/messages

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A valid access token which allows access to any projects you want to replicate data from.** Stitch will only be able to access the same projects as the user who creates the access token.

setup-steps:
  - title: "Create a {{ integration.display_name }} token"
    anchor: "create-access-token"
    content: |
      1. Sign into your GitHub account.
      2. Click the **User menu (your icon) > Settings**.
      3. Click **Developer settings** in the navigation on the left side of the page.
      4. Click **Personal access tokens**.
      5. On the Personal access tokens page, click the **Generate new token** button. If prompted, enter your password.
      7. In the **Description** field, enter `stitch`. This will allow you to easily idenfiy what application is using the token.
      8. Click the **Generate token** button.
      9. The new access token will display on the next page. **Copy the token before navigating away from the page** - GitHub won't display it again.
  - title: "add integration"
    content: |
      4. In the **GitHub Access Token** field, paste the access token you created in the Step 1.
      5. In the **GitHub Repository Name** field, enter the paths of the repositories you want to track. The path is relative to `https://github.com`. For example: The path for the Stitch Docs repository is `stitchdata/docs`

         To track multiple repositories, enter a space delimited list of the repository paths. For example: `stitchdata/docs stitchdata/docs-about-docs`

         **Note**: At this time, only one repository may be tracked per integration. To track multiple repositories, you'll need to create additional GitHub integrations in your Stitch account.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/github

---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}
