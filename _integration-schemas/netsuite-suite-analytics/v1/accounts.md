---
tap: "netsuite-suite-analytics"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/account.html"
description: |
  The `{{ table.name }}` table contains info about the accounts in the Chart of Accounts in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the account was last modified."

  - name: "account_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The account ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "account-id"

  - name: "account_extid"
    type: "string"
    description: "The account's external ID."

  - name: "accountnumber"
    type: "string"
    description: "The account number."

  - name: "cashflow_rate_type"
    type: "string"
    description: "The cash flow rate type for the account."

  - name: "category_1099_misc"
    type: "string"
    description: "The 1099-MISC category for the account."

  - name: "category_1099_misc_mthreshold"
    type: "number"
    description: "The 1099-MISC category for the account."

  - name: "class_id"
    type: "integer"
    description: "The class for the account."
    foreign-key-id: "class-id"

  - name: "currency_id"
    type: "integer"
    foreign-key-id: "currency-id"
    description: "The ID of the currency for funds in the account."

  - name: "deferral_account_id"
    type: "integer"
    description: "The deferral account for the account."
    foreign-key-id: "account-id"

  - name: "department_id"
    type: "integer"
    description: "The department with access to the account."
    foreign-key-id: "department-id"

  - name: "description"
    type: "string"
    description: "The account description."

  - name: "full_description"
    type: "string"
    description: "The full account description."

  - name: "full_name"
    type: "string"
    description: "The full name for the account."

  - name: "general_rate_type"
    type: "string"
    description: "The general rate type for the account."

  - name: "is_balancesheet"
    type: "string"
    description: ""


  - name: "is_included_in_elimination"
    type: "string"
    description: ""


  - name: "is_included_in_reval"
    type: "string"
    description: ""


  - name: "is_including_child_subs"
    type: "string"
    description: "Indicates whether the account is shared with all sub-subsidiaries associated with each subsidiary associated with the account."

  - name: "is_leftside"
    type: "string"
    description: ""


  - name: "is_summary"
    type: "string"
    description: ""


  - name: "isinactive"
    type: "string"
    description: "Indicates if the account is inactive."

  - name: "legal_name"
    type: "string"
    description: |
      The legal name of the account. **Note**: This requires that the **Use Legal Name in Accounting** preference is enabled in NetSuite.

  - name: "location_id"
    type: "integer"
    description: "The location with access to the account."
    foreign-key-id: "location-id"

  - name: "name"
    type: "string"
    description: "The account name as it displays on reports."

  - name: "openbalance"
    type: "integer"
    description: "The open balance for the account."

  - name: "parent_id"
    type: "integer"
    description: "The parent account."
    foreign-key-id: "account-id"

  - name: "type_name"
    type: "string"
    description: "The account type."

  - name: "type_sequence"
    type: "integer"
    description: ""

---