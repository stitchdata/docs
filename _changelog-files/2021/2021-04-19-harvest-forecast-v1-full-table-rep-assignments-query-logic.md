---
title: "Harvest Forecast (v1) improvement: Corrected replication for Full Table and assignments"
content-type: "changelog-entry"
date: 2021-04-19
entry-type: improvement
entry-category: integration
connection-id: harvest-forecast
connection-version: 1
pull-request: "https://github.com/singer-io/tap-harvest-forecast/pull/17"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This fix addresses a few issues:

- **Replication for `assignments`**: This table now replicates using Full Table Replication. Previously, Stitch would encounter errors from Harvest's API when attempting to replicate data incrementally. We've determined this was caused by a change in Harvest's API, so we changed this table's Replication Method to accommodate that change.

- **Full Table Replication**: Stitch will now correctly refresh tables using Full Table Replication.