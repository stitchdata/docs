---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
# version: "1.0"

name: "content_areas"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/contentarea.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/content_areas.py
description: |
  The `{{ table.name }}` table contains info about the reusable content sections in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve content areas"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/contentarea.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The content area ID."
    foreign-key-id: "content-area-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the content area was last modified."

  - name: "BackgroundColor"
    type: "string"
    description: "The background color of the content area."

  - name: "BorderColor"
    type: "string"
    description: "The color of the border surrounding the content area."

  - name: "BorderWidth"
    type: "integer"
    description: "The pixel width of the border surrounding the content area."

  - name: "CategoryID"
    type: "integer"
    description: "The ID of the folder associated with the content area."
    # foreign-key-id: "folder-id"

  - name: "Cellpadding"
    type: "integer"
    description: "The pixel value of the padding around the content area."

  - name: "Cellspacing"
    type: "integer"
    description: "The pixel value of the spacing for the content area."

  - name: "Content"
    type: "string"
    description: "The content contained in a the content area."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the content area was created."

  - name: "CustomerKey"
    type: "string"
    description: "User-supplied unique identifier for an object within an object type (corresponds to the external key assigned to an object in the user interface."

  - name: "FontFamily"
    type: "string"
    description: "The font family used in the content area."

  - name: "HasFontSize"
    type: "boolean"
    description: "Indicates whether the content area includes a specified font size or not."

  - name: "IsBlank"
    type: "boolean"
    description: "Indicates if the content area contains no content."

  - name: "IsDynamicContent"
    type: "boolean"
    description: "Indicates if the content area contains dynamic content."

  - name: "IsLocked"
    type: "boolean"
    description: "Indicates if specific email the content area within an Enterprise or Enterprise 2.0 account is locked and cannot be changed by subaccounts."

  - name: "IsSurvey"
    type: "boolean"
    description: "Indicates whether a specific the content area contains survey questions."

  - name: "Key"
    type: "string"
    description: "Specifies key associated with the content area in HTML body. Relates to the `email` object via a custom type."

  - name: "Name"
    type: "string"
    description: "The name of the object or property."

  - name: "ObjectID"
    type: "string"
    description: "The content area's object ID."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "Width"
    type: "integer"
    description: "The pixel width of the content area."
---
