---
title: Form Properties
content-type: "api-doc"
order: 8

sections:
  - content: |
      Stitch connects to a large, diverse universe of applications and data warehouses, each of which is configured differently.

      The `properties` objects contain the properties necessary to create a source or destination object. These properties can also be found in the destination and source's report card `step: form`.

      All properties should be sent as strings.

      {% include connect/api-endpoint-rollup.html type="form-property" %}

  - title: "Destination Form Properties"
    anchor: "destination-form-properties"
    content: |
      Destination form properties should be sent in the `connection` argument when using the [Create a Destination endpoint]({{ api.core-objects.destinations.create.anchor }}). 

      All properties should be sent as strings.

      {% include connect/api-endpoint-rollup.html type="form-property" subtype="destination" %}
    include: |
      {% include connect/api-form-properties.html content="destination" %}
      

  - title: "Source Form Properties"
    anchor: "source-form-properties"
    content: |
      Source form properties should be sent in the `properties` argument when using the [Create a Source endpoint]({{ api.core-objects.sources.create.anchor }}).

      All properties should be sent as strings.

      {% include connect/api-endpoint-rollup.html type="form-property" subtype="source" %}
    include: |
      {% include connect/api-form-properties.html content="source" %}
---