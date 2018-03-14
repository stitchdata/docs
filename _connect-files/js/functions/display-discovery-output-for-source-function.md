---
content-type: "stitch-js-function"
key: "source-discovery-function"
order: 3


title: "Source Discovery"
definition: "displayDiscoveryOutputForSource(options)"
description: "{{ js.source-discovery.description }}"


options:
  - name: "id"
    required: true
    description: "The unique identifier for the source."

  - name: "discovery_job_name"
    required: true
    description: "The discovery job that should be displayed."

  - name: "ephemeral_token"
    required: false
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    description: "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - title: ""
    description: "Discovering schemas for a source."
    code: |
      Stitch.displayDiscoveryOutputForSource({
          "id": 123,
          "discovery_job_name": "987-123-4567891234-checks"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });
---