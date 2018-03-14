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
    description: "The unique identifier for the source."

  - name: "ephemeral_token"
    required: false
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    description: |
      "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - title: ""
    description: "Selecting streams for a source."
    code: |
      Stitch.selectStreamsForSource({
          "id": 123,
          "default_streams": {
              "campaigns": true,
              "companies": true
          },
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });
---