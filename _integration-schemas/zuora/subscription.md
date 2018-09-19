---
tap: "zuora"
version: 1.0 

name: "subscription"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Subscriptions
description: |
  The `subscription` table contains info about your products and/or services with recurring charges.

  ### Custom Attributes

  If your Zuora subscription records contain custom attributes, Stitch will replicate them.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The subscription ID."
    foreign-key-id: "subscription-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the subscription was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with this subscription."
    foreign-key-id: "account-id"

  - name: "autoRenew"
    type: "boolean"
    description: "If `true`, the subscription automatically renews at the end of the term."

  - name: "cancelledDate"
    type: "date-time"
    description: "The date on which the subscription was canceled."

  - name: "contractAcceptanceDate"
    type: "date-time"
    description: "The date when the customer accepted the contract."

  - name: "contractEffectiveDate"
    type: "date-time"
    description: "The date when the contract takes effect."

  - name: "cpqBundleJsonId__qt"
    type: "string"
    description: "The bundle product structures from Zuora Quotes, if you utilize bundling in your Salesforce integration with Zuora."

  - name: "createdById"
    type: "string"
    description: "The ID of user who created the subscription."

  - name: "createdDate"
    type: "date-time"
    description: "The date the subscription was created."

  - name: "creatorAccountId"
    type: "string"
    description: "The account ID that created the subscription or the amended subscription."

  - name: "creatorInvoiceOwnerId"
    type: "string"
    description: "The account ID that owns the invoices associated with the subscription or the amended subscription."

  - name: "currentTerm"
    type: "integer"
    description: "The length of the period for the current subscription term."

  - name: "currentTermPeriodType"
    type: "string"
    description: "The period type for the current subscription term."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "initialTerm"
    type: "integer"
    description: "The length of the period for the first subscription term."

  - name: "initialTermPeriodType"
    type: "string"
    description: |
      The period type for the first subscription term. Possible values are:

      - `Month`
      - `Year`
      - `Day`
      - `Week`

  - name: "invoiceOwnerId"
    type: "string"
    description: "The account ID that owns the invoices associated with the subscription."
    # foreign-key-id: "invoice-owner-id"

  - name: "isInvoiceSeparate"
    type: "boolean"
    description: "If `true`, then all charges for this subscription are collected into the subscription's own invoice."

  - name: "name"
    type: "string"
    description: "The unqiue name of the subscription."

  - name: "notes"
    type: "string"
    description: "Any notes about the subscription."

  - name: "opportunityCloseDate__qt"
    type: "date-time"
    description: "The closing date of the Opportunity."

  - name: "opportunityName_qt"
    type: "string"
    description: "The unique name of the Opportunity."

  - name: "originalCreatedDate"
    type: "date-time"
    description: "The date when the subscription was originally created."

  - name: "originalId"
    type: "string"
    description: "The original ID of the subscription."

  - name: "previousSubscriptionId"
    type: "string"
    description: "The subscription ID immediately prior to the current subscription."

  - name: "quoteBusinessType__qt"
    type: "string"
    description: "The identifier for the type of business transaction the quote represents. For example: New, Renewal, Churn."

  - name: "quoteNumber__qt"
    type: "string"
    description: "The unique identifier of the Quote."

  - name: "quoteType__at"
    type: "string"
    description: "The Quote type that represents the subscription lifecycle stage. For example: Amendement, Renew."

  - name: "renewalSetting"
    type: "string"
    description: |
      Indicates whether a termed subscription will remain termed or change to evergreen when it is renewed. Possible values are:

      - `RENEW_WITH_SPECIFIC_TERM`
      - `RENEW_TO_EVERGREEN`

  - name: "renewalTerm"
    type: "integer"
    description: "The length of the period for the subscription renewal term."

  - name: "renewalTermPeriodType"
    type: "string"
    description: |
      The period type for the subscription renewal term. Possible values are:

      - `Month`
      - `Year`
      - `Day`
      - `Week`

  - name: "serviceActivationDate"
    type: "date-time"
    description: "The date when the subscription is activated."

  - name: "status"
    type: "string"
    description: |
      The status of the subscription. Possible values are:

      - `Draft`
      - `PendingActivation`
      - `PendingAcceptance`
      - `Active`
      - `Cancelled`
      - `Expired`
      - `Suspended`

  - name: "subscriptionEndDate"
    type: "date-time"
    description: |
      The date when the subscription term ends, where the subscription ends at midnight the day before.

      For example: If this date is `01/01/2018`, the subscription ends at midnight (`00:00:00`) on `12/31/2017`.

  - name: "subscriptionStartDate"
    type: "date-time"
    description: "The date when the subscription term starts."

  - name: "termEndDate"
    type: "date-time"
    description: "The date when the subscription term ends."

  - name: "termStartDate"
    type: "date-time"
    description: "The date when the subscription term begins."

  - name: "termType"
    type: "string"
    description: "Indicates if a subscription is termed or evergreen."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the subscription."
---