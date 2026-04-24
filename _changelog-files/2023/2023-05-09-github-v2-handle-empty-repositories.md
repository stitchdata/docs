---
title: "GitHub (v2) bug fix: Handle empty repositories"
content-type: "changelog-entry"
date: 2023-05-09
entry-type: bug-fix
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/187"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to allow the sync to continue when it encounters an empty repository.