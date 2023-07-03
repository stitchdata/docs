---
tap: "netsuite"
version: "2"
name: Vendor
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Vendor.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Vendor
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: category
  type: varies
  description: ""
- name: rolesList
  type: varies
  description: ""
- name: middleName
  type: string
  description: ""
- name: faxTransactions
  type: boolean, string
  description: ""
- name: emailPreference
  type: varies
  description: ""
- name: password2
  type: string
  description: ""
- name: receiptAmount
  type: string, number
  description: ""
- name: eligibleForCommission
  type: boolean, string
  description: ""
- name: fax
  type: string
  description: ""
- name: email
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: isPerson
  type: boolean, string
  description: ""
- name: representingSubsidiary
  type: varies
  description: ""
- name: vatRegNumber
  type: string
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
- name: currencyList
  type: varies
  description: ""
- name: subscriptionsList
  type: varies
  description: ""
- name: isJobResourceVend
  type: boolean, string
  description: ""
- name: terms
  type: varies
  description: ""
- name: password
  type: string
  description: ""
- name: phone
  type: string
  description: ""
- name: purchaseOrderAmount
  type: string, number
  description: ""
- name: isAccountant
  type: boolean, string
  description: ""
- name: purchaseOrderQuantityDiff
  type: string, number
  description: ""
- name: altPhone
  type: string
  description: ""
- name: sendEmail
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: mobilePhone
  type: string
  description: ""
- name: firstName
  type: string
  description: ""
- name: creditLimit
  type: string, number
  description: ""
- name: salutation
  type: string
  description: ""
- name: incoterm
  type: varies
  description: ""
- name: payablesAccount
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: receiptQuantityDiff
  type: string, number
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: legalName
  type: string
  description: ""
- name: taxRegistrationList
  type: string
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: defaultTaxReg
  type: string
  description: ""
- name: balancePrimary
  type: string, number
  description: ""
- name: title
  type: string
  description: ""
- name: requirePwdChange
  type: boolean, string
  description: ""
- name: homePhone
  type: string
  description: ""
- name: predConfidence
  type: string, number
  description: ""
- name: purchaseOrderQuantity
  type: string, number
  description: ""
- name: currency
  type: varies
  description: ""
- name: balance
  type: string, number
  description: ""
- name: unbilledOrdersPrimary
  type: string, number
  description: ""
- name: openingBalance
  type: string, number
  description: ""
- name: unbilledOrders
  type: string, number
  description: ""
- name: giveAccess
  type: boolean, string
  description: ""
- name: externalId
  type: string
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
- name: printOnCheckAs
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: emailTransactions
  type: boolean, string
  description: ""
- name: altName
  type: string
  description: ""
- name: altEmail
  type: string
  description: ""
- name: image
  type: varies
  description: ""
- name: predictedDays
  type: string, integer
  description: ""
- name: openingBalanceDate
  type: string
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: pricingScheduleList
  type: varies
  description: ""
- name: workCalendar
  type: varies
  description: ""
- name: companyName
  type: string
  description: ""
- name: printTransactions
  type: boolean, string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: laborCost
  type: string, number
  description: ""
- name: entityId
  type: string
  description: ""
- name: expenseAccount
  type: varies
  description: ""
- name: taxIdNum
  type: string
  description: ""
- name: is1099Eligible
  type: boolean, string
  description: ""
- name: receiptQuantity
  type: string, number
  description: ""
- name: openingBalanceAccount
  type: varies
  description: ""
- name: taxItem
  type: varies
  description: ""
- name: bcn
  type: string
  description: ""
---