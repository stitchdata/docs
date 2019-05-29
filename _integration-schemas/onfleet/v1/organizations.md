---
tap: "onfleet"
version: "1.0"

name: "organizations"
doc-link: "http://docs.onfleet.com/docs/organizations"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/organizations.json"
description: |
  The `{{ table.name }}` table contains info about the organizations in your {{ integration.display_name }} account. In {{ integration.display_name }}, an organization is the top-most entity - it contains administrators, teams, works, and tasks, all of which belong to the organization.

replication-method: "Key-based Incremental"

api-method:
    name: "Get details"
    doc-link: "http://docs.onfleet.com/docs/organizations#get-details"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The organization ID."
    foreign-key-id: "organization-id"

  - name: "timeLastModified"
    type: "date-time"
    replication-key: true
    description: "The time the organization was last modified."

  - name: "country"
    type: "string"
    description: "The country the organization resides in."

  - name: "delegatees"
    type: "array"
    description: "A list of IDs of organizations that the organization can assign tasks to."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the organization that can be assigned tasks."
        foreign-key-id: "organization-id"

  - name: "email"
    type: "string"
    description: "The email address for the organization."

  - name: "image"
    type: "string"
    description: "The image associated with the integration."

  - name: "name"
    type: "string"
    description: "The full name of the organization."

  - name: "timeCreated"
    type: "date-time"
    description: "The time the organization was created."

  - name: "timezone"
    type: "string"
    description: "The timezone the organization resides in."
---