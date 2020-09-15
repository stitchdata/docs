---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Bronto (v1)
permalink: /integrations/saas/bronto
keywords: bronto, integration, schema, etl bronto, bronto etl, bronto schema
summary: "Connection instructions, replication info, and schema details for Stitch's Bronto integration."
layout: singer

key: "bronto-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "bronto"
display_name: "Bronto"

singer: true 
repo-url: https://github.com/singer-io/tap-bronto

this-version: "1"

api: |
  [{{ integration.display_name }} SOAP API](https://help.bronto.com/bmp/concept/c_api_soap_intro.html){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.bronto"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false

extraction-logs: true
loading-reports: true

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
      **Admin permissions in Bronto.** This is required to create an API token.

setup-steps:
  - title: "Create a {{ integration.display_name }} API token"
    anchor: "create-access-token"
    content: |
      {% include note.html type="single-line" content="**Note**: You need Administrator permissions in Bronto to complete this step." %}
      
      1. Sign into your Bronto account.
      2. Navigate to **Home > Settings**.
      3. Click **Data Exchange** in the left side menu.
      4. Under **SOAP API Tokens**, click the **Add Access Token** button.
      5. In the **API Token Name** field, enter `Stitch`. This will allow you to easily identify what application is using the token.
      6. Click the checkbox next to **Read** to allow read access for this token.
      7. Ensure that the checkbox next to **Token is active?** is checked, and click **Save**.
      8. The access token will appear on the page under the name `Stitch` once the modal closes. Copy this to be used in setting up the connection from within the Stitch application.
  - title: "add integration"
    content: |
      4. In the **Bronto API Token** field, paste the access token you created in Step 1.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/bronto
---
{% assign integration = page %}
{% include misc/data-files.html %}