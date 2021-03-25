---
title: "Pendo (v1) improvement: Improve performance for visitors and events tables"
content-type: "changelog-entry"
date: 2021-03-12
entry-type: improvement
entry-category: "integration"
connection-id: "pendo"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-pendo/pull/28"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've implemented [ijson](https://github.com/ICRAR/ijson){:target="new"}, which is used in other Singer taps, to streamline replication for {{ this-connection.display_name }}'s `visitors` and `events` tables. This improvement reduces the amount of memory needed to replicate large amounts of data, potentially leading to improved Extraction times.
