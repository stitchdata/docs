---
tap: "netsuite"
version: "1.0"

name: "Account"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/account.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Account.json"
description: |
  The `{{ table.name }}` table contains info about the accounts in the Chart of Accounts in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "account"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "_class"
    type: "varies"
    description: ""

  - name: "acctName"
    type: "string"
    description: "The account name as it displays on reports."

  - name: "acctNumber"
    type: "string"
    description: "The account number."

  - name: "acctType"
    type: "varies"
    description: |
      The account type. According to [{{ integration.display_name }}'s 2018.1 Schema Browser]({{ table.doc-link }}){:target="new"}, account type codes are:

      - 0 - Bank
      - 1 - Accts Receivable
      - 2 - Inventory
      - 4 - Other Curr Assets
      - 5 - Fixed Assets
      - 6 - Accum Deprec.
      - 8 - Other Assets
      - 10 - Accts Payable
      - 12 - Oth Curr Liab. 
      - 14 - Long Term Liab.
      - 16 - Equity-No Close
      - 18 - Retained Earn
      - 19 - Equity-Closes
      - 21 - Income
      - 23 - COGS
      - 24 - Expense
      - 25 - Other Income
      - 26 - Other Expense

  - name: "billableExpensesAcct"
    type: "varies"
    description: ""

  - name: "cashFlowRate"
    type: "varies"
    description: "The type of exchange rate used to translate foreign currency amounts for this account in the cash flow statement."

  - name: "category1099Misc"
    type: "varies"
    description: ""

  - name: "curDocNum"
    type: "integer, string"
    description: "The next check number in the sequence for the account."

  - name: "currency"
    type: "varies"
    description: "The currency for funds in the account."

  - name: "customFieldList"
    type: "varies"
    description: "The custom fields associated with the account."

  - name: "deferralAcct"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: "The department with access to the account."

  - name: "description"
    type: "string"
    description: "The account description."

  - name: "eliminate"
    type: "boolean, string"
    description: "Indicates whether the account is an intercompany account."

  - name: "exchangeRate"
    type: "string"
    description: "The exchange rate for the account's `currency`."

  - name: "externalId"
    type: "string"
    description: ""

  - name: "generalRate"
    type: "varies"
    description: |
      Possible values are:

      - `_average'
      - `_current`
      - `_historical`

  - name: "includeChildren"
    type: "boolean, string"
    description: "Indicates whether the account is shared with all sub-subsidiaries associated with each subsidiary associated with the account."

  - name: "inventory"
    type: "boolean, string"
    description: "Indicates if the account balance is included in the Inventory KPI."

  - name: "isInactive"
    type: "boolean, string"
    description: "Indicates if the account is inactive."

  - name: "legalName"
    type: "string"
    description: |
      The legal name of the account. **Note**: This requires that the **Use Legal Name in Accounting** preference is enabled in {{ integration.display_name }}.

  - name: "localizationsList"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: "The location with access to the account."

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "openingBalance"
    type: "number, string"
    description: "The opening balance for the account."

  - name: "parent"
    type: "varies"
    description: "The parent account."

  - name: "restrictToAccountingBookList"
    type: "varies"
    description: ""

  - name: "revalue"
    type: "boolean, string"
    description: "Indicates if the account is selected for open balance currency revaluation."

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "unit"
    type: "varies"
    description: |
      The base unit assigned to `unitsType`. Applicable only when `accType` is `_statistical`.

  - name: "unitsType"
    type: "varies"
    description: |
      The type of unit associated with the statistical account. Applicable only when `accType` is `_statistical`.
---