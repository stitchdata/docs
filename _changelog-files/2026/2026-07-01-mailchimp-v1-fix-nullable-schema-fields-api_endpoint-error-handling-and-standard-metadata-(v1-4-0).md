---
title: "MailChimp (v1): Fix nullable schema fields, api_endpoint error handling, and standard metadata"
content-type: "changelog-entry"
date: 2026-07-01
entry-type: bug-fix
entry-category: integration
connection-id: mailchimp
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mailchimp/pull/77"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix: nullable schema fields, api_endpoint error handling, and standard metadata (v1.4.0).