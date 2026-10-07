---
title: "MongoDB (v3): PyMongo upgrade raises the minimum supported MongoDB version to 4.4"
content-type: "changelog-entry"
date: 2026-10-07
entry-type: deprecation
entry-category: integration
connection-id: mongodb
connection-version: 3
pull-request: "https://github.com/singer-io/tap-mongodb/pull/136"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've upgraded the `pymongo` version used by our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to 4.18.2.

PyMongo 4.18 no longer supports {{ this-connection.display_name }} versions below `4.4`. As a result, this integration now supports {{ this-connection.display_name }} `4.4` through `7.0`. Connections to databases running `3.6`, `4.0`, or `4.2` will fail. All three of these versions have reached end of life with MongoDB.
