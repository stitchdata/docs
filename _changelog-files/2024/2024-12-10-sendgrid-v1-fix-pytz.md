---
title: "SendGrid Core (v1): ModuleNotFound error"
content-type: "changelog-entry"
date: 2024-12-10
entry-type: bug-fix
entry-category: integration
connection-id: sendgrid-core
connection-version: 1
pull-request: "https://github.com/singer-io/tap-sendgrid/pull/13"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the `ModuleNotFoundError: No module named 'pytz'` error by adding `pytz`.