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
tags: [saas_integrations]
keywords: salesforce marketing cloud, integration, schema, etl salesforce marketing cloud, salesforce marketing cloud etl, salesforce marketing cloud schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "salesforce-marketing-cloud"
display_name: "Salesforce Marketing Cloud"

singer: true 
tap-name: "Exact Target"
repo-url: https://github.com/singer-io/tap-exacttarget
status-url: "https://status.salesforce.com/"

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
icon: /images/integrations/icons/salesforce-marketing-cloud.svg

anchor-scheduling: true
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
      - name: "Data Extensions"
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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be using the Pro, Corporate, or Enterprise edition of {{ integration.display_name }}.** Salesforce requires this to [access the {{ integration.display_name }} API](https://www.salesforce.com/content/dam/web/en_us/www/documents/pricing/mc_email_journey_pricing_sheet.pdf){:target="new"}.
  - item: |
      **A {{ integration.display_name }} user with the Marketing Cloud Administrator Role**. Salesforce requires this to [generate {{ integration.display_name }} API credentials](https://help.salesforce.com/articleView?id=mc_overview_marketing_cloud_roles.htm&type=5){:target="new"}.

      **Note**: While this role is required to complete the setup, you'll be able to limit Stitch's access in {{ integration.display_name }}. This is outlined in [Step 1.2 of this guide](#add-api-component-to-package).

setup-steps:
  - title: "Generate API credentials"
    anchor: "generate-api-credentials"
    content: |
      To use {{ integration.display_name }}'s API, you need a client ID and secret. These credentials are generated when you create an installed package in Marketing Cloud and add an API Integration component.

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
# https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-app-development.meta/mc-app-development/install-packages.htm
      - title: "Create an Installed Package for Stitch"
        anchor: "create-installed-package"
        content: |
          1. Sign into your {{ integration.display_name }} account.
          2. Click the **user menu** in the top right corner, then **Administration**.
          3. On the **Administration** page, click **Account > Installed Packages**.
          4. Click the **New** button.
          5. In the **New Package Details** window, enter a **Name** and **Description** for the package. For example: `Stitch`
          6. Click **Save**.

# https://developer.salesforce.com/docs/atlas.en-us.mc-app-development.meta/mc-app-development/api-integration.htm
      - title: "Add an API Integration component to the package"
        anchor: "add-api-component-to-package"
        content: |
          After the package has been saved, you'll need to add a component and grant the required permissions. This will allow Stitch to connect to your {{ integration.display_name }} instance.

          1. Click the **Add Component** button.
          2. In the **Add Component** window, select the **API Integration** option.
          3. In the **Add API Integration** window, you'll grant permissions to the Stitch app.

             Check the **Read** option next to the options listed below for each category:

             <table class="attribute-list">
             {% for category in integration.permission-categories %}
             {% cycle 'cat-before':'<tr>','','',''' %}
             <td class="25%; fixed">
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
          4. Click **Save**.

      - title: "Locate your API credentials"
        anchor: "locate-api-credentials"
        content: |
          After the permissions are saved, you'll be directed back to the app's summary page. In the **Components** section, locate the **Client Id** and **Client Secret** fields, which are highlighted in the image below:

          ![Client ID and Client Secret fields highlighted in {{ integration.display_name }} App Components Summary page]({{ site.baseurl }}/images/integrations/salesforce-marketing-cloud-api-credentials.png)

          Keep these handy - you'll need them to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **Client ID** field, paste the {{ integration.display_name }} Client ID you retrieved in [Step 1.3](#locate-api-credentials).
      5. In the **Client Secret** field, paste the {{ integration.display_name }} Client Secret you retrieved in [Step 1.3](#locate-api-credentials).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/salesforce-marketing-cloud

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}