---
title: "Yotpo (v1) update:"
content-type: "changelog-entry"
date: 2021-06-17
entry-type: improvement
entry-category: "integration"
connection-id: "yotpo"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-yotpo/pull/20"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made some updates to our {{ this-connection.display_name }} integration that improves error handling and messaging during Extraction:

- **Fixed a transform error with the `unsubscribers` table**. Previously, records without valid Primary Key values would result in a critical error that stopped extraction. Now, these records will be dropped and a message will display in the Extraction Logs. This allows Extraction to continue for records with valid Primary key values.

- **Some errors now result in an automatic retry.**. Previously, if the integration received certain response codes from {{ this-connection.display_name }}'s API, Stitch would stop Extraction. The following response codes now trigger an exponential backoff and then automatic retry:

   |**Response code** | **Message** |
   |-----------------:|-------------|
   | 401              | Invalid authorization credentials. |
   | 429              | The API rate limit for your organisation/application pairing has been exceeded. |
   | 502              | Server received an invalid response. |
   | 503              | API service is currently unavailable. |
   | 504              | API service time out, please check Yotpo server. |