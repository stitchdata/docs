---
title: Form Properties
content-type: "api-doc"
order: 8

# This parameter is used in _includes/connect/api-endpoint-rollup.html
# To display the correct description for a given form property
property-description: |
  {% assign integration = VARIABLE.display-name %}

  {% if VARIABLE.property-description %}
  {{ integration }} connections read data from {{ VARIABLE.property-description }} and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% else %}
  {% case VARIABLE.source-type %}
  {% when 'database' %}
  {% assign first-letter = integration | slice: 0 %}

  {% if first-letter == "A"
  or first-letter == "O"
  or first-letter == "I"
  or first-letter == "E"
  or first-letter == "U" %}
      {% assign article = "an" %}
  {% else %}
  {% assign article = "a" %}
  {% endif %}

  {{ article | capitalize }} {{ integration }} connection reads data from {{ article }} {{ integration }} database and corresponds to source `type: {{ VARIABLE.api-type }}`.

  {% when 'saas' %}
  {{ integration }} connections read data from the {{ integration }} API and correspond to source `type: {{ VARIABLE.api-type }}`.
  
  {% else %}
  {% assign destination = VARIABLE.display-name %}
  A {{ destination }} connection writes data to a {{ destination }} database and corresponds to destination `type: {{ VARIABLE.api-type }}`.
  {% endcase %}
  {% endif %}


sections:
  - content: |
      Stitch connects to a large, diverse universe of applications and data warehouses, each of which is configured differently.

      The `properties` objects contain the properties necessary to create a source or destination object.

      For sources, these properties can also be found in the source's report card `step: form`.

      {% include connect/api-endpoint-rollup.html type="form-property" %}

  - title: "Destination Form Properties"
    anchor: "destination-form-properties"
    content: |
      Destination form properties should be sent in the `connection` argument when using the [Create]({{ api.core-objects.destinations.create.anchor }}) or [Update a Destination]({{ api.core-objects.destinations.update.anchor }}) endpoints.

      {% include connect/api-endpoint-rollup.html type="form-property" subtype="destination" %}
    include: |
      {% include connect/api-form-properties.html content="destination" %}
      

  - title: "Source Form Properties"
    anchor: "source-form-properties"
    content: |
      Source form properties should be sent in the `properties` argument when using the [Create]({{ api.core-objects.sources.create.anchor }}) or [Update a Source]({{ api.core-objects.sources.update.anchor }}) endpoints.

      All properties should be sent as strings.

      {% include connect/api-endpoint-rollup.html type="form-property" subtype="source" %}
    include: |
      {% include connect/api-form-properties.html content="source" %}
---