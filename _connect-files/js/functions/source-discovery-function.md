---
content-type: "stitch-js-function"
key: "source-discovery-function"
order: 3


title: "Source Discovery"
definition: "displayDiscoveryOutputForSource(options)"
description: "Checks the source's connection and discovers its schema."


options:
  - name: "id"
    required: true
    description: "The unique identifier for the source."

  - name: "discovery_job_name"
    required: true
    description: "The discovery job that should be displayed."

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
      Stitch.displayDiscoveryOutputForSource({
        id: 123,
        discovery_job_name: "987-123-4567891234-checks"
      }).then((result) => {
        console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
        console.log("Integration not created.", error);
      });
---