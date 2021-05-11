---
title: "MailChimp (v1) update: Error message for `campaigns` table"
content-type: "changelog-entry"
date: 2021-04-13
entry-type: updated-feature
entry-category: integration
connection-id: mailchimp
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mailchimp/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the export timeout error message for the `campaigns` table to indicate that the export will continue to be extracted in the next replication.

New error message: |
  `Mailchimp campaigns export is still in progress after {} seconds. Will continue with this export on the next sync.`