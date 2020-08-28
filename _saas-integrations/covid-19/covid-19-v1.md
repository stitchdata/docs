---

# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: COVID-19 Public Data
permalink: /integrations/saas/covid-19
keywords: public health, coronavirus, covid, github schema
layout: singer
# input: false

key: "covid-19-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "covid-19"
display_name: "COVID-19 public data"

singer: true
status-url: https://status.github.com/messages

tap-name: "COVID-19"
repo-url: https://github.com/singer-io/tap-covid-19

this-version: "1"

api: |
  [GitHub REST API v3](https://developer.github.com/v3/){:target="new"}


# ---------------------------- #
#       Stitch Details       #
# ---------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.covid-19"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

setup-name: "COVID-19"


# --------------------------------- #
#      Feature Summary       #
# --------------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration was developed in a collaboration between [Bytecode](https://bytecode.io/){:target="new"} and [Talend](https://www.talend.com/){:target="new"}. It replicates data from multiple public data sources using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# ------------------------------- #
#      Setup Instructions    #
# ------------------------------- #

requirements-list:
  - item: |
      **A regular (free) GitHub account.** The GitHub repo for this integration is public - no special access is required.


setup-steps:
  - title: "Create a GitHub personal access token"
    anchor: "create-access-token"
    content: |
      1. Sign into your GitHub account.
      2. Click the **User menu (your icon) > Settings**.
      3. Click **Developer settings** in the navigation on the left side of the page.
      4. Click **Personal access tokens**.
      5. On the Personal access tokens page, click the **Generate new token** button. If prompted, enter your password.
      7. In the **Description** field, enter `stitch`. This will allow you to easily identify what application is using the token.
      8. In the **Select Scopes** section, check the **repo** option:

         ![Highlighted repo scopes on the GitHub Personal Access Tokens page]({{ site.baseurl }}/images/integrations/github-token-scopes.png)

         **Note**: While these are full permissions, Stitch will only ever read your data. The **repo** scope is required due to how GitHub structures permissions.
      9. Click the **Generate token** button.
      10. The new access token will display on the next page. **Copy the token before navigating away from the page** - GitHub won't display it again.

  - title: "add integration"
    content: |
      4. In the **GitHub Access Token** field, paste the access token you created in [Step 1](#create-access-token).

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# ------------------------------ #
#     Integration Tables     #
# ------------------------------ #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/covid-19
---
{% assign integration = page %}
{% include misc/data-files.html %}