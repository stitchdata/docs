---
tap: "netsuite"
version: "2"
name: Opportunity
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Opportunity.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Opportunity
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: shipIsResidential
  type: boolean, string
  description: ""
- name: leadSource
  type: varies
  description: ""
- name: billAddressList
  type: varies
  description: ""
- name: estGrossProfit
  type: string, number
  description: ""
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: syncPartnerTeams
  type: boolean, string
  description: ""
- name: nexus
  type: varies
  description: ""
- name: weightedTotal
  type: string, number
  description: ""
- name: buyingReason
  type: varies
  description: ""
- name: altSalesRangeLow
  type: string, number
  description: ""
- name: accountingBookDetailList
  type: varies
  description: ""
- name: salesRep
  type: varies
  description: ""
- name: recurAnnually
  type: string, number
  description: ""
- name: competitorsList
  type: varies
  description: ""
- name: partner
  type: varies
  description: ""
- name: tax2Total
  type: string, number
  description: ""
- name: isBudgetApproved
  type: boolean, string
  description: ""
- name: exchangeRate
  type: string, number
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: recurMonthly
  type: string, number
  description: ""
- name: daysOpen
  type: string, integer
  description: ""
- name: itemList
  type: varies
  description: ""
- name: expectedCloseDate
  type: string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: partnersList
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: source
  type: string
  description: ""
- name: entityTaxRegNum
  type: varies
  description: ""
- name: taxDetailsOverride
  type: boolean, string
  description: ""
- name: probability
  type: string, number
  description: ""
- name: altSalesRangeHigh
  type: string, number
  description: ""
- name: projectedTotal
  type: string, number
  description: ""
- name: vatRegNum
  type: string
  description: ""
- name: closeDate
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: winLossReason
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: estGrossProfitPercent
  type: string, number
  description: ""
- name: taxPointDate
  type: string
  description: ""
- name: totalCostEstimate
  type: string, number
  description: ""
- name: rangeLow
  type: string, number
  description: ""
- name: externalId
  type: string
  description: ""
- name: subsidiaryTaxRegNum
  type: varies
  description: ""
- name: taxRegOverride
  type: boolean, string
  description: ""
- name: status
  type: string
  description: ""
- name: salesGroup
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: salesTeamList
  type: varies
  description: ""
- name: projAltSalesAmt
  type: string, number
  description: ""
- name: salesReadiness
  type: varies
  description: ""
- name: recurQuarterly
  type: string, number
  description: ""
- name: createdDate
  type: string
  description: ""
- name: tranDate
  type: string
  description: ""
- name: syncSalesTeams
  type: boolean, string
  description: ""
- name: rangeHigh
  type: string, number
  description: ""
- name: tranId
  type: string
  description: ""
- name: oneTime
  type: string, number
  description: ""
- name: taxDetailsList
  type: varies
  description: ""
- name: buyingTimeFrame
  type: varies
  description: ""
- name: shippingAddress
  type: varies
  description: ""
- name: shipAddressList
  type: varies
  description: ""
- name: contribPct
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: entity
  type: varies
  description: ""
- name: forecastType
  type: varies
  description: ""
- name: currencyName
  type: string
  description: ""
- name: estimatedBudget
  type: string, number
  description: ""
- name: taxTotal
  type: string, number
  description: ""
- name: recurWeekly
  type: string, number
  description: ""
- name: actionItem
  type: string
  description: ""
- name: memo
  type: string
  description: ""
- name: billingAddress
  type: varies
  description: ""
- name: entityStatus
  type: varies
  description: ""
- name: job
  type: varies
  description: ""
