---
tap: "marketo"
version: "2.0"

name: "programs"
doc-link: http://developers.marketo.com/rest-api/assets/programs/
singer-schema: https://github.com/singer-io/tap-marketo/blob/master/tap_marketo/schemas/programs.json
description: |
  The `programs` table contains info about your Marketo programs. Programs can be parents to most types of assets in Marketo and allow you to track membership and success of leads.

replication-method: "Incremental"
api-method:
  name: "getPrograms"
  doc-link: 

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the program."

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the asset was most recently updated."

  - name: "createdAt"
    type: "date-time"
    description: "The time the asset was created."

  - name: "description"
    type: "string"
    description: "The description of the asset."

  - name: "name"
    type: "string"
    description: "The name of the asset."

  - name: "url"
    type: "string"
    description: "The URL of the asset in the Marketo UI."

  - name: "type"
    type: "string"
    description: |
      The type of program. Possible values include:

      - `program`
      - `event`
      - `webinar`
      - `nurture`

  - name: "channel"
    type: "string"
    description: "The channel of the program."

  - name: "status"
    type: "string"
    description: |
      The status of the program. Only applicable to email and engagement programs. Possible values include:

      - `locked`
      - `unlocked`
      - `on`
      - `off`

  - name: "workspace"
    type: "string"
    description: "The name of the workspace."

  - name: "folder"
    type: "object"
    description: "Details about the asset's parent folder."
    object-attributes:
      - name: "type"
        type: "string"
        description: "The type of the parent folder. Possible values are `Folder` or `Program`."

      - name: "value"
        type: "integer"
        description: "The ID of the parent folder."

      - name: "folderName"
        type: "string"
        description: "The name of the parent folder."
---