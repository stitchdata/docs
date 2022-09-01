---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: GitHub (v1)
permalink: /integrations/saas/github/v1
keywords: github, integration, schema, etl github, github etl, github schema
summary: "Connection instructions, replication info, and schema details for Stitch's GitHub integration."
layout: singer
input: false

key: "github-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "github"
display_name: "GitHub"

singer: true
repo-url: https://github.com/singer-io/tap-github

this-version: "1"

api: |
  [{{ integration.display_name }} REST API v3](https://developer.github.com/v3/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: https://status.github.com/messages

api-type: "platform.github"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

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
      **Access to the projects you want to replicate data from.** Stitch will only be able to access the same projects as the user who authorizes the connection in Stitch.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      5. In the **GitHub Repository Name** field, enter the paths of the repositories you want to track. The path is relative to `https://github.com`. For example: The path for the Stitch Docs repository is `stitchdata/docs`

         To track multiple repositories, enter a space delimited list of the repository paths. For example: `stitchdata/docs stitchdata/docs-about-docs`

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch-access"
    content: |
      1. Once you've configured the integration parameters, click **Authorize**. You will be prompted to grant Stitch access to your {{ integration.display_name }} account.
      2. Sign in to {{ integration.display_name }}.
      3. If you want to replicate data from private repositories, click **Request** next to the name of the relevant {{ integration.display_name }} organization, then click **Request approval from owners**. The owners of the repository will then receive an email prompting them to approve or deny the request.
      
          **Note**: This step is not needed if you only want to access public repositories. Any public repository, even within your work organization, should be available without approval from the owners.

          ![GitHub authorization screen]({{ site.baseurl }}/images/integrations/github-oauth.png)
      4. Click **Authorize singer-bot**.

      Once the authorization process is completed, you will be redirected to Stitch. You will be able to start replicating data from public repositories. The extraction from private repositories will fail until the owner has approved the access request.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/github

---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}