---
title: "Documentation update: Parent and child table info now available"
content-type: "changelog-entry"
date: 2021-05-27
entry-type: improvement
entry-category: "documentation"
pull-request: "https://github.com/stitchdata/docs/pull/646"
---

We've updated the integration schema documentation to include info about parent and child tables. Now you can tell, at a glance, if a table is dependent upon another table for replication:

![Parent table info in a child table's snapshot and description]({{ site.home | append:site.baseurl }}/images/changelog/child-table-example.png)

The **Parent table** field contains the name of the table that must also be selected for the child table to replicate successfully. This info will also be included in the child table's description. In this example, the `teams` table must be selected for the `team_members` table to replicate.

For parent tables, their descriptions will contain info about the child tables that depend on them:

![Child table info in a parent table's description]({{ site.home | append: site.baseurl }}/images/changelog/parent-table-example.png)

In this example, the `team_memberships` and `team_members` tables will only replicate successfully if the `teams` table is also selected.

We hope this additional info about integration tables provides additional insight into how Stitch replicates data and will help you avoid Extraction errors.

Currently this data is only available in the [GitHub (v1) docs]({{ site.home | append: site.baseurl | append: "/integrations/saas/github#schema" }}), but we'll roll it out to other integrations as we make updates.