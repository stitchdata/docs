---
title: Time-based replication scheduling is now available!
content-type: "changelog-entry"
date: 2018-05-23
entry-type: new-feature
entry-category: replication
---

Stitch customers now have some control over when extractions begin. This new feature allows users to "anchor" extraction start times to a specific time, ensuring Stitch is predictably replicating data when it's most needed.

For example: Setting a six (6) hour replication with an anchor time of 12:00 PM would create this schedule:

- 12:00PM
- 06:00PM
- 12:00AM
- 06:00AM

Check out the [docs]({{ site.data.urls.replication.anchor-scheduling | prepend: site.baseurl }}) for full details.