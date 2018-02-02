---
content-type: "stitch-js-function"
key: "source-authorization-function"
order: 2


title: "Source Authorization"
definition: "authorizeSource(options)"
description: "Sends the user to Stitch, which will redirect to the third-party to complete an OAuth handshake."


options:
  - name: "id"
    required: true
    description: "The unique identifier for the source."

  - name: "ephemeral_token"
    required: false
    description: "The token used to automatically log the user into the Stitch client account. Retrieved by creating a session using the [Create Session endpoint](#create-a-session)."

  - name: "default_streams"
    required: false
    description: |
      Sets the default selections for the data structures (tables) to be replicated during the source integration setup. Should be an object of the form `{"table_name": true}`.

      Only top-level tables can be provided - nesting is not currently supported.

      **Note**: If a table name is provided that isn't provided by the source integration, it is ignored. Values other than `true` are also ignored.


examples:
  - title: ""
    description: "Selecting the `campaigns` and `companies` streams for a HubSpot source."
    code: |
      Stitch.authorizeSource({
        id: 123
      }).then((result) => {
        console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
        console.log("Integration not created.", error);
      });
---