---
title: Salesforce (v15-10-2015)
permalink: /integrations/saas/salesforce/v15-10-2015
tags: [saas_integrations]
keywords: salesforce, integration, schema, etl salesforce, salesforce etl, salesforce schema
summary: "Connections instructions, replication info, and schema details for Stitch's Salesforce integration."
layout: singer
input: false
old-schema-template: true

key: "salesforce-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "salesforce"
display_name: "Salesforce"
status-url: "https://trust.salesforce.com/trust/instances"

this-version: "15-10-2015"

api: |
  [{{ integration.display_name }} Force.com REST API (v41.0)](https://developer.salesforce.com/docs/atlas.en-us.194.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

frequency: "30 minutes"
historical: "1 year"
tier: "Standard"

table-selection: true
column-selection: true

anchor-scheduling: false
cron-scheduling: false

extraction-logs: false
loading-reports: true

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Salesforce enforces a daily API quota that limits the amount
## of API usage. This can impact Stitch's ability to continuously
## replicate data. Details are in the Replication section.

enforces-api-limits: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**To verify your Domain type.** This version of Stitch's {{ integration.display_name }} only supports **Production** domains."
  - item: "**To verify your object access.** Stitch will only be able to access and replicate the objects that the user setting up the integration has access to. Before beginning, we recommend verifying that you have access to everything you want to replicate."
  - item: |
      **To verify your API access.** To use Stitch's {{ integration.display_name }} integration, your {{ integration.display_name }} account must have Web Service API access enabled. 

      Some editions of {{ integration.display_name }} include Web Service API access while others don't. Info about this feature can be found on [Salesforce's plan details page](https://www.salesforce.com/editions-pricing/sales-cloud-b/){:target="_blank"} in the **Connect sales info to any app** section, located near the bottom of the page.

      Contact {{ integration.display_name }} support if you're unsure about your {{ integration.display_name }} plan's API access.

setup-steps:
  - title: "Set Trusted IPs in Salesforce"
    anchor: "whitelist-stitch-ips"
    content: |
      Depending on how your Salesforce instance is set up, you may need to whitelist Stitch's IP addresses.

      [The instructions in this Salesforce article](https://help.salesforce.com/articleView?id=security_networkaccess.htm&type=0) will walk you through how to do this in Salesforce; below are all the Stitch IP addresses that must be added to the trusted list:

      {% for ip-address in ip-addresses %}
      - {{ ip-address.ip }}
      {% endfor %}

      Complete this step before proceeding with the rest of the setup, or you may encounter connection issues.

  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to Access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen asking for authorization to Salesforce will display. **Note that Stitch will only ever read your data.**
      3. Click **Allow.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"
    content: |
      {% capture large-numbers-of-columns %}
      **Replicating Large Numbers of Columns**<br>
      Occasionally, setting large numbers of columns in a single object to replicate can cause replication issues in Stitch. Refer to the [Salesforce Replication and Selecting Too Many Columns]({{ link.troubleshooting.salesforce-too-many-columns | prepend: site.baseurl }}) guide for more info.
      {% endcapture %}
      {% include note.html content=large-numbers-of-columns %}

# -------------------------- #
#    Replication Details     #
# -------------------------- #

replication-sections:
  - title: "Replication Key Selection"
    anchor: "replication-key-selection"
    content: |
      While Stitch generally uses Incremental Replication to replicate data from Salesforce, the Replication Key used to identify new and updated data may vary from object to object.

      Stitch's Salesforce integration dynamically selects a column to use as the Replication Key based on the columns that are available in the object. This means that Stitch will loop over the fields below, **in order**, and select the first one found to use as the Replication Key:

      1. `SystemModStamp`
      2. `LastModifiedDate`
      3. `CreatedDate`

      If none of these fields are found, the object will be replicated using Full Table Replication.

      The exception to this is the `LoginHistory` table, where Stitch will check for the fields listed above and the `LoginTime` field.

      **Note**: Data in formula fields may become "stale" as a result of Stitch's replication approach and how these fields are updated in Salesforce. Refer to the [Stale Salesforce Data & Formula Fields guide]({{ link.troubleshooting.salesforce-formula-fields | prepend: site.baseurl }}) for info on preventing discrepancies.

  - title: "Sync Time & API Quota"
    anchor: "sync-time-api-quota"
    content: |
      Usage of Salesforce's API is determined by how much API quota you have. {{ site.data.tooltips.api-quota }}

      Due to the volume of data and the [daily API quotas imposed by Salesforce](https://help.salesforce.com/apex/HTViewSolution?id=000003706&language=en_US), an initial sync of your Salesforce data can take awhile.

      - **If a single replication attempt uses 20% of your daily quota**, replication will stop.
      - **If more than 80% of your daily quota has been used** - this includes usage from Stitch as well as any other apps you may be using - replication will stop and resume once more is available.

      Continually hitting these limits can cause an initial sync to take several days. Check out this [Salesforce article](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) for more info on calculating and increasing your total API calls.



# -------------------------- #
#       Schema Details       #
# -------------------------- #

objects-stitch-replicates:
  - type: "Standard Object"
    description: "Standard objects are those that are created by Salesforce and included in your account by default."
    convention: "sf_[object_name]"
    example: "sf_account"

  - type: "Custom Object"
    description: "Custom objects are tables created by you that enable you to store info unique to your organization. Refer to the **Custom Objects section** in the [Object Reference guide](https://resources.docs.salesforce.com/sfdc/pdf/object_reference.pdf) for more info."
    convention: "sf_[object_name]__c"
    example: "sf_issue__c"

  - type: "Standard Field"
    description: "Fields are attributes that describe an object. A Standard field is created by Salesforce."
    convention: "[field_name]"
    example: "account_id"

  - type: "Custom Field"
    description: "A Custom field is a field created by you. Refer to the **Custom Fields section** in the [Object Reference guide](https://resources.docs.salesforce.com/sfdc/pdf/object_reference.pdf) for more info."
    convention: "[field_name]__c"
    example: "first_notice__c"

schema-sections:
  - content: |
      In Salesforce's API, "object" is synonymous with "table." When Stitch replicates data from a Salesforce object, a table for that object will be created in your data warehouse. The "fields" contained in an object are the same as columns in a database table.

      **Note**: Tables won't automatically be created in your data warehouse. You must set tables and columns to sync in the {{ app.page-names.int-details }} page first.

      Stitch will replicate the majority of Salesforce objects (with the exception of those [listed here](#unsupported-stitch-objects)). To ensure we can provide you with up-to-date docs, we won't dive into the specifics of the hundreds of Salesforce objects Stitch can replicate.

  - title: "Objects Stitch Replicates"
    anchor: "supported-stitch-objects"
    content: |
      Below you'll find the objects and fields Stitch can replicate, a brief description, and how different table and column types will be named in your data warehouse.

      <table>
      <tr>
      <th width="17%; fixed">Type</th>
      <th width="">Description</th>
      <th width="15%; fixed">Naming Convention</th>
      <th width="20%; fixed">Example</th>
      </tr>
      {% for object in integration.objects-stitch-replicates %}
      <tr>
      <td>{{ object.type }}</td>
      <td>{{ object.description | flatify | markdownify }}</td>
      <td markdown="span">`{{ object.convention }}`</td>
      <td markdown="span">`{{ object.example }}`</td>
      </tr>
      {% endfor %}
      </table>

  - title: "Objects Stitch Doesn't Replicate"
    anchor: "unsupported-stitch-objects"
    content: |
      Stitch will not replicate:

      1. Objects that the authorizing user doesn't have permission to access, and
      2. [External objects](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_external_objects.htm) (which are objects created by you to map to data stored outside of your organization).

  - title: "Object/Field Names & Collision Errors"
    anchor: "names-collision-errors"
    content: |
      In Salesforce, it's possible to have objects and fields with names that use both upper and lower case. For example: `columnName`

      If the uniqueness of the field name is **only in the case** - meaning that the only difference between them is upper and lower case characters - you may encounter field collision errors if:

      1. The data warehouse you're using is **case insensitive** AND doesn't maintain case, and
      2. There's more than one field in the table with the same name

      You can check out the [Destination Comparison Rollup]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl | append: "#comparing-destinations" }}) for more info on how your data warehouse implements case sensitivity.

      #### Collision Example

      An `orders` table contains two columns: `salesOrder` and `salesorder`. These columns are different only in that one has an upper-case `O` and one has a lower-case `o`.

      If the data warehouse doesn't maintain the case, these field names will canonicalize - or be converted - **into the same name.** Because Stitch won't know where to insert the data if both field names are the same, this will result in a `field collision` error.

      You can resolve this error by changing the name of the field in Salesforce to something unique.
---
{% assign integration = page %}
{% include misc/data-files.html %}