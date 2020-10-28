---
tap: "marketo"
version: "2"

name: "activities_[activity_type]"
doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET"
singer-schema: https://github.com/singer-io/tap-marketo/blob/master/tap_marketo/schemas/activities.json
description: |
  In [version 1 of Stitch's Marketo integration]({{ site.baseurl }}/integrations/saas/{{ integration.name }}/v1), the `activities` table contained all data pertaining to lead activities.

  In this version, you can choose to replicate lead activity data for specific activity types. For every activity type defined in your {{ integration.display_name }} account, you'll see an `{{ table.name }}` table in the {{ app.buttons.tables }} tab. For example: `activities_click_email` contains lead activity data for the `click_email` activity type.

  These tables will contain the fields listed below, along with any fields specific to that activity type.

replication-method: "Key-based Incremental"
api-method:
  name: "Get lead activities"
  doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET"

attributes:
  - name: "marketoGuid"
    type: "string"
    primary-key: true
    description: "The ID of the activity."
    # foreign-key-id: "activity-id"

  - name: "activityDate"
    type: "date-time"
    replication-key: true
    description: "The date of the activity."

  - name: "leadId"
    type: "integer"
    description: "The ID of the lead associated with the activity."
    foreign-key-id: "lead-id"

  - name: "activityTypeId"
    type: "integer"
    description: "The ID of the activity type."
    foreign-key-id: "activity-type-id"

  - name: "primary_attribute_value_id"
    type: "integer"
    description: "The ID of the activity's primary attribute."

  - name: "primary_attribute_name"
    type: "string"
    description: "The name of the activity's primary attribute."

  - name: "primary_attribute_value"
    type: "string"
    description: "The value of the activity's primary attribute."

  # - name: "attributes"
  #   type: "array"
  #   description: "Secondary attributes of the activity."
  #   subattributes:
  #     - name: "name"
  #       type: "string"
  #       description: "The name of the secondary attribute."

  #     - name: "value"
  #       type: "string"
  #       description: "The value of the secondary attribute."
---