---
title: "MongoDB (v11-01-2016) integrations: Replication Keys modification support"
content-type: "changelog-entry"
date: 2016-09-12
entry-type: new-feature
entry-category: replication
connection-id: mongo
connection-version: "11-01-2016"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Ever select the wrong Replication Key for a {{ this-connection.display_name }} integration when setting up Incremental Replication? If so, you'll know that it's a headache to change it.

Now, you can easily change it to the correct field within the Stitch app. Note that doing so will force a full re-replication of the table, to ensure all data is replicated using the correct Replication Key.