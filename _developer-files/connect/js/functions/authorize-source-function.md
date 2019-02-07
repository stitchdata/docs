---
product-type: "connect"
content-type: "stitch-js-function"
key: "source-authorization-function"
order: 2


title: "Source Authorization"
definition: "authorizeSource(options)"
description: "{{ js.authorize-a-source.description }}"


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
    description: "The code below will first send the user to Stitch and then re-direct to the appropriate third-party to complete an OAuth handshake."
    code: |
      Stitch.authorizeSource({
          "id": 45612,
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });

  - type: "Result"
    description: |
      Stitch.js will send the user to Stitch and then re-direct to the appropriate third-party to complete an OAuth handshake.

      In this example, the source being authorized is HubSpot (`type: platform.hubspot`).
    image: "connect/js-authorize-source-function-result.png"
    image-caption: "Authorization page in HubSpot application"
---