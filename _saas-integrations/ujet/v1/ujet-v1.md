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

title: UJET (v1)
permalink: /integrations/saas/ujet
keywords: ujet, integration, schema, etl ujet, ujet etl, ujet schema
layout: singer
# input: false

key: "ujet-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ujet"
display_name: "UJET"

singer: true
status-url: ""

tap-name: "UJET"
repo-url: https://github.com/singer-io/tap-ujet

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://support.ujet.co/hc/en-us/articles/115006908127-UJET-Data-API#h_7d95eafc-6c02-446b-bcc6-b733f4e1143e){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.ujet"

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
#      Setup Instructions    #
# -------------------------- #
requirements-list:
  - item: "A {{ integration.display_name }} account with **admin privileges**. You need this privilege to retrieve the information required for the Stitch integration."

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} company credentials"
    anchor: "retrieve-keys"
    content: |
      1. Login to your {{ integration.display_name }} Console.
      2. Click on **Settings > Developer Settings**.
      3. In the **Agent Platform** section, click on the {{ integration.display_name }} bubble.
      4. Click **Save Changes**.
      4. Your **Company Key** and **Company Secret Code** will display. Keep these available to complete your setup in Stitch.
         ![Your UJET Company and Company Secret Key.]({{ site.baseurl }}/images/integrations/ujet-company-keys.png){:style="max-width: 550px;"}

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Company Key** field, enter the Company Key that you retrieved in [Step 1](#retrieve-keys).
      5. In the **Company Secret** field, enter the Company Secret Code that you retrieved in [Step 1](#retrieve-keys).
      6. In the **Domain Field** field, your {{ integration.display_name }} domain. This will usually be `ujet`, but if you are unsure, check your welcome email from {{ integration.display_name }}.
      7. In the **Subdomain** field, enter the subdomain of your {{ integration.display_name }} account's URL. For example: The subdomain for `stitch.ujet.com` would be `stitch`.
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
# Each table has a its own .md file in /_integration-schemas/ujet/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
