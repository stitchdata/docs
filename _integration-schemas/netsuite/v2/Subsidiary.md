---
tap: "netsuite"
version: "2"
name: Subsidiary
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Subsidiary.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Subsidiary
description: |
  The `{{ table.name }}` table contains info about the subsidiary records in your {{ integration.display_name }} account. A subsidiary represents a separate company within your global organization.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "subsidiary"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: receiptAmount
  type: string, number
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
- name: isElimination
  type: boolean, string
  description: ""
- name: accountingBookDetailList
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: tranPrefix
  type: string
  description: ""
- name: logo
  type: varies
  description: ""
- name: purchaseOrderAmount
  type: string, number
  description: ""
- name: purchaseOrderQuantityDiff
  type: string, number
  description: ""
- name: allowPayroll
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: showSubsidiaryName
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: ssnOrTin
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: receiptQuantityDiff
  type: string, number
  description: ""
- name: state
  type: string
  description: ""
- name: addrLanguage
  type: string
  description: ""
- name: classTranslationList
  type: varies
  description: ""
- name: legalName
  type: string
  description: ""
- name: taxRegistrationList
  type: varies
  description: ""
- name: purchaseOrderQuantity
  type: string, number
  description: ""
- name: currency
  type: varies
  description: ""
- name: mainAddress
  type: varies
  description: ""
- name: returnAddress
  type: varies
  description: ""
- name: interCoAccount
  type: varies
  description: ""
- name: nexusList
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: taxFiscalCalendar
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: federalIdNumber
  type: string
  description: ""
- name: fiscalCalendar
  type: varies
  description: ""
- name: edition
  type: string
  description: ""
- name: state1TaxNumber
  type: string
  description: ""
- name: pageLogo
  type: varies
  description: ""
- name: checkLayout
  type: varies
  description: ""
- name: shippingAddress
  type: varies
  description: ""
- name: country
  type: varies
  description: ""
- name: receiptQuantity
  type: string, number
  description: ""
---