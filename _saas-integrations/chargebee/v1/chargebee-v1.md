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

title: Chargebee
permalink: /integrations/saas/chargebee
keywords: chargebee, integration, schema, etl chargebee, chargebee etl, chargebee schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "chargebee"
display_name: "Chargebee"

singer: true 
tap-name: "Chargebee"
repo-url: https://github.com/singer-io/tap-chargebee

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "http://status.chargebee.com/"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Generate an API Key"
    anchor: "generate-api-key"
    content: |
      First, you'll generate a {{ integration.display_name }} API Key for Stitch. This will allow Stitch to read data from your {{ integration.display_name }} account using the {{ integration.display_name }} API.

      {% include layout/image.html type="right" file="/integrations/chargebee-create-api-key.png" max-width="450" %}
      1. Sign into your [{{ integration.display_name }} account](https://app.chargebee.com/login){:target="new"}.
      2. In the left sidenav, click **Settings > Configure {{ integration.display_name }}**.
      3. Click the **API keys and webhooks** button.
      4. On the API Keys page, click the **+ Add API Key** button. The **Create an API Key** modal will display.
      5. Select **Read-Only Key** as the API key type.
      6. Select **All** to define the API key's access. This will grant read-only access to your {{ integration.display_name }} site.
      7. In the **Name the API key** field, enter `Stitch`.
      8. Click **Create Key**.

      {{ integration.display_name }} will create the API key and redirect you back to the API Keys page:

      ![]({{ site.baseurl }}/images/integrations/chargebee-api-key.png)

      Copy the API key somwhere handy - you'll need it to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the API key you generated in [Step 1](#generate-api-key).
      5. In the **Site** field, enter the name of your {{ integration.display_name }} site. This can be found in the URL of your {{ integration.display_name }} site. For example: If the URL was `https://stitch.chargebee.com`, only `stitch` would be entered into this field.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/chargebee
---
{% assign integration = page %}
{% include misc/data-files.html %}