---
title: "JIRA (v2) update: Date format transformation"
content-type: "changelog-entry"
date: 2022-05-20
entry-type: updated-feature
entry-category: integration
connection-id: jira
connection-version: 2
pull-request: "https://github.com/singer-io/tap-jira/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This update converts the `userStartDate` and `userReleaseDate` fields in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) to `yyyy-mm-dd` format before transformation.