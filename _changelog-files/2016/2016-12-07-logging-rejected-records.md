---
title: "Logging for rejected records"
content-type: "changelog-entry"
date: 2016-12-07
entry-type: new-feature
entry-category: replication
---

Occasionally, Stitch encounters data that it can’t load into a destination for a variety of reasons: Dates that fall out of range, table names that are too long, etc. 

Stitch now logs these records into a special table (`{{ site.data.stitch.system-tables.sdc-rejected.name }}`) for each integration. Each rejected record includes the reason for the rejection and as much data from the original record as can fit.

Learn more in the [docs]({{ site.data.urls.destinations.storage.rejected-records | prepend: site.baseurl | prepend: site.home }}).