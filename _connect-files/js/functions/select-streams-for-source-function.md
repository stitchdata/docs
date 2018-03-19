---
content-type: "stitch-js-function"
key: "source-stream-selection-function"
order: 4


title: "Source Stream Selection"
definition: "selectStreamsForSource(options)"
description: "{{ js.select-streams.description }}"


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
    description: |
      {{ connect.common.attributes.default-streams | flatify }}


examples:
  - type: "function"
    language: "javascript"
    description: "The code below will prompt the user to select the streams (tables) they want to replicate for source `45612`."
    code: |
      Stitch.selectStreamsForSource({
          "id": 45612,
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });

  - type: "result"
    description: "Stitch.js will display the streams available for replication. The example below lists the streams for source `platform.hubspot`."
    image: "connect/js-source-stream-selection-function-result.png"
    image-caption: "The streams (tables) available for replication in Stitch."
---