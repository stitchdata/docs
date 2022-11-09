---
title: "Yotpo (v1) improvement: Handling response with 500 status code"
content-type: "changelog-entry"
date: 2022-06-01
entry-type: improvement
entry-category: integration
connection-id: yotpo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-yotpo/pull/31"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors by adding an excption for status code `500`, and an expection class of `500` for backoff.