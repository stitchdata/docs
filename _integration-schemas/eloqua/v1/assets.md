---
tap: "eloqua"
version: "1"

name: "assets"
key: "assets"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-assets-externals-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/assets.json"
description: |
  The `{{ table.name }}` table contains info about the external assets associated with your {{ integration.display_name }} account. External assets are non-{{ integration.display_name }}, or offline, activities performed by your contacts or prospects.

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of external assets"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the external asset."
    foreign-key-id: "asset-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the external asset was last updated."

  - name: "accessedAt"
    type: "date-time"
    description: "The date and time the external asset was last accessed, expressed in Unix time."

  - name: "createdAt"
    type: "date-time"
    description: "The date and time the external asset was created, expressed in Unix time."

  - name: "createdBy"
    type: "string"
    description: "The login ID of the user who created the external asset."

  - name: "currentStatus"
    type: "string"
    description: "The external asset's current status."

  - name: "depth"
    type: "string"
    description: |
      Level of detail returned by the request. {{ integration.display_name }} APIs can retrieve entities at three different levels of depth: `minimal`, `partial`, and `complete`. Any other values passed are reset to `complete` by default. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/index.html#CSHID=RequestDepth){:target="new"} for more info.

  - name: "description"
    type: "string"
    description: "The description of the external asset."

  - name: "externalAssetTypeId"
    type: "string"
    description: "The ID of the external asset type."

  - name: "folderId"
    type: "string"
    description: "The ID of the folder that contains the external asset."

  - name: "name"
    type: "string"
    description: "The name of the external asset."

  - name: "permissions"
    type: "array"
    description: "The permissions for the external asset granted to your current instance."
    subattributes:
      - name: "value"
        type: "string"
        description: "The permission for the external asset."

  - name: "scheduledFor"
    type: "string"
    description: "The date the external asset is scheduled."

  - name: "sourceTemplateId"
    type: "string"
    description: "The ID of the template used to create the external asset."

  - name: "type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."

  - name: "updatedBy"
    type: "string"
    description: "The ID of the user that last updated the external asset."
---