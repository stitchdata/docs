---
tap: "netsuite"
version: "10-15-2015"

name: "netsuite_item_revision"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2015_1/schema/record/itemrevision.html
description: |
  The `{{ table.name }}` table contains info about item revisions.

replication-method: "Full Table"
abstract: true

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-revision"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} ID.

  - name: "_type"
    type: "string"
    primary-key: true
    description: |
      The type of item that was revised.

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---