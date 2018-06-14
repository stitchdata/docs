---
tap: "hubspot"
version: "2.0"

name: "forms"
doc-link: https://developers.hubspot.com/docs/methods/forms/forms_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/forms.json
description: |
  The `forms` table contains info about your HubSpot website forms.

notes: 

replication-method: "Key-based Incremental"
api-method:
  name: getAllFormsFromAPortal
  doc-link: https://developers.hubspot.com/docs/methods/forms/v2/get_forms

attributes:
## Primary Key
  - name: "guid"
    type: "string"
    primary-key: true
    description: "The GUID of the form."

## Replication Key
  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the form was last updated."

  - name: "deletedAt"
    type: "integer"
    description: "If the form was deleted, the time that the deletion took place."

  - name: "portalId"
    type: "integer"
    description: "The ID of the portal the form belongs to."

  - name: "name"
    type: "string"
    description: "The name of the form."

  - name: "action"
    type: "string"
    description: &deprecated-field "Deprecated by {{ integration.display_name }}."

  - name: "method"
    type: "string"
    description: "The API method used to send the form submission. For example: `POST`"

  - name: "cssClass"
    type: "string"
    description: "The CSS class associated with the form."

  - name: "redirect"
    type: "string"
    description: "The URL that the visitor will be redirect to after filling out the form."

  - name: "submitText"
    type: "string"
    description: "The text that displays to the end-user to submit the form. For example: `Submit` or `Send Form`"

  - name: "followUpId"
    type: "string"
    description: *deprecated-field

  - name: "notifyRecipients"
    type: "string"
    description: "A list of email addresses that should receive submission notifications."

  - name: "leadNurturingCampaignId"
    type: "string"
    description: "The ID of the lead nurturing campaign the form is associated with."
    foreign-key: true

  - name: "formFieldGroups"
    type: "array"
    description: "Details about the fields in the form."
    array-attributes:
      - name: "default"
        type: "boolean"
        description: "Indicates if the form group is a default group." 

      - name: "isSmartGroup"
        type: "boolean"
        description: "Indicates if the form field group is a smart group."

      - name: "richText"
        type: "object"
        description: "Details about the rich text separators used between form field groups."
        object-attributes:
          - name: "content"
            type: "string"
            description: "The content of the rich text separator."

      - name: "fields"
        type: "array"
        description: "Details about the form field in the form."
        array-attributes:
          - name: "name"
            type: "string"
            description: "The name of the form field. This is the **internal** name for the form field. For example: `customerlastname`"

          - name: "label"
            type: "string"
            description: "The label of the form field. This is the **external** name for the form field. For example: `Last Name`"

          - name: "type"
            type: "string"
            description: "The data type of the form field. For example: `string`"

          - name: "fieldType"
            type: "string"
            description: "The type of form field. For example: `text` or `radio select`"

          - name: "description"
            type: "string"
            description: "A description of the form field."

          - name: "groupName"
            type: "string"
            description: "The name of the group the form field belongs to. For example: `contact information`"

          - name: "displayOrder"
            type: "integer"
            description: "The display order of the form field in the form."

          - name: "required"
            type: "boolean"
            description: "Indicates if the form field is required in the form."

          - name: "enabled"
            type: "boolean"
            description: "Indicates if the form field is enabled."

          - name: "hidden"
            type: "boolean"
            description: "Indicates if the form field is hidden."

          - name: "defaultValue"
            type: "string"
            description: "The default value of the form field."

          - name: "isSmartField"
            type: "boolean"
            description: "Indicates if the form field is a smart field."

          - name: "unselectedLabel"
            type: "string"
            description: *deprecated-field

          - name: "placeholder"
            type: "string"
            description: "The value of the placeholder text for the form field."

          - name: "labelHidden"
            type: "boolean"
            description: "Indicates if the label for the form field is hidden."

          - name: "options"
            type: "array"
            description: "For enumerated fields, this will be the options available for a field."
            array-attributes:
              - name: "description"
                type: "string"
                description: "The description of the field option."

              - name: "displayOrder"
                type: "integer"
                description: "The display order of the field option."

              - name: "doubleData"
                type: "number"
                description: *deprecated-field

              - name: "hidden"
                type: "boolean"
                description: "Indicates if the field option is hidden."

              - name: "label"
                type: "string"
                description: "The label of the field option."

              - name: "readOnly"
                type: "boolean"
                description: "Indicates if the field option is read-only."

              - name: "value"
                type: "string"
                description: "The value of the field option."

          - name: "validation"
            type: "object"
            description: "Details about the validation options applied to form fields."
            object-attributes:
              - name: "name"
                type: "string"
                description: "The name of validation option."

              - name: "message"
                type: "string"
                description: "The validation message."

              - name: "data"
                type: "string"
                description: "The method used to validate the data. For example: entering a minimum and maximum number of characters to validate phone number length. If you entered a minimum of 7 and maximum of 11, the value for this field would show as `7:11`"

              - name: "useDefaultBlockList"
                type: "boolean"
                description: "Indicates if the `Block free email providers` setting is enabled for email fields."

              - name: "blockedEmailAddresses"
                type: "array"
                description: "For email fields, the domains that are blocked. For example: `yahoo.com`"
                array-attributes:
                  - name: "value"
                    type: "string"
                    description: "The blocked email domain."

  - name: "createdAt"
    type: "date-time"
    description: "The time the form was created."

  - name: "performableHtml"
    type: "string"
    description: *deprecated-field

  - name: "migratedFrom"
    type: "string"
    description: *deprecated-field

  - name: "ignoreCurrentValues"
    type: "boolean"
    description: "Indicates if the form will pre-populate fields with known values for known contacts."

  - name: "deleteable"
    type: "boolean"
    description: "Indicates if the form is deleteable."

  - name: "inlineMessage"
    type: "string"
    description: "The 'thank you' message that displays on the page after the form is submitted."

  - name: "tmsId"
    type: "string"
    description: *deprecated-field

  - name: "captchaEnabled"
    type: "boolean"
    description: "Indicates if a Captcha is enabled on the form."

  - name: "campaignGuid"
    type: "string"
    description: "The GUID of the campaign the form is associated with."

  - name: "cloneable"
    type: "boolean"
    description: "Indicates if the form is cloneable."

  - name: "editable"
    type: "boolean"
    description: "Indicates if the form is editable."

  - name: "formType"
    type: "string"
    description: "The type of form. For example: `HUBSPOT`"

  - name: "metaData"
    type: "array"
    description: "Metadata about the form."
    array-attributes:
      - name: "name"
        type: "string"
        description: *deprecated-field

      - name: "value"
        type: "string"
        description: *deprecated-field
---