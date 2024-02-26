---
title: "MongoDB (v3) update: MongoDB server not supporting sessions"
content-type: "changelog-entry"
date: 2024-02-14
entry-type: improvement
entry-category: integration
connection-id: mongodb
connection-version: 3
pull-request: "https://github.com/singer-io/tap-mongodb/pull/112"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to handle the MongoDB server when its not supporting sessions. It will now revert to the prior behavior without using a session and without sending a keepalive message.