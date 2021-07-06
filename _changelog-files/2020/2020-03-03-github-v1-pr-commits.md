---
title: "GitHub (v1) update: Squashed pull request commit data now available!"
content-type: "changelog-entry"
date: 2020-03-03
entry-type: updated-feature
entry-category: integration
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/67"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration: `pr_commits`.

This table is a slight modification of the existing `commits` table, but allows you to associate commits to pull requests that have been squash merged.