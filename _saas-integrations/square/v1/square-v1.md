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

title: Square (v1)
permalink: /integrations/saas/square
keywords: square, integration, schema, etl square, square etl, square schema
layout: singer
# input: false

key: "square-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "square"
display_name: "Square"

singer: true
status-url: "http://issquareup.com/"

tap-name: "Square" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-square

this-version: "1"

api: |
  [{{ integration.display_name }} V2 and Connect V1 APIs](https://developer.squareup.com/reference/square){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.square"

anchor-scheduling: true
cron-scheduling: true

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
      **To log into your {{ integration.display_name }} sandbox environment, if you're connecting a sandbox.** To allow Stitch to successfully access the sandbox, you must be logged into it prior to setting up the {{ integration.display_name }} integration in Stitch. 
      
      **If you're connecting a production environment**, start with [Step 2](#add-stitch-data-source) of this guide.

setup-steps:
  - title: "Login to your {{ integration.display_name }} sandbox environment"
    anchor: "sandbox-environment"
    content: |
      {% capture skip-step %}
      **Note**: If you're connecting a {{ integration.display_name}} sandbox, this step is required. Skip to [step 2](#add-stitch-data-source) if you're connecting a production environment.
      {% endcapture %}

      {% include important.html type="single-line" content=skip-step %}

      To connect to your {{ integration.display_name }} sandbox environment, you'll need to login to your sandbox environment before completing the next step. This is required to grant Stitch authorization to access the sandbox environment. For more info, refer to the [{{ integration.display_name }} documentation](https://developer.squareup.com/docs/oauth-api/walkthrough#33-test-your-authorization-flow){:target="new"}.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Check the **Connect to a sandbox environment** if choosing to connect to your {{ integration.display_name }} sandbox. **Note**: Make sure you completed [Step 1](#sandbox-environment) before continuing.
      
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorizing Stitch to Access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to {{ integration.display_name }}'s website to complete the setup.

      1. Enter your {{ integration.display_name }} credentials and click **Login**.
      2. After the authorization process successfully completes, you'll be redirected back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.
      
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/square/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
