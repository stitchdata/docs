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
  [REST API v3](https://developer.surveymonkey.com/api/v3/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

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
  - title: "Retrieve your survey ID"
    anchor: "retrieve-survey-id"
    content: |
      1. Login to your your {{ integration.display_name }} and click on **My Surveys** on the upper left-hand portion of the screen.
      2. Select the survey that you want to replicate data from.
      3. Go to **Collect Responses** to access your survey link. If you don't currently have a link to your survey, continue to the next step. If you do, skip to step 5.

         ![{{ integration.display_name }} Collect Responses tab]({{ site.baseurl }}/images/integrations/surveymonkey-collect-responses.png){:style="max-width: 450px;"}
         {:start="4"}
      4. Click **Send Surveys Your Way** and then **Get Web Link**.
      5. The last portion of your survey URL is the survey ID. Keep this readily available.
         ![Survey URL containing the Survey ID.]({{ site.baseurl }}/images/integrations/surveymonkey-survey-id-weblink.png){:style="max-width: 450px;"}

  - title: "Obtain your access token"
    anchor: "obtain-access-token"
    content: |
      1. Login to your SurveyMonkey account on the [developer website](https://developer.surveymonkey.com/).
      2. Select **My Apps** on the upper menu panel.
      3. Click **Add a New App**.
      4. In the pop-up window, give your app a nickname, for example: Stitch Integration. Select **Private App**, and then click on the **Create App** button.

         ![Window to create your SurveyMonkey app.]({{ site.baseurl }}/images/integrations/surveymonkey-app-creation.png){:style="max-width: 400px;"}
         {:start="5"}
      5. You are now in your app. Click the **Settings** tab underneath your app's nickname.
      6. Scroll down to **Credentials** and you will find your access token. Keep this credential readily available for the integration.
         
         ![Your SurveyMonkey access token.]({{ site.baseurl }}/images/integrations/surveymonkey-access-token.png){:style="max-width: 600px;"}
         {:start="7"}
      7. To allow Stitch to access your survey information, you will need to give view permissions. Scroll down to the **Scope** section and you will see several scope requirements. **View Surveys**, **View Responses**, and **View Survey Details** are all required view permissions that Stitch needs. Click on each of those until it appears green and shows that it's required.

         ![SurveyMonkey app scope requirements]({{ site.baseurl }}/images/integrations/surveymonkey-scope-requirements.png){:style="max-width: 600px;"}
         {:start="8"}
      8. Click **Update Scopes**.

      **Note**: You do not need a paid SurveyMonkey account to have access to your access token, however without a paid account you will not be able deploy your app and it will be disabled in 90 days. You can contact SurveyMonkey at api-support@surveymonkey.com to request an extention.

  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI. EX:
      # 4. In the [FIELD_NAME] field, [instructions]
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