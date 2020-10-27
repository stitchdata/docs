---
title: Marketo (v2)
permalink: /integrations/saas/marketo
keywords: marketo, integration, schema, etl marketo, marketo etl, marketo schema
summary: "Connection instructions and schema details for Stitch's Marketo integration."
layout: singer

key: "marketo-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "marketo"
display_name: "Marketo"

singer: true
repo-url: https://github.com/singer-io/tap-marketo

this-version: "2"

api: |
  [{{ integration.display_name }} REST API](https://developers.marketo.com/rest-api/){:target="new"} and [{{ integration.display_name }} Bulk API](https://developers.marketo.com/rest-api/bulk-extract/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "12 hours"
tier: "Standard"
status-url: http://status.marketo.com/

api-type: "platform.marketobulk"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


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
      {% include note.html type="single-line" content="If you have an [API-Only User Role](http://docs.marketo.com/display/public/DOCS/Create+an+API+Only+User+Role) in your Marketo account, [skip to the next section](#create-stitch-marketo-api-user)." %}

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
      Next, [you’ll create an API User](http://docs.marketo.com/display/public/DOCS/Create+an+API+Only+User) for Stitch. Creating a Stitch-specific user ensures that Stitch is easily distinguishable in any logs or audits.

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

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Endpoint Base URL** field, paste your **Marketo REST API Endpoint URL**.
      5. In the **Identity Base URL** field, paste your **Marketo REST API Identity URL**.
      6. In the **Client ID** field, paste your **Marketo API Client ID**.
      7. In the **OAuth Client Secret** field, paste your **Marketo API Client Secret**.
      8. In the **Max Daily API Calls** field, either keep the default 40,000 value or use a larger number based on your **Marketo API Quota**
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


replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.title }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Marketo Daily REST API call limits"
    anchor: "marketo-daily-api-call-limits"
    content: |
      By default, all {{ integration.display_name }} accounts have a maximum number of 50,000 daily account calls.
       
      The integration's **Max Daily API Calls** field dictates the quantity of your total API quota Stitch is allowed to use per 24 hour period. **Note**: This includes API usage from other apps. By default, Stitch's {{ integration.display_name }} integration will use up to 40,000 of these calls per day, which can be increased or reduced by setting a **Max Daily API Calls** value.
       
      When the integration detects that the source account's quota usage has exceeded the specified **Max Daily API Calls** limit, Stitch will be unable to replicate any {{ integration.display_name }} data until more API quota is available. If you find that the 50,000 total call limit isn't enough, contact {{ integration.display_name }} support to inquire about raising your limit.

  - title: "Activities and Leads replication"
    anchor: "activities-leads-replication"
    content: |
      To efficiently replicate activity and lead data, Stitch's {{ integration.display_name }} integration uses the Bulk API to extract data. While this approach is more efficient than the REST API, it may also impact your overall row count and frequency with which data is replicated.

    subsections:
      - title: "Leads replication"
        anchor: "leads-replication"
        content: |
          To incrementally replicate `leads` data, Marketo requires the authorizing account to have the ability to filter using the `updatedAt` field. This allows Stitch to use an `updatedAt` query parameter to extract only new and updated data from the `leads` endpoint.

          If your account doesn't have this filter enabled, Stitch will use the `createdAt` field to incrementally replicate `leads` data. **Note**: This will result in data for this table using [Append-Only loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}).

      - title: "Bulk API limits"
        anchor: "bulk-api-limits"
        content: |
          {% include note.html type="single-line" content="**Note**: This section applies to the `activity_[activity_types]` and `leads` tables. Bulk API call limits are a separate quota from REST API call limits." %}

          Part of the extraction process using the Bulk API involves writing and downloading a file of the extracted data. Stitch then pushes the data from this file into your destination.

          {{ integration.display_name }} currently [limits the amount of data pulled on a daily basis to 500MB](http://developers.marketo.com/rest-api/bulk-extract/#limits){:target="new"}. Exceeding the limit will pause replication until midnight CT, when it will be possible to resume.


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/marketo
---
{% assign integration = page %}
{% include misc/data-files.html %}
