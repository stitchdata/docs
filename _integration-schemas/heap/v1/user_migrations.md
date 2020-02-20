---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "heap"
version: "1" 

name: "user_migrations"
doc-link: https://docs.heapanalytics.com/docs/heap-sql-retroactive-s3-specification
description: |
  The `{{ table.name }}` table contains info about user migrations.

  **Note**: Custom attributes are supported for this table. As {{ integration.display_name }} schemas are dynamic, Stitch's `{{ table.name }}` documentation will only list the non-custom attributes outlined in {{ integration.display_name }}'s documentation.

replication-method: "Key-based Incremental"

replication-key:
  name: "[See Replication](#incremental-replication-for-heap)"

attributes:
  - name: "from_user_id"
    type: "string"
    primary-key: true
    description: "The migrating user's ID."

  - name: "to_user_id"
    type: "integer"
    description: "The destination user's ID."
    foreign-key-id: "user-id"

  - name: "time"
    type: "string"
    description: "The timestamp when the migration occurred."
---