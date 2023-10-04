---
title: "MailChimp (v1) update: New property for reports_email_activity stream"
content-type: "changelog-entry"
date: 2023-06-08
entry-type: updated-feature
entry-category: integration
connection-id: mailchimp
connection-version: 
pull-request: "https://github.com/singer-io/tap-mailchimp/pull/61"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a new `date_window` property in the `reports_email_activity` stream.