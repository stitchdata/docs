---
title: Zendesk (v1.0)
permalink: /integrations/saas/zendesk
tags: [saas_integrations]
keywords: zendesk, integration, schema, etl zendesk, zendesk etl, zendesk schema
summary: "Connection instructions, replication info, and schema details for Stitch's Zendesk integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zendesk"
display_name: "Zendesk"
singer: true
status-url: "https://status.zendesk.com/"
repo-url: "https://github.com/singer-io/tap-zendesk"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "60 minutes"
tier: "Paid"
icon: /images/integrations/icons/zendesk.svg

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in Zendesk**. Some data types in Zendesk may only be accessed with Admin permissions. For example: To replicate ticket metric or tag data, Zendesk's API requires a user with Admin permissions.

      To ensure you can replicate all the data you need, we recommend a user with Admin permissions set up the integration.
      
  - item: |
      **A specific Zendesk plan if replicating ticket forms or SLA policies:**

         - To replicate **SLA policies**, you must be on an Enterprise or Professional Zendesk plan.
         - To replicate **ticket forms**, you must be on an Enterprise Zendesk plan, or a Professional Zendesk plan with the ticket forms add-on.

      All other tables, with the exception of `sla_policies` and `ticket_forms` will be available for replication even if you aren't on either of these Zendesk plans.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Zendesk Subdomain** field, enter your Zendesk site prefix. For example: For `stitchdata.zendesk.com`, only `stitchdata` would be entered into this field.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access Zendesk"
    anchor: "grant-stitch-authorization"
    content: |
      {% include note.html type="single-line" content="**Note**: A Zendesk user with Admin permissions must complete this step." %}

      1. Next, you'll be prompted to sign into your Zendesk account.
      2. After the authorization process is successfully completed, you'll be directed back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#        Replication         #
# -------------------------- #

replication-sections:
  - title: "Replicating SLA policies and ticket forms"
    anchor: "replicate-ticket-forms"
    content: |
      To replicate SLA policies and ticket forms - or the `sla_policies` and `ticket_forms` tables - you need to be on an Enterprise or Professional Zendesk plan. [To replicate `ticket_forms` on a Professional plan](https://support.zendesk.com/hc/en-us/articles/203661616-Creating-ticket-forms-to-support-multiple-request-types-Professional-add-on-and-Enterprise-){:target="_blank"}, you'll also need to have the ticket forms add-on enabled in your Zendesk account.

      If you set either table to replicate and don't meet the requirements listed above, an error similar to the following will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}):

      ```
      tap - INFO replicated 0 records from "ticket_forms" endpoint
      tap - CRITICAL {"error": {"message": "You do not have access to this page. Please contact the account owner of this help desk for further help.", "title": "Forbidden"}}
      ```

      To resolve the error, de-select the appropriate table(s). Reach out to Zendesk if you have questions about your Zendesk plan.
      

  - title: "Replicating user and organization custom fields"
    anchor: "replicate-user-organization-custom-fields"
    content: |
      To replicate custom fields for Users and Organizations - or the `users` and `organizations` tables - [you need to be on an Enterprise, Professional, or Team Zendesk plan](https://support.zendesk.com/hc/en-us/articles/203662066-Adding-custom-fields-to-users){:target="_blank"}.

      If you set custom fields in the `users` or `organizations` tables to replicate and don't meet the requirements listed above, an error similar to the following will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}):

      ```
      tap - WARNING The account credentials supplied do not have access to `organizations` custom fields.
      tap - WARNING The account credentials supplied do not have access to `users` custom fields.
      ```

      To resolve the error, de-select the appropriate field(s). Reach out to Zendesk if you have questions about your Zendesk plan.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #
---
{% assign integration = page %}
{% include misc/data-files.html %}
