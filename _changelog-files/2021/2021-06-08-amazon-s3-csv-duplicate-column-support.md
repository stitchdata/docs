---
title: "Amazon S3 CSV (v1) improvement: Duplicate column headers and extra value support"
content-type: "changelog-entry"
date: 2021-06-08
entry-type: improvement
entry-category: "integration, documentation"
connection-id: "amazon-s3-csv"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Our {{ this-connection.display_name }} integration now supports duplicate column headers and extra values in rows. We've added an additional system column (`{{ site.data.stitch.sdc-columns.current-columns.extra }}`) to support these scenarios.

Check out the [{{ this-connection.display_name }} docs]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}##loading--handling-duplicate-column-headers) for more info and examples.