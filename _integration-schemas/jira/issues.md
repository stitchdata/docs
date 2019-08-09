---
tap: "jira"
version: "1.0"


name: "issues"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/issue-getIssue
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/issues.json
description: |
  The `issues` table contains info about the issues in your {{ integration.display_name }} instance. This table only contains core issue data - some data is located in other tables, such as [`changelogs`](#changelogs), [`issue_comments`](#issue_comments), and [`issue_transitions`](#issue_transitions).

  **Note**: To replicate this data, the `Browse projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} for the project that the issue is in is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

  #### Identifying deleted issues

  When an issue is hard-deleted in JIRA, the record for the issue will remain in your destination. This is due to the nature of Stitch [Replication Keys]({{ link.replication.rep-keys | prepend: baseurl }}) and the design of JIRA's API:

  - **Replication Keys**: This table uses the values in the `{{ replication-keys | strip }}` column to identify new and updated data for replication. If a record is hard-deleted, there won't be a value for Stitch to check and thus no way to identify the change, meaning the record will remain in the destination.
  - **JIRA's API**: Currently, JIRA's API doesn't include a way to identify deleted issues.

  To identify deleted issues, [Atlassian's suggested workaround](https://answers.atlassian.com/questions/75537/how-do-i-find-if-an-issue-has-been-deleted){:target="new"} is:

  1. Create a status in JIRA that will be applied to issues you want to delete.
  2. **Before deleting the issue, apply the status**.
  3. Allow Stitch to extract and load the updated data into your destination.
  4. Delete the issue.
  5. After Stitch finishes loading the data, use the `fields__status__name` field in your queries to filter issues with the deleted status you applied in step 2. For example, the following query would return any issues that had been marked with a the deleted status:

     ```sql
     SELECT *
     FROM stitch_jira.issues
     WHERE fields__status__name = 'Deleted'
     ```

replication-key:
  name: "updated"

replication-method: "Key-based Incremental"

api-method:
  name: search(fields=*all, expand=changelog,transitions)
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/search-search


## COMMON ATTRIBUTES

json-type-attributes: &json-type-attributes
  - name: "type"
    type: "string"
    description: "The data type of the field."

  - name: "items"
    type: "string"
    description: "When the `type` is an `array`, the name of the field items within the array."

  - name: "system"
    type: "string"
    description: "If the field is a system field, the name of the field."

  - name: "custom"
    type: "string"
    description: "If the field is a custom field, the URI of the field."

  - name: "customId"
    type: "integer"
    description: "If the field is a custom field, the custom ID of the field."



attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue ID."
    foreign-key-id: "issue-id"

  - name: "expand"
    type: "string"
    description: &stitch-field "**This field is used by Stitch to request data from {{ integration.display_name }}.**"

  - name: "self"
    type: "string"
    description: "The URL of the issue."

  - name: "key"
    type: "string"
    description: "The issue key."

  - name: "renderedFields"
    type: ""
    description: *stitch-field

  - name: "names"
    type: "object"
    description: "The display names of the fields in the issue."
    subattributes:
      - name: "patternProperties"
        type: "string"
        description: ""

  - name: "schema"
    type: "object"
    description: "The schema describing a field type."
    subattributes: *json-type-attributes

  - name: "editmeta"
    type: "object"
    description: "Details about how each issue field can be edited."
    subattributes:
      - name: "required"
        type: "boolean"
        description: "Indicates whether the field is required."

      - name: "schema"
        type: "object"
        description: ""
        subattributes: *json-type-attributes

      - name: "name"
        type: "string"
        description: "The name of the field."

      - name: "key"
        type: "string"
        description: "The field key."

      - name: "autoCompleteUrl"
        type: "string"
        description: "The URL that can be used to automatically complete the field."

      - name: "hasDefaultValue"
        type: "boolean"
        description: "Indicates whether the field has a default value."

      - name: "operations"
        type: "array"
        description: "The list of operations that can be performed on the field."
        subattributes:
          - name: "value"
            type: "string"
            description: "The operation that can be performed on the field."

      - name: "allowedValues"
        type: "array"
        description: "The list of values allowed in the field."
        subattributes:
          - name: "value"
            type: "string"
            description: "The value allowed in the field."

      - name: "defaultValue"
        type: "varies"
        description: "The default value of the field."

  - name: "versionedRepresentations"
    type: ""
    description: *stitch-field

  - name: "fieldsToInclude"
    type: ""
    description: *stitch-field

  - name: "fields"
    type: "object"
    description: |
      Details about the fields in the issue.

      **Note**: While only a handful of fields are listed here, Stitch will replicate and persist any fields returned by {{ integration.display_name }}'s API. This includes custom fields as well as standard issue fields such as `assignee` or `description`.
    subattributes:
      - name: "updated"
        type: "date-time"
        description: "The date and time the field was last updated."

      - name: "created"
        type: "date-time"
        description: "The date and time the field was created."

      - name: "lastViewed"
        type: "date-time"
        description: "The date and time the field was last viewed."

      - name: "attachment"
        type: "array"
        description: "Details about issue attachment."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The attachment ID."

          - name: "self"
            type: "string"
            description: "The URL of the attachment."

          - name: "thumbnail"
            type: "string"
            description: "The URL of the thumbnail version of the attachment."

          - name: "filename"
            type: "string"
            description: "The filename of the attachment."

          - name: "created"
            type: "date-time"
            description: "The date and time when the attachment was created."

          - name: "author"
            type: "object"
            description: "Details about the attachment author."
            subattributes:
              - name: "accountId"
                type: "string"
                description: "The author's account ID."

              - name: "active"
                type: "boolean"
                description: "Indicates if the author is an active user."

              - name: "avatarUrls"
                type: "object"
                description: "The URLs associated with the avatars used by the {{ attribute.name }}."
                subattributes:
                  - name: "16x16"
                    type: "string"
                    description: "The URL of the {{ attribute.name }}'s 16x16 avatar."

                  - name: "24x24"
                    type: "string"
                    description: "The URL of the {{ attribute.name }}'s 24x24 avatar."

                  - name: "32x32"
                    type: "string"
                    description: "The URL of the {{ attribute.name }}'s 32x32 avatar."

                  - name: "48x48"
                    type: "string"
                    description: "The URL of the {{ attribute.name }}'s 48x48 avatar."

              - name: "displayName"
                type: "string"
                description: "The {{ attribute.name }}'s display name."

              - name: "emailAddress"
                type: "string"
                description: "The {{ attribute.name }}'s email address."

              - name: "key"
                type: "string"
                description: "The {{ attribute.name }} ID."
                foreign-key-id: "user-key"

              - name: "name"
                type: "string"
                description: "The {{ attribute.name }}'s name."

              - name: "self"
                type: "string"
                description: "The URL of the {{ attribute.name }} in {{ integration.display_name }}."

              - name: "timeZone"
                type: "string"
                description: "The {{ attribute.name }}'s time zone."
---
