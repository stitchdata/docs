---
tap: "netsuite"
version: "2"
name: Customer
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Customer.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Customer
description: |
  The `{{ table.name }}` table contains info about customers.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "customer"

replication-method: "Key-based Incremental"
attributes:
- name: assignedWebSite
  type: string
  description: ""
- name: leadSource
  type: varies
  description: ""
- name: category
  type: varies
  description: ""
- name: contactRolesList
  type: varies
  description: ""
- name: shipComplete
  type: boolean, string
  description: ""
- name: middleName
  type: string
  description: ""
- name: faxTransactions
  type: boolean, string
  description: ""
- name: consolDepositBalance
  type: string, number
  description: ""
- name: emailPreference
  type: varies
  description: ""
- name: password2
  type: string
  description: ""
- name: consolBalance
  type: string, number
  description: ""
- name: negativeNumberFormat
  type: varies
  description: ""
- name: fax
  type: string
  description: ""
- name: consolAging3
  type: string, number
  description: ""
- name: email
  type: string
  description: ""
- name: reminderDays
  type: string, integer
  description: ""
- name: consolUnbilledOrders
  type: string, number
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: syncPartnerTeams
  type: boolean, string
  description: ""
- name: isPerson
  type: boolean, string
  description: ""
- name: drAccount
  type: varies
  description: ""
- name: depositBalance
  type: string, number
  description: ""
- name: visits
  type: string, integer
  description: ""
- name: representingSubsidiary
  type: varies
  description: ""
- name: vatRegNumber
  type: string
  description: ""
- name: stage
  type: varies
  description: ""
- name: buyingReason
  type: varies
  description: ""
- name: overrideCurrencyFormat
  type: boolean, string
  description: ""
- name: aging
  type: string, number
  description: ""
- name: addressbookList
  type: varies
  description: ""
- name: accountNumber
  type: string
  description: ""
- name: defaultAddress
  type: string
  description: ""
- name: receivablesAccount
  type: varies
  description: ""
- name: salesRep
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: currencyList
  type: varies
  description: ""
- name: subscriptionsList
  type: varies
  description: ""
- name: terms
  type: varies
  description: ""
- name: creditCardsList
  type: varies
  description: ""
- name: partner
  type: varies
  description: ""
- name: displaySymbol
  type: string
  description: ""
- name: password
  type: string
  description: ""
- name: phone
  type: string
  description: ""
- name: consolOverdueBalance
  type: string, number
  description: ""
- name: isBudgetApproved
  type: boolean, string
  description: ""
- name: altPhone
  type: string
  description: ""
- name: creditHoldOverride
  type: varies
  description: ""
- name: sendEmail
  type: boolean, string
  description: ""
- name: prefCCProcessor
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: accessRole
  type: varies
  description: ""
- name: mobilePhone
  type: string
  description: ""
- name: groupPricingList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: resaleNumber
  type: string
  description: ""
- name: firstName
  type: string
  description: ""
- name: creditLimit
  type: string, number
  description: ""
- name: lastVisit
  type: string
  description: ""
- name: salutation
  type: string
  description: ""
- name: thirdPartyCarrier
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: webLead
  type: string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: partnersList
  type: varies
  description: ""
- name: consolAging
  type: string, number
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: taxRegistrationList
  type: string
  description: ""
- name: consolDaysOverdue
  type: string, integer
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: keywords
  type: string
  description: ""
- name: defaultTaxReg
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: requirePwdChange
  type: boolean, string
  description: ""
- name: monthlyClosing
  type: varies
  description: ""
- name: homePhone
  type: string
  description: ""
- name: numberFormat
  type: varies
  description: ""
- name: downloadList
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: symbolPlacement
  type: varies
  description: ""
- name: aging1
  type: string, number
  description: ""
- name: consolAging4
  type: string, number
  description: ""
- name: itemPricingList
  type: varies
  description: ""
- name: referrer
  type: string
  description: ""
- name: endDate
  type: string
  description: ""
- name: balance
  type: string, number
  description: ""
- name: firstVisit
  type: string
  description: ""
- name: sourceWebSite
  type: string
  description: ""
- name: openingBalance
  type: string, number
  description: ""
- name: unbilledOrders
  type: string, number
  description: ""
- name: fxAccount
  type: varies
  description: ""
- name: daysOverdue
  type: string, integer
  description: ""
- name: territory
  type: varies
  description: ""
- name: giveAccess
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: defaultOrderPriority
  type: string, number
  description: ""
- name: language
  type: varies
  description: ""
- name: salesGroup
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: billPay
  type: boolean, string
  description: ""
- name: lastName
  type: string
  description: ""
- name: alcoholRecipientType
  type: varies
  description: ""
- name: consolAging2
  type: string, number
  description: ""
- name: printOnCheckAs
  type: string
  description: ""
- name: thirdPartyAcct
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: salesTeamList
  type: varies
  description: ""
- name: salesReadiness
  type: varies
  description: ""
- name: emailTransactions
  type: boolean, string
  description: ""
- name: altName
  type: string
  description: ""
- name: aging4
  type: string, number
  description: ""
- name: overdueBalance
  type: string, number
  description: ""
- name: aging2
  type: string, number
  description: ""
- name: altEmail
  type: string
  description: ""
- name: image
  type: varies
  description: ""
- name: openingBalanceDate
  type: string
  description: ""
- name: priceLevel
  type: varies
  description: ""
- name: taxable
  type: boolean, string
  description: ""
- name: clickStream
  type: string
  description: ""
- name: lastPageVisited
  type: string
  description: ""
- name: campaignCategory
  type: varies
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: companyName
  type: string
  description: ""
- name: consolAging1
  type: string, number
  description: ""
- name: buyingTimeFrame
  type: varies
  description: ""
- name: printTransactions
  type: boolean, string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: contribPct
  type: string
  description: ""
- name: defaultAllocationStrategy
  type: string
  description: ""
- name: aging3
  type: string, number
  description: ""
- name: estimatedBudget
  type: string, number
  description: ""
- name: entityId
  type: string
  description: ""
- name: thirdPartyZipcode
  type: string
  description: ""
- name: taxExempt
  type: boolean, string
  description: ""
- name: entityStatus
  type: varies
  description: ""
- name: shippingItem
  type: varies
  description: ""
- name: openingBalanceAccount
  type: varies
  description: ""
- name: taxItem
  type: varies
  description: ""
- name: thirdPartyCountry
  type: varies
  description: ""
---