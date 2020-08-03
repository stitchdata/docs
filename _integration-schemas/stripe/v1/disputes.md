---
tap: "stripe"
version: "1"

name: "disputes"
doc-link: "https://stripe.com/docs/api/disputes/object"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/disputes.json"
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
    type: "date-time"
    description: "Time at which the dispute was created. Measured in seconds since the Unix epoch."
    replication-key: true  

  - name: "amount"
    type: "integer"
    description: "The disputed amount of money."

  - name: "balance_transactions"
    type: "array"
    description: "A list of zero, one, or two balance transactions that show funds withdrawn and reinstated to a Stripe account as a result of the dispute."
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
    description: "The three-letter ISO currency code of the disputed charge."

  - name: "evidence"
    type: "object"
    description: ""
    subattributes:
      - name: "access_activity_log"
        type: "string"
        description: "Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product."
      - name: "billing_address"
        type: "string"
        description: "The billing address provided by the customer."
      - name: "cancellation_policy"
        type: "string"
        description: "The subscription cancellation policy, as shown to the customer."
      - name: "cancellation_policy_disclosure"
        type: "string"
        description: "The explanation of how and when the customer was shown the refund policy prior to purchase."
      - name: "cancellation_rebuttal"
        type: "string"
        description: "The justification for why the customer’s subscription was not canceled."
      - name: "customer_communication"
        type: "string"
        description: "Any communication with the customer that is relevant to your case."
      - name: "customer_email_address"
        type: "string"
        description: "The email address of the customer."
      - name: "customer_name"
        type: "string"
        description: "The name of the customer."
      - name: "customer_purchase_ip"
        type: "string"
        description: "The IP address that the customer used when making the purchase."
      - name: "customer_signature"
        type: "string"
        description: "A relevant document or contract showing the customer’s signature."
      - name: "duplicate_charge_documentation"
        type: "string"
        description: "Documentation for the prior charge that can uniquely identify the charge."
      - name: "duplicate_charge_explanation"
        type: "string"
        description: "The explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate."
      - name: "duplicate_charge_id"
        type: "string"
        description: "The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge."
      - name: "product_description"
        type: "string"
        description: "The description of the product or service that was sold."
      - name: "receipt"
        type: "string"
        description: "The receipt or message sent to the customer notifying them of the charge."
      - name: "refund_policy"
        type: "string"
        description: "The refund policy, as shown to the customer."
      - name: "refund_policy_disclosure"
        type: "string"
        description: "Documentation demonstrating that the customer was shown your refund policy prior to purchase."
      - name: "refund_refusal_explanation"
        type: "string"
        description: "The justification for why the customer is not entitled to a refund."
      - name: "service_date"
        type: "string"
        description: "The date on which the customer received or began receiving the purchased service."
      - name: "service_documentation"
        type: "string"
        description: "Documentation showing proof that a service was provided to the customer."
      - name: "shipping_address"
        type: "string"
        description: "The address to which a physical product was shipped."
      - name: "shipping_carrier"
        type: "string"
        description: "The delivery service that shipped a physical product, such as `Fedex`, `UPS`, `USPS`, etc."
      - name: "shipping_date"
        type: "string"
        description: "The date on which a physical product began its route to the shipping address."
      - name: "shipping_documentation"
        type: "string"
        description: "Documentation showing proof that a product was shipped to the customer at the same address the customer provided."
      - name: "shipping_tracking_number"
        type: "string"
        description: "The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated, these will be comma-delineated."
      - name: "uncategorized_file"
        type: "string"
        description: "Any additional evidence or statements."
      - name: "uncategorized_text"
        type: "string"
        description: "Any additional evidence or statements."

  - name: "evidence_details"
    type: "object"
    description: "Information about the evidence submitted."
    subattributes:
      - name: "due_by"
        type: "date-time"
        description: "The date by which evidence must be submitted in order to successfully challenge dispute."
      - name: "has_evidence"
        type: "boolean"
        description: "Whether or not evidence has been staged for the dispute."
      - name: "past_due"
        type: "boolean"
        description: "Whether the last evidence submission was submitted past the due date."
      - name: "submission_count"
        type: "integer"
        description: "The number of times evidence has been submitted."

  - name: "is_charge_refundable"
    type: "boolean"
    description: "Whether or not the disputed charge is refundable."

  - name: "livemode"
    type: "boolean"
    description: "Has the value `TRUE` if the object exists in live mode or the value `FALSE` if the object exists in test mode."

  - name: "metadata"
    type: "object"
    description: "A set of key-value pairs that you can attach to an object."
    subattributes:

  - name: "object"
    type: "string"
    description: "The object type. In this table, the value is `dispute`."

  - name: "reason"
    type: "string"
    description: |
      The reason given by the cardholder for the dispute. Possible values are: 

      - `bank_cannot_process`
      - `check_returned`
      - `credit_not_processed`
      - `customer_initiated`
      - `debit_not_authorized`
      - `duplicate`
      - `fraudulent`
      - `general`
      - `incorrect_account_details`
      - `insufficient_funds`
      - `product_not_received`
      - `product_unacceptable`
      - `subscription_canceled`
      - `unrecognized`

  - name: "status"
    type: "string"
    description: |
      The current status of the dispute. Possible values are: 

      - `warning_needs_response`
      - `warning_under_review`
      - `warning_closed`
      - `needs_response`
      - `under_review`
      - `charge_refunded`
      - `won`
      - `lost`

  - name: "updated"
    type: "date-time"
    description: "The time at which the dispute was last updated."
---