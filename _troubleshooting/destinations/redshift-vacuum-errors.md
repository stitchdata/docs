---
title: Redshift VACUUM Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply
permalink: /troubleshooting/destinations/redshift-vacuum-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "If you received a `VACUUM` notification, it means that Stitch hasn't been able to successfully complete `VACUUM` some tables in your data warehouse for more than 10 days."
type: "redshift-destination, error"
promote: "false"
---
{% include misc/data-files.html %}

> "We've been unable to `VACUUM` for awhile."

If you received this notification from us, it means that Stitch hasn't been able to successfully perform `VACUUM` on some tables in your data warehouse for more than 10 days.

To keep things tidy in your data warehouse, Stitch will occasionally execute a ``VACUUM`` command after tables that use Full Table Replication have finished replicating. The purpose of `VACUUM`ing is to reclaim disk space and reduce storage. You can read more about [vacuuming in Redshift here](http://docs.aws.amazon.com/redshift/latest/dg/t_Reclaiming_storage_space202.html).

Stitch needs to be able to execute this command to keep these tables from growing too large with deleted rows.

---

## Resolving VACUUM Errors

Typically these errors are caused by insufficient permissions associated with the Stitch Redshift user. 

The other cause has to do with the number of tables that use Full Table Replication and how often they're replicated.

### Verify the Stitch Redshift User's Permissions

**The Redshift user that Stitch uses to access your data warehouse must be the owner of all the integration schemas and tables created by Stitch.** This will ensure that Stitch can successfully run the `VACUUM` command.

Verify that the Stitch user is the owner of the tables listed in the notification you received. If Stitch isn't the owner, update the user's permissions.

### Manually Vacuuming Tables

If a large number of tables are set to Full Table Replication and these tables are replicated frequently, Stitch may be unable to execute the `VACUUM` command due to how the timing works out in the replication process.

For example: if a large number of fully replicated tables are replicated back-to-back, there might not be a break in the process during which Stitch can `VACUUM`. The likelihood of this occurring will increase with the higher number of tables that use Full Table Replication and more frequent replication attempts.

**Stitch will wait 10 days to notify you about the issue if this is the root cause** - we do this to give things time to work themselves out. If you receive the `VACUUM` error AND the permissions are correct, we recommend that you `VACUUM` the affected tables manually to ensure they stay at a reasonable size. 