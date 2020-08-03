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

title: RingCentral (v1)
permalink: /integrations/saas/ringcentral
keywords: ringcentral, integration, schema, etl ringcentral, ringcentral etl, ringcentral schema
layout: singer
# input: false

key: "ringcentral-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ringcentral"
display_name: "RingCentral"

singer: true 
tap-name: "RingCentral"
repo-url: https://github.com/singer-io/tap-ringcentral

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.ringcentral.com/"

api-type: "platform.ringcentral"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

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
  - title: "Generate {{ integration.display_name }} credentials"
    anchor: "generate-credentials"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index}}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Create a {{ integration.display_name }} developer application"
        anchor: "create-developer-application"
        content: |
          In this step, you'll create a {{ integration.display_name }} developer application.

          
          1. Navigate to the [{{ integration.display_name }} Developer Console](https://developers.ringcentral.com/my-account.html#/applications){:target="new"}.
          2. Create a free account, if you don't already have one.
          3. After you've created an account and logged in, click the **Create App** button.
          {% include layout/image.html type="right" file="/integrations/ringcentral-app-settings.png" alt="RingCentral App Type & Platform window for creating a developer app." enlarge=true max-width="450" %}
          {:start="4"}
          4. In the window that displays, enter a name and description for the app.
          5. In the **App Type & Platform** window, fill in the fields as follows:
             - **Application Type**: Select **Private**.
             - **Platform Type**: Select **Server-only (No UI)**.
          6. Click **Next**.
          {% include layout/image.html type="right" file="/integrations/ringcentral-app-permissions.png" alt="RingCentral OAuth Settings window for creating a developer app." enlarge=true max-width="450" %}
          {:start="7"}
          7. Next, you'll grant permissions to the app. In the **Permissions Needed** field, select the following:
             - **Read Accounts**
             - **Read Call Log**
             - **Read Messages**
          8. Click **Create**.

      - title: "Retrieve application credentials"
        anchor: "retrieve-application-credentials"
        content: |
          After your application is created, you'll retrieve its credentials.

          1. On the **Apps** page, click the developer application you created in the previous step.
          2. Click the **Credentials** option in the menu on the left side of the page.
          {% include layout/image.html type="right" file="/integrations/ringcentral-app-credentials.png"  enlarge=true alt="RingCentral Application Credentials page with the Production Environment column highlighted." max-width="525" %}
          {:start="3"}
          3. In the **Application Credentials** section, locate the following in the **Production Environment** column:

             - **API Server URL**
             - **Client ID**
             - **Client Secret**

          Keep this page handy for now - you'll need it to complete the setup in Stitch.
  
  - title: "add integration"
    content: |
      4. In the **Client ID** field, enter the **Client ID** from [Step 1.2](#retrieve-application-credentials).
      5. In the **Client Secret** field, enter the **Client Secret** from [Step 1.2](#retrieve-application-credentials).
      6. In the **Username** field, enter the username for the {{ integration.display_name }} developer app. This is typically the phone number used to create the app.
      7. In the **Password** field, enter the password for the {{ integration.display_name }} developer app.
      8. In the **API URL** field, enter the **API Server URL** from [Step 1.2](#retrieve-application-credentials).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/ringcentral
---
{% assign integration = page %}
{% include misc/data-files.html %}