---
tap: "netsuite"
version: "1"

name: "BillingAccount"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/billingaccount.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/BillingAccount.json"
description: |
  The `{{ table.name }}` table contains info about the billing accounts in your {{ integration.display_name }} account. A billing account is a record used to show all billing information for a customer or subcustomer. A billing account contains billing-specific information, including billing schedule, default payment terms, bill-to address, and currency.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "billing-account"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "billing-account-id"

  - name: "_class"
    type: "varies"
    description: ""

  - name: "billingSchedule"
    type: "varies"
    description: ""

  - name: "cashSaleForm"
    type: "varies"
    description: ""

  - name: "createdBy"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "customerDefault"
    type: "boolean, string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "varies"
    description: ""

  - name: "idNumber"
    type: "string"
    description: ""

  - name: "inactive"
    type: "boolean, string"
    description: ""

  - name: "invoiceForm"
    type: "varies"
    description: ""

  - name: "lastBillCycleDate"
    type: "date-time"
    description: ""

  - name: "lastBillDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nextBillCycleDate"
    type: "date-time"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---