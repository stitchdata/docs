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

title: UJET
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
tier: "Free"

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
  - A {{ integration.display_name }} account with **admin privileges**. You need this privilege to retrieve the information required for the Stitch integration.

setup-steps:
  - title: "Retrieve your company and company secret keys"
    anchor: "retrieve-keys"
    content: |
      1. Login to {{ integration.display_name }} Console.
      2. Click on **Settings** to open its dropdown menu, and then click on **Developer Settings**.
      3. In the **Agent Platform** section, click on the {{ integration.display_name }} bubble, save your changes, and then you'll see your **Company Key** and **Company Secret Code**. Keep these available to complete your setup in Stitch.
         ![Your UJET Company and Company Secret Key.]({{ site.baseurl }}/images/integrations/ujet-company-keys.png){:style="max-width: 550px;"}

  - title: "add integration"
    content: |
      4. In the **Company Key** field, enter your Company Key that you retrieved in [step 1](#retrieve-keys).
      5. In the **Company Secret** field, enter your Company Secret Code that you retrieved in [step 1](#retrieve-keys).
      6. In the **Domain Field** field, enter `ujet`, as this is the domain of your {{ integration.display_name }} account URL.
      7. In the **Subdomain** field, enter the subdomain of your {{ integration.display_name }} account's URL.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/ujet/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}