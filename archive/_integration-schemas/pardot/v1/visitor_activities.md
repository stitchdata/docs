---
tap: "pardot"
version: "1"
key: "visitor-activity"

name: "visitor_activities"
doc-link: "http://developer.pardot.com/kb/object-field-references/#visitor-activity"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/visitor_activities.json"
description: |
  The `{{ table.name }}` table contains info about visitor activities.

replication-method: "Key-based Incremental"

api-method:
  name: "Query visitor activities"
  doc-link: "http://developer.pardot.com/kb/api-version-3/visitor-activities/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The visitor activity ID."
    foreign-key-id: "visitor-activity-id"

  - name: "campaign"
    type: "object"
    description: "TODO"

  - name: "created_at"
    type: "date-time"
    description: "The time the visitor activity was created."

  - name: "details"
    type: "string"
    description: "Details about the visitor activity."

  - name: "email_id"
    type: "integer"
    description: "The ID of the email associated with the visitor activity."

  - name: "email_template_id"
    type: "integer"
    description: "The ID of the email template associated with the visitor activity."
    foreign-key-id: "email-template-id"

  - name: "file_id"
    type: "integer"
    description: "The ID of the file associated with the visitor activity."

  - name: "form_handler_id"
    type: "integer"
    description: "The ID of the form handler associated with the visitor activity."

  - name: "form_id"
    type: "integer"
    description: "The ID of the form associated with the visitor activity."

  - name: "landing_page_id"
    type: "integer"
    description: "The ID of the landing page associated with the visitor activity."

  - name: "list_email_id"
    type: "integer"
    description: "The ID of the list email associated with the visitor activity."
    foreign-key-id: "list-email-id"

  - name: "multivariate_test_variation_id"
    type: "integer"
    description: "The ID of the multivariate test variation associated with the visitor activity."

  - name: "paid_search_id_id"
    type: "integer"
    description: "The ID of the paid search ad associated with the visitor activity."

  - name: "prospect_id"
    type: "integer"
    description: "The ID of the prospect associated with the visitor activity."
    foreign-key-id: "prospect-id"

  - name: "site_search_query_id"
    type: "integer"
    description: "The ID of the site search query associated with the visitor activity."

  - name: "type"
    type: "integer"
    doc-link: "http://developer.pardot.com/kb/object-field-references/#visitor-activity"
    description: |
      The type of the visitor activity. Refer to [{{ integration.display_name }}'s documentation](http://developer.pardot.com/kb/object-field-references/#visitor-activity){:target="new"} for a full list of possible values.

  - name: "type_name"
    type: "string"
    doc-link: "http://developer.pardot.com/kb/object-field-references/#visitor-activity"
    description: |
      The type name of the visitor activity. Refer to [{{ integration.display_name }}'s documentation](http://developer.pardot.com/kb/object-field-references/#visitor-activity){:target="new"} for a full list of possible values.

  - name: "visitor_id"
    type: "integer"
    description: "The ID of the visitor."
    foreign-key-id: "visitor-id"

  - name: "visitor_page_view_id"
    type: "integer"
    description: "The ID of the visitor page view associated with the visitor activity."
---