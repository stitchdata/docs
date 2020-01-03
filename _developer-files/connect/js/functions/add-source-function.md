---
product-type: "connect"
content-type: "stitch-js-function"
key: "source-creation-function"
order: 1


title: "Source Creation"
definition: "addSource(options)"
description: "{{ js.create-a-source.description }}"


options:
  - name: "type"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.type }}"

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
    description: "The code below will create a HubSpot integration (`type: platform.hubspot`) in the user's Stitch account, with the `campaigns` and `companies` tables pre-selected for replication."
    code: |
      Stitch.addSource({
          "type": "platform.hubspot",
          "ephemeral_token": "<EPHEMERAL_TOKEN>",
          "default_streams":{
             "campaigns": true,
             "companies": true
          }
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });

  - type: "Result"
    description: |
      Stitch.js will send the user to Stitch and open the Integration Settings page, where the user can configure the integration.
    image: "connect/js-create-a-source-result.png"
    image-caption: "HubSpot Integration Settings page in Stitch"
---