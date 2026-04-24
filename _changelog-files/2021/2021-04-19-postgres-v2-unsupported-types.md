---
title: "PostgreSQL (HP) (v2) integration: Removed support for Composite, Range and OID types"
content-type: "changelog-entry"
date: 2021-04-19
entry-type: removed
entry-category: integration
connection-id: postgres
connection-version: 2
pull-request: "https://github.com/stitchdata/tap-hp-postgres/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've removed support for Composite Types, Range Types and Object Identifier Types from our {{ this-connection.display_name }} integration.