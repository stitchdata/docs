---
tap: "netsuite"
version: "2"
name: BillingAccount
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BillingAccount.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/BillingAccount
description: |
  The `{{ table.name }}` table contains info about the billing accounts in your {{ integration.display_name }} account. A billing account is a record used to show all billing information for a customer or subcustomer. A billing account contains billing-specific information, including billing schedule, default payment terms, bill-to address, and currency.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "billing-account"

replication-method: "Full Table"

attributes:
- name: inactive
  type: boolean, string
  description: ""
- name: department
  type: varies
  description: ""
- name: billingSchedule
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: cashSaleForm
  type: varies
  description: ""
- name: createdBy
  type: string
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: frequency
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: idNumber
  type: string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: customer
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: invoiceForm
  type: varies
  description: ""
- name: customerDefault
  type: boolean, string
  description: ""
- name: nextBillCycleDate
  type: string
  description: ""
- name: externalId
  type: string
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
- name: lastBillCycleDate
  type: string
  description: ""
- name: createdDate
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
- name: lastBillDate
  type: string
  description: ""
---