---
title: Marketo - DEPRECATED VERSION; REPLACED BY SINGER
permalink: /integrations/saas/marketo
keywords: marketo, integration, schema, etl marketo, marketo etl, marketo schema
tags: [saas_integrations]

name: "marketo"
display_name: "Marketo"
author: "Stitch"
author-url: https://www.stitchdata.com
status: "Open Beta"
historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://status.marketo.com/
repo-url: https://github.com/singer-io/tap-marketo
icon: /images/integrations/icons/marketo.svg
whitelist:
  tables: "No"
  columns: "No"

format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

tables:
## Campaigns
  - name: "marketo_campaigns"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Campaigns/getCampaignsUsingGET
    description: "info about the campaigns in your Marketo account."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Campaign ID (<code>id</code>)
      - name: active
      - name: createdat
      - name: description
      - name: name
      - name: type
      - name: updatedat
      - name: workspacename

## Lead Activities
  - name: "marketo_lead_activities"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET
    description: "info about lead activities."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: true/false
    attributes:
      - name: Lead Activity ID (<code>id</code>)
      - name: leadid
      - name: attributes<code>*</code>
      - name: activitydate
      - name: activitytypeid
      - name: primaryattributevalueid
      - name: primaryattributevalue

## Lead Activity Types
  - name: "marketo_lead_activity_types"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getAllActivityTypesUsingGET
    description: "metadata about the activity types - form fill, web page visit, lead creation, and so on - available in Marketo."
    notes: |
      ### Filtering Deleted Leads
      When joined with the `marketo_lead_activities` table, you can use specific activity types to filter out deleted leads, assess list membership, and more. Here are a few noteworthy activity types:
      
      - **Add to List and Remove from List** - These events can be used to discover lead list membership.
      - **Delete Lead** - A delete lead event indicates leads that have been deleted. We recommend using this activity to filter out deleted leads.
      - **Add a Lead to a Nurture Program, Change Nurture Track, and Change Nurture Cadence** - These events can help you determine what nurture programs a lead is in and lead activity against that program.
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Lead Activity Type ID (<code>id</code>)
      - name: attributes<code>*</code>
      - name: name
      - name: description

## Leads
  - name: "marketo_leads"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Leads/getLeadsByFilterUsingGET
    description: "contains info about your Marketo leads."
    notes: |
      In addition to the attributes listed below, our Marketo integration will also replicate any custom fields.
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Lead ID (<code>id</code>)
      - name: acquiredby
      - name: isexhausted
      - name: membershipdate
      - name: nurturecadence
      - name: progressionstatus
      - name: reachedsuccess
      - name: reachedsuccessdate
      - name: stream

## Lists
  - name: "marketo_lists"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Static_Lists/getListsUsingGET
    description: "info about the static lists in your Marketo account. <strong>Note that due to some of the limitations in Marketo’s API, only static lists are available.</strong>"
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: List ID (<code>id</code>)
      - name: name
      - name: description
      - name: programname
      - name: workspacename
      - name: createdat
      - name: updatedat

## Programs
  - name: "marketo_programs"
    doc-link: http://developers.marketo.com/rest-api/endpoint-reference/asset-endpoint-reference/#!/Programs/browseProgramsUsingGET
    description: "info about the programs in your Marketo account."
    notes: 
    replication-method: "Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Program ID (<code>id</code>)
      - name: channel
      - name: createdat
      - name: description
      - name: name
      - name: sfdcid
      - name: sfdcname
      - name: status
      - name: type
      - name: updatedat
      - name: url
      - name: workspace
---

{% contentfor setup %}
Connecting your Marketo data to Stitch is a eight-step process:

1. [Create an API-Only user role in Marketo](#create-api-only-user-role)`*`
2. [Create a Stitch Marketo API user](#create-stitch-marketo-api-user)
3. [Create an API custom service in Marketo](#create-api-custom-service)
4. [Whitelist Stitch's IP addresses](#whitelist-stitch-ips)`*`
5. [Retrieve your Marketo REST API base URLs](#retrieve-marketo-base-urls)
6. [Add Marketo as a Stitch data source](#add-stitch-data-source)
7. [Define the Historical Sync](#define-historical-sync)
8. [Define the Replication Frequency](#define-rep-frequency)

`*` Completing these steps may not be necessary depending on how your Marketo account is configured. Refer to the sections below for more detail.

### Creating an API-Only User Role in Marketo {#create-api-only-user-role}

**Completing this step is required only if you DON'T have an [API-Only](http://docs.marketo.com/display/public/DOCS/Create+an+API+Only+User+Role) user role in your Marketo account.** Skip to the next section if your account has this role.

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

### Creating a Stitch Marketo API User {#create-stitch-marketo-api-user}

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

### Creating an API Custom Service in Marketo {#create-api-custom-service}

To generate the API credentials you need to connect Stitch to Marketo, you need to [create an API Custom Service](http://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API) and associate it with the Stitch API user.

1. In A**Admin**, open the **Integration** menu.
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

### Whitelisting Stitch's IP Addresses {#whitelist-stitch-ips}
**Completing this step is required only if you have IP Restriction enabled.** You can check if this setting is enabled by clicking **Admin > Web Services** and looking in the **IP Restrictions** section. If this setting isn't enabled, skip ahead to the next step.

1. In the **Integration** menu, click **Web Services**.
2. In the **IP Restrictions section**, click the **Edit** button.
3. In the **Allowed Addresses** field, paste one of the IP addresses listed below and then click **Add**.

   {% include custom/site-wide/stitch-ip-addresses.html %}

4. Repeat step 4 until all the Stitch IP addresses are added.
5. Click the **Save** button.

Leave the Web Services page open - you’ll need it in the next step.

### Retrieving Your Marketo REST API Base URLs {#retrieve-marketo-base-urls}

The last thing you need to do is retrieve your Marketo REST API base URLs.

1. On the Web Services page, scroll down to the **REST API** section.
2. In this section, find the **Endpoint** and **Identity** fields.
3. Copy these URLs into the text file where you have your Client ID and Client Secret.

{% include custom/integrations/setup/connection-setup.html %}
4. In the **Endpoint Base URL** field, paste your **Marketo REST API Endpoint URL**.
5. In the **Identity Base URL** field, paste your **Marketo REST API Identity URL**.
6. In the **Client ID** field, paste your **Marketo API Client ID**.
7. In the **OAuth Client Secret** field, paste your **Marketo API Client Secret**.

{% include custom/integrations/setup/historical-sync.html %}

{% include custom/integrations/setup/replication-frequency.html %}
{% endcontentfor %}