---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "google-analytics"
version: "14-09-2016"

name: "report"
description: |
  The `{{ table.name }}` table will contain the [Metrics and Dimensions selected during integration setup](#schema).

  ### Data pagination

  {{ integration.display_name }} data is paginated on a daily basis. This means that a single row in this table pertains to a specific day. Use the `start_date` and `end_date` columns to identify what day the row is for.

  ### Primary keys

  The Primary Key for this table is a composite key made up of all **Dimension columns** and the `start_date` and `end_date` columns.

  For example: If `referralPath` and `country` were Dimension columns in the table, both columns, along with `start_date` and `end_date` would make up the Primary Key for the table.

replication-method: "Key-based Incremental"

replication-key:
  name: "start-date"
## Note: This is a query param the integration passes in the API request.
## See: https://developers.google.com/analytics/devguides/reporting/core/v3/reference#startDate

attributes:
  - name: "start_date"
    type: "date-time"
    primary-key: true
    description: "The start date for the record."

  - name: "end_date"
    type: "date-time"
    primary-key: true
    description: "The end date for the record."

  - name: "[DIMENSIONS_YOU_SELECT]"
    type: "varies"
    primary-key: true
    description: |
      A column will be created for every Dimension selected during setup. Every Dimension column comprises the composite Primary Key for the table.

  - name: "[METRICS_YOU_SELECT]"
    type: "varies"
    description: |
      A column will be created for every Metric selected during setup.
---