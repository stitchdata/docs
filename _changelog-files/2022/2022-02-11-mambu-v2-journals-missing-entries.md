---
title: "Mambu (v2) bug fix: Fixed missing records"
content-type: "changelog-entry"
date: 2022-02-11
entry-type: bug-fix
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/66"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Sorting has been added to the **Journals** endpoint to ensure no records are missed during extraction.