---
tap: "salesforce"
version: "1.0"

name: "opportunity"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm
singer-schema: 
description: |
  The `opportunity` table contains info about your opportunities, which are sales or pending deals.

notes: 

replication-method: "Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The opportunity ID."

  - name: "systemModStamp"
    type: "date-time"
    replication-key: true
    description: "The time when a user or automated process (ex: a trigger) last modified the opportunity."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the opportunity."
    # foreign-key:
    #   - table: "account"
    #     attribute: "id"

  - name: "amount"
    type: "number"
    description: "The estimated total sale amount. For opportunities with products, the amount will be the total sum of the related products."

  - name: "campaignId"
    type: "string"
    description: "The ID of a related campaign. **Only defined for organizations where the campaign feature is enabled.**"

  - name: "closeDate"
    type: "date-time"
    description: "The date the opportunity is expected to close."

  - name: "connectionReceivedId"
    type: "string"
    description: "The ID of the `PartnerNetworkConnection` that shared the opportunity record with your organization. **Only available if Salesforce to Salesforce is enabled.**"

  - name: "connectionSentId"
    type: "string"
    description: "The ID of the `PartnerNetworkConnection` that you shared the opportunity record with. **Deprecated by Salesforce.**"

  - name: "currencyIsoCode"
    type: "string"
    description: "The ISO code for any currency allowed by the organization. **Only available for organizations with the multicurrency feature enabled.**"

  - name: "description"
    type: "string"
    description: "The description of the opportunity."

  - name: "expectedRevenue"
    type: "number"
    description: "Amount equal to the product of the opportunity `amount` field and the `probability`."

  - name: "fiscal"
    type: "string"
    description: "The name of the fiscal quarter or period in which the opportunity `closeDate` falls. Applicable if fiscal years are not enabled."

  - name: "fiscalQuarter"
    type: "integer"
    description: "The numerical representation of the fiscal quarter. Possible values are `1`, `2`, `3`, or `4`."

  - name: "fiscalYear"
    type: "integer"
    description: "The fiscal year."

  - name: "forecastCategory"
    type: "string"
    doc-link: "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm?search_text=opportunity#i1455578"
    description: "The forecast category for the opportunity."

  - name: "forecastCategoryName"
    type: "string"
    description: "The name of the forecast category for the opportunity."

  - name: "hasOpenActivity"
    type: "boolean"
    description: "Indicates if the opportunity has associated line items (`true`) or not (`false`)."

  - name: "hasOpportunityLineItem"
    type: "boolean"
    doc-link: "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm?search_text=opportunity#i1455618"
    description: "Indicates if the opportunity has an open event (`true`) or not (`false`). Opportunities can have opportunity line items only if the opportunity has a price book."

  - name: "hasOverdueTask"
    type: "boolean"
    description: "Indicates if an opportunity has an overdue task (`true`) or not (`false`)."

  - name: "isClosed"
    type: "boolean"
    description: "Indicates if the opportunity is closed (`true`) or not (`false`)."

  - name: "isDeleted"
    type: "boolean"
    description: "Indicates if the opportunity has been moved to the Recycle Bin (`true`) or not (`false`)."

  - name: "isExcludedFromTerritory2Filter"
    type: "boolean"
    description: "Indicates if the opportunity is exclued (`true`) or included (`false`) each time the APEX filter is executed."

  - name: "isSplit"
    type: "boolean"
    description: "Indicates whether credit for the opportunity is split between team members (`true`) or not (`false`)."

  - name: "isWon"
    type: "boolean"
    description: "Indicates if the opportunity is won (`true`) or not (`false`)."

  - name: "lastActivityDate"
    type: "date-time"
    description: "The due date of the most recently logged event OR the most recently closed task associated with the opportunity, whichever is more recent."

  - name: "lastReferenceDate"
    type: "date-time"
    description: "The date a record associated with the opportunity was last viewed."

  - name: "lastViewedDate"
    type: "date-time"
    description: "The date the opportunity was last viewed."

  - name: "leadSource"
    type: "string"
    description: "The source from which the opportunity was obtained. For example: `Advertisement`, `Trade Show`"

  - name: "name"
    type: "string"
    description: "The name of the opportunity."

  - name: "nextStep"
    type: "string"
    description: "The description of the next task in closing the opportunity."

  - name: "ownerId"
    type: "string"
    description: "The ID of the user who has been assigned to work the opportunity."

  - name: "pricebook2Id"
    type: "string"
    description: "The ID of the related Pricebook2 object. **Only available if the products feature is enabled for an organization.**"

  - name: "pricebookId"
    type: "string"
    description: "The ID of the related Pricebook object. **Deprecated by Salesforce.**"

  - name: "probability"
    type: "integer"
    description: "The percentage of estimated confidence in closing the opportunity."

  - name: "recordTypeId"
    type: "string"
    description: "The ID of the record type assigned to the opportunity."

  - name: "stageName"
    type: "string"
    description: "The current stage of the opportunity."

  - name: "syncedQuoteId"
    type: "string"
    description: "The ID of the quote that syncs with the opportunity."

  - name: "territory2Id"
    type: "string"
    description: "The ID of the territory assigned to the opportunity. **Only available if Enterprise Territory Management is enabled.**"

  - name: "totalOpportunityQuantity"
    type: "number"
    description: "The number of items included in the opportunity."

  - name: "type"
    type: "string"
    description: "The type of opportunity. For example: `Existing Business`"
---