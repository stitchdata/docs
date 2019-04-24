---
tap: "netsuite"
version: "1.0"

name: "HcmJob"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/hcmjob.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/HcmJob.json"
description: |
  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "hcmjob"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "hcm-job-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "employmentCategory"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "jobId"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---