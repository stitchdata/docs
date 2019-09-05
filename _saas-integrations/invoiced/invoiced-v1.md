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

title: Invoiced
permalink: /integrations/saas/invoiced
keywords: invoiced, integration, schema, etl invoiced, invoiced etl, invoiced schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "invoiced"
display_name: "Invoiced"

singer: true 
tap-name: "Invoiced"
repo-url: https://github.com/singer-io/tap-invoiced

# this-version: "1.0"

api: |
  [{{ integration.display_name }} REST API](https://invoiced.com/docs/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://www.invoicedstatus.com/"

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

setup-steps:
  - title: "Generate an {{ integration.display_name }} API key"
    anchor: "generate-api-key"
    content: |
      1. [Sign into your {{ integration.display_name }} account](https://dashboard.invoiced.com/login){:target="new"}.
      2. Click **Settings** on the left side of the page.
      3. In the **Business Settings** section, click **Developers**.
      4. On the Developers page, click the **New API Key** button. A **New API Key** window will display.
      5. In the **Key Description** field, enter a description that identifies the API key. For example: `Stitch`
      6. Click **Save**. This will direct you back to the Developers page after the API key is created.
      7. A section for the new API key will display on the Developers page. Click the **Show Secret** link next to the name of the API key to display it:

         ![A highlighted API key field on the Developers page in the Invoiced app]({{ site.baseurl }}/images/integrations/invoiced-api-key.png)

      Leave this page open for now - you'll need it to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **API Key** field, paste your {{ integration.display_name }} API key.
      5. If the {{ integration.display_name }} instance you're connecting to is a sandbox, check the **Is this a sandbox connection?** box.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/invoiced
---
{% assign integration = page %}
{% include misc/data-files.html %}