---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Bronto
permalink: /integrations/saas/bronto
tags: [saas_integrations]
keywords: bronto, integration, schema, etl bronto, bronto etl, bronto schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "bronto"
display_name: "Bronto"
singer: true 
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-bronto

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Stitch-supported integration

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: 
icon: /images/integrations/icons/bronto.svg
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A valid and active API token with Read permissions**

# From Bronto's docs (though this doesn't all seem super relevant):
# http://dev.bronto.com/gettingstarted/soap-how-to-get-started/how-to-access-the-api/
# Account must have the API feature enabled
# Must have at least one API token created
#    - Create API tokens from an administrator account, and specify access on them
# What permissions? Access Type: Read is all we need
# Click "Add Access Token" and type in a name
# Under Permissions & Settings, Select "Read", and ensure that "Token is active?" is checked

# Go to Home->Settings->Data Exchange in the Bronto application

requirements-info:

setup-steps:
  - title: "Create a {{ integration.display_name }} API token"
    anchor: "create-access-token"
    content: |
      1. Sign into your Bronto account as an Administrator.
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

