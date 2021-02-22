---
title: Replication scheduling change for non-database integrations
content-type: "changelog-entry"
date: 2017-07-25
entry-type: updated-feature
entry-category: replication
---

Non-database integrations now schedule replication by waiting the configured interval from the last time they were scheduled. This means that integrations with a daily schedule will run at the same time every day, and those with an hourly schedule will run at the same number of minutes past every hour. With the change, all integrations now use this scheduling logic.

Refer to the [docs]({{ site.data.urls.replication.rep-frequency | prepend: site.baseurl }}) for more info and examples.