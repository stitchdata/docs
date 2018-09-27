---
tap-reference: "xero"
version: "1.0"

name: "tracking_categories"
doc-link: https://developer.xero.com/documentation/api/tracking-categories
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/tracking_categories.json

attributes:
  - name: "TrackingCategoryID"
    type: "string"
    description: "The tracking category ID."

  - name: "Status"
    type: "string"
    description: "The status of the tracking category."

  - name: "TrackingCategoryName"
    type: "string"
    description: "The name of the tracking category."

  - name: "Name"
    type: "string"
    description: "The name of the tracking option."

  - name: "Option"
    type: "string"
    description: "The value of the tracking option."

  - name: "Options"
    type: "array"
    description: "Details about the tracking option."
    array-attributes:
      - name: "IsActive"
        type: "boolean"
        description: "If `true`, the tracking option is active."

      - name: "IsDeleted"
        type: "boolean"
        description: "If `true`, the tracking option has been deleted."

      - name: "TrackingOptionID"
        type: "string"
        description: "The ID of the tracking option."

      - name: "IsArchived"
        type: "boolean"
        description: "If `true`, the tracking option has been archived."

      - name: "Status"
        type: "string"
        description: "The status of the tracking option."

      - name: "Name"
        type: "string"
        description: "The name of the tracking option."
---