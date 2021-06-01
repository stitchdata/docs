---
title: "Mambu (v1) bug fix: Resolved decimal precision failures"
content-type: "changelog-entry"
date: 2021-03-17
entry-type: bug-fix
entry-category: integration
connection-id: "mambu"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mambu/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, if Stitch extracted decimal data larger than the constraint defined in the {{ this-connection.display_name }} integration (`1e-10`), data validation would fail and result in Extraction errors.

The integration has been updated to expand the constraint, ensuring that big decimal values will no longer result in validation failures.