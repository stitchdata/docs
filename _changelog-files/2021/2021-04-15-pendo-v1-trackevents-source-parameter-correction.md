---
title: "Pendo (v1) bug fix: Fixed replication issue for track_events table"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: bug-fix
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This bug fix resolves the following 400 error for {{ this-connection.display_name }} integrations where the `track_events` table is selected:

```
bad pipeline: bad source: bad parameters for source type trackEvents: unexpected parameters`.
```

We corrected the source parameter for the `trackEvents` source from `trackId` to `trackTypeId`, allowing this table to now replicate successfully.