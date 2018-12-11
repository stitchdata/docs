---
tap: "stripe"
version: "1.0"

name: "charges"
doc-link: "https://stripe.com/docs/api/charges/object"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/charges.json"
description: |
  The `{{ table.name }}` table contains info about charges to credit and debit cards.

# TODO: Will disputes be in this table now, or in `events` as it was in the old integration?

replication-method: "Key-based Incremental"

api-method:
    name: "List all charges"
    doc-link: "https://stripe.com/docs/api/charges/list"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The charge ID."
    foreign-key-id: "charge-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "Time at which the object was created. Measured in seconds since the Unix epoch."

  - name: "amount"
    type: "integer"
    description: |
      A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal){:target="new"} (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency) representing how much to charge. The minimum amount is $0.50 USD or [equivalent in charge currency](https://support.stripe.com/questions/what-is-the-minimum-amount-i-can-charge-with-stripe){:target="new"}.

  - name: "amount_refunded"
    type: "integer"
    description: "Amount in cents refunded (can be less than `amount` if a partial refund was issued)."

  - name: "application"
    type: "string"
    description: "The ID of the Connect application that created the charge."

  - name: "application_fee"
    type: "string"
    description: "The application fee (if any) for the charge."

  - name: "balance_transaction"
    type: "string"
    description: "The ID of the balance transaction that describes the impact of this charge on the {{ integration.display_name }} account."
    foreign-key-id: "balance-transaction-id"

  - name: "captured"
    type: "boolean"
    description: "If the charge was created without capturing, this attribute will indicate whether it's still uncaptured or has since been captured."

  - name: "card"
    type: "object"
    description: &source-description "Details about the credit or debit card that is the source of the charge."
    object-attributes: &source-attributes
      - name: "id"
        type: "string"
        description: "The card ID."
        foreign-key-id: "card-id"

      - name: "address_city"
        type: "string"
        description: "The city associated with the card's billing address."

      - name: "address_country"
        type: "string"
        description: "The billing address country."

      - name: "address_line1"
        type: "string"
        description: "The first line of the billing address."

      - name: "address_line1_check"
        type: "string"
        description: |
          If `address_line1` was provided, the results of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "address_line2"
        type: "string"
        description: "The second line of the billing address."

      - name: "address_state"
        type: "string"
        description: "The state/county/province/region of the billing address."

      - name: "address_zip"
        type: "string"
        description: "The zip or postal code of the billing address."

      - name: "address_zip_check"
        type: "string"
        description: |
          If `address_zip` was provided, the results of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "brand"
        type: "string"
        description: |
          The brand of the card. Possible values are:

          - `American Express`
          - `Diners Club`
          - `Discover`
          - `JCB`
          - `MasterCard`
          - `UnionPay`
          - `Visa`
          - `Unknown`

      - name: "country"
        type: "string"
        description: "The two-letter ISO code representing the country of the card."

      - name: "customer"
        type: "string"
        description: "The ID of the customer that the card belongs to."
        foreign-key-id: "customer-id"

      - name: "cvc_check"
        type: "string"
        description: |
          If a CVC was provided, this will be the result of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "dynamic_last4"
        type: "string"
        description: "**For tokenized numbers only.** The last four digits of the device account number."

      - name: "exp_month"
        type: "integer"
        description: "The two-digit number representing the card's expiration month."

      - name: "exp_year"
        type: "integer"
        description: "The four-digit number representing the card's expiration year."

      - name: "fingerprint"
        type: "string"
        description: "A unique ID for the card number."

      - name: "funding"
        type: "string"
        description: |
          The card's funding type. Possible values are:

          - `credit`
          - `debit`
          - `prepaid`
          - `unknown`

      - name: "last4"
        type: "string"
        description: "The last four digits of the card."

      - name: "metadata"
        type: "object"
        description: "Additional information attached to the card."
        object-attributes:
          - name: ""
            type: 
            description: ""

      - name: "name"
        type: "string"
        description: "The name of the cardholder."

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `card`."

      - name: "tokenization_method"
        type: "string"
        description: |
          If the card number is tokenized, this is the method that was used. Possible values are:

          - `apple_pay`
          - `android_pay`

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

  - name: "customer"
    type: "string"
    description: "The ID of the customer associated with the charge."
    foreign-key-id: "customer-id"

  - name: "description"
    type: "string"
    description: "An arbitrary string attached to the object. Often useful for displaying to users."

  - name: "destination"
    type: "string"
    description: "The account (if any) the charge was made on behalf of, with an automatic transfer."

  - name: "dispute"
    type: "string"
    description: "Details about the dispute, if the charge has been dispuated."

  - name: "failure_code"
    type: "string"
    description: |
      The error code explaining the reason for a charge failure, if available. Refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/api#errors){:target="new"} for a list of possible error codes.

  - name: "failure_message"
    type: "string"
    description: "The message that displays to the user that further explains the reason for the charge failure."

  - name: "fraud_details"
    type: "object"
    description: |
      Details about fraud assessments for the charge.
    object-attributes:
      - name: "stripe_report"
        type: "string"
        description: |
          If not `null`, this indicates that a {{ integration.display_name }} fraud assessment exists for the charge. This field may have a value of `fraudulent`.

      - name: "user_report"
        type: "string"
        description: |
          If not `null`, this indicates that a fraud assessment reported by you exists for the charge. Possible values are:

          - `safe`
          - `fraudulent`

  - name: "invoice"
    type: "string"
    description: "The ID of the invoice the charge is for."
    foreign-key-id: "invoice-id"

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: "Additional information attached to the charge."
    object-attributes:
      - name: ""
        type: 
        description: ""

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `charge`."

  - name: "on_behalf_of"
    type: "string"
    description: "The account the charge was made on behalf of without triggering an automatic transfer."

  - name: "order"
    type: "string"
    description: "The ID of the order this charge is for."

  - name: "outcome"
    type: "object"
    description: "Details about whether the payment was accepted and why."
    object-attributes:
      - name: "network_status"
        type: "string"
        description: |
          The network status of the outcome. Possible values are:

          - `approved_by_network`
          - `declined_by_network`
          - `not_sent_to_network`
          - `reversed_after_approval` - This value indicates that [{{ integration.display_name }} blocked the payment](https://stripe.com/docs/declines#blocked-payments){:target="new"} after bank authorization, and may temporarily appear as "pending" on a cardholder's statement.

      - name: "reason"
        type: "string"
        description: |
          A detailed explanation of the outcome's `type`. Possible values are:

          - `highest_risk_level` - Indicates the charge was blocked by Radar's default block rule.
          - `elevated_risk_level` - Indicates the charge was placed in review by Radar's default review rule.
          - `rule` - Indicates the charge was authorized, blocked, or placed in review by a custom rule.

          Refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/declines){:target="new"} for more info about this attribute.

      - name: "risk_level"
        type: "string"
        description: |
          Indicates {{ integration.display_name }}'s evaluation of the riskiness of the payment. Possible values are:

          - `normal`, `elevated`, `highest` - Evaluated payments
          - `not_assessed` - Non-card payments, and card-based payments predating the public assignment of risk levels
          - `unknown` - Indicates an error in the risk evaluation

      - name: "risk_score"
        type: "integer"
        description: |
          Indicates {{ integration.display_name }}'s evaluation of the riskiness of the payment.

          - For evaluated payments, this attribute will contain a value between `0` and `100`.

          - For non-card payments, and card-based payments predating the public assignment of risk levels, this field will be `null`.

      - name: "seller_message"
        type: "string"
        description: "A description of the outcome type and reason designed for you, the recipient of the payment."

      - name: "type"
        type: "string"
        description: |
          The type of the outcome. Possible values are:

          - `authorized`
          - `manual_review`
          - `issuer_declined`
          - `blocked`
          - `invalid`

  - name: "paid"
    type: "boolean"
    description: "Indicates if the charge succeeded (`true`) or was successfully authorzed for later capture (`false`)."

  - name: "payment_intent"
    type: "string"
    description: "The ID of the payment intent associated with the charge."
    # foreign-key-id: "payment-intent-id"

  - name: "receipt_email"
    type: "string"
    description: "The email address that the receipt for the charge was sent to."

  - name: "receipt_number"
    type: "string"
    description: "The transaction number that appears on email receipts for the charge. This will be `null` until a receipt is sent."

  - name: "refunded"
    type: "boolean"
    description: "Indicates if the charge has been fully refunded. If the charge is only partially refunded, this attribute will be `false`."

  - name: "refunds"
    type: "array"
    description: "A list of refunds that have been applied to the charge."
    array-attributes:
      - name: "value"
        type: "string"
        primary-key: true
        description: "The ID of the refund."

  - name: "review"
    type: "string"
    description: "The ID of the review associated with the charge."

  - name: "shipping"
    type: "object"
    description: "The shipping information for the charge."
    object-attributes:
      - name: "address"
        type: "object"
        description: "The shipping address."
        object-attributes:
          - name: "city"
            type: "string"
            description: "The city of the shipping address."

          - name: "country"
            type: "string"
            description: "The two-letter country code of the shipping address. For example: `us`"

          - name: "line1"
            type: "string"
            description: "The first address line of the shipping address."

          - name: "line2"
            type: "string"
            description: "The second address line of the shipping address."

          - name: "postal_code"
            type: "string"
            description: "The zip or postal code of the shipping address."

          - name: "state"
            type: "string"
            description: "The state, county, province, region, etc. of the shipping address"

      - name: "carrier"
        type: "string"
        description: "The delivery service that shipped a physical product. For example: `FedEx`"

      - name: "name"
        type: "string"
        description: "The recipient's name."

      - name: "phone"
        type: "string"
        description: "The recipient's phone number, including extension."

      - name: "tracking_number"
        type: "string"
        description: "The tracking number for a physical product, obtained from the delivery service (`carrier`)."

  - name: "source"
    type: "object"
    description: *source-description
    object-attributes: *source-attributes

  - name: "source_transfer"
    type: "string"
    description: "The transfer ID that created the charge. Only present if the charge came from another {{ integration.display_name }} account."
    foreign-key-id: "transfer-id"

  - name: "statement_description"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "statement_descriptor"
    type: "string"
    description: "Additional information about the charge. This appears on the customer's credit card statement."

  - name: "status"
    type: "string"
    description: |
      The status of the payment. Possible values are:

      - `succeeded`
      - `pending`
      - `failed`

  - name: "transfer_group"
    type: "string"
    description: "A string that identifies this transaction as part of a group."

  - name: "updated"
    type: "date-time"
    description: "The time at which the charge was last updated."
---