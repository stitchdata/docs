---
title: Deleted Record Handling
permalink: /replication/deleted-record-handling
keywords: deletes, delete, hard delete, soft delete, deletion
tags: [replication]
category: "syncing"

summary: "[TODO]"
type: "settings"
toc: true
weight: 5
---
{% include misc/data-files.html %}
{% include misc/support-icons.html %}

Depending on the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) being used and how records are deleted in the source, deletes may not be captured during the replication process.

---

## Deletion methods

There are two methods that can be used to delete a source record:

- **Soft deletes**, which will leave a record in the source and use a flag to indicate deletion, such as `is_deleted` or `deleted_on`. If the delete event updates the record's Replication Key value, Stitch will detect and replicate the changes.
- **Hard deletes**, which completely remove records from the source. It's as if the record never existed. If using Key-based Incremental Replication, this will remove the record's Replication Key value, which Stitch uses to identify new and updated records. Without a Replication Key value to check, Stitch can't identify the change and update the record in the destination.

### Delete support overview

In the table below are each of Stitch's Replication Methods and the level at which each deletion method is supported.

Click the Replication Method name to check out examples of how each deletion method works with that specific Replication Method.

{% include replication/replication-methods-deleted-records.html %}

---

## Log-based Incremental Replication {#log-based-incremental}

{% include replication/deleted-record-examples.html replication-method="log-based-incremental" display-name="Log-based Incremental" %}

---

## Key-based Incremental Replication {#key-based-incremental}

{% include replication/deleted-record-examples.html replication-method="key-based-incremental" display-name="Key-based Incremental" %}

---

## Full Table Replication {#full-table}

{% include replication/deleted-record-examples.html replication-method="full-table" display-name="Full Table" %}