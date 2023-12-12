---
title: "HubSpot (v2): Custom objects support"
content-type: "changelog-entry"
date: 2023-12-12
entry-type: new-feature
entry-category: integration
connection-id: hubspot
connection-version: 2
pull-request: "https://github.com/singer-io/tap-hubspot/pull/242"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add support for custom objects. You will now be able to replicate a table for each custom object in our {{ this-connection.display_name }} account. 

The custom object tables support both standard and custom properties, and also support associations with `emails`, `meetings`, `notes`, `tasks`, `calls`, `conversations`, `contacts`, `companies`, `deals`, and `tickets`.

If you already have a {{ this-connection.display_name }} connection, you will need to re-authorize it to be able to select the new tables.