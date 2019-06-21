---
title: Zuora (v1.0)
permalink: /integrations/saas/zuora
keywords: zuora, integration, schema, etl zuora, zuora etl, zuora schema
summary: "Connection instructions and schema details for Stitch's Zuora integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zuora"
display_name: "Zuora"

singer: true
repo-url: https://github.com/singer-io/tap-zuora

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"
status-url: "http://trust.zuora.com/"

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Administrator permissions in {{ integration.display_name }}.** These permissions are required to create a {{ integration.display_name }} user for Stitch."

setup-steps:
  - title: "Create a Stitch {{ integration.display_name }} user"
    anchor: "#create-stitch-zuora-user"
    content: |
      In this step, you'll create a {{ integration.display_name }} user for Stitch. Creating a Stitch-specific user will ensure that Stitch is distinguishable in any logs or audits.

      {% capture zuora-user-requirements %}
      To replicate your {{ integration.display_name }} data, Stitch requires a user that:

      1. **Has Standard user permissions.** While Stitch will only ever read your data, these permissions are required to access certain objects in {{ integration.display_name }}.
      2. **Has two-factor authentication disabled.** If this is enabled, connection and replication issues will occur after setup. Refer to the **Disable or Reset Two-Factor Authentication** section [in this {{ integration.display_name }} documentation](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication) for help disabling this setting.
      3. **Has credentials that don't expire.** This is applicable only if your company enforces Password Expiration rules. If Stitch's {{ integration.display_name }} credentials expire, connection issues may arise. [Refer to this {{ integration.display_name }} support article for a workaround](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F){:target="new"}.
      {% endcapture %}

      {% include important.html first-line="**Zuora user requirements**" content=zuora-user-requirements %}

      #### Create the {{ integration.display_name }} user

      {% include layout/image.html type="right" file="/integrations/zuora-user-setup.png" alt="Zuora user permissions" max-width="400px" %}
      1. Sign into your {{ integration.display_name }} account, if you haven't already.
      2. Click your username in the top-right corner.
      3. Click **Administration**, then **Manage Users**.
      4. Click **Add Single User**.
      5. Enter a first and last name for the user.
      6. Enter an email address in the **Work Email** field.
      7. Enter an email address in the **Login Field**.
      8. In the **{{ integration.display_name }} Platform Role** field, select **Standard User**.
      9. For the remaining **Role** fields, select the **Standard User** option.
      10. There aren't any requirements for the **Locale** and **Language** fields - leave them as the defaults.
      11. Click **Save** to create the user.

      After the user is created, {{ integration.display_name }} will send a verification email to the email address in the **Work Email** field. Complete the verification and set a password for the Stitch user before moving on to the next step.

  - title: "add integration"
    content: |
      4. If the {{ integration.display_name }} instance you want to connect to Stitch is a sandbox, check the **Connect to a Sandbox Environment** checkbox.
      5. In the **Username** field, enter the Stitch {{ integration.display_name }} user's username. This is the email address that was in the **Login Name** field when you created the user.
      6. In the **Password** field, enter the password associated with the Stitch {{ integration.display_name }} user.
      7. If the {{ integration.display_name }} instance you want to connect to Stitch is a **sandbox**, check the **Connect to a Sandbox Environment** box.
      8. If the {{ integration.display_name }} instance you want to connect to Stitch is **based in Europe**, check the **Connect to a European endpoint** box. If you aren't sure if this is applicable to you, [refer to Zuora's documentation](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Zuora_Data_Centers).

  - title: "Select a {{ integration.display_name }} extraction API"
    anchor: "rest-vs-aqua-api"
    content: |
      Stitch's {{ integration.display_name }} integration gives you the ability to select the API that you want Stitch to use to extract data. If you aren't sure which API you should use, take a look at the brief comparison below.

      **Note**: This setting can be changed at any time, but will only affect extractions that take place after the change.

      Once you've decided, click the radio button next to the API you want to use.

      {% include note.html type="single-line" content="If using the AQuA API, you'll also need to enter a partner ID in the **Zuora Partner ID** field. If you don't already have this credential, reach out to [Zuora Global Support](http://support.zuora.com/) before proceeding." %}

      <table>
      <tr>
      <tr>
      <td width="24%; fixed">
      </td>
      <td width="30%; fixed">
      <strong>REST API</strong>
      </td>
      <td width="46%; fixed">
      <strong>AQuA API</strong>
      </td>
      </tr>
      {% for comparison in site.data.taps.extraction.zuora.api-comparison %}
      <tr>
      <td width="24%; fixed">
      <strong>{{ comparison.name }}</strong> {{ comparison.icon | flatify }}
      </td>
      <td width="30%; fixed">
      {{ comparison.rest-api | flatify | markdownify }}
      </td>
      <td width="46%; fixed">
      {{ comparison.aqua-api | flatify | markdownify }}
      </td>
      </tr>
      {% endfor %}

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#         REPLICATION        #
# -------------------------- #

replication-sections:
  - title: "Replicate deleted data"
    anchor: "replicate-deleted-data"
    content: |
      {% capture aqua-api-note %}**Note**: This section is only applicable if using the [AQuA API for data extraction](#rest-vs-aqua-api). {{ integration.display_name }}'s REST API does not support extracting deleted data.
      {% endcapture %}

      {% include note.html type="single-line" content=aqua-api-note %}

      If using the AQuA API for data extraction, deleted data will be replicated for objects that support it. Supported objects will contain a boolean column named `deleted` that indicates a record's deletion status.

      **Note**: This column won't be automatically included for replication - [it must be set to replicate](#setting-data-to-replicate).

      Deleted data is supported for all objects with the exception of the following:

      {% for type in blacklisted-objects.list %}
      {% if type.api contains "deleted" %}
      {% for object in type.objects %}
      - `{{ object.name }}`
      {% endfor %}
      {% endif %}
      {% endfor %}

  - title: "Custom field replication"
    anchor: "custom-field-replication"
    content: |
      Custom object properties, or attributes, are supported by Stitch's {{ integration.display_name }} integration. If custom fields are available through {{ integration.display_name }}'s API, Stitch will replicate them to your destination.

      This is applicable to any object that supports custom fields in {{ integration.display_name }}. Refer to [Zuora's documentation](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Manage_Custom_Fields/Objects_that_Support_Custom_Fields_in_Zuora) for info on which objects support custom fields.

  - title: "Unsupported objects"
    anchor: "unsupported-objects"
    content: |
      {% for type in blacklisted-objects.list %}
      {% if type.api contains "common" %}
      {{ type.reason | flatify | markdownify }}
      {% for object in type.objects %}
      - `{{ object.name }}`
      {% endfor %}
      {% endif %}
      {% endfor %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

schema-sections:
  - title: "{{ integration.display_name }} object relationships"
    anchor: "zuora-entity-relationships"
    content: |
      To get a better understanding of how {{ integration.display_name }} objects relate to each other, check out [{{ integration.display_name }}'s Entity Relationship Diagram](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Business_Objects_Relationship). 

      Understanding the relationships between different data sets will allow you to perform more in-depth and complex analyses.

      **Don't see a table listed here?** The list of tables shown below is not an exhaustive list of all the tables Stitch can replicate from {{ integration.display_name }}.

      We're working on adding documentation for additional {{ integration.display_name }} tables. If there's a specific table you'd like to see here, let us know by [opening an issue in the Stitch Docs GitHub repo](https://github.com/stitchdata/docs).
---
{% assign integration = page %}
{% include misc/data-files.html %}