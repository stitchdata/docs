---
tap: "stripe"
version: "2"
key: ""

name: "disputes"
doc-link: "https://stripe.com/docs/api/disputes/object"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/disputes.json
description: "This table contains information about customer disputes related to charges on their credit card."

replication-method: "Key-based Incremental"

api-method:
    name: "List all disputes"
    doc-link: "https://stripe.com/docs/api/disputes/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The dispute ID."
    foreign-key-id: "dispute-id"

  - name: "created"
    type: "string"
    description: "Time at which the dispute was created. Measured in seconds since the Unix epoch."
    replication-key: true 

  - name: "amount"
    type: "integer"
    description: ""

  - name: "balance_transactions"
    type: "array"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: "The balance transaction ID."
      foreign-key-id: "balance-transaction-id"


  - name: "charge"
    type: "string"
    description: "The ID of the disputed charge."
    foreign-key-id: "charge-id"

  - name: "currency"
    type: "string"
    description: ""

  - name: "evidence"
    type: "string, object"
    description: ""
    subattributes:
    - name: "refund_policy"
      type: "string"
      description: ""

    - name: "shipping_address"
      type: "string"
      description: ""

    - name: "duplicate_charge_explanation"
      type: "string"
      description: ""

    - name: "shipping_tracking_number"
      type: "string"
      description: ""

    - name: "customer_signature"
      type: "string"
      description: ""

    - name: "uncategorized_text"
      type: "string"
      description: ""

    - name: "cancellation_policy_disclosure"
      type: "string"
      description: ""

    - name: "refund_policy_disclosure"
      type: "string"
      description: ""

    - name: "receipt"
      type: "string"
      description: ""

    - name: "customer_name"
      type: "string"
      description: ""

    - name: "refund_refusal_explanation"
      type: "string"
      description: ""

    - name: "cancellation_rebuttal"
      type: "string"
      description: ""

    - name: "product_description"
      type: "string"
      description: ""

    - name: "shipping_date"
      type: "string"
      description: ""

    - name: "customer_email_address"
      type: "string"
      description: ""

    - name: "duplicate_charge_id"
      type: "string"
      description: ""

    - name: "shipping_documentation"
      type: "string"
      description: ""

    - name: "access_activity_log"
      type: "string"
      description: ""

    - name: "customer_purchase_ip"
      type: "string"
      description: ""

    - name: "service_date"
      type: "string"
      description: ""

    - name: "shipping_carrier"
      type: "string"
      description: ""

    - name: "service_documentation"
      type: "string"
      description: ""

    - name: "duplicate_charge_documentation"
      type: "string"
      description: ""

    - name: "cancellation_policy"
      type: "string"
      description: ""

    - name: "customer_communication"
      type: "string"
      description: ""

    - name: "uncategorized_file"
      type: "string"
      description: ""

    - name: "billing_address"
      type: "string"
      description: ""


  - name: "evidence_details"
    type: "object"
    description: ""
    subattributes:
    - name: "due_by"
      type: "string"
      description: ""

    - name: "has_evidence"
      type: "boolean"
      description: ""

    - name: "past_due"
      type: "boolean"
      description: ""

    - name: "submission_count"
      type: "integer"
      description: ""

  - name: "is_charge_refundable"
    type: "boolean"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "object"
    type: "string"
    description: ""

  - name: "reason"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---