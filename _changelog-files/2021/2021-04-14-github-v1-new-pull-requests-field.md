---
title: "GitHub (v1) update: New base branch data available for pull_requests"
content-type: "changelog-entry"
date: 2021-04-14
entry-type: improvement
entry-category: "integration, documentation"
connection-id: github
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/109"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Several fields have been added to the `pull_requests` table in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The `base` object contains details about the base branch used in a given pull request, including the repository it originated from.

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#pull-requests"}}).