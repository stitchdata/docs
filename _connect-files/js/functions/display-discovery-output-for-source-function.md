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
    type: "integer"
    description: "The unique identifier for the source. For example: `12345`"

  - name: "discovery_job_name"
    required: true
    type: "string"
    description: |
      When a source is updated, Stitch will run a [connection check]({{ api.section | prepend: site.baseurl | append: api.data-structures.connection-checks.section | flatify }}) to test the source's connection parameters and discover its schema. This value is the name of the job that should be displayed.

      To initiate a connection check, use the [Update a Source]({{ api.section | prepend: site.baseurl | append: api.core-objects.sources.update.anchor | flatify }}) endpoint. The `check_job_name` attribute in the response will contain a discovery job name.

  - name: "ephemeral_token"
    required: false
    type: "string"
    description: "{{ connect.common.attributes.ephemeral-token-js | flatify }}"

  - name: "default_streams"
    required: false
    type: "object"
    description: "{{ connect.common.attributes.default-streams | flatify }}"


examples:
  - type: "function"
    language: "javascript"
    description: "The code below will run a connection check, discover the schema for source `45612`, and output the results."
    code: |
      Stitch.displayDiscoveryOutputForSource({
          "id": 45612,
          "discovery_job_name": "1234-45612-4567891234-checks"
      }).then((result) => {
          console.log(`Integration created, type=${result.type}, id=${result.id}`);
      }).catch((error) => {
          console.log("Integration not created.", error);
      });

  - type: "result"
    description: "Stitch.js will run a connection check and output the source's schema. The example below is for source `platform.hubspot`."
    image: "connect/js-source-discovery-function-result.gif"
    image-caption: "Stitch running a connection check and displaying the schema discovery result."
---