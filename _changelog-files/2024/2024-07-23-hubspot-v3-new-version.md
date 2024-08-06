---
title: "Hubspot integration: New version (v3) now available!"
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

- Upgrading `owners` API endpoint from v2 to v3.
- Updating the primary key in the `owners` table from `ownerId` to `id`.
- Schema modifications to align with the Hubspot API.

Full details can be found on the pull request against the open sourced integration [here](https://github.com/singer-io/tap-hubspot/pull/256).
