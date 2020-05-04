---
tap: "bing-ads"
version: "2"

name: "accounts"
doc-link: https://docs.microsoft.com/en-us/advertising/customer-management-service/getaccount?view=bingads-13
singer-schema: 
description: |
  The `{{ table.name }}` table contains high-level information about each of the ad accounts you selected during setup. Each row in this table corresponds to a single account.

  [This is a **Core Object** table](#replication).

  #### Schema changes from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, the schema of this table has changed. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `CurrencyType` is now `CurrencyCode`
  - `AccountType` has been removed
  - `CountryCode` has been removed
  - `AutoTagType` has been added
  - `BusinessAddress` has been added
  - `SoldToPaymentInstrumentId` has been added

replication-method: "Key-based Incremental"

attributes:
  - name: "Id"
    type: "integer"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "LastModifiedTime"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: |
      The time (in UTC) the account was last updated.

      **Note**: The date and time value reflects the date and time at the Bing server, not the client.

  - name: "AccountFinancialStatus"
    type: "string"
    description: "The financial status of the account."

  - name: "AccountLifeCycleStatus"
    type: "string"
    description: "The status of the account."

  - name: "AutoTagType"
    type: "string"
    description: "Indicates whether supported UTM tracking codes are appended or replaced."

  - name: "BillToCustomerId"
    type: "integer"
    description: "The ID of the customer that is billed for the charges that the account generates. This is either the reseller that manages the account on behalf of the owner or the ID of the customer that owns the account."

  - name: "BusinessAddress"
    type: "array"
    description: |
      The location where your business is legally registered. If you're an agency working as an agent for your customer, this is the location where your client is legally registered. 
    subattributes:
      - name: "Id"
        type: "string"
        primary-key: true
        description: "The ID of the address object."

      - name: "BusinessName"
        type: "string"
        description: "The legal business name."

      - name: "City"
        type: "string"
        description: "The city."

      - name: "CountryCode"
        type: "string"
        description: |
          The country/region code. For a list of possible values, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/geographical-location-codes?view=bingads-12){:target="new"}.

      - name: "Line1"
        type: "string"
        description: "The first line of the address."

      - name: "Line2"
        type: "string"
        description: "The second line of the address."

      - name: "Line3"
        type: "string"
        description: "The third line of the address."

      - name: "Line4"
        type: "string"
        description: "The fourth line of the address."

      - name: "PostalCode"
        type: "string"
        description: "The postal or zip code."

      - name: "StateOrProvince"
        type: "string"
        description: |
          The state or province. For a list of possible values, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/geographical-location-codes?view=bingads-12){:target="new"}.

      - name: "TimeStamp"
        type: "date-time"
        description: "The date and time that the address was last updated."

  - name: "CurrencyCode"
    type: "string"
    description: |
      The type of currency used to settle the account. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/customer-management-service/currencycode?view=bingads-12){:target="new"} for a list of possible values.

  - name: "ForwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the account."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    subattributes:
      - name: "KeyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the account's forward compatibility settings."
        subattributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "Language"
    type: "string"
    description: "The language used to render the invoice for the account, if invoice is used as the payment method."

  - name: "LastModifiedByUserId"
    type: "integer"
    description: "The ID of the user who last updated the account's information."

  - name: "Name"
    type: "string"
    description: "The name of the account."

  - name: "Number"
    type: "string"
    description: "The account number generated by Bing Ads used to identify the account in the Bing Ads web app. This value is alphanumeric."

  - name: "ParentCustomerId"
    type: "integer"
    description: "The ID of the customer that owns the account."

  - name: "PauseReason"
    type: "integer"
    description: |
      Indicates the reason the account is paused. Possible values include:

      - `1` - A user paused the account
      - `2` - The billing service paused the account
      - `4` - The user and billing service paused the account

  - name: "PaymentMethodId"
    type: "integer"
    description: "The ID of the payment instrument used to settle the account."

  - name: "PaymentMethodType"
    type: "string"
    description: "The type of payment instrument used to settle the account."

  - name: "PrimaryUserId"
    type: "integer"
    description: "The ID of the account manager who is primarily responsible for managing the account. By default, this value is set to the reseller's user ID."

  - name: "SoldToPaymentInstrumentId"
    type: "string"
    description: "The ID of the payment instrument of your client (the sold-to customer) used to settle the account."

  - name: "Timestamp"
    type: "timestamp"
    description: "The timestamp value used internally by Bing Ads to reconcile updates between account update and delete operations."

  - name: "Timezone"
    type: "string"
    description: |
      The default timezone value to use for campaigns in this account.

      If left unspecified when the account is created, this value will default to `PacificTimeUSCanadaTijuana`.
---