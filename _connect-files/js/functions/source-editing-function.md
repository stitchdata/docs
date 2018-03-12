---
content-type: "stitch-js-function"
key: "source-editing-function"
order: 5


title: "Source Editing"
definition: "editSource(options)"
description: "Edits the source form and settings."


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
      Stitch.editSource({
        id: 123
      }).then((result) => {
        console.log(`Source updated, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
        console.log("Editing source failed.", error);
      });
---