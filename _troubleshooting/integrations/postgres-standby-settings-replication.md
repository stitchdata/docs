---
title: PostgreSQL Read Replicas & Slow Replication
keywords: postgresql troubleshooting, postgres issue, postgres replication, hot_standby, standby, read replica, follower database, timeout, slow replication
permalink: /troubleshooting/postgres-hot-standby-settings-replication
tags: [data_discrepancy, database_integrations]

summary: "If you connected a PostgreSQL read replica as a database integration and are experiencing extremely slow replication, the root cause may be the database's `standby` settings."

type: "discrepancy, database-integration, replication"
promote: "false"
---
{% include misc/data-files.html %}

If you connected a PostgreSQL read replica as a database integration and are experiencing extremely slow replication, the root cause may be the database's `standby` settings.

---

## Default Standby Settings & Stitch Queries {#default-settings-query-impact}

A read replica, or follower, is a database that runs a **copy** of an active - or master - database.

If a PostgreSQL read replica is running in [hot standby mode](https://www.postgresql.org/docs/9.2/static/hot-standby.html), the default values for some of its settings may prevent Stitch from successfully completing queries. These settings define the amount of time the replica is permitted to get behind the production database before canceling the conflicting queries.

If Stitch's queries take too long to run - which can happen when tables are extraordinarily wide or when the master attempts to update the read replica - Stitch's queries will be interrupted. This results in a slow trickle of replicated data.

To learn more about how Postgres defines query conflicts, [check out their documentation](https://www.postgresql.org/docs/9.2/static/hot-standby.html#HOT-STANDBY-CONFLICT).

---

## Next Steps

By default, the `max_standby_streaming_delay` and `max_standby_archive_delay` settings are set to 30 seconds.

To ensure Stitch's queries are successful, **increase these settings to 8-12 hours**, especially for large historical syncs. You can also increase these values in smaller increments until you find the perfect middle ground.

After the initial historical sync completes, you can typically decrease these settings again.