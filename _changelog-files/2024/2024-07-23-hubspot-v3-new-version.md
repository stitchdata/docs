---
title: "Hubspot integration: New version (v3)"
content-type: "changelog-entry"
date: 2024-07-23
entry-type: new-feature
entry-category: integration
connection-id: hubspot
connection-version: 3
pull-request: "https://github.com/singer-io/tap-hubspot/pull/256"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v3) of the Hubspot integration is now available!

Changes in this version include:

- Upgrading to V3 of the Hubspot API.
- Updating the primary key in the `owners` table from `ownerId` to `id`.
- Schema modifications to align with the Hubspot API.
- Updating of the Hubspot `owners` documentation link.

Full details can be found on the pull request against the open sourced integration [here](https://github.com/singer-io/tap-hubspot/pull/256).
