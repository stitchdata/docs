---
tap: "marketo"
version: "2"

name: "activity_types"
doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getAllActivityTypesUsingGET"
singer-schema: https://github.com/singer-io/tap-marketo/blob/master/tap_marketo/schemas/activity_types.json
description: |
  The `{{ table.name }}` table contains metadata about the activity types - form fill, web page visit, lead creation, and so on - available in {{ integration.display_name }}.

# notes: |
#   #### Filter Deleted Leads
#   When joined with the `activities` table, you can use specific activity types to filter out deleted leads, assess list membership, and more. Here are a few noteworthy activity types:

#   - **Add to List and Remove from List** - These events can be used to discover lead list membership.
#   - **Delete Lead** - A `delete lead` event indicates leads that have been deleted. We recommend using this activity to filter out deleted leads.
#   - **Add a Lead to a Nurture Program, Change Nurture Track, and Change Nurture Cadence** - These events can help you determine what nurture programs a lead is in and lead activity against that program.

replication-method: "Full Table"
api-method:
  name: "Get all activity types"
  doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getAllActivityTypesUsingGET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The activity type ID."
    foreign-key-id: "activity-type-id"

  - name: "name"
    type: "string"
    description: "The name of the activity type. Ex: `Change Nurture Track`"

  - name: "description"
    type: "string"
    description: "The description of the activity type."

  - name: "primaryAttribute"
    type: "object"
    description: "Primary attributes of the activity type."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the primary attribute."

      - name: "dataType"
        type: "string"
        description: "The data type of the primary attribute."

  - name: "attributes"
    type: "array"
    description: "Secondary attributes of the activity type."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the secondary attribute."

      - name: "dataType"
        type: "string"
        description: "The data type of the secondary attribute."
---