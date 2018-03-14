---
title: Introduction
content-type: "js-doc"
order: 1

sections:
  - content: |
      For many Stitch data sources and destinations, the user must directly grant access to Stitch. For example: Granting access via an OAuth handshake between Stitch and an API. Stitch.js makes it easy to embed secure workflows for source and destination creation and management into your web application.

      Stitch sources require a unique sequence of [connection steps]({{ api.section | flatify | prepend: site.baseurl | append: api.data-structures.connection-steps.section }}) specific to the source `type`. When a user is sent to a particular step using Stitch.js, the user will also be prompted to complete any successive steps to complete configuration of the source.
---

