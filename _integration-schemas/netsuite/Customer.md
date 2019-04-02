---
tap: "netsuite"
version: "1.0"

name: "Customer"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2018_1/schema/record/customer.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Customer.json"
description: |
  The `{{ table.name }}` table contains info about customers.

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "customer-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The time the customer was last updated."

  - name: "accessRole"
    type: "varies"
    description: "The role assigned to the customer."

  - name: "accountNumber"
    type: "string"
    description: "The number of the account assigned for the customer."

  - name: "addressbookList"
    type: "varies"
    description: ""

  - name: "aging"
    type: "number, string"
    description: &aging "The overdue Accounts Receiveable balance for the customer."

  - name: "aging1"
    type: "number, string"
    description: *aging

  - name: "aging2"
    type: "number, string"
    description: *aging

  - name: "aging3"
    type: "number, string"
    description: *aging

  - name: "aging4"
    type: "number, string"
    description: *aging

  - name: "alcoholRecipientType"
    type: "varies"
    description: "The customer's default intended recipient type. This info is included for FedEx shipments containing alcohol."

  - name: "altEmail"
    type: "string"
    description: "The alternate email for the customer."

  - name: "altName"
    type: "string"
    description: "The name of the person or company."

  - name: "altPhone"
    type: "string"
    description: "The customer's alternate phone number."

  - name: "balance"
    type: "number, string"
    description: "The customer's currency Accounts Receivable balance."

  - name: "billPay"
    type: "boolean, string"
    description: "Indicates if the customer has online bill pay enabled."

  - name: "buyingReason"
    type: "varies"
    description: "The customer's reason for buying from your company."

  - name: "buyingTimeFrame"
    type: "varies"
    description: "The timeframe for the customer to purchase from your company."

  - name: "campaignCategory"
    type: "varies"
    description: "The campaign category associated with the customer."

  - name: "category"
    type: "varies"
    description: "The category associated with the customer."

  - name: "clickStream"
    type: "string"
    description: "The click stream for the customer on first visit."

  - name: "comments"
    type: "string"
    description: "Additional comments about the customer."

  - name: "companyName"
    type: "string"
    description: "The name of the customer's company."

  - name: "consolAging"
    type: "number, string"
    description: &consolaging "The overdue consolidated Accounts Receivable balance for the customer. These totals include the balance from all the customers and subcustomers in this hierarchy."

  - name: "consolAging1"
    type: "number, string"
    description: *consolaging

  - name: "consolAging2"
    type: "number, string"
    description: *consolaging

  - name: "consolAging3"
    type: "number, string"
    description: *consolaging

  - name: "consolAging4"
    type: "number, string"
    description: *consolaging

  - name: "consolBalance"
    type: "number, string"
    description: "The current Accounts Receivable balance due for the customer-subcustomer hierarchy this customer is a member of."

  - name: "consolDaysOverdue"
    type: "integer, string"
    description: "The number of days the `consolOverdueBalance` is overdue."

  - name: "consolDepositBalance"
    type: "number, string"
    description: "The total amount of unapplied deposits for the customer-subcustomer hierarchy the customer is a member of."

  - name: "consolOverdueBalance"
    type: "number, string"
    description: "The consolidated total owed for open transactions for the customer-subcustomer hierarchy that are past their due date. **Note**: According to {{ integration.display_name }}'s documentation, for open transactions that don't have a due date, the transaction date is used as the due date to calculate this value."

  - name: "consolUnbilledOrders"
    type: "number, string"
    description: "The total amount of orders that have been entered but not yet billed for the customer-subcustomer hierarchy this customer is a member of."

  - name: "contactRolesList"
    type: "varies"
    description: ""

  - name: "contribPct"
    type: "string"
    description: ""

  - name: "creditCardsList"
    type: "varies"
    description: ""

  - name: "creditHoldOverride"
    type: "varies"
    description: |
      Possible values include:

      - `_auto`
      - `_on`
      - `_off`

  - name: "creditLimit"
    type: "number, string"
    description: "The credit limit for the customer."

  - name: "currency"
    type: "varies"
    description: "The currency used by the customer."

  - name: "currencyList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: "The custom fields associated with the customer."

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dateCreated"
    type: "date-time"
    description: "The date the customer was created."

  - name: "daysOverdue"
    type: "integer, string"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: "The customer's default billing address."

  - name: "defaultOrderPriority"
    type: "number, string"
    description: "The default order priority for the customer."

  - name: "depositBalance"
    type: "number, string"
    description: "The deposit balance for the customer."

  - name: "displaySymbol"
    type: "string"
    description: "The currency symbol and text to use for the customer's currency."

  - name: "downloadList"
    type: "varies"
    description: ""

  - name: "drAccount"
    type: "varies"
    description: "The deferred revenue account to use by default to post revenue reclassification amounts generated by revenue reclassification journal entries for the customer."

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "emailPreference"
    type: "varies"
    description: "The customer's email preference. For example: `_PDF`, `_HTML`"

  - name: "emailTransactions"
    type: "boolean, string"
    description: |
      The preferred transaction delivery method for the customer. Possible values are:

      - `Email`
      - `Print`
      - `Fax`

  - name: "endDate"
    type: "date-time"
    description: "The projected end date for the customer."

  - name: "entityId"
    type: "string"
    description: "The name of the customer record."

  - name: "entityStatus"
    type: "varies"
    description: ""

  - name: "estimatedBudget"
    type: "number, string"
    description: "The estimated budget for the customer."

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: "The customer's fax number."

  - name: "faxTransactions"
    type: "boolean, string"
    description: ""

  - name: "firstName"
    type: "string"
    description: "The customer's first name."

  - name: "firstVisit"
    type: "date-time"
    description: "The date of the customer's first visit."

  - name: "fxAccount"
    type: "varies"
    description: "The revenue account to use by default to post foreign currency adjustments that result when exchange rates are different for billilng and revenue postings for the customer. This will be an Income account."

  - name: "giveAccess"
    type: "boolean, string"
    description: "Indicates if the customer has login access to your {{ integration.display_name }} account."

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: |
      The customer's subscription status. Possible values include:

      - Confirmed Opt-In
      - Soft Opt-In
      - Soft Opt-Out
      - Confirmed Opt-Out

  - name: "groupPricingList"
    type: "varies"
    description: ""

  - name: "homePhone"
    type: "string"
    description: "The customer's home phone number."

  - name: "image"
    type: "varies"
    description: "A reference to a file in the file cabinet for the customer."

  - name: "isBudgetApproved"
    type: "boolean, string"
    description: "Indicates if the customer's budget has been approved."

  - name: "isInactive"
    type: "boolean, string"
    description: "Indicates if the customer is inactive."

  - name: "isPerson"
    type: "boolean, string"
    description: "Indicates if the customer is a person, versus a company."

  - name: "itemPricingList"
    type: "varies"
    description: ""

  - name: "keywords"
    type: "string"
    description: "The keywords the customer used in the search engine for their first visit."

  - name: "language"
    type: "varies"
    description: "The language used by the customer."

  - name: "lastName"
    type: "string"
    description: "The customer's last name."

  - name: "lastPageVisited"
    type: "string"
    description: "The last page the customer visited on their most recent visit to your web site."

  - name: "lastVisit"
    type: "date-time"
    description: "The date the customer last visited your web site."

  - name: "leadSource"
    type: "varies"
    description: "Indicates how the customer was referred to your company."

  - name: "middleName"
    type: "string"
    description: "The customer's middle name."

  - name: "mobilePhone"
    type: "string"
    description: "The customer's mobile phone number."

  - name: "monthlyClosing"
    type: "varies"
    description: ""

  - name: "negativeNumberFormat"
    type: "varies"
    description: "The customer's negative number format preference, if any. This indicates whether negative numbers should be preceeded by a minus sign (`-`) or enclosed in parenthesis `( )`."

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberFormat"
    type: "varies"
    description: "The customer's positive number format preference. In {{ integration.display_name }}, this setting controls how the thousands separator and decimals display for the customer."

  - name: "openingBalance"
    type: "number, string"
    description: "The opening balance for the customer's account."

  - name: "openingBalanceAccount"
    type: "varies"
    description: "The account the opening balance was applied to."

  - name: "openingBalanceDate"
    type: "date-time"
    description: "The date of the balance entered in the Opening Balance field."

  - name: "overdueBalance"
    type: "number, string"
    description: "The overdue balance for the customer."

  - name: "overrideCurrencyFormat"
    type: "boolean, string"
    description: "Indicates if the currency format has been customized for the customer."

  - name: "parent"
    type: "varies"
    description: "If the customer is a subcustomer or a smaller entity of another customer, this will be the parent customer."

  - name: "partner"
    type: "varies"
    description: "The partner associated with the customer."

  - name: "partnersList"
    type: "varies"
    description: ""

  - name: "password"
    type: "string"
    description: "The password assigned to allow the customer to access {{ integration.display_name }}."

  - name: "password2"
    type: "string"
    description: "The password confirmation field value for the customer."

  - name: "phone"
    type: "string"
    description: "The customer's phone number."

  - name: "phoneticName"
    type: "string"
    description: "The furigana character used to sort the customer record in {{ integration.display_name }}."

  - name: "prefCCProcessor"
    type: "varies"
    description: "The customer's preferred credit card processor."

  - name: "priceLevel"
    type: "varies"
    description: "The price level used for selling to the customer."

  - name: "printOnCheckAs"
    type: "string"
    description: "The value that prints on the `Pay to the Order Of` line of checks sent to the customer."

  - name: "printTransactions"
    type: "boolean, string"
    description: ""

  - name: "receivablesAccount"
    type: "varies"
    description: "The Default Account Receivables Account to use for the customer."

  - name: "referrer"
    type: "string"
    description: "The site that referred the customer to your {{ integration.display_name }} website on their first visit."

  - name: "reminderDays"
    type: "integer, string"
    description: "The number of days before the end date that a reminder should be sent for renewing the customer's contract or project."

  - name: "representingSubsidiary"
    type: "varies"
    description: "Indicates if the customer is an intercompany customer."

  - name: "requirePwdChange"
    type: "boolean, string"
    description: "Indicates if a password change will be required on the next {{ integration.display_name }} login for the customer."

  - name: "resaleNumber"
    type: "string"
    description: "The customer's tax license number. This is used in cases where sales tax is not collected from the customer."

  - name: "salesGroup"
    type: "varies"
    description: "The sales team group associated with the customer when team sellilng is enabled in {{ integration.display_name }}."

  - name: "salesReadiness"
    type: "varies"
    description: "Indicates how close the customer is to purchasing."

  - name: "salesRep"
    type: "varies"
    description: "The sales rep associated with the customer."

  - name: "salesTeamList"
    type: "varies"
    description: ""

  - name: "salutation"
    type: "string"
    description: "The salutation for the customer."

  - name: "sendEmail"
    type: "boolean, string"
    description: "Indicates if the customer is automatically sent an email notification when access to {{ integration.display_name }} is provided."

  - name: "shipComplete"
    type: "boolean, string"
    description: "Indicates if orders should only be shipped to the customer when they're totally fulfilled."

  - name: "shippingItem"
    type: "varies"
    description: "The default shipping method for the customer."

  - name: "stage"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: "The date the person/company became a customer, lead, or prospect. If the customer has a contract, this may be the start date of the contract. If an estimate or opportunity is entered for the customer, {{ integration.display_name }} may update this value with the date of that transaction."

  - name: "subscriptionsList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: "The subsidiary associated with the customer."

  - name: "symbolPlacement"
    type: "varies"
    description: "Indicates whether symbols are placed before or after numbers for the customer."

  - name: "syncPartnerTeams"
    type: "boolean, string"
    description: "Indicates whether changes made to the partner team will update the customer's transactions."

  - name: "taxExempt"
    type: "boolean, string"
    description: "Indicates if the customer is tax exempt."

  - name: "taxItem"
    type: "varies"
    description: "The standard tax rate for the customer."

  - name: "taxable"
    type: "boolean, string"
    description: "Indicates if the customer pays sales tax according to the `taxItem` rate."

  - name: "terms"
    type: "varies"
    description: "The terms for the customer."

  - name: "territory"
    type: "varies"
    description: "The sales territory the customer is in."

  - name: "thirdPartyAcct"
    type: "string"
    description: "The customer's FedEx or UPS account number."

  - name: "thirdPartyCountry"
    type: "varies"
    description: "The country associated with the customer's FedEx or UPS account."

  - name: "thirdPartyZipcode"
    type: "string"
    description: "The zip code associated with the customer's FedEx or UPS account."

  - name: "title"
    type: "string"
    description: "The job title for the customer at `companyName`."

  - name: "unbilledOrders"
    type: "number, string"
    description: "The total amount of orders that have been entered into {{ integration.display_name }} but not yet billed."

  - name: "url"
    type: "string"
    description: "The URL associated with the customer."

  - name: "vatRegNumber"
    type: "string"
    description: "**For the UK edition of {{ integration.display_name }}**. The customer's VAT registration number."

  - name: "visits"
    type: "integer, string"
    description: "The total number of visits the customer has made to your website. A new visit is counted after the customer leaves the site and returns."

  - name: "webLead"
    type: "string"
    description: "Indicates whether the customer registered via a {{ integration.display_name }} website. Possible values are `Yes` or `No`."
---