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

title: SurveyMonkey
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
tier: "Free"

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
  - title: "Retrieve your access token and Survey ID"
    anchor: "retrieve-access-token-and-survey-id"
    content: |

      {% capture first-line %}**Enterprise {{ integration.display_name }} account required**{% endcapture %}

      {% capture paid-account-content %}
      An Enterprise {{ integration.display_name }} account is required to install the Stitchdata ETL app and retrieve the access token and survey id required for this installation. 
      {% endcapture %}

      {% include note.html first-line=first-line content=paid-account-content %}

      1. Login to your {{ integration.display_name }} and go to [App Directory](https://www.surveymonkey.com/apps).
      2. Type in **stitchdata** in the search input box to find the Stitchdata ETL app. 
      3. Click **Visit Site** button on the right. 
      4. Click **Authorize** button.
      5. The access token and the list of surveys are shown after authorization. Keep this readily available. Note: You may come back at any time to retrieve your access token or identify a new survey id.
       
        ![Access token and the list of Survey IDs.]({{ site.baseurl }}/images/integrations/surveymonkey-access-token.png){:style="max-width: 450px;"}


  - title: "add integration"
    content: |
      4. In the **Access Token** field, add your access token that you obtained in [Step 1](#retrieve-access-token-and-survey-id).
      5. In the **Survey Id** field, add your survey ID that you retrieved in [Step 1](#retrieve-access-token-and-survey-idd).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/surveymonkey/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}