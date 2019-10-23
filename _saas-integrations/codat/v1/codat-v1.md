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

title: Codat
permalink: /integrations/saas/codat
keywords: codat, integration, schema, etl codat, codat etl, codat schema
layout: singer
# input: false

key: "codat-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "codat"
display_name: "Codat"

singer: true 
tap-name: "Codat"
repo-url: https://github.com/singer-io/tap-codat

this-version: "1.0"

api: |
  [{{ integration.display_name }} API](https://docs.codat.io/docs){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.codat.io/"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator or Developer privileges in {{ integration.display_name }}.** These are required to generate an API key. Refer to [{{ integration.display_name }}'s documentation](https://docs.codat.io/reference/authentication){:target="new"} for more info.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API key"
    anchor: "retrieve-codat-api-key"
    content: |
      {% include note.html type="single-line" content="**Note**: This step requires Administrator or Developer privileges in Codat." %}

      1. Sign into your {{ integration.display_name }} account.
      2. Click **Accounts > Profile** in the sidenav.
      3. On the **Manage Profile** page, locate the **API Key** field.
      4. Click the copy icon to copy the API key.

      Paste the API key somewhere handy - you'll need it in the next step.
      
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the {{ integration.display_name }} API key you generated in [Step 1](#generate-codat-api-key).
      5. Check the **Use Codat UAT environment** box if you're connecting to your UAT (sandbox) environment in {{ integration.display_name }}.

         **Note**: Use this setting only if you are connecting to a UAT (sandbox) {{ integration.display_name }} instance. Checking this box when the instance isn't a sandbox will prevent a successful connection and `401 Bad Credentials` errors in the connection check logs.
# This is the error from the logs:
# 2019-05-30 13:53:49,162Z    tap - INFO HTTP request to "companies" endpoint took 0.329s, returned status code 401
# 2019-05-30 13:53:49,163Z    tap - CRITICAL 401 Client Error: Bad Credentials for url: https://api.codat.io/companies
# 2019-05-30 13:53:49,164Z    tap - requests.exceptions.HTTPError: 401 Client Error: Bad Credentials for url: https://api.codat.io/companies
# 2019-05-30 13:53:49,183Z   main - INFO Tap exited abnormally with status 1
# 2019-05-30 13:53:49,184Z   main - INFO Exit status is: Discovery failed with code 1 and error message: "401 Client Error: Bad Credentials for url: https://api.codat.io/companies".

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/codat
---
{% assign integration = page %}
{% include misc/data-files.html %}