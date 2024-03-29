---
tap: "bing-ads"
version: "1"

name: "accounts"
doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/account

description: |
  The `accounts` table contains high-level information about each of the ad accounts you selected during setup. Each row in this table corresponds to a single account.

  [This is a **Core Object** table](#replication).

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/account

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "lastModifiedTime"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: |
      The time (in UTC) the account was last updated.

      **Note**: The date and time value reflects the date and time at the Bing server, not the client.

  - name: "accountFinancialStatus"
    type: "string"
    description: "The financial status of the account."

  - name: "accountLifeCycleStatus"
    type: "string"
    description: "The status of the account."

  - name: "accountType"
    type: "string"
    description: "The type of the account."

  - name: "billToCustomerId"
    type: "integer"
    description: "The ID of the customer that is billed for the charges that the account generates. This is either the reseller that manages the account on behalf of the owner or the ID of the customer that owns the account."

  - name: "countryCode"
    type: "string"
    description: "The code of the country/region in which the account operates. See [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/ad-languages) for a list of country code values."

  - name: "currencyType"
    type: "string"
    description: "The type of currency used to settle the account."

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the account."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    subattributes:
      - name: "keyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the account's forward compatibility settings."
        subattributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "language"
    type: "string"
    description: "The language used to render the invoice for the account, if invoice is used as the payment method."

  - name: "lastModifiedByUserId"
    type: "integer"
    description: "The ID of the user who last updated the account's information."

  - name: "name"
    type: "string"
    description: "The name of the account."

  - name: "number"
    type: "string"
    description: "The account number generated by Bing Ads used to identify the account in the Bing Ads web app. This value is alphanumeric."

  - name: "parentCustomerId"
    type: "integer"
    description: "The ID of the customer that owns the account."

  - name: "pauseReason"
    type: "integer"
    description: |
      Indicates the reason the account is paused. Possible values include:

      - `1` - A user paused the account
      - `2` - The billing service paused the account
      - `4` - The user and billing service paused the account

  - name: "paymentMethodId"
    type: "integer"
    description: "The ID of the payment instrument used to settle the account."

  - name: "paymentMethodtype"
    type: "string"
    description: "The type of payment instrument used to settle the account."

  - name: "primaryUserId"
    type: "integer"
    description: "The ID of the account manager who is primarily responsible for managing the account. By default, this value is set to the reseller's user ID."

  - name: "timestamp"
    type: "timestamp"
    description: "The timestamp value used internally by Bing Ads to reconcile updates between account update and delete operations."

  - name: "timezone"
    type: "string"
    description: |
      The default timezone value to use for campaigns in this account.

      If left unspecified when the account is created, this value will default to `PacificTimeUSCanadaTijuana`.
---