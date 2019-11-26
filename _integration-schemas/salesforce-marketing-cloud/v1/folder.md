---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1.0"

name: "folder"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/datafolder.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/folders.py
description: |
  The `{{ table.name }}` table contains info about the folders in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve folders"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/datafolder.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The folder ID."
    foreign-key-id: "folder-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the folder was last modified."

  - name: "AllowChildren"
    type: "boolean"
    description: "Specifies whether a data folder can have child data folders."

  - name: "ContentType"
    type: "string"
    description: "Defines the type of content contained within a folder."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the folder was created."

  - name: "CustomerKey"
    type: "string"
    description: "User-supplied unique identifier for an object within an object type (corresponds to the external key assigned to an object in the user interface."

  - name: "Description"
    type: "string"
    description: "A description of the folder."

  - name: "Name"
    type: "string"
    description: "Name of the object or property."

  - name: "ObjectID"
    type: "string"
    description: "The folder's object ID."

  - name: "ParentFolder"
    type: "integer"
    description: "Specifies the parent folder for a data folder."
    foreign-key-id: "folder-id"

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""
  
  - name: "Type"
    type: "string"
    description: |
      Indicates type of specific list. Possible values are:

      - `Public`
      - `Private`
      - `Salesforce`
      - `GlobalUnsubscribe`
      - `Master`
---