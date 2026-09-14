---
title: "GitLab (v1): fix: convert branches and users child streams to INCREMENTAL replication"
content-type: "changelog-entry"
date: 2026-09-08
entry-type: bug-fix
entry-category: integration
connection-id: gitlab
connection-version: 1
pull-request: "https://github.com/singer-io/tap-gitlab/pull/56"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix: convert branches and users child streams to INCREMENTAL replication.