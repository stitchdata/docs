---
tap: "netsuite"
# version: "1.0"

name: "Opportunity"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Opportunity.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "anything"
    description: ""

  - name: "accountingBookDetailList"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "billingAddress"
    type: "anything"
    description: ""

  - name: "buyingReason"
    type: "anything"
    description: ""

  - name: "buyingTimeFrame"
    type: "anything"
    description: ""

  - name: "closeDate"
    type: "date-time"
    description: ""

  - name: "competitorsList"
    type: "anything"
    description: ""

  - name: "contribPct"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "anything"
    description: ""

  - name: "currencyName"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "daysOpen"
    type: "integer, string"
    description: ""

  - name: "department"
    type: "anything"
    description: ""

  - name: "entity"
    type: "anything"
    description: ""

  - name: "entityStatus"
    type: "anything"
    description: ""

  - name: "entityTaxRegNum"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isBudgetApproved"
    type: "boolean, string"
    description: ""

  - name: "itemList"
    type: "anything"
    description: ""

  - name: "job"
    type: "anything"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "leadSource"
    type: "anything"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nexus"
    type: "anything"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "oneTime"
    type: "number, string"
    description: ""

  - name: "partner"
    type: "anything"
    description: ""

  - name: "partnersList"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "salesReadiness"
    type: "anything"
    description: ""

  - name: "salesRep"
    type: "anything"
    description: ""

  - name: "salesTeamList"
    type: "anything"
    description: ""

  - name: "shipAddressList"
    type: "anything"
    description: ""

  - name: "shipIsResidential"
    type: "boolean, string"
    description: ""

  - name: "shippingAddress"
    type: "anything"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""

  - name: "subsidiaryTaxRegNum"
    type: "anything"
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
    type: "anything"
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
    type: "anything"
    description: ""
---
