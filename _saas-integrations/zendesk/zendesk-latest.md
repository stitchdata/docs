---
title: Zendesk
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
author: "Stitch"
author-url: "https://www.stitchdata.com"
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
      
  - **To be on a specific Zendesk plan, if replicating ticket forms.** In this case, you need to be on an Enterprise Zendesk plan or a Professional Zendesk plan with the ticket forms add-on to replicate the `ticket_forms` table.
  
     All other tables, with the exception of `ticket_forms`, will be available for replication even if you aren't on either of these plans.

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
  - title: "Replicating ticket forms"
    anchor: "replicate-ticket-forms"
    content: |
      - Only available for Professional and Enterprise plans

      https://support.zendesk.com/hc/en-us/articles/203661616-Creating-ticket-forms-to-support-multiple-request-types-Professional-add-on-and-Enterprise-

  - title: "Replicating user and organization custom fields"
    anchor: "replicate-user-organization-custom-fields"
    content: |
      - Only able to replicate User and Organization custom fields for Team, Professional, and Enterprise plans

      https://support.zendesk.com/hc/en-us/articles/203662066-Adding-custom-fields-to-users

# -------------------------- #
#     Integration Tables     #
# -------------------------- #
---
{% assign integration = page %}
{% include misc/data-files.html %}
