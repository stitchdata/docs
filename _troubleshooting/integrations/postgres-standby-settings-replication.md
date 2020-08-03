---
title: PostgreSQL Read Replicas and Slow Replication
keywords: postgresql troubleshooting, postgres issue, postgres replication, hot_standby, standby, read replica, follower database, timeout, slow replication
permalink: /troubleshooting/postgres-hot-standby-settings-replication
summary: "If you connected a PostgreSQL read replica as a database integration and are experiencing extremely slow replication, the root cause may be the database's `standby` settings."
layout: general
toc: false

type: "discrepancy, database-integration, replication"
promote: "false"

intro: |
  {% assign all-databases = site.database-integrations | where:"input",true %}
  {% assign postgresql-databases = all-databases | where:"db-type","postgres" | sort: title %}

  This article is applicable to the following database integrations:

  {% for database in postgresql-databases %}
  {% unless database.name == "heroku" %}
  - [{{ database.title | remove: "(v1)" }}]({{ database.url | prepend: site.baseurl }})
  {% endunless %}
  {% endfor %}

sections:
  - title: "Symptoms"
    anchor: "symptoms"
    content: |
      Extremely slow, intermittent replication from a PostgreSQL read replica. It will look like data is "trickling" in.

  - title: "Cause"
    anchor: "cause"
    content: |
      A read replica, or follower, is a database that runs a **copy** of an active - or master - database.

      If a PostgreSQL read replica is running in [hot standby mode](https://www.postgresql.org/docs/9.2/static/hot-standby.html), the default values for some of its settings may prevent Stitch from successfully completing queries. These settings define the amount of time the replica is permitted to get behind the production database before canceling the conflicting queries.

      If Stitch's queries take too long to run - which can happen when tables are extraordinarily wide or when the master attempts to update the read replica - Stitch's queries will be interrupted. This results in a slow trickle of replicated data.

      To learn more about how PostgreSQL defines query conflicts, [check out the official documentation](https://www.postgresql.org/docs/9.2/static/hot-standby.html#HOT-STANDBY-CONFLICT){:target="new"}.

  - title: "Solution"
    anchor: "solution"
    content: |
      By default, the `max_standby_streaming_delay` and `max_standby_archive_delay` settings are set to 30 seconds.

      To ensure Stitch's queries are successful, **increase these settings to 8-12 hours**, especially for large historical jobs. You can also increase these values in smaller increments until you find the perfect middle ground.

      After the initial historical replication completes, you can typically decrease these settings again.
---
{% include misc/data-files.html %}