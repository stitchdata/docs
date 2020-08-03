---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "heap"
version: "1" 

name: "users"
doc-link: https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#users-table
description: |
  The `{{ table.name }}` table contains info about users.

  **Note**: Custom attributes are supported for this table. As {{ integration.display_name }} schemas are dynamic, Stitch's `{{ table.name }}` documentation will only list the non-custom attributes outlined in {{ integration.display_name }}'s documentation.

replication-method: "Key-based Incremental"

replication-key:
  name: "[See Replication](#incremental-replication-for-heap)"

attributes:
  - name: "user_id"
    type: "string"
    primary-key: true
    description: "The user ID." 

  - name: "identity"
    type: "string"
    description: "The user's username or other unique token."

  - name: "handle"
    type: "string"
    description: "The user's username or other unique token."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "joindate"
    type: "string"
    description: "The UTC timestamp when the user was first seen."

  - name: "last_modified"
    type: "string"
    description: "The UTC timestamp when the user's data was last modified."

  - name: "Custom Attributes"
    type: 
    description: "Any custom attributes applied to the user model in {{ integration.display_name }}."
---