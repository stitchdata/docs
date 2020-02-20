---
tap-reference: "xero"
version: "1"

name: "validation_errors"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/validation_errors.json

attributes:
  - name: "Message"
    type: "string"
    description: "The validation error message."
---