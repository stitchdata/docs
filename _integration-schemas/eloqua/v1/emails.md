---
tap: "eloqua"
version: "1.0"

name: "emails"
key: "emails"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-1.0-assets-emails-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/emails.json"
description: |
  The `{{ table.name }}` table contains details about the emails sent from your {{ integration.display_name }} account.

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of emails"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The email ID."
    foreign-key-id: "email-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the email was last updated."

  - name: "accessedAt"
    type: "date-time"
    description: "The date and time the email was last accessed, expressed in Unix time."

  - name: "archive"
    type: "boolean"
    description: ""

  - name: "bounceBackEmail"
    type: "string"
    description: "The email address which is notified if the email is undeliverable."

  # - name: "contentSections"
  #   type: "array"
  #   description: "A list of associated Content Section assets."
  #   subattributes:

  - name: "createdAt"
    type: "date-time"
    description: "The date and time the email was created, expressed in Unix time."

  - name: "createdBy"
    type: "string"
    description: "The ID of the user who created the email."

  - name: "currentStatus"
    type: "string"
    description: "The asset's current status."

  - name: "depth"
    type: "string"
    description: &depth |
      Level of detail returned by the request. {{ integration.display_name }} APIs can retrieve entities at three different levels of depth: `minimal`, `partial`, and `complete`. Any other values passed are reset to `complete` by default. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/index.html#CSHID=RequestDepth){:target="new"} for more info.

  - name: "description"
    type: "string"
    description: "The description of the email."

  - name: "dynamicContents"
    type: "array"
    description: "A list of associated dynamic content."
    subattributes:
      - name: "createdAt"
        type: "date-time"
        description: "The date and time the dynamic content was created, expressed in Unix time."

      - name: "createdBy"
        type: "string"
        description: "The ID of the user who created the dynamic content."

      - name: "currentStatus"
        type: "string"
        description: "The dynamic content's current status."

      - name: "defaultContentSection"
        type: "string"
        description: ""

      - name: "depth"
        type: "string"
        description: *depth

      - name: "description"
        type: "string"
        description: "The description of the dynamic content."

      - name: "folderId"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: "The dynamic content ID."

      - name: "name"
        type: "string"
        description: "The name of the dynamic content."

      - name: "permissions"
        type: "string"
        description: "The permissions for the dynamic content granted to your current instance."

      - name: "rules"
        type: "string"
        description: "The dynamic content's rules."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the dynamic content was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the dynamic content."

  - name: "emailFooterId"
    type: "string"
    description: "The ID of the email footer."

  - name: "emailGroupId"
    type: "string"
    description: "The ID of the email group."

  - name: "emailHeaderId"
    type: "string"
    description: "The ID of the email header."

  - name: "encodingId"
    type: "string"
    description: "The ID of the encoding used."

  - name: "fieldMerges"
    type: "array"
    description: "A list of associated field merges."
    subattributes:
      - name: "accessedAt"
        type: "date-time"
        description: "The date and time the field merge was last accessed, expressed in Unix time."

      # - name: "accountFieldId"
      #   type: "string"
      #   description: "The ID of the associated account field."

      - name: "allowUrlsInValue"
        type: "string"
        description: ""

      - name: "contactFieldId"
        type: "string"
        description: "The ID of the associated contact field."

      - name: "createdAt"
        type: "date-time"
        description: "The date and time the field merge was created, expressed in Unix time."

      - name: "createdBy"
        type: "string"
        description: "The ID of the user who created the field merge."

      - name: "defaultValue"
        type: "string"
        description: "The default value of the field merge."

      - name: "depth"
        type: "string"
        description: *depth

      - name: "description"
        type: "string"
        description: "The description of the campaign."

      - name: "eventFieldId"
        type: "string"
        description: "The ID of the associated event field."

      - name: "eventId"
        type: "string"
        description: "The ID of the associated event."

      - name: "eventSessionFieldId"
        type: "string"
        description: "The ID of the associated event session field."

      # - name: "fieldConditions"
      #   type: "string"
      #   description: ""

      # - name: "folderId"
      #   type: "string"
      #   description: ""

      - name: "id"
        type: "string"
        description: "The ID of the field merge."

      - name: "mergeType"
        type: "string"
        description: |
          The type of the field merge. Possible values include: 

          - `contactField`
          - `accountField` 
          - `eventField`
          - `eventSessionField`
          - `customObjectField`

      - name: "name"
        type: "string"
        description: "The name of the field merge."

      - name: "permissions"
        type: "string"
        description: "The permissions for the field merge granted to your current instance."

      - name: "syntax"
        type: "string"
        description: "The syntax of the field merge."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the field merge was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the field merge."

  - name: "files"
    type: "array"
    description: "A list of imported files."
    subattributes:
      - name: "accessedAt"
        type: "date-time"
        description: "The date and time the imported file was last accessed, expressed in Unix time."

      - name: "createdAt"
        type: "date-time"
        description: "The date and time the imported file was created, expressed in Unix time."

      - name: "createdBy"
        type: "string"
        description: "The ID of the user who created the imported file."

      - name: "currentStatus"
        type: "string"
        description: "The imported file's current status."

      - name: "depth"
        type: "string"
        description: *depth

      - name: "description"
        type: "string"
        description: "The description of the imported file."

      - name: "fileName"
        type: "string"
        description: "The file name of the imported file."

      - name: "id"
        type: "string"
        description: "The imported file ID."

      - name: "link"
        type: "string"
        description: "The imported file's complete URL."

      - name: "name"
        type: "string"
        description: "The name of the imported file."

      - name: "permissions"
        type: "string"
        description: "The permissions for the imported file granted to your current instance."

      - name: "trackedLink"
        type: "string"
        description: "The imported file's tracked complete URL."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the imported file was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the imported file."

  # - name: "folderId"
  #   type: "string"
  #   description: ""

  - name: "forms"
    type: "array"
    description: "A list of associated Form assets."
    subattributes:
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
        description: |
          The form's current status. For example: `draft`, `active`, or `complete`.

      - name: "depth"
        type: "string"
        description: *depth

      - name: "description"
        type: "string"
        description: "The description of the form."

      - name: "elements"
        type: "array"
        description: "A list of form elements."
        subattributes:
          - name: "accessedAt"
            type: "date-time"
            description: "The date and time the form element was last accessed, expressed in Unix time."

          - name: "createdAt"
            type: "date-time"
            description: "The date and time the form element was created, expressed in Unix time."

          - name: "createdBy"
            type: "string"
            description: "The ID of the user who created the form element."

          - name: "currentStatus"
            type: "string"
            description: |
              The form element's current status. For example: `draft`, `active`, or `complete`.

          - name: "depth"
            type: "string"
            description: *depth

          - name: "description"
            type: "string"
            description: "The description of the form element."

          - name: "id"
            type: "string"
            description: "The form element ID."

          - name: "instructions"
            type: "string"
            description: "The form element's field instructions. Field instructions are optional instructions that help users fill in fields."

          - name: "name"
            type: "string"
            description: "The name of the form element."

          - name: "permissions"
            type: "string"
            description: "The permissions for the form element granted to your current instance."

          - name: "style"
            type: "string"
            description: "The asset's main layout style."

          - name: "type"
            type: "string"
            description: "The asset's type in {{ integration.display_name }}."

          - name: "updatedAt"
            type: "date-time"
            description: "The Unix timestamp for the date and time the form element was last updated."

          - name: "updatedBy"
            type: "string"
            description: "The ID of the user that last updated the form element."

      - name: "emailAddressFormField"
        type: "string"
        description: "The email address form field entity's unique identifier."

      - name: "html"
        type: "string"
        description: "The asset's raw HTML content."

      - name: "id"
        type: "string"
        description: "The form ID."
        foreign-key-id: "form-id"

      - name: "isHidden"
        type: "string"
        description: "Indicates whether the form is hidden or not."

      - name: "name"
        type: "string"
        description: "The name of the form."

      - name: "permissions"
        type: "string"
        description: "The permissions for the form granted to your current instance."

      - name: "processingSteps"
        type: "array"
        description: "A list of the form's processing steps."

      - name: "processingType"
        type: "string"
        description: |
          A list of the form's processing types. For example: `externalEmail`, `externalWebsite`, `internallyHosted`, `internalAgentProxyForm`.

      - name: "style"
        type: "string"
        description: "The asset's main layout style."

      - name: "submitFailedLandingPageId"
        type: "string"
        description: "The landing page ID of the failed submit."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the form was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the form."

  - name: "htmlContent"
    type: "object"
    description: "Details about the HTML content in the email."
    subattributes:
      - name: "contentSource"
        type: "string"
        description: ""

      - name: "cssHeader"
        type: "string"
        description: ""

      - name: "docType"
        type: "string"
        description: ""

      - name: "documentDescription"
        type: "string"
        description: ""

      - name: "html"
        type: "string"
        description: ""

      - name: "htmlBody"
        type: "string"
        description: ""

      - name: "metaTags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "root"
        type: "string"
        description: ""

      - name: "systemHeader"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "hyperlinks"
    type: "array"
    description: "A list of hyperlinks contained within the email."
    subattributes:
      - name: "createdAt"
        type: "date-time"
        description: "The date and time the hyperlink was created, expressed in Unix time."

      - name: "createdBy"
        type: "string"
        description: "The ID of the user who created the hyperlink."

      - name: "depth"
        type: "string"
        description: *depth

      - name: "folderId"
        type: "string"
        description: "The ID of the folder containing the hyperlink asset."

      - name: "href"
        type: "string"
        description: "The href value of the hyperlink."

      - name: "hyperlinkType"
        type: "string"
        description: |
          The type of hyperlink. Possible values include:

          - `ExternalURL`
          - `ICSCalendarURL`
          - `LandingPageURL`
          - `ReferrerURL`
          - `RSSURL`
          - `TrackedExternalURL`

      - name: "id"
        type: "string"
        description: "The hyperlink ID."

      - name: "name"
        type: "string"
        description: "The name of the hyperlink."

      - name: "referencedEntityId"
        type: "string"
        description: "The ID of the referenced entity."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the hyperlink was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the hyperlink."

  - name: "images"
    type: "array"
    description: "A list of associated Image assets."
    subattributes:
      - name: "createdAt"
        type: "date-time"
        description: "The date and time the image was created, expressed in Unix time."

      - name: "createdBy"
        type: "string"
        description: "The ID of the user who created the image."

      - name: "currentStatus"
        type: "string"
        description: "The image's current status."

      - name: "depth"
        type: "string"
        description: *depth

      - name: "folderId"
        type: "string"
        description: "The ID of the folder containing the image."

      - name: "fullImageUrl"
        type: "string"
        description: "The image's complete URL."

      - name: "id"
        type: "string"
        description: "The image ID."

      - name: "name"
        type: "string"
        description: "The name of the image."

      - name: "permissions"
        type: "string"
        description: "The permissions for the image granted to your current instance."

      - name: "size"
        type: "string"
        description: ""

      - name: "syncDate"
        type: "date-time"
        description: ""

      - name: "thumbnailUrl"
        type: "string"
        description: "The image's thumbnail URL."

      - name: "type"
        type: "string"
        description: "The asset's type in {{ integration.display_name }}."

      - name: "updatedAt"
        type: "date-time"
        description: "The Unix timestamp for the date and time the image was last updated."

      - name: "updatedBy"
        type: "string"
        description: "The ID of the user that last updated the image."

  - name: "isContentProtected"
    type: "boolean"
    description: "Indicates whether the asset's content is protected."

  - name: "isPlainTextEditable"
    type: "string"
    description: "Indicates whether the asset's text is editable."

  - name: "isPrivate"
    type: "boolean"
    description: ""

  - name: "isTracked"
    type: "string"
    description: "Indicates whether {{ integration.display_name }} will track the asset."

  - name: "landingPages"
    type: "array"
    description: "A list of associated landing page assets."
    # subattributes:
    #   - name: "accessedAt"
    #     type: "date-time"
    #     description: "The date and time the landing page was last accessed, expressed in Unix time."

    #   - name: "createdAt"
    #     type: "date-time"
    #     description: "The date and time the landing page was created, expressed in Unix time."

    #   - name: "createdBy"
    #     type: "string"
    #     description: "The ID of the user who created the landing page."

    #   - name: ""
    #     type: 
    #     description: ""

  - name: "layout"
    type: "string"
    description: "The email's main layout."

  - name: "name"
    type: "string"
    description: "The name of the email."

  - name: "permissions"
    type: "string"
    description: "The permissions for the email granted to your current instance."

  - name: "plainText"
    type: "string"
    description: "The email's content in plain text."

  - name: "renderMode"
    type: "string"
    description: ""

  - name: "replyToEmail"
    type: "string"
    description: "The email address targeted when recipients click 'reply'."

  - name: "replyToName"
    type: "string"
    description: "The sender name recipients of the email will see."

  - name: "sendPlainTextOnly"
    type: "string"
    description: "Indicates whether the sent email is plain text only."

  - name: "senderEmail"
    type: "string"
    description: "The address the email will appear to be sent from."

  - name: "senderName"
    type: "string"
    description: "The sender name recipients of the email will see."

  - name: "sourceTemplateId"
    type: "string"
    description: "The ID of the template used to create the asset."

  - name: "style"
    type: "string"
    description: "The email's main layout style."

  - name: "subject"
    type: "string"
    description: "The email's subject line text."

  - name: "type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."

  - name: "updatedBy"
    type: "string"
    description: "The ID of the user that last updated the email."

  - name: "virtualMTAId"
    type: "string"
    description: ""
---