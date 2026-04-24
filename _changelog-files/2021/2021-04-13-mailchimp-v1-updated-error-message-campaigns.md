---
title: "MailChimp (v1) improvement: Improved timeout message for campaigns"
content-type: "changelog-entry"
date: 2021-04-13
entry-type: improvement
entry-category: integration
connection-id: mailchimp
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mailchimp/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the export timeout error message for the `campaigns` table to indicate that the export will continue to be extracted in the next replication:

```
Mailchimp campaigns export is still in progress after [number] seconds. Will continue with this export on the next sync.
```

Previously, this message (`campaigns - export deadline exceeded ([number] secs)`) didn't clearly set expectations for the table during the next replication job.