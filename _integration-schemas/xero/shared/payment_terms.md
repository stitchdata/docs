---
tap-reference: "xero"
version: "1.0"

name: "payment_terms"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/payment_terms.json

attributes:
  - name: "Sales"
    type: "object"
    description: "Details about the payment terms used for sales transactions."
    object-attributes:
      - name: "Day"
        type: "integer"
        description: "An integer used with the payment term type to indicate the calendar date of the payment term used for sales transactions."

      - name: "Type"
        type: "integer"
        description: |
          The payment term type used for sales transactions. Possible values are:

          - `DAYSAFTERBILLDATE` - _n_ day(s) after the bill date
          - `DAYSAFTERBILLMONTH`- _n_ day(s) after the bill month
          - `OFCURRENTMONTH` - Of the current month
          - `OFFOLLOWINGMONTH` - Of the following month

  - name: "Bills"
    type: "object"
    description: "Details about the payment terms used for bills (invoices)."
    object-attributes:
      - name: "Day"
        type: "integer"
        description: "An integer used with the payment term type to indicate the calendar date of the payment term used for bills."

      - name: "Type"
        type: "integer"
        description: |
          The payment term type used for bills (invoices). Possible values are:

          - `DAYSAFTERBILLDATE` - _n_ day(s) after the bill date
          - `DAYSAFTERBILLMONTH`- _n_ day(s) after the bill month
          - `OFCURRENTMONTH` - Of the current month
          - `OFFOLLOWINGMONTH` - Of the following month
---