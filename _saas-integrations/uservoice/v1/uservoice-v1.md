---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: UserVoice (v1.0)
permalink: /integrations/saas/uservoice
tags: [saas_integrations]
keywords: uservoice, integration, schema, etl uservoice, uservoice etl, uservoice schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "uservoice"
display_name: "UserVoice"
singer: true 
repo-url: https://github.com/singer-io/tap-uservoice

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: https://status.uservoice.com/

table-selection: true
column-selection: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to Settings in your {{ integration.display_name }} account.** This is required to generate API credentials for Stitch."

setup-steps:
  - title: "Generate {{ integration.display_name }} API credentials"
    anchor: "generate-uservoice-api-credentials"
    substeps:
      - title: "Create a Stitch {{ integration.display_name }} API client"
        anchor: "create-stitch-api-client"
        content: |
          {% include layout/inline_image.html type="right" file="integrations/uservoice-create-api-client.png" alt="Add API key window in UserVoice" max-width="400px" %}

          1. Sign into your {{ integration.display_name }} account.
          2. Click **Settings**, which is in the bottom left corner.
          3. Click **Integrations**.
          4. Click **{{ integration.display_name }} API keys**.
          5. Click the **Add API key** button.
          6. In the window that displays, fill in the fields as follows:
             - **Name** - Enter a name for the API client. For example: `stitch`
             - **Trusted** - Check the checkbox.
          7. When finished, click the **Add API key** to create the API client.

      - title: "Locate API credentials"
        anchor: "locate-api-credentials"
        content: |
          The API client will display on the page after it's created. In the image below the **API key** and **API Secret** are highlighted:

          ![UserVoice UI with highlighted API key and API secret fields]({{ site.baseurl }}/images/integrations/uservoice-api-credentials.png)

          Leave this page open for now - you'll need it to complete the next step in Stitch.

  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} Subdomain** field, enter your {{ integration.display_name }} subdomain. For example: If the full subdomain were `stitch.{{ integration.name }}.com`, you'd enter `stitch` into this field.
      5. In the **{{ integration.display_name }} API Key** field, paste your {{ integration.display_name }} API key.
      6. In the **{{ integration.display_name }} API Secret** field, paste the API secret.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/uservoice
---
{% assign integration = page %}
{% include misc/data-files.html %}