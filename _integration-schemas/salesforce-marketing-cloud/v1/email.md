---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
# version: "1.0"

name: "email"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/email.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/emails.py
description: |
  The `{{ table.name }}` table contains info about the emails in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve emails"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/email.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The email ID."
    foreign-key-id: "email-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the email was last modified."

  - name: "CategoryID"
    type: "integer"
    description: "The ID of the folder containing the email."
    foreign-key-id: "folder-id"

  - name: "CharacterSet"
    type: "string"
    description: "Indicates encoding used in an email message."

  - name: "ClonedFromID"
    type: "integer"
    description: "THe ID of email message from which the specified email message was created."
    foreign-key-id: "email-id"

  - name: "ContentAreaIDs"
    type: "array"
    description: "The IDs of the content areas contained in the email message."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The content area ID."
        foreign-key-id: "content-area-id"

  - name: "ContentCheckStatus"
    type: "string"
    description: "Indicates whether content validation has completed for this email message."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the email was created."

  - name: "CustomerKey"
    type: "string"
    description: "User-supplied unique identifier for an object within an object type (corresponds to the external key assigned to an object in the user interface."
  
  - name: "EmailType"
    type: "string"
    description: "Defines preferred email type."

  - name: "HasDynamicSubjectLine"
    type: "boolean"
    description: "Indicates whether email message contains a dynamic subject line."

  - name: "HTMLBody"
    type: "string"
    description: "THe HTML body of an email message."

  - name: "IsActive"
    type: "boolean"
    description: "Indicates whether the object is active."

  - name: "IsHTMLPaste"
    type: "boolean"
    description: "Indicates whether email message was created via pasted HTML."

  - name: "Name"
    type: "string"
    description: "The name of the object or property."

  - name: "ObjectID"
    type: "string"
    description: "The email's object ID."

  # - name: "PartnerProperties"
  #   type: ""
  #   description: ""

  - name: "PreHeader"
    type: "string"
    description: "The text used in preheader of email message on mobile devices."

  - name: "Status"
    type: "string"
    description: "Defines status of object. Status of an address."

  - name: "Subject"
    type: "string"
    description: "The subject area information for a message."

  - name: "SyncTextWithHTML"
    type: "boolean"
    description: "Makes the text version of an email contain the same content as the HTML version."

  - name: "TextBody"
    type: "string"
    description: "Contains raw text body of a message."
---