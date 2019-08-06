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

title: Deputy
permalink: /integrations/saas/deputy
keywords: deputy, integration, schema, etl deputy, deputy etl, deputy schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "deputy"
display_name: "Deputy"

singer: true 
tap-name: "Deputy"
repo-url: https://github.com/singer-io/tap-deputy

# this-version: "1.0"

api: |
  [{{ integration.display_name }} API](https://www.deputy.com/api-doc/API/Getting_Started){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.deputy.com/"

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
  - title: "Create a {{ integration.display_name }} OAuth client"
    anchor: "create-a-oauth-client"
    content: |
      In this step, you'll create a [{{ integration.display_name }} OAuth client](https://www.deputy.com/api-doc/API/Authentication){:target="new"}. This is required to generate credentials for the integration.

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Create the OAuth client"
        anchor: "create-oauth-client"
        content: |
          1. Sign into your {{ integration.display_name }} account.
          2. In your browser, add `/exec/devapp/oauth_clients` to the URL path. For example: `https://[subdomain].{{ integration.name }}.com/exec/devapp/oauth_clients`
          3. Click **Create New OAuth Client** in the top-left corner.
          4. Fill in the fields as follows:
             - **Name**: Enter `Stitch`
             - **Redirect Uri**: Enter `https://localhost`. **Note**: This is a placeholder value and is not used by {{ integration.display_name }}.
          5. When finished, click **Save This OAuth Client**.

      - title: "Retrieve OAuth client credentials"
        anchor: "retrieve-oauth-client-credentials"
        content: |
          After the OAuth client is successfully created, a page with the client's credentials will display.

          Locate the **Client Id**, **Client Secret**, and **Redirect Uri** fields:

          ![OAuth Client Id, Client Secret, and Redirect Uri fields highlighted in the Deputy OAuth UI]({{ site.baseurl }}/images/integrations/deputy-oauth-credentials.png)

          Keep this info handy - you'll need it to complete the setup in Stitch.

      - title: "Retrieve OAuth refresh token"
        anchor: "retrieve-refresh-token"
        content: |
          {% include note.html type="single-line" content="**Note**: If your user is de-activated from Deputy, this token will stop working. Another user should create a new token to ensure the integration continues functioning." %}

          Next, click the **Get An Access Token** option at the top of the page.

          A prompt containing the token will display. **Copy the token before closing the window**, as {{ integration.display_name }} will only display it once:

          ![The Access Token prompt in Deputy after an access token is created]({{ site.baseurl }}/images/integrations/deputy-access-token.png)

  - title: "add integration"
    content: |
      4. In the **Client ID** field, paste the **Client Id** from [Step 1.2](#retrieve-oauth-client-credentials).
      5. In the **Client Secret** field, paste the **Client Secret** from [Step 1.2](#retrieve-oauth-client-credentials).
      6. In the **Domain** field, enter your {{ integration.display_name }} subdomain. For example: If the URL to your {{ integration.display_name }} account is `https://stitchdata.{{ integration.name }}.com`, you'd enter `stitchdata.{{ integration.name }}.com` into this field.
      7. In the **Redirect URI** field, paste the **Redirect Uri** from [Step 1.2](#retrieve-oauth-client-credentials).
      8. In the **Refresh Token** field, paste the paste the **Access Token** from [Step 1.3](#retrieve-refresh-token).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/deputy/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}