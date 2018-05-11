---
tap: "zuora"
version: 1.0

name: "amendment"
doc-link: https://live-www.zuora.com/developer/api-reference/#operation/Object_GETAmendment
#singer-schema: 
description: |
  The `amendment` table contains information about subscription amendments, which are changes to customer subscriptions. For example: Changing the terms of a contract, adding/removing a product, canceling a subscription, etc.

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The amendment ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the amendment was last updated."

  - name: "autoRenew"
    type: "boolean"
    description: "If `true`, the subscription will auto-renew at the end of the term."

  - name: "code"
    type: "string"
    description: "A unique string that identifies the amendment."

  - name: "contractEffectiveDate"
    type: "date-time"
    description: "The date when the amendment's charges become effective for billing purposes."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the amendment."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the amendment was created."

  - name: "currentTerm"
    type: "integer"
    description: "The length of the period for the current subscription term. This field is used with the `currentTermPeriodType` field to specify the current subscription term."

  - name: "currentTermPeriodType"
    type: "string"
    description: |
      The period type for the current subscription term. This field is used with the `currentTerm` field to specify the current subscription term.

      Possible values are:

      - `Month`
      - `Year`
      - `Day`
      - `Week`

  - name: "customerAcceptanceDate"
    type: "date-time"
    description: "The date when the customer accepted the amendment's changes to the subscription."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "description"
    type: "string"
    description: "The description of the amendment."

  - name: "effectiveDate"
    type: "date-time"
    description: "The date when the amendment's charges take effect."

  - name: "name"
    type: "string"
    description: "The name of the amendment."

  - name: "renewalSetting"
    type: "string"
    description: |
      Indicates whether a termed subscription will remain termed or change to evergreen when renewed. Possible values are:

      - `RENEW_WITH_SPECIFIC_TERM`
      - `RENEW_TO_EVERGREEN`

  - name: "renewalTerm"
    type: "string"
    description: "The term of the renewal for the amended subscription. This field is used with the `renewalTermPeriodType' field to specify the subscription renewal term."

  - name: "renewalTermPeriodType"
    type: "string"
    description: |
      The period type for the subscription renewal term. This field is used with the `renewalTerm' field to specify the subscription renewal term.

      Possible values are:

      - `Month`
      - `Year`
      - `Day`
      - `Week`

  - name: "serviceActivationDate"
    type: "date-time"
    description: "The date when service is activated."

  - name: "specificUpdateDate"
    type: "date-time"
    description: "The date when the UpdateProduct amendment takes effect. Only applicable if there is already a future-dated UpdateProduct amendment on the subscription."

  - name: "status"
    type: "string"
    description: |
      The status of the amendment. Possible values are:

      - `Draft`
      - `Pending Activation`
      - `Pending Acceptance`
      - `Completed`

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription that the amendment changes."
    foreign-key: true

  - name: "termStartDate"
    type: "string"
    description: |
      Indicates if the subscription is `TERMED` or `EVERGREEN`.

  - name: "type"
    type: "string"
    description: |
      The type of amendment. Possible values are:

      - `Cancellation`
      - `NewProduct`
      - `OwnerTransfer`
      - `RemoveProduct`
      - `Renewal`
      - `UpdateProduct`
      - `TermsAndConditions`
      - `SuspendSubscription`
      - `ResumeSubscription`

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the amendment."

  - name: ""
    type: 
    description: ""

---