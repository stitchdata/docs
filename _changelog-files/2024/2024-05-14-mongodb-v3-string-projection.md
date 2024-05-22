---
title: "MongoDB (v3) update: String projection"
content-type: "changelog-entry"
date: 2024-05-14
entry-type: improvement
entry-category: integration
connection-id: mongodb
connection-version: 3
pull-request: "https://github.com/singer-io/tap-mongodb/pull/94"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to allow the specification of a string projection, instead of using only integer values. 

For example, the following sample projection now works:

```
{"name": "$personName"}
```