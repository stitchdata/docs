---
title: Doorbell.io
permalink: /integrations/saas/doorbell-io
keywords: doorbell.io, doorbell.io schema, doorbell.io data, etl doorbell.io, doorbell.io etl
summary: "Connection instructions and schema details for Stitch's Doorbell.io integration."
layout: singer
no-schema: true ## Prevents the Singer Table Schema include from running

key: "doorbell-io-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "doorbell-io"
display_name: "Doorbell.io"
singer: false
author: "Stitch"
author-url: https://www.stitchdata.com

this-version: ""

api: |
  [Stitch Import API]({{ link.import-api.getting-started | prepend: site.baseurl }}){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "import-api"
branded: true
setup-name: "Import API"

historical: "n/a"
frequency: "Continuous"
tier: "Free"
status-url: "http://status.doorbell.io/"
icon: /images/integrations/icons/doorbell-io.svg

table-selection: false
column-selection: false

anchor-scheduling: false
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration uses the {{ integration.api | flatify }} to send data from {{ integration.display_name }} to Stitch.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Locate your Stitch client ID"
    anchor: "locate-your-stitch-client-id"
    content: |
      To locate your client ID, look at the URL in your web browser when you're logged into Stitch:

      ![Stitch client ID in the web app URL]({{ site.baseurl }}/images/integrations/locate-client-id.png)

      Your client ID is the number between `client/` and `/pipeline`. In this example, the client ID is `100608`.

  - title: "add integration"
    content: |
      After you save the integration, Stitch will generate and display an API token. This will be used in the next step to authenticate with {{ integration.display_name }}.

      **Note**: Stitch will only display this token once, so be sure to copy it before closing the page. Otherwise, you'll need to generate a new token.

  - title: "Add your API token to {{ integration.display_name }}"
    anchor: "add-api-token-to-doorbell-io"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/doorbell-io-setup.png" alt="Entering Stitch API credentials in Doorbell.io" max-width="500px" %}
      1. Sign into your Doorbell.io account.
      2. Click the application you want to connect to Stitch.
      3. On the application's homepage, click the Setup (gear) icon near the top-right corner of the page.
      4. On the **Setup** page, click the **Backup/Export** option from the menu on the left.
      5. In the **Client ID** field, enter your Stitch client ID.
      6. In the **API Token** field, paste the API token you generated in [Step 2](#add-stitch-data-source).
      7. Click **Connect**.
      

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/doorbell.io
---
{% assign integration = page %}
{% include misc/data-files.html %}
