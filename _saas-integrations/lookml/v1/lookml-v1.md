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

title: LookML (v1)
permalink: /integrations/saas/lookml ## Add if there are multiple versions: /vVERSION
keywords: lookml, integration, schema, etl lookml, lookml etl, lookml schema
layout: singer
# input: false

key: "lookml-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "lookml"
display_name: "LookML"

singer: true
status-url: "https://www.githubstatus.com/"

tap-name: "LookML" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-lookml

this-version: "1"

api: |
  [GitHub v3 API](https://docs.github.com/en/rest){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.lookml"

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

requirements-list:
  - item: |
      **Access to the projects you want to replicate data from.** Stitch will only be able to access the same projects as the user who creates the access token.


setup-steps:
  - title: "Create access token"
    anchor: "create-access-token"
    content: |
      1. Sign into your GitHub account.
      2. Click the **User menu (your icon) > Settings**.
      3. Click **Developer settings** in the navigation on the left side of the page.
      4. Click **Personal access tokens**.
      5. On the Personal access tokens page, click the **Generate a personal access token** button. If prompted, enter your password.
      7. In the **Description** field, enter `stitch`. This will allow you to easily idenfiy what application is using the token.
      8. In the **Select Scopes** section, check the **repo** option:

         ![Highlighted repo scopes on the GitHub Personal Access Tokens page]({{ site.baseurl }}/images/integrations/github-token-scopes.png)

         **Note**: While these are full permissions, Stitch will only ever read your data. The **repo** scope is required due to how GitHub structures permissions.
      9. Click the **Generate token** button.
      10. The new access token will display on the next page. **Copy the token before navigating away from the page** - GitHub won't display it again.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Token** field, paste the access token you copied from [step 1](#create-access-token).
      5. In the **Git Owner** field, enter the Git Owner of the repositories you want to replicate. You can find this info in the URL of the repositories. For example, the Git Owner of `https://github.com/stitch/stitch-repo` would be `stitch`. Keep in mind that you can only replicate data from one Git Owner per Stitch {{ integration.display_name }} integration.
      6. In the **Git Repositories** field, enter the repositories you want to replicate. You can find this info in its URL. For example, the repository of `https://github.com/stitch/stitch-repo` would be `stitch-repo`. The repositories must be comma-delimited if replicating multiple repositories. Ex: `repo-1, repo-2`."

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
# Each table has a its own .md file in /_integration-schemas/lookml


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}