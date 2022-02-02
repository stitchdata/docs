---
title: "Salesforce (v1): Primary Key (PK) chunking"
content-type: "changelog-entry"
date: 2017-12-06
entry-type: improvement
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/18"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've implemented {{ this-connection.display_name }}'s [Primary Key (PK) chunking](https://developer.salesforce.com/docs/atlas.en-us.210.0.api_asynch.meta/api_asynch/async_api_headers_enable_pk_chunking.htm){:target="new"} feature into our integration.

If the integration is using the Bulk API and encounters a timeout error, Stitch will now re-try using the `Sforce-Enable-PKChunking` header in the API request. This approach 'chunks' data into small batches, allowing the integration to more efficiently extract large volumes of data.