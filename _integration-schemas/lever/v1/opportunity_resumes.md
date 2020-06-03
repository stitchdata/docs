---
tap: "lever"
version: "1"
key: "candidate-resumes"

name: "opportunity_resumes"
doc-link: "https://hire.lever.co/developer/documentation#opportunities"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/opportunity_resumes.json"
description: |
  The `{{ table.name }}` table contains info about candidate resumes.

  **Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

replication-method: "Key-based Incremental"

replication-key:
  name: "opportunities.updated_at"

api-method:
  name: "List all opportunities"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-opportunities"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The resume ID."
    foreign-key-id: "resume-id"

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the resume was created in {{ integration.display_name }}."

  - name: "file"
    type: "object"
    description: "Metadata about the resume file."
    subattributes:
      - name: "downloadUrl"
        type: "string"
        description: "The resume file download URL."

      - name: "ext"
        type: "string"
        description: "The resume file extension."

      - name: "name"
        type: "string"
        description: "The resume file name."

      - name: "uploadedAt"
        type: "number"
        description: "The datetime when the file was uploaded in {{ integration.display_name }}."

  - name: "parsedData"
    type: "object"
    description: "The candidate's parsed resume, usually extracted from an attached PDF/Word document or online profile."
    subattributes:
      - name: "positions"
        type: "array"
        description: "A list of positions held by the candidate."
        subattributes:
          - name: "org"
            type: "string"
            description: "The organization."

          - name: "title"
            type: "string"
            description: "The title of the position."

          - name: "summary"
            type: "string"
            description: "The summary of the position."

          - name: "location"
            type: "string"
            description: "The location of the position."

          - name: "start"
            type: "object"
            description: "The start date of the position."
            anchor-id: 1
            subattributes: &month-year
              - name: "month"
                type: "integer"
                description: "The month."

              - name: "year"
                type: "integer"
                description: "The year."

          - name: "end"
            type: "object"
            description: "The end date of the position."
            anchor-id: 1
            subattributes: *month-year

      - name: "school"
        type: "array"
        description: "A list of schools the candidate attended."
        subattributes:
          - name: "org"
            type: "string"
            description: "The name of the school."

          - name: "degree"
            type: "string"
            description: "The name of the degree the candidate pursued."

          - name: "summary"
            type: "string"
            description: "The summary of the candidate's studies."

          - name: "field"
            type: "string"
            description: "The candidate's field of study."

          - name: "start"
            type: "object"
            description: "The date the candidate started studying at the school."
            anchor-id: 2
            subattributes: *month-year

          - name: "end"
            type: "object"
            description: "The date the candidate left the school."
            anchor-id: 2
            subattributes: *month-year
---