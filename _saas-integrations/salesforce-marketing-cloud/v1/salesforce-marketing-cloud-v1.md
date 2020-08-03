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

title: Salesforce Marketing Cloud (v1)
permalink: /integrations/saas/salesforce-marketing-cloud
keywords: salesforce marketing cloud, integration, schema, etl salesforce marketing cloud, salesforce marketing cloud etl, salesforce marketing cloud schema
summary: "Connection instructions, replication info, and schema details for Stitch's Salesforce Marketing Cloud (Exact Target) integration."
layout: singer
# input: false

key: "salesforce-marketing-cloud-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "salesforce-marketing-cloud"
display_name: "Salesforce Marketing Cloud"

singer: true 
tap-name: "Exact Target"
repo-url: https://github.com/singer-io/tap-exacttarget
status-url: "https://status.salesforce.com/"

this-version: "1"

api: |
  [{{ integration.display_name }} SOAP Web Service API](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/web_service_guide.htm){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.exacttarget"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#  Required App Permissions  #
# -------------------------- #

## These come in during the app component step of the setup.

permission-categories:
  - name: "Channels"
    permissions:
      - name: "Email"
      - name: "Push"
      - name: "SMS"
      - name: "Social"
      - name: "Web"
  - name: "Assets"
    permissions:
      - name: "Documents and Images"
      - name: "Saved Content"
  - name: "Automation"
    permissions:
      - name: "Automations"
      - name: "Journeys"
  - name: "Contacts"
    permissions:
      - name: "Audiences"
      - name: "List and Subscribers"
  - name: "Data"
    permissions:
      - name: "Data Extensions (Read/Write)"
      - name: "File Locations"
      - name: "Tracking Events"
  - name: "Hub"
    permissions:
      - name: "Calendar"
      - name: "Campaign"
      - name: "Tags"
  - name: "Provisioning"
    permissions:
      - name: "Accounts"
      - name: "Users"
  - name: "Webhooks"
    permissions:
      - name: "Webhooks"


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be using the Pro, Corporate, or Enterprise edition of {{ integration.display_name }}.** Salesforce requires this to [access the {{ integration.display_name }} API](https://www.salesforce.com/content/dam/web/en_us/www/documents/pricing/mc_email_journey_pricing_sheet.pdf){:target="new"}.
  - item: |
      **A {{ integration.display_name }} user with the Marketing Cloud Administrator Role**. Salesforce requires this to [generate {{ integration.display_name }} API credentials](https://help.salesforce.com/articleView?id=mc_overview_marketing_cloud_roles.htm&type=5){:target="new"}.

      **Note**: While this role is required to complete the setup, you'll be able to limit Stitch's access in {{ integration.display_name }}. This is outlined in [Step 2.2 of this guide](#add-api-component-to-package).

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} tenant subdomain"
    anchor: "retrieve-tenant-subdomain"
    content: |
      A [tenant subdomain](https://help.salesforce.com/articleView?id=mc_rn_october_2018_platform_tenant_specific_subdomains.htm&type=5){:target="new"} is an auto-generated ID unique to your {{ integration.display_name }} account. You can retrieve this info by looking at the URL when you sign into your {{ integration.display_name }} account.

      1. Navigate to the [{{ integration.display_name }} login page](https://mc.exacttarget.com/){:target="new"}.
      2. Enter your {{ integration.display_name }} username and click **Next**.
      3. Look at the URL for the page you're currently on.  The string between `https://` and `.login` is your tenant subdomain:

         ![The tenant subdomain, highlighted in the login URL for {{ integration.display_name }}]({{ site.baseurl }}/images/integrations/salesforce-marketing-cloud-tenant-subdomain.png)

         In this example, the tenant subdomain is `mcx21dt54chc0gprl638px2g7r48`. Keep this handy - you'll need it to complete the setup in Stitch.
      4. Enter your {{ integration.display_name }} password and click **Log In**.

  - title: "Generate API credentials"
    anchor: "generate-api-credentials"
    content: |
      To use {{ integration.display_name }}'s API, you need a client ID and secret. These credentials are generated when you create an installed package in Marketing Cloud and add an API Integration component.

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Create an Installed Package for Stitch"
        anchor: "create-installed-package"
        content: |
          2. While signed into your {{ integration.display_name }} account, click the **user menu** in the top right corner, then **Setup**.
          3. In the menu on the left side, click **Apps > Installed Packages**.
          4. Click the **New** button.
          5. In the **New Package Details** window, enter a **Name** and **Description** for the package. For example: `Stitch`
          6. Click **Save**.

# https://developer.salesforce.com/docs/atlas.en-us.mc-app-development.meta/mc-app-development/api-integration.htm
      - title: "Configure the package settings"
        anchor: "add-api-component-to-package"
        content: |
          After the package has been saved, you'll need to add a component and grant the required permissions. This will allow Stitch to connect to your {{ integration.display_name }} instance.

          1. Click the **Add Component** button.
          2. Select the **API Integration** option in the **Choose Your Component Type** window. Click **Next**.
          3. Select the **Server-to-Server** option in the **Choose Your Integration Type** window:

             ![Server-to-Server integration type highlighted in the Choose Your Integration Type window of the Installed Package creation workflow]({{ site.baseurl }}/images/integrations/salesforce-marketing-cloud-server-to-server.png)

             Click **Next**.
          4. In the **Set Server-to-Server Properties** window, you'll grant permissions to the Stitch app. 

             The table below lists the categories of permissions and the specific permissions Stitch requires. Unless otherwise noted, select the **Read** permission next to the following options:

             <table class="attribute-list">
             {% for category in integration.permission-categories %}
             {% cycle 'cat-before':'<tr>','','',''' %}
             <td width="25%; fixed">
             <p><strong>{{ category.name }}</strong></p>
             <ul>
             {% for permission in category.permissions %}
             <li>{{ permission.name }}</li>
             {% endfor %}
             </ul>
             </td>
             {% cycle 'cat-after': '', '', '', '</tr>' %}
             {% endfor %}
             </table>

             **Note**: To replicate **Data Extension** data, you will also need to select the **Write** permission.

          5. Click **Save**.

      - title: "Locate your API credentials"
        anchor: "locate-api-credentials"
        content: |
          After the permissions are saved, you'll be directed back to the app's summary page. In the **Components** section, locate the **Client Id** and **Client Secret** fields, which are highlighted in the image below:

          ![Client ID and Client Secret fields highlighted in {{ integration.display_name }} App Components Summary page]({{ site.baseurl }}/images/integrations/salesforce-marketing-cloud-api-credentials.png)

          Keep these handy - you'll need them to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **Client ID** field, paste the {{ integration.display_name }} Client ID you retrieved in [Step 2.3](#locate-api-credentials).
      5. In the **Client Secret** field, paste the {{ integration.display_name }} Client Secret you retrieved in [Step 2.3](#locate-api-credentials).
      6. In the **Tenant Subdomain** field, paste the {{ integration.display_name }} tenant subdomain you retrieved in [Step 1](#retrieve-tenant-subdomain).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/salesforce-marketing-cloud
---
{% assign integration = page %}
{% include misc/data-files.html %}