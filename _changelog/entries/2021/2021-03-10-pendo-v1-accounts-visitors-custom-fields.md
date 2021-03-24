---
title: "Pendo (v1) bug fix: Custom fields error resolved"
content-type: "changelog-entry"
date: 2021-03-10
entry-type: bug-fix
entry-category: "integration"
connection-id: "pendo"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-pendo/pull/27"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Fixes made to the `visitors` and `accounts` tables:

1. Custom fields without defined types will no longer return a `null` value. 
2. The last property on tables with multiple custom fields were being overwritten. New code was added to avoid this.