---
title: "Salesforce (v1) integrations: Correct date chunking for Bulk API replication"
content-type: "changelog-entry"
date: 2018-12-12
entry-type: bug-fix
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/60"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

For {{ this-connection.display_name }} integrations using the Bulk API, when a query to the API times out, Stitch would cut the requested date range in half and re-try the request. However, after replicating the records, the integration wouldn't attempt to replicate the second half of the original window, resulting in missed records.

Because the integration only updates Replication Keys when records are extracted, Replication Keys wouldn't advance if records weren't received in the first half of the date range. This meant that the integration wouldn't ever try to replicate records in the second half of the date range.

This fix adds a check to see if the date range was chunked, and if so, queries the second half of the chunked range and extracts records, if any exist.