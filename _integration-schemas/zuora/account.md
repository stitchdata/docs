---
tap: "zuora"
version: 1.0

name: "account"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounts
#singer-schema: 
description: |
  The `account` table contains information about the customer accounts in your Zuora instance.

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."
    ## foreign-keys:
    ##   - table-name: "contact"
    ##     attribute: "accountId"

    ##   - table-name: "invoice"
    ##     attribute: "accountId"

    ##   - table-name: "payment"
    ##     attribute: "accountId"

    ##   - table-name: "refund"
    ##     attribute: "accountId"

    ##   - table-name: "subscription"
    ##     attribute: "accountId"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the account was last updated."

  - name: "accountNumber"
    type: "string"
    description: "The unique account number assigned to the account."

  - name: "additionalEmailAddresses"
    type: "string"
    description: "A list of additional email addresses to receive emailed invoices."

  - name: "allowInvoiceEdit"
    type: "boolean"
    description: "If `true`, the account's associated invoices may be edited."

  - name: "autoPay"
    type: "boolean"
    description: "If `true`, future payments for the account are automatically collected when they're due during a Payment Run."

  - name: "balance"
    type: "decimal"
    description: "The current outstanding balance for the account."

  - name: "batch"
    type: "string"
    description: "The batch group the account is a part of."

  - name: "bcdSettingOption"
    type: "string"
    description: "The billing cycle day setting option for the account."

  - name: "billCycleDay"
    type: "integer"
    description: "The billing cycle day (BCD) on which bill runs generate invoices for the account."

  - name: "billToId"
    type: "string"
    description: "The ID of the person to bill for the account."

  - name: "communicationProfileId"
    type: "string"
    description: "The ID of the communication profile associated with the account."

  - name: "createdByID"
    type: "string"
    description: "The ID of the Zuora user who created the account."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the account was created."

  - name: "creditBalance"
    type: "decimal"
    description: "The total credit balance for the account."

  - name: "crmId"
    type: "string"
    description: "The CRM account ID for the account. Used when Salesforce is integrated with your Zuora instance."

  - name: "currency"
    type: "string"
    description: "The currency that the customer is billed in."

  - name: "customerServiceRepName"
    type: "string"
    description: "The name of the account's customer service representative, if applicable."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The ID of the default payment method for the account."

  - name: "invoiceDeliveryPrefsEmail"
    type: "boolean"
    description: "If `true`, the customer wants to receive invoices through email."

  - name: "invoiceDeliveryPrefsPrint"
    type: "boolean"
    description: "If `true`, the customer wants to receive printed invoices."

  - name: "invoiceTemplateId"
    type: "string"
    description: "The ID of the invoice template used for the account."

  - name: "lastInvoiceDate"
    type: "date-time"
    description: "The date when the previous invoice was generated for the account. This field will be `NULL` if no invoice has ever been generated for the account."

  - name: "name"
    type: "string"
    description: "The name of the account as displayed in the Zuora UI."

  - name: "notes"
    type: "string"
    description: "Any comments about the account."

  - name: "parentId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in Zuora."

  - name: "paymentGateway"
    type: "string"
    description: "The gateway used for processing electronic payments and refunds."

  - name: "paymentTerm"
    type: "string"
    description: "Indicates when the customer pays for subscriptions."

  - name: "purchaseOrderNumber"
    type: "string"
    description: "The number of the purchase order associated with this account."

  - name: "salesRepName"
    type: "string"
    description: "The name of the sales representative associated with the account, if applicable."

  - name: "soldToId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."

  - name: "status"
    type: "string"
    description: |
      The status of the account in the system. Possible values are:

      - `Draft`
      - `Active`
      - `Canceled`

  - name: "taxExemptCertificateId"
    type: "string"
    description: "The ID of the customer's tax exemption certificate."

  - name: "taxExemptCertificateType"
    type: "string"
    description: "The type of tax exemption certificate that the customer holds."

  - name: "taxExemptDescription"
    type: "string"
    description: "The description of the tax exemption certificate that the customer holds."

  - name: "taxExemptEffectiveDate"
    type: "date-time"
    description: "The date when the customer's tax exemption starts."

  - name: "taxExemptExpirationDate"
    type: "date-time"
    description: "The date when the customer's tax exemption expires."

  - name: "taxExemptIssuingJurisdiction"
    type: "string"
    description: "The jurisdiction in which the customer's tax exemption certificate was issued."

  - name: "taxExemptStatus"
    type: "string"
    description: |
      The status of the account's tax exemption. Possible values are:

      - `Yes`
      - `No`
      - `PendingVerification`

  - name: "totalInvoiceBalance"
    type: "decimal"
    description: "The total balance of the account's invoices."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the account."
---