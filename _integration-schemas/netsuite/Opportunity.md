---
tap: "netsuite"
version: "1"

name: "Opportunity"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/opportunity.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Opportunity.json"
description: |
  The `{{ table.name }}` table contains info about the opportunities in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "opportunity"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "opportunity-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "accountingBookDetailList"
    type: "varies"
    description: ""

  - name: "actionItem"
    type: "string"
    description: ""

  - name: "altSalesRangeHigh"
    type: "number, string"
    description: ""

  - name: "altSalesRangeLow"
    type: "number, string"
    description: ""

  - name: "billAddressList"
    type: "varies"
    description: ""

  - name: "billingAddress"
    type: "varies"
    description: ""

  - name: "buyingReason"
    type: "varies"
    description: ""

  - name: "buyingTimeFrame"
    type: "varies"
    description: ""

  - name: "closeDate"
    type: "date-time"
    description: ""

  - name: "competitorsList"
    type: "varies"
    description: ""

  - name: "contribPct"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "currencyName"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "daysOpen"
    type: "integer, string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "entity"
    type: "varies"
    description: ""

  - name: "entityStatus"
    type: "varies"
    description: ""

  - name: "entityTaxRegNum"
    type: "varies"
    description: ""

  - name: "estGrossProfit"
    type: "number, string"
    description: ""

  - name: "estGrossProfitPercent"
    type: "number, string"
    description: ""

  - name: "estimatedBudget"
    type: "number, string"
    description: ""

  - name: "exchangeRate"
    type: "number, string"
    description: ""

  - name: "expectedCloseDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "forecastType"
    type: "varies"
    description: ""

  - name: "isBudgetApproved"
    type: "boolean, string"
    description: ""

  - name: "itemList"
    type: "varies"
    description: ""

  - name: "job"
    type: "varies"
    description: ""

  - name: "leadSource"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nexus"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "oneTime"
    type: "number, string"
    description: ""

  - name: "partner"
    type: "varies"
    description: ""

  - name: "partnersList"
    type: "varies"
    description: ""

  - name: "probability"
    type: "number, string"
    description: ""

  - name: "projAltSalesAmt"
    type: "number, string"
    description: ""

  - name: "projectedTotal"
    type: "number, string"
    description: ""

  - name: "rangeHigh"
    type: "number, string"
    description: ""

  - name: "rangeLow"
    type: "number, string"
    description: ""

  - name: "recurAnnually"
    type: "number, string"
    description: ""

  - name: "recurMonthly"
    type: "number, string"
    description: ""

  - name: "recurQuarterly"
    type: "number, string"
    description: ""

  - name: "recurWeekly"
    type: "number, string"
    description: ""

  - name: "salesGroup"
    type: "varies"
    description: ""

  - name: "salesReadiness"
    type: "varies"
    description: ""

  - name: "salesRep"
    type: "varies"
    description: ""

  - name: "salesTeamList"
    type: "varies"
    description: ""

  - name: "shipAddressList"
    type: "varies"
    description: ""

  - name: "shipIsResidential"
    type: "boolean, string"
    description: ""

  - name: "shippingAddress"
    type: "varies"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "subsidiaryTaxRegNum"
    type: "varies"
    description: ""

  - name: "syncPartnerTeams"
    type: "boolean, string"
    description: ""

  - name: "syncSalesTeams"
    type: "boolean, string"
    description: ""

  - name: "tax2Total"
    type: "number, string"
    description: ""

  - name: "taxDetailsList"
    type: "varies"
    description: ""

  - name: "taxDetailsOverride"
    type: "boolean, string"
    description: ""

  - name: "taxRegOverride"
    type: "boolean, string"
    description: ""

  - name: "taxTotal"
    type: "number, string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "totalCostEstimate"
    type: "number, string"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "tranId"
    type: "string"
    description: ""

  - name: "vatRegNum"
    type: "string"
    description: ""

  - name: "weightedTotal"
    type: "number, string"
    description: ""

  - name: "winLossReason"
    type: "varies"
    description: ""
---