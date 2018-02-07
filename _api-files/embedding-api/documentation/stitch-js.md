---
title: Stitch.js
content-type: "embed-doc"
order: 9

include: api/js-function.html

sections:
  - content: |
      For many Stitch data sources and destinations, the user must directly grant access to Stitch. For example: Granting access via an OAuth handshake between Stitch and an API. Stitch.js makes it easy to embed secure workflows for source and destination creation and management into your web application.

      Stitch sources require a unique sequence of [connection steps]({{ page.anchors.data-structures.connection-steps }}) specific to the source type. When a user is sent to a particular step using Stitch.js, the user will also be prompted to complete any successive steps to complete configuration of the source.

      Stitch.js supports the functions listed below. All of the functions expect an `options` object as the only argument and return a `Promise`.
---