---
title: Pendo (v1) improvement: using ijson to improve `visitors` and `events` replication
content-type: "changelog-entry"
date: 2021-03-12
entry-type: improvement
entry-category: "integration"
connection-id: "pendo"
connection-version: "1"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

ijson is now being used for {{ this-connection.display_name }}'s `visitors` and `events` streams to improve performance. It reduces the amount of memory needed to replicate its potentially large amounts of data.