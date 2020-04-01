---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "google-analytics"
version: "1"

name: "SAMPLE REPORT"
description: |
  For every report you create in the integration's settings page, Stitch will create a corresponding table in your destination. The table will contain the [metrics and dimensions you select](#track-data), along with a few columns Stitch requires for replication.

  **Note**: Every row in this table pertains to a specific day. Use the `start_date` and `end_date` columns to identify what day the row is for.

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ site.data.stitch.sdc-columns.current-columns.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      This column is a Stitch-generated SHA 256 hash that should be used as a Primary Key. The hash consists of a UTF-8 encoded JSON list containing:

      - The account ID, web property ID, and profile ID of the associated report
      - Pairs of `ga:dimension_name` and `dimension_value`
      - The `start_date` and `end_date` values for the record, in `YYYY-mm-dd` format

  - name: "start_date"
    type: "date-time"
    replication-key: true
    description: "The start date for the record."

  - name: "account_id"
    type: "integer"
    description: "The ID of the account to which this view (profile) belongs. For example: `30481`"

  - name: "[DIMENSIONS_YOU_SELECT]"
    type: "varies"
    description: |
      A column will be created for every Dimension selected during setup, up to Google's maximum of 7.

  - name: "end_date"
    type: "date-time"
    description: "The end date for the record."

  - name: "[METRICS_YOU_SELECT]"
    type: "varies"
    description: |
      A column will be created for every metric selected during setup, up to Google's maximum of 10.

  - name: "profile_id"
    type: "string"
    description: "The view (profile) id. For example: `1174`"

  - name: "web_property_id"
    type: "string"
    description: "The ID of the web property to which the view (profile) belongs to. For example: `UA-30481-1`"
---