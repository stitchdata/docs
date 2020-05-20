---
title: Connection properties
product-type: "connect"
content-type: "api-doc"
order: 8

# This parameter is used in _includes/connect/api-endpoint-rollup.html
# To display the correct description for a given form property
property-description: |
  {% assign connection-name = VARIABLE.display-name %}

  {% case VARIABLE.form-type %}

  {% when "source" %}
  {% if VARIABLE.property-description %}
  {{ connection-name }} connections read data from {{ VARIABLE.property-description | flatify }} and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% else %}

  {% case VARIABLE.source-type %}
  {% when 'database' %}

  {{ connection-name }} connections read data from {{ connection-name }} databases and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% when 'saas' %}
  {{ connection-name }} connections read data from the {{ connection-name }} API and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% when 'import-api' %}
  {{ connection-name }} connections receive data you push to the Import API and correspond to source `type: {{ VARIABLE.api-type }}`.
  
  {% endcase %}
  {% endif %}

  {% when "destination" %}
  {% if VARIABLE.property-description %}
  {{ connection-name }} connections write data to {{ VARIABLE.property-description | flatify }} and correspond to destination `type: {{ VARIABLE.api-type }}`.

  {% else %}

  {{ connection-name }} connections write data to a {{ connection-name }} database and correspond to destination `type: {{ VARIABLE.api-type }}`.

  {% endif %}
  {% endcase %}

sections:
  - content: |
      Stitch connects to a large, diverse universe of applications and data warehouses, each of which is configured differently.

      The `properties` objects contain the properties necessary to create a source or destination object.

      These properties can also be found in the `form` step of the source or destination's report card. If the source or destination also supports OAuth authentication, the properties required for OAuth can be found in the `oauth` step of the report card. Refer to the [Performing OAuth with Stitch Connect guide]({{ link.connect.guides.configure-connection-oauth | prepend: site.baseurl }}) for more info about OAuth configuration for connections.

  - title: "Destination connection properties"
    anchor: "destination-form-properties"
    content: |
      Destination connection properties should be sent in the `properties` argument when using the [Create]({{ api.core-objects.destinations.create.anchor }}) or [Update a Destination]({{ api.core-objects.destinations.update.anchor }}) endpoints.

      {% include developers/api-endpoint-rollup.html type="form-property" subtype="destination" %}
    include: |
      {% include developers/api-form-properties.html content="destination" %}
      
  - title: "Source connection properties"
    anchor: "source-form-properties"
    content: |
      Source connection properties should be sent in the `properties` argument when using the [Create]({{ api.core-objects.sources.create.anchor }}) or [Update a Source]({{ api.core-objects.sources.update.anchor }}) endpoints.
    include: |
      {% include developers/api-form-properties.html content="source" %}
---