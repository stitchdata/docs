---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1.0"

name: "list"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/list.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/lists.py
description: |
  The `{{ table.name }}` table contains info about the lists in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve lists"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/retrieve.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the list was last modified."

  - name: "Category"
    type: "integer"
    description: "The ID of the folder that an item is located in."
    foreign-key-id: "folder-id"
    
  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the list was created."

  - name: "ObjectID"
    type: "string" 
    description: "The list's object ID."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "ListClassification"
    type: "string"
    description: "Specifies the classification for a list."

  - name: "ListName"
    type: "string"
    description: "The name of a specific list."

  - name: "Description"
    type: "string"
    description: "A description of the list."

  - name: "SendClassification"
    type: "string"
    description: "Indicates the send classification to use as part of a send definition."

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