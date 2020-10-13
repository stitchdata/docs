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

title: SurveyMonkey (v1)
permalink: /integrations/saas/surveymonkey
keywords: surveymonkey, integration, schema, etl surveymonkey, surveymonkey etl, surveymonkey schema
layout: singer
# input: false

key: "surveymonkey-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "surveymonkey"
display_name: "SurveyMonkey"

singer: true
status-url: "https://developer.surveymonkey.com/tools/api_status/"

tap-name: "SurveyMonkey"
repo-url: https://github.com/singer-io/tap-surveymonkey

this-version: "1"

api: |
  [{{ integration.display_name }} REST API v3](https://developer.surveymonkey.com/api/v3/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.surveymonkey"

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

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
      **An Enterprise {{ integration.display_name }} account.** This is required to complete the setup in {{ integration.display_name }}.

setup-steps:
  - title: "Retrieve your access token and Survey ID"
    anchor: "retrieve-access-token-and-survey-id"
    content: |
      {% capture paid-account-content %}
      **Note**: An Enterprise {{ integration.display_name }} account is required to complete this step. 
      {% endcapture %}

      {% include note.html type="single-line" content=paid-account-content %}

      1. Login to your {{ integration.display_name }} and go to [App Directory](https://www.surveymonkey.com/apps){:target="new"}.
      2. Type `stitchdata` in the search input box to find the Stitchdata ETL app. 
      3. Click the **Visit Site** button on the right side of the page. 
      4. Click the **Authorize** button.
      5. The access token and list of surveys are shown after authorization:
       
         ![Access token and the list of Survey IDs.]({{ site.baseurl }}/images/integrations/surveymonkey-access-token.png){:style="max-width: 450px;"}

      Leave this page open - you'll need it in the next step. **Note**: You may come back at any time to retrieve your access token or identify a new survey ID.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Access Token** field, add your access token that you obtained in [Step 1](#retrieve-access-token-and-survey-id).
      5. In the **Survey Id** field, add your survey ID that you retrieved in [Step 1](#retrieve-access-token-and-survey-id).
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/surveymonkey/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
