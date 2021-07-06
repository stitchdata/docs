---
title: "MySQL (v1) integrations: Primary Keys can't be an unsupported data type"
content-type: "changelog-entry"
date: 2017-10-25
entry-type: bug-fix
entry-category: "integration"
connection-id: "mysql"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mysql/pull/45"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, this integration would allow columns with unsupported data types to be included in the Primary Keys (`key_properties`) for a table. This has been corrected.