---
content-type: "stitch-js-function"
key: "source-stream-selection-function"
order: 4


title: "Source Stream Selection"
definition: "selectStreamsForSource(options)"
description: "Selects the tables and fields that should be replicated from the source."


options:
  - name: "id"
    required: true
    description: "The unique identifier for the source."

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
  - title: ""
    description: ""
    code: |
      Stitch.selectStreamsForSource({
        id: 123
      }).then((result) => {
        console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
        console.log("Integration not created.", error);
      });
---