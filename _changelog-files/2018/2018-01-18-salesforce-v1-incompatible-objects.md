---
title: "Salesforce (v1): Additional incompatible objects"
content-type: "changelog-entry"
date: 2018-01-18
entry-type: removed
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/34"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've found that the following objects are incompatible with Stitch's querying strategy, and as a result are no longer available for replication:

- `LookedUpFromActivity`
- `AttachedContentNote`
- `QuoteTemplateRichTextData`