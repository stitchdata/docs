---
tap: "impact"
version: "1"
key: "ftp-file-submission"

name: "ftp_file_submissions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/ftp_file_submissions.json"
description: |
  The `{{ table.name }}` table contains info about FTP file submissions.

replication-method: "Key-based Incremental"

api-method:
  name: "Get FTP file submissions"
  doc-link: "https://developer.impact.com/default#operations-FTP_File_Submissions-GetFTPFileSubmissions"

attributes:
  - name: "batch_id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "ftp-file-submission-id"

  - name: "submission_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "completion_date"
    type: "date-time"
    description: ""

  - name: "errors_uri"
    type: "string"
    description: ""

  - name: "file_name"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "total_errors"
    type: "string"
    description: ""

  - name: "total_records"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---