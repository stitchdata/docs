---
tap: "netsuite"
version: "1"

name: "Deleted"
doc-link: "https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Deleted.json"
description: |
  The `{{ table.name }}` table contains info about deleted records.

  {{ integration.permission-for-table | flatify }}

  #### Objects with delete support

  According to [{{ integration.display_name }}'s documentation](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html){:target="new"}, only certain objects support the `{{ table.api-method.name }}` operation Stitch uses to retrieve deleted record data from the SuiteTalk API.

  Refer to the [Deleted records](#deleted-records) section for more info and a list of record types with delete support.

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "deleted"

replication-method: "Key-based Incremental"

api-method:
    name: "getDeleted"
    doc-link: "https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: "The record's ID."

  - name: "type"
    type: "string"
    primary-key: true
    description: |
      The value of this column will vary depending on the record type:

      - **Custom records** - This field will contain a numerical ID pertaining to the record.
      - **Standard records** - This field will contain the type of record that was deleted. For example: `Invoice`. Refer to the [Record types with delete support](#record-types-with-delete-support) section for a list of possible record types.

  - name: "deletedDate"
    type: "date-time"
    replication-key: true
    description: "The time the record was deleted."

  - name: "customRecord"
    type: "boolean"
    description: |
      If `true`, the record that was deleted was a custom record. If `false`, the record that was deleted was a standard record.

  - name: "externalId"
    type: "string"
    description: "The record's external ID, if available."

  - name: "name"
    type: "string"
    description: |
      The value of this column will vary depending on the record type:

      - **Custom records** - This field will contain the record's `internalId`.
      - **Standard records** - This field will contain the name of the record that was deleted. For example: `Invoice #INV197`.

  - name: "scriptId"
    type: "string"
    description: "The script ID identifying the specific custom record or custom transaction type."
---