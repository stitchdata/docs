---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1"

name: "campaign"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/campaign.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/campaigns.py
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Retrieve campaigns"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/campaign.htm"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    #description: "The campaign ID."

  - name: "modifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the campaign was last modified."

  - name: "createdDate"
    type: "date-time"
    description: "The date and time the campaign was created."

  - name: "campaignCode"
    type: "string"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: "A description of the campaign."

  - name: "name"
    type: "string"
    description: "The name of the campaign."
---