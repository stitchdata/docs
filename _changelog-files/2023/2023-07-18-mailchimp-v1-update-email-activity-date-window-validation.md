---
title: "MailChimp (v1) bug fix: Update email_activity_date_window validation"
content-type: "changelog-entry"
date: 2023-07-18
entry-type: bug-fix
entry-category: integration
connection-id: mailchimp
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mailchimp/pull/62"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to better handle `None` values for the `email_activity_date_window` property.