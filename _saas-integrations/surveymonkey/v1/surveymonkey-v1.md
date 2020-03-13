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
  - title: "Retrieve your survey ID"
    anchor: "retrieve-survey-id"
    content: |
      1. Login to your {{ integration.display_name }} and click on **My Surveys** on the upper left-hand portion of the screen.
      2. Select the survey that you want to replicate data from.
      3. Go to **Collect Responses** to access your survey link. If you don't currently have a link to your survey, continue to the next step. If you do, skip to step 5.

         ![{{ integration.display_name }} Collect Responses tab]({{ site.baseurl }}/images/integrations/surveymonkey-collect-responses.png){:style="max-width: 450px;"}
         {:start="4"}
      4. Click **Send Surveys Your Way** and then **Get Web Link**.
      5. The last portion of your survey URL is the survey ID. Keep this readily available.
         ![Survey URL containing the Survey ID.]({{ site.baseurl }}/images/integrations/surveymonkey-survey-id-weblink.png){:style="max-width: 450px;"}

  - title: "Create a {{ integration.display_name }} app"
    anchor: "app-creation"
    content: |
      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Obtain your access token"
        anchor: "obtain-access-token"
        content: |
          1. Login to your {{ integration.display_name }} account on the [developer website](https://developer.surveymonkey.com/).
          2. Select **My Apps** on the upper menu panel.
          3. Click **Add a New App**.
          4. In the pop-up window, give your app a nickname, for example: Stitch Integration. Select **Private App**, and then click on the **Create App** button.

             ![Window to create your SurveyMonkey app.]({{ site.baseurl }}/images/integrations/surveymonkey-app-creation.png){:style="max-width: 400px;"}
             {:start="5"}
          5. You are now in your app. Click the **Settings** tab underneath your app's nickname.
          6. Scroll down to **Credentials** and you will find your access token. Keep this credential readily available for the integration.
             
             ![Your SurveyMonkey access token.]({{ site.baseurl }}/images/integrations/surveymonkey-access-token.png){:style="max-width: 600px;"}

      - title: "Grant scopes (permissions)"
        anchor: "grant-scopes-permissions"
        content: |
          {% include layout/image.html file="/integrations/surveymonkey-scope-requirements.png" type="right" max-width="450" %}
          To allow Stitch to access your survey information, you will need to give view permissions. Scroll down to the **Scope** section and click on the following scopes:

          - **View Surveys**
          - **View Responses**
          - **View Survey Details**

          The scopes will turn green and show as `Required`.
          
          Click **Update Scopes**.

      - title: "Deploy your app"
        anchor: "deploy-app"
        content: |
          {% capture first-line %}**Free {{ integration.display_name }} users and auto-disabling apps**{% endcapture %}

          {% capture paid-account-content %}
          Deplying your {{ integration.display_name }} app is necessary to prevent the app from being auto-disabled by {{ integration.display_name }}. Only paid {{ integration.display_name }} accounts have the ability to deploy apps.

          **Undeployed apps are disabled by {{ integration.display_name }} 90 days from their creation.** 

          If you don't have a paid {{ integration.display_name }} account, you can still use your access token to set up the integration in Stitch, but {{ integration.display_name }} will auto-disable your app after 90 days. If your app is is disabled, contact SurveyMonkey at **api-support@surveymonkey.com** to request an extension.
          {% endcapture %}

          {% include note.html first-line=first-line content=paid-account-content %}
          
          If you have a paid {{ integration.display_name }} account, scroll back up to the top of this web page and click **Deploy** in the upper right section:

          ![Deploy button on the SurveyMonkey app Settings page]({{ site.baseurl }}/images/integrations/surveymonkey-deploy-app.png){:style="max-width: 450px"}

  - title: "add integration"
    content: |
      4. In the **Access Token** field, add your access token that you obtained in [Step 2.1](#obtain-access-token).
      5. In the **Survey Id** field, add your survey ID that you retrieved in [Step 1](#retrieve-survey-id).
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