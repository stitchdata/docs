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

title: BigCommerce (v1)
permalink: /integrations/saas/bigcommerce
keywords: bigcommerce, integration, schema, etl bigcommerce, bigcommerce etl, bigcommerce schema
summary: "Connection instructions, replication info, and schema details for Stitch's BigCommerce integration."
layout: singer
# input: false

key: "bigcommerce-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "bigcommerce"
display_name: "BigCommerce"

singer: true 
tap-name: "BigCommerce"
repo-url: https://github.com/singer-io/tap-bigcommerce

api: |
  [{{ integration.display_name }} REST API](https://developer.bigcommerce.com/){:target="new"}

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "https://status.bigcommerce.com/"

api-type: "platform.bigcommerce"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Store owner privileges in {{ integration.display_name }}.** This is required to create an API account, which will generate {{ integration.display_name }} API credentials. In {{ integration.display_name }}, [only store owners can create API accounts](https://developer.bigcommerce.com/api-docs/getting-started/authentication){:target="new"}.

setup-steps:
  - title: "Generate {{ integration.display_name }} API credentials"
    anchor: "generate-bigcommerce-api-credentials"
    content: |
      In this step, you'll create an API account and generate read-only API credentials for the {{ integration.display_name }} store you want to connect to Stitch.

      {% for substep in step.substeps %}
      - [Step {{ section-step-number | strip }}.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Create an API account for the store"
        anchor: "create-store-api-account"
        content: |
          {% capture credentials-notice %}
          **Note**: This step requires store owner privileges in {{ integration.display_name }}.
          {% endcapture %}
          {% include note.html type="single-line" content=credentials-notice %}

          {% capture api-account-caption %}
          Click to enlarge. The {{ integration.display_name }} Create API Account page, with required permissions highlighted.
          {% endcapture %}

          {% include layout/image.html type="right" file="/integrations/bigcommerce-api-permissions.png" max-width="350" alt=api-account-caption enlarge=true %}

          1. [Sign into your {{ integration.display_name }} store](https://login.bigcommerce.com/login){:target="new"} as the store owner.
          2. Click **Advanced Settings > API Accounts**. This will display the Store API Accounts page.
          3. Click the **Create API Account** button.
          4. In the **Name** field, enter `Stitch`.
          5. In the **OAuth Scopes** section, you'll set the permissions that Stitch has. Define the following fields:

             - **Customers** - Set to **Read-only**
             - **Marketing** - Set to **Read-only**
             - **Orders** - Set to **Read-only**
             - **Products** - Set to **Read-only**
             
          6. When finished, click the **Save** button.

      - title: "Retrieve your API credentials"
        anchor: "retrieve-api-credentials"
        content: |
          After the API account has been successfully created, a pop-up will display and you'll be prompted to download a `.txt` file containing the API credentials. **If you aren't prompted to download the `.txt` file or you encounter other issues**, [contact {{ integration.display_name }} support](https://support.bigcommerce.com/s/){:target="new"}.

          Download the file to your computer, and then open it. It'll look similar to the following:

          {% capture text-file-image-caption %}
          A {{ integration.display_name }} API credentials text file. The highlighted portion of the API path is the store hash.
          {% endcapture %}

          {% capture text-file-image-alt %}
          Click to enlarge. A {{ integration.display_name }} API credentials text file. The store has portion of the API path is highlighted.
          {% endcapture %}

          {% include layout/image.html file="/integrations/bigcommerce-api-text-file.png" alt=text-file-image-alt caption=text-file-image-caption enlarge=true %}

          You'll need the following credentials from this file:

          - Client ID
          - Access Token
          - API Path. This contains your store hash. The value between `stores/` and `/v3/` in the API path is your store hash - this is highlighted in the image above.

             For example: If the API path were `https://api.bigcommerce.com/stores/123456/v3/`, the store hash would be `123456`.
      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Client ID** field, paste the client ID from the `.txt` file you opened in [Step 1.2](#retrieve-api-credentials).
      5. In the **Access Token** field, paste the access token from the `.txt` file you opened in [Step 1.2](#retrieve-api-credentials).
      6. In the **Store Hash** field, paste the store hash from the `.txt` file you opened in [Step 1.2](#retrieve-api-credentials).

         To find your store hash, locate the **API Path** in the `.txt` file. The value between `stores/` and `/v3/` in the API path is your store hash. For example: If the API path were `https://api.bigcommerce.com/stores/123456/v3/`, the store hash would be `123456`.
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
# Each table has a its own .md file in /_integration-schemas/bigcommerce
---
{% assign integration = page %}
{% include misc/data-files.html %}