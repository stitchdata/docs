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

title: Recurly (v1.0)
permalink: /integrations/saas/recurly/v1
keywords: recurly, integration, schema, etl recurly, recurly etl, recurly schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "recurly"
display_name: "Recurly"

singer: true 
tap-name: "Recurly"
repo-url: https://github.com/singer-io/tap-recurly

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Paid"
status-url: "https://status.recurly.com/"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin or Manager permissions in {{ integration.display_name }}.** These permissions are required to create an API key for Stitch.

setup-steps:
  - title: "Generate a {{ integration.display_name }} API key"
    anchor: "generate-api-key"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have Admin or Manager permissions in Recurly to complete this step." %}

      In this step, you'll create an API key for Stitch.

      1. Sign into your {{ integration.display_name }} account.
      2. Click **Admin > Users** in the sidenav.
      3. On the **Users** page, click the **Configure API Access** button at the top of the page. Thsi will open the **API Credentials** page.
      4. Click the **Add Private API Key** button. The **Add Private API Key** page will display.
      5. Fill in the fields as follows:
         - **Key Name**: Enter a name for the API key. For example: `Stitch`
         - **Notes**: Enter any notes you want about the API key.
      6. Click **Save Changes**.

      Leave this page open for now - you'll need it to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the {{ integration.display_name }} API key you created in [Step 1](#generate-api-key).
      5. In the **{{ integration.display_name }} Subdomain** field, enter your {{ integration.display_name }} subdomain. For example: If the full URL of the subdomain were `stitchdata.recurly.com`, you'd only enter `stitchdata` into this field.
      6. In the **Quota Limit** field, enter the percentage of the API rate limit you want to allocate to the integration. For example: A value of `30` would be `30%` of the rate limit. Refer to [{{ integration.display_name }}'s documentation](https://dev.recurly.com/docs/rate-limits){:target="new"} for more info.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/recurly
---
{% assign integration = page %}
{% include misc/data-files.html %}