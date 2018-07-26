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

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "In Development"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: 
whitelist:
  tables: true
  columns: false

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
          The API client will display on the page after it's created. In the image below the **Client ID** and **Client Secret** are highlighted:

          ![UserVoice UI with highlighted API client ID and client secret fields]({{ site.baseurl }}/images/integrations/uservoice-api-credentials.png)

          Leave this page open for now - you'll need it to complete the next step in Stitch.

  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} Subdomain** field, enter your {{ integration.display_name }} subdomain. For example: If the full subdomain were `stitch.{{ integration.name }}.com`, you'd enter `stitch` into this field.
      5. In the **{{ integration.display_name }} Client ID** field, enter the API client name. This is what you entered in the **Name** field when [creating the API client in {{ integration.display_name }}](#create-stitch-api-client).
      6. In the **{{ integration.display_name }} Client Secret** field, paste the API client secret.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/uservoice

schema-sections:
  - title: ""
    anchor: ""
    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}