---
title: Introduction
product-type: "connect"
content-type: "js-doc"
order: 1

sections:
  - content: |
      The Stitch {{ js.name }} is a library for integrating Stitch's data source creation and configuration workflows seamlessly into your web application. Using a pop-up window, end-users can:

        - Create a source of a particular type, such as Marketo or Salesforce
        - Authorize an existing source
        - Run a connection check for an existing source and discover its schema
        - Select streams (tables) to replicate for an existing source
        - Edit an existing source

  - title: "Data sources and connection steps"
    anchor: "data-sources-connection-steps"
    content: |
      Stitch data sources require a unique sequence of [connection steps]({{ api.section | flatify | prepend: site.baseurl | append: api.data-structures.connection-steps.section }}) specific to the source `type` to be fully configured. 

      When a user is sent to a particular step using the JavaScript client, the user will also be prompted to complete any successive steps to complete configuration of the source.

      For example: When the `addSource` function is used, the user will be prompted to first add the data source. The user will next be directed to authorize the source and select the streams they want to replicate.
---