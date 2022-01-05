---
title: "Heap (v1) bug fix: Handle non-union types in Avro schema"
content-type: "changelog-entry"
date: 2021-09-08
entry-type: bug-fix
entry-category: integration
connection-id: heap
connection-version: 1
pull-request: "https://github.com/singer-io/tap-heap/pull/18"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Avro can have a non-union type for a `type`. This can manifest as a single string type rather than a list. This resulted in an error. 

We added error handling that moves replication forward in the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration when faced with non-union types.