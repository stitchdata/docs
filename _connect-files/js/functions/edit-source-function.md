---
content-type: "stitch-js-function"
key: "source-editing-function"
order: 5


title: "Source Editing"
definition: "editSource(options)"
description: "{{ js.edit-source.description }}"


options:
  - name: "id"
    required: true
    description: "The unique identifier for the source."

  - name: "ephemeral_token"
    required: false
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    description: "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - title: ""
    description: "Editing the stream selection for a source."
    code: |
      Stitch.editSource({
          "id": 123,
          "default_streams": {
              "campaigns": false,
              "companies": true
          },
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Source updated, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Editing source failed.", error);
      });
---