---
type: "connect"
content-type: "stitch-js-function"
key: "source-editing-function"
order: 5


title: "Source Editing"
definition: "editSource(options)"
description: "{{ js.edit-source.description }}"


options:
  - name: "id"
    required: true
    type: "integer"
    description: "The unique identifier for the source. For example: `12345`"

  - name: "ephemeral_token"
    required: false
    type: "string"
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    type: "object"
    description: "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - type: "Function"
    language: "javascript"
    description: "The code below will send the user to Stitch and open the Integration Settings page for source `45612`, where the source's settings can be updated."
    code: |
      Stitch.editSource({
          "id": 45612,
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Source updated, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Editing source failed.", error);
      });

  - type: "Result"
    description: "Stitch.js will display the Integration Settings page for the source, where the user can update the source's configuration settings."
    image: "connect/js-edit-source-function-result.png"
    image-caption: "The Integration Settings page in Stitch."
---