---
tap: "zoom"
version: "1"
key: "webinar-registrant"

name: "webinar_registrants"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarregistrants"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_registrants.json"
description: |
  The `{{ table.name }}` table contains information about the users registered for a webinar in your {{ integration.display_name }} account. Only webinars where registration is required are included in this table.

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, the following requirements must be met to retrieve this data:

  - A Pro plan or higher with a webinar add-on
  - An authentication app with the `webinar:read:admin` and `webinar:read` scopes

replication-method: "Full Table"

api-method:
  name: "Get webinar registrants"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarregistrants"

attributes:
  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The registrant ID." 
    # foreign-key-id: "webinar-registrant-id"

  - name: "address"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "county"
    type: "string"
    description: ""

  - name: "create_time"
    type: "date-time"
    description: ""

  - name: "custom_questions"
    type: "array"
    description: ""
    subattributes:
      - name: "title"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""
  
  - name: "industry"
    type: "string"
    description: ""

  - name: "job_title"
    type: "string"
    description: ""

  - name: "join_url"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "no_of_employees"
    type: "string"
    description: ""

  - name: "org"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "purchasing_time_frame"
    type: "string"
    description: ""

  - name: "role_in_purchase_process"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""
  
  - name: "zip"
    type: "string"
    description: ""
---