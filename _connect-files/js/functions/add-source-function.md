---
content-type: "stitch-js-function"
key: "source-creation-function"
order: 1


title: "Source Creation"
definition: "addSource(options)"
description: "{{ js.create-a-source.description }}"


options:
  - name: "type"
    required: true
    description: "{{ connect.common.attributes.type }}"

  - name: "ephemeral_token"
    required: false
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    description: "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - title: "HubSpot stream selection"
    description: "Select the `campaigns` and `companies` streams for a HubSpot source."
    code: |
      Stitch.addSource({
          "type": "platform.hubspot",
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