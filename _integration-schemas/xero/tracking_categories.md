---
tap: "xero"
version: "1.0"

name: "tracking_categories"
doc-link: &api-doc https://developer.xero.com/documentation/api/tracking-categories
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/tracking_categories.json
description: |
  The `tracking_categories` table contains info about the tracking categories in your Xero account. Tracking categories are used to track the performance of different areas of a business.

replication-method: "Full Table"

api-method:
  name: getTrackingCategories
  doc-link: *api-doc

attributes:
  - name: "TrackingCategoryID"
    type: "string"
    primary-key: true
    description: "The tracking category ID."

  - name: "Name"
    type: "string"
    description: "The name of the tracking category."

  - name: "Status"
    type: "string"
    description: |
      The status of the tracking category. Possible values are:

  - name: "Option"
    type: "string"
    description: ""

  - name: "TrackingCategoryName"
    type: "string"
    description: ""

  - name: "TrackingOptionID"
    type: "string"
    description: ""

  - name: "TrackingOptionName"
    type: "string"
    description: ""

  - name: "Options"
    type: "array"
    description: ""
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

      # - name: "HasValidationErrors"
      #   type: "boolean"
      #   description: ""
---