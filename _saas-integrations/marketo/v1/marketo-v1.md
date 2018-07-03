---
title: Marketo
permalink: /integrations/saas/marketo-v1
keywords: marketo, integration, schema, etl marketo, marketo etl, marketo schema
tags: [saas_integrations]
summary: "Connection instructions and schema details for Stitch's Marketo integration."
layout: singer
input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "marketo"
display_name: "Marketo"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-marketo

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"

status-url: http://status.marketo.com/
icon: /images/integrations/icons/marketo.svg

## Features in Stitch

whitelist:
  tables: true
  columns: false
anchor-scheduling: true
cron-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Admin permissions in Marketo.** Marketo Admin permissions are required to complete portions of the setup process."

requirements-info: |
  Prior to set up, we recommend that you monitor your **Marketo API call usage** if other applications are also connected to your Marketo account. While Stitch is designed to use only a portion of your allotted API calls, replication may be impacted if numerous applications are using the API.

  See the [Replication section](#replication) for more details.

setup-steps:
  - title: "Create an API-Only User Role in Marketo"
    anchor: "create-api-only-user-role"
    content: |
      {% include note.html content="If you have an [API-Only User Role](http://docs.marketo.com/display/public/DOCS/Create+an+API+Only+User+Role) in your Marketo account, [skip to the next section](#create-stitch-marketo-api-user)." %}

      1. Sign into your Marketo account.
      2. Click the **Admin** option.
      3. Under Admin, open the **Security** menu.
      4. Click **Users & Roles**.
      5. Click the **Roles** tab.
      6. Click **New Role**.
      7. In the **Create New Role** window, do the following:
         - **Role Name** - Enter a name for the role. If it’s specific to Stitch, make the name specific - something like "Stitch API Role."
         - **Description** - Enter a description.
         - **Permissions** - Click the checkbox next to the **Access API** option.
      8. Click **Create**.

  - title: "Create a Stitch Marketo API User"
    anchor: "create-stitch-marketo-api-user"
    content: |
      Next, [you’ll create an API User](http://docs.marketo.com/display/public/DOCS/Create+an+API+Only+User) for Stitch. Creating a Stitch-specific user will ensure that Stitch is easily distinguishable in any logs or audits.

      1. Click the **Admin** option.
      2. Under Admin, open the **Security** menu.
      3. Click **Users & Roles**.
      4. In the Users tab, click **Invite New User**.
      5. In the **INFO** section, enter an email address and first and last name.
      6. Click **Next**.
      7. In the **PERMISSIONS** section, click the checkboxes next to the **API User Role** you created and the **API Only option**.
      8. Click **Next**.
      9. In the **MESSAGE** section, click the **Send** button to create the user.

  - title: "Create an API Custom Service in Marketo"
    anchor: "create-api-custom-service"
    content: |
      To generate the API credentials you need to connect Stitch to Marketo, you need to [create an API Custom Service](http://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API) and associate it with the Stitch API user.

      1. In **Admin**, open the **Integration** menu.
      2. Click **LaunchPoint**.
      3. Click **New** and then **New Service**.
      4. In the New Service window, do the following:
         - **Display Name** - Enter "Stitch".
         - **Service** - Select **Custom** from the dropdown.
         - **Description** - Enter a description.
         - **API Only User** - Select the Stitch user you created.
      5. Click **Create**.
      6. After the service is created, it’ll display in the Installed Services grid. Click the **View Details** link to display your API credentials.
      7. Copy the **Client ID** and **Secret** into a text file.

  - title: "Whitelist Stitch's IP Addresses in Marketo"
    anchor: "whitelist-stitch-ips"
    content: |
      {% include note.html content="**Completing this step is required only if you have IP Restriction enabled in Marketo.** You can check if this setting is enabled by clicking **Admin > Web Services** and looking in the **IP Restrictions** section. If this setting isn't enabled, skip ahead to the next step." %}

      1. In the **Integration** menu, click **Web Services**.
      2. In the **IP Restrictions section**, click the **Edit** button.
      3. In the **Allowed Addresses** field, paste one of the IP addresses listed below and then click **Add**.

         {% for ip-address in ip-addresses %}
         - {{ ip-address.ip }}
         {% endfor %}

      4. Repeat step 4 until all the Stitch IP addresses are added.
      5. Click the **Save** button.

      Leave the Web Services page open - you’ll need it in the next step.

  - title: "Retrieve Your Marketo REST API Base URLs"
    anchor: "retrieve-marketo-base-urls"
    content: |
      1. On the Web Services page, scroll down to the **REST API** section.
      2. In this section, find the **Endpoint** and **Identity** fields.
      3. Copy these URLs into the text file where you have your Client ID and Client Secret.

  - title: "add integration"
    content: |
      4. In the **Endpoint Base URL** field, paste your **Marketo REST API Endpoint URL**.
      5. In the **Identity Base URL** field, paste your **Marketo REST API Identity URL**.
      6. In the **Client ID** field, paste your **Marketo API Client ID**.
      7. In the **OAuth Client Secret** field, paste your **Marketo API Client Secret**.
  - title: "historical sync"
  - title: "replication frequency"


replication-sections:
  - title: "Stitch & Marketo Daily API Call Limits"
    anchor: "marketo-daily-api-call-limits"
    content: |
      By default, all Marketo accounts have a maximum number of 10,000 daily account calls. Stitch's Marketo integration is designed to use up to 8,000 of these calls per day to allow other applications API access to your Marketo account.

      When the 10,000 account call limit has been reached, Stitch will be unable to replicate any Marketo data until more API quota is available. If you find that the 10,000 call limit isn't enough, **contact Marketo support** to inquire about raising the limit.


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/marketo/v1

---
{% assign integration = page %}
{% include misc/data-files.html %}
