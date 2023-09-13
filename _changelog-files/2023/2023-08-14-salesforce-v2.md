---
title: "Salesforce integration: New version (v2) now available!"
content-type: "changelog-entry"
date: 2023-08-14
entry-type: new-feature
entry-category: integration
connection-id: salesforce
connection-version: 2
pull-request: "https://github.com/singer-io/tap-salesforce/pull/163"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available!

We've updated the `LightningUriEvent` stream to use the `EventIdentifier` field as the Primary Key.