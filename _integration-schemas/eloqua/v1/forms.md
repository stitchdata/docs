---
tap: "eloqua"
version: "1"

name: "forms"
key: "forms"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-1.0-assets-forms-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/forms.json"
description: |
  The `{{ table.name }}` table contains info about the forms in your {{ integration.display_name }} account.

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of forms"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The form ID."
    foreign-key-id: "form-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the form was last updated."

  - name: "accessedAt"
    type: "date-time"
    description: "The date and time the form was last accessed, expressed in Unix time."

  - name: "createdAt"
    type: "date-time"
    description: "The date and time the form was created, expressed in Unix time."

  - name: "createdBy"
    type: "string"
    description: "The ID of the user who created the form."

  - name: "currentStatus"
    type: "string"
    description: "The form's current status. For example: `draft`, `active`, or `complete`."

  - name: "customCSS"
    type: "string"
    description: ""

  - name: "defaultKeyFieldMapping"
    type: "string"
    description: ""

  - name: "depth"
    type: "string"
    description: &depth |
      Level of detail returned by the request. {{ integration.display_name }} APIs can retrieve entities at three different levels of depth: `minimal`, `partial`, and `complete`. Any other values passed are reset to `complete` by default. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/index.html#CSHID=RequestDepth){:target="new"} for more info.

  - name: "description"
    type: "string"
    description: "The description of the form."

  - name: "elements"
    type: "array"
    description: "A list of elements associated with the form."
    subattributes:
      - name: "altText"
        type: "string"
        description: ""

      - name: "createdFromContactFieldId"
        type: "string"
        description: ""

      - name: "dataType"
        type: "string"
        description: ""

      - name: "depth"
        type: "string"
        description: *depth

      - name: "displayType"
        type: "string"
        description: ""

      - name: "fieldMergeId"
        type: "string"
        description: ""

      - name: "fields"
        type: "string"
        description: ""

      - name: "htmlName"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: "The form element ID."

      - name: "instructions"
        type: "string"
        description: "The form element's field instructions. Field instructions are optional instructions that help users fill in fields."

      - name: "name"
        type: "string"
        description: ""

      - name: "numberOfFieldsToDisplay"
        type: "string"
        description: ""

      - name: "onlyShowIncompleteFields"
        type: "string"
        description: ""

      - name: "optionListId"
        type: "string"
        description: ""

      - name: "randomizeFields"
        type: "string"
        description: ""

      - name: "style"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "useGlobalSubscriptionStatus"
        type: "string"
        description: ""

      - name: "validations"
        type: "string"
        description: ""

  - name: "emailAddressFormFieldId"
    type: "string"
    description: "The form element's field instructions. Field instructions are optional instructions that help users fill in fields."

  - name: "folderId"
    type: "string"
    description: ""

  - name: "html"
    type: "string"
    description: "The asset's raw HTML content."

  - name: "htmlName"
    type: "string"
    description: "The asset's raw HTML name."

  - name: "name"
    type: "string"
    description: "The name of the form."

  - name: "permissions"
    type: "string"
    description: "The permissions for the form granted to your current instance."

  - name: "processingSteps"
    type: "array"
    description: "A list of the form's processing steps."
    subattributes:
      - name: "allowResend"
        type: "boolean"
        description: ""

      - name: "campaignElementId"
        type: "string"
        description: ""

      - name: "campaignId"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "emailAddressFormFieldId"
        type: "string"
        description: ""

      - name: "emailId"
        type: "string"
        description: ""

      - name: "eventId"
        type: "string"
        description: ""

      - name: "execute"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "keyFieldId"
        type: "string"
        description: ""

      - name: "keyFieldMapping"
        type: "string"
        description: ""

      - name: "landingPageId"
        type: "string"
        description: ""

      - name: "mappings"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "resendLimit"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "processingType"
    type: "string"
    description: |
      A list of the form's processing types. For example: `externalEmail`, `externalWebsite`, `internallyHosted`, `internalAgentProxyForm`.

  - name: "size"
    type: "string"
    description: ""

  - name: "style"
    type: "string"
    description: "The asset's main layout style."

  - name: "submitFailedLandingPageId"
    type: "string"
    description: "The landing page ID of the failed submit."

  - name: "type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."

  - name: "updatedBy"
    type: "string"
    description: "The ID of the user that last updated the form."
---