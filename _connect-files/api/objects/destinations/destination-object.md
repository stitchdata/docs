---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "destinations"
order: 4


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination"
endpoint-url: "/destinations"

description: "{{ api.core-objects.destinations.description }}"
intro-short: "Create, update, and delete destinations" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false

  - number: "3"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "create-a-destination"
    title: "Create a destination"
    method: "post"
    short: "{{ api.core-objects.destinations.create.description | flatify }}"

  - id: "update-a-destination"
    title: "Update a destination"
    method: "put"
    short: "{{ api.core-objects.destinations.update.description | flatify }}"

  - id: "list-destinations"
    title: "List destinations"
    method: "get"
    short: "{{ api.core-objects.destinations.list.description | flatify }}"

  - id: "delete-a-destination"
    title: "Delete a destination"
    method: "delete"
    short: "{{ api.core-objects.destinations.delete.description | flatify }}"


# -------------------------- #
#      COMMON ATTRIBUTES     #
# -------------------------- #

## These attributes are shared across all versions of the object.
## Attributes specific to a version are in that object's file.

## Ex: _connect-files/api/objects/destinations/v4/destination-object-v4.md
## Has the attributes specific to version 4 of this object.

common-attributes:
  - name: "id"
    type: "integer"
    description: "A unique identifier for this destination."
    example-value: |
      110397

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the destination object was created."
    example-value: |
      "2018-11-14T20:09:30Z"

  - name: "type"
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"
    example-value: |
      "postgres"

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the destination object was last updated."
    example-value: |
      "2018-11-27T15:25:20Z"
---