---
tap: "eloqua"
version: "1"

name: "campaigns"
key: "campaigns"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-assets-campaigns-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account. Campaigns are comprised of different elements (such as segments, emails, landing pages, etc.) that are used to perform a variety of functions.

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of campaigns"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the campaign was last updated."

  - name: "accessedAt"
    type: "date-time"
    description: "The date and time the campaign was last accessed, expressed in Unix time."

  - name: "actualCost"
    type: "string"
    description: "The campaign's actual cost."

  - name: "badgeId"
    type: "string"
    description: "The badge ID of the campaign."

  - name: "budgetedCost"
    type: "string"
    description: "The campaign's projected cost."

  - name: "campaignCategory"
    type: "string"
    description: |
      Defines whether a campaign is simple or multi-step. Possible values are:

      - `emailMarketing` - Used for simple campaigns
      - `contact` - Used for multi-step campaigns

  - name: "campaignType"
    type: "string"
    description: "The campaign's type."

  - name: "clrEndDate"
    type: "date-time"
    description: "The end date of the clr."

  - name: "createdAt"
    type: "date-time"
    description: "The date and time the campaign was created, expressed in Unix time."

  - name: "createdBy"
    type: "string"
    description: "The ID of the user who created the campaign."

  - name: "crmId"
    type: "string"
    description: "The ID of the customer relationship management application."

  - name: "currentStatus"
    type: "string"
    description: |
      The campaign's current status. Possible values are:

      - `Active`
      - `Draft`
      - `Scheduled`
      - `Completed`

  - name: "depth"
    type: "string"
    description: |
       Level of detail returned by the request. {{ integration.display_name }} APIs can retrieve entities at three different levels of depth: `minimal`, `partial`, and `complete`. Any other values passed are reset to `complete` by default. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/index.html#CSHID=RequestDepth){:target="new"} for more info.

  - name: "description"
    type: "string"
    description: "The description of the campaign."

# This looks like a full list of subproperties for the campaign (CampaignElement)
  # - name: "elements"
  #   type: "array"
  #   description: ""
  #   subattributes:
  #     - name: "value"
  #       type: "anything"
  #       description: ""

  - name: "endAt"
    type: "date-time"
    description: "The date and time the campaign will end."

  # - name: "fieldValues"
  #   type: "array"
  #   description: "Array containing type and id values for all of the contactFields associated with a given contact. For campaigns, "fieldValues" include all custom campaign fields (type, id, value)."
  #   subattributes:
  #     - name: "value"
  #       type: "anything"
        # description: ""

  - name: "firstActivation"
    type: "date-time"
    description: "The date and time the campaign was originally activated."

  - name: "folderId"
    type: "string"
    description: "The ID of the folder containing the campaign."

  - name: "isEmailMarketingCampaign"
    type: "string"
    description: "Indicates whether the campaign is an email marketing campaign."

  - name: "isIncludedInROI"
    type: "string"
    description: "Indicates whether the campaign is included in return on investment."

  - name: "isMemberAllowedReEntry"
    type: "string"
    description: "Indicates whether members are allowed to re-enter the campaign."

  - name: "isReadOnly"
    type: "string"
    description: "Indicates whether the campaign is read only."

  - name: "isSyncedWithCRM"
    type: "string"
    description: "Indicates whether the campaign is synced with a customer relationship management application."

  - name: "memberCount"
    type: "string"
    description: "The amount of members in the campaign."

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "permissions"
    type: "array"
    description: "The permissions for the campaign granted to your current instance."
    subattributes:
      - name: "value"
        type: "string"
        description: "The permission for the campaign."

  - name: "product"
    type: "string"
    description: "The campaign's product value."

  - name: "region"
    type: "string"
    description: "The campaign's region value."

  - name: "runAsUserId"
    type: "string"
    description: "The ID of the user to activate the campaign."

  - name: "scheduledFor"
    type: "date-time"
    description: "The date the campaign is scheduled."

  - name: "sourceTemplateId"
    type: "string"
    description: "The ID of the template used to create the asset."

  - name: "startAt"
    type: "date-time"
    description: "The date time for which the campaign will activate."

  - name: "type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."

  - name: "updatedBy"
    type: "string"
    description: "The ID of the user that last updated the campaign."
---