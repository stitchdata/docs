---
content-type: "stitch-js-function"
key: "source-creation-function"
order: 1


title: "Source Creation"
definition: "addSource(options)"
description: "Initiates the creation of a source in the user's Stitch client account."


options:
  - name: "type"
    required: true
    description: "The source type. For example: `platform.hubspot` or `platform.marketo`."

  - name: "ephemeral_token"
    required: false
    description: "The token used to automatically log the user into the Stitch client account. Retrieved by creating a session using the [Create a Session endpoint](#create-a-session)."
  - name: "default_streams"
    required: false
    description: |
      Sets the default selections for the data structures (tables) to be replicated during the source integration setup. Should be an object of the form `{"table_name": true}`.

      Only top-level tables can be provided - nesting is not currently supported.

      **Note**: If a table name is provided that isn't provided by the source integration, it is ignored. Values other than `true` are also ignored.


examples:
  - title: "HubSpot stream selection"
    description: "Selecting the `campaigns` and `companies` streams for a HubSpot source."
    code: |
      Stitch.addSource({
        type: "platform.hubspot",
        default_streams: {"campaigns": true, "companies": true},
        ephemeral_token: "<EPHEMERAL_TOKEN>"
      }).then((result) => {
        console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
        console.log("Integration not created.", error);
      });
---