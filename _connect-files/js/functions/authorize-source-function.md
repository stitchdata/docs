---
content-type: "stitch-js-function"
key: "source-authorization-function"
order: 2


title: "Source Authorization"
definition: "authorizeSource(options)"
description: "{{ js.authorize-a-source.description }}"


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
  - title: "Authorize source"
    description: "Authorizing a source."
    code: |
      Stitch.authorizeSource({
          "id": 123,
          "ephemeral_token": "<EPHEMERAL_TOKEN>"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });
---