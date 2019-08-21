---
title: Salesforce (v1.0)
permalink: /integrations/saas/salesforce/
keywords: salesforce, integration, schema, etl salesforce, salesforce etl, salesforce schema
summary: "Connections instructions, replication info, and schema details for Stitch's Salesforce integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "salesforce"
display_name: "Salesforce"

singer: true
repo-url: https://github.com/singer-io/tap-salesforce
status-url: "https://trust.salesforce.com/trust/instances"

this-version: "1.0"

api: |
  [{{ integration.display_name }} Lightning Platform REST API (v41.0)](https://developer.salesforce.com/docs/atlas.en-us.210.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "1 hour"
historical: "1 year"
tier: "Standard"
whitelist-ips: true

anchor-scheduling: true
cron-scheduling: false

table-selection: true
column-selection: true
define-replication-methods: true

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
  - item: "**To verify your object access.** Stitch will only be able to access and replicate the objects that the user setting up the integration has access to. Before beginning, we recommend verifying that you have access to everything you want to replicate."
  - item: |
      **To verify your API access.** To use Stitch's {{ integration.display_name }} integration, your {{ integration.display_name }} account must have Web Service API access enabled. 

      Some editions of {{ integration.display_name }} include Web Service API access while others don't. Info about this feature can be found on [Salesforce's plan details page](https://www.salesforce.com/editions-pricing/sales-cloud-b/){:target="_blank"} in the **Connect sales info to any app** section, located near the bottom of the page.

      Contact {{ integration.display_name }} support if you're unsure about your {{ integration.display_name }} plan's API access.


setup-steps:
  - title: "Set trusted IPs in {{ integration.display_name }}"
    anchor: "whitelist-stitch-ips"
    content: |
      Depending on how your {{ integration.display_name }} instance is set up, you may need to whitelist Stitch's IP addresses. In {{ integration.display_name }}, this is referred to as "setting trusted IPs".

      [The instructions in this {{ integration.display_name }} article](https://help.salesforce.com/articleView?id=security_networkaccess.htm&type=0) will walk you through how to do this in {{ integration.display_name }}. **Note**: Because these are exact IP addresses and not ranges, the same IP address must be entered in the **Start IP Address** and **End IP Address** fields in {{ integration.display_name }}.

      Add the following IP addresses to the trusted list:

      {% for ip-address in ip-addresses %}
      - {{ ip-address.ip }}
      {% endfor %}

      Complete this step before proceeding with the rest of the setup, or you may encounter connection issues.

  - title: "add integration"
    content: |
      4. If the instance you want to connect to Stitch is a **sandbox**, check the **Connect to a Sandbox Environment** box.

  - title: "Configure Stitch's {{ integration.display_name }} API Usage"
    anchor: "configure-salesforce-api-usage"
    content: |
      Usage of the {{ integration.display_name }} API depends on two factors:

      1. The type of API used for data extraction (Bulk vs REST), and
      2. The amount of standard API quota your account has. {{ site.data.tooltips.api-quota }}

      Stitch's {{ integration.display_name }} integration allows you to control both of these settings so you can replicate data as you see fit.
      
    substeps:
      - title: "Select extraction API"
        anchor: "bulk-vs-rest-api"
        content: |
          If you're not sure which API you should use, take a look at the brief comparison below. Consider how much data you need to replicate, how often you require updates, how many additional apps are connected to your {{ integration.display_name }} instance, and so on.

          {% include note.html type="single-line" content="**Note**: The extraction API you select cannot be changed after the integration is saved." %}

          Once you've decided, click radio button next to the API you want to use.

          <table>
          <tr>
          <tr>
          <td width="24%; fixed">
          </td>
          <td width="38%; fixed">
          <strong>REST API</strong>
          </td>
          <td width="38%; fixed">
          <strong>Bulk API</strong>
          </td>
          </tr>
          {% for comparison in site.data.taps.extraction.salesforce.api-comparison %}
          <tr>
          <td width="24%; fixed">
          <strong>{{ comparison.name }}</strong> {{ comparison.icon | flatify }}
          </td>
          <td width="38%; fixed">
          {{ comparison.rest-api | flatify | markdownify }}
          </td>
          <td width="38%; fixed">
          {{ comparison.bulk-api | flatify | markdownify }}
          </td>
          </tr>
          {% endfor %}

      - title: "Define standard API quota usage limits"
        anchor: "configure-standard-api-quota-usage"
        content: |
          Next, you'll define the percentage of your standard API quota Stitch is allowed to use. If these limits are reached, Stitch will pause replication and resume when additional quota becomes available.

          {% include note.html type="single-line" content="**Note**: Even if you choose the Bulk API for extraction, Stitch still requires usage of Salesforce's REST API to detect changes and additions to objects and fields." %}

          Before defining these limits, we recommend reviewing your overall API usage in {{ integration.display_name }} to ensure Stitch or other apps won't be negatively impacted. This [Salesforce {{ integration.display_name }} topic](https://success.salesforce.com/answers?id=90630000000DOzAAAW){:target="new"} can help you locate your current API quota and usage.

          <table>
          <tr>
          <th>
          </th>
          <th width="40%; fixed">
          Description
          </th>
          <th>
          Example
          </th>
          </tr>
          <tr>
          <td markdown="span" width="20%; fixed">
          **Max Percentage of<br>
          total standard API quota**
          </td>
          <td markdown="span">
          The percentage of your total API quota Stitch is allowed to use per 24 hour period.<br><br>

          **Note**: This includes API usage from other apps.
          </td>
          <td markdown="span">
          If set to **80%** and the quota is 10,000 calls 24 hour period:<br><br>

          10,000 x .8 = 8,000<br><br>

          Stitch will replicate data up until 8,000 calls are used across all your connected apps.
          </td>
          </tr>
          <tr>
          <td markdown="span">
          **Max Percentage of<br>
          standard API quota per job**
          </td>
          <td>
          The percentage of your total standard API quota Stitch is allowed to use per replication job.
          </td>
          <td markdown="span">
          If set to **10%** and the quota is 10,000 calls:<br><br>

          10,000 x .1 = 1,000<br><br>

          Stitch will use up to 1,000 calls per replication job.
          </td>
          </tr>
          </table>

          Once you know what you want Stitch's maximum allowed standard API percentages to be, enter them as whole numbers (ex: `80` for 80%) into their respective fields.

  - title: "Define new field selection"
    anchor: "new-field-selection"
    content: |
      By default, when new fields are added to {{ integration.display_name }} objects, Stitch will automatically detect and begin replicating data from them.

      If you prefer to track new fields manually, uncheck the **Replicate new fields automatically** checkbox. **Note**: This setting cannot be changed after the integration is saved.

      {% capture new-fields-replicating-tables %}
      Data in new fields in already-replicating tables will only be available for records added or updated **after** the column is tracked, whether they're tracked manually or automatically. **This is only applicable to tables using Key-based Incremental Replication.**

      To backfill columns - or get data for a new field into existing rows - you'll need to queue a full re-replication of the table by resetting its Replication Key values on the {{ app.buttons.update-table-settings }} page.
      {% endcapture %}

      {% include note.html first-line="**Data for new fields in already-replicating tables**" content=new-fields-replicating-tables %}

  - title: "historical sync"

  - title: "replication frequency"

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen asking for authorization to {{ integration.display_name }} will display. **Note that Stitch will only ever read your data.**
      3. Click **Allow.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

schema-sections:
  - content: |
      Stitch currently supports the replication of the majority of {{ integration.display_name }} objects, with the exception of those listed in the [**Unsupported Objects** row of this table](#bulk-vs-rest-api).

      To ensure we can provide you with up-to-date documentation, this section will only cover a few of the most popular tables Stitch's {{ integration.display_name }} integration offers.

      See the [{{ integration.display_name }} Object Reference](https://resources.docs.salesforce.com/sfdc/pdf/object_reference.pdf){:target="new"} guide for info on objects not listed here, including the fields available in each object.

  - title: "Custom {{ integration.display_name }} object and field replication"
    anchor: "custom-objects-fields-replication"
    content: |
      Stitch's {{ integration.display_name }} integration supports the replication of custom objects and fields.

      Custom object and field names are appended with `__c` to make identification easier. For example: `AE_Assignment__c` or `Assignment_Group_Name__c`
---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}