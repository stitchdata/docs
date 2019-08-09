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

title: Pipedrive (v1)
permalink: /integrations/saas/pipedrive
keywords: pipedrive, integration, schema, etl pipedrive, pipedrive etl, pipedrive schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pipedrive"
display_name: "Pipedrive"

singer: true 
tap-name: "Pipedrive"
repo-url: https://github.com/singer-io/tap-pipedrive

this-version: "1.0"

api: |
  [{{ integration.display_name }} REST API](https://developers.pipedrive.com/docs/api/v1/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "http://status.pipedrive.com/"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

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
      **Admin permissions in {{ integration.display_name }}.** These permissions are required to ensure Stitch can successfully replicate your {{ integration.display_name }} data.

setup-steps:
  - title: "Create a {{ integration.display_name }} user for Stitch"
    anchor: "create-pipedrive-user"
    content: |
      To ensure Stitch can access and replicate all your data, the {{ integration.display_name }} credentials you use to connect to Stitch need **Admin permissions**. We recommend that you [create a separate {{ integration.display_name }} Admin user for Stitch](http://support.pipedrive.com/hc/en-us/articles/207319685-How-to-add-edit-remove-a-user){:target="new"}, but this isn’t mandatory to use the integration. Creating a user for us simply makes our activity easier to distinguish in logs and audits.

      **If you don’t want to create a user for us**, simply ensure that the credentials you use to connect to Stitch have Admin permissions. If the API token associated with a non-Admin user is used to set up the integration, Stitch may be unable to access and replicate all of your data.

      **Note**: Users are counted at the account-level in {{ integration.display_name }}, not the company level. If you want to create a user for us and are concerned about the cost of your {{ integration.display_name }} subscription, don’t worry - you won’t be charged twice.

  - title: "Retrieve your {{ integration.display_name }} API token"
    anchor: "retrieve-pipedrive-api-token"
    content: |
      1. If you created a {{ integration.display_name }} user for Stitch, sign into {{ integration.display_name }} as the Stitch user.

         If you didn’t, sign into {{ integration.display_name }} as an Admin user.
      2. Click the **user menu** (where your avatar is) in the top right corner of the screen.
      3. Click **Settings**.
      4. In the settings menu, click **API**.
      5. The user’s API Token will display:

         ![Personal API token in the Pipedrive app]({{ site.baseurl }}/images/integrations/pipedrive-api-token.png)

      Leave this page open for now - you'll need it to complete the setup in Stitch.

  - title: "Connect multiple {{ integration.display_name }} companies"
    anchor: "connect-multiple-companies"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you aren't connecting multiple Pipedrive companies." %}
      If you want to connect more than one {{ integration.display_name }} company to Stitch, you’ll have to repeat the entire process in this article for every company you want to add. Essentially, you’ll have to create a separate {{ integration.display_name }} integration for each company.

      Our {{ integration.display_name }} integration uses an API Token to authenticate. **{{ integration.display_name }} API tokens are unique not only at the user level, but the company level as well**. This means that a user’s API Token will vary from company to company, even if everything is housed in the same {{ integration.display_name }} account.

  - title: "add integration"
    content: |
      4. In the **API Token** field, paste the API token you retrieved in [Step 2](#retrieve-pipedrive-api-token).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pipedrive
---
{% assign integration = page %}
{% include misc/data-files.html %}