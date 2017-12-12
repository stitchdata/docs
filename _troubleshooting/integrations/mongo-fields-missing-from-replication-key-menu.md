---
title: Mongo Fields Missing from Replication Key Menu
keywords: troubleshooting, integration, database integration, trouble, issue, help, mongo, mongodb, replication key, rep key
permalink: /troubleshooting/mongo-fields-missing-from-replication-key-menu
tags: [data_discrepancy, database_integrations]

summary: "If you don't see all the fields you expect to in the Replication Key field for you Mongo integration, the root cause may be insufficient permissions or a lack of field indexing."
type: "discrepancy, database-integration, replication"
---
{% include misc/data-files.html %}

{{ page.summary }}

---

{% include replication/rep-key-requirements.html %}

There are also some other considerations around Mongo Replication Keys, which you can read about in the [Selecting & Changing Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}).

---

## Detect Fields for Use as Replication Keys {#detecting-mongo-fields}

Stitch uses the `listIndexes` command to find fields that you can use for Incremental Replication. This means:

- If the Stitch user doesn't have permissions to run this command on a specified collection OR
- The field you want to use isn't indexed

Stitch will only be able to display the `_id` field in the Replication Key selection field.

**If the collection is append-only**, this may be perfectly fine.

**If the collection isn't append-only**, another field may be needed. We recommend reviewing the [Selecting & Changing Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) for help selecting an appropriate Replication Key.

---

## Next Steps

1. Verify that the Stitch Mongo user has all the required permissions as outlined in the [Mongo connection instructions]({{ site.baseurl }}/integrations/databases/mongodb).
2. Verify that the field you want to use is indexed.
3. Verify that the field you want to use as a Replication Key exists in the root of the document.

**Note that it may take some time for Stitch to detect and process these changes after you've applied them.** We recommend waiting for a replication cycle to complete before reaching out to support.

---

## Contact Support

If you've done all of the above, a full replication cycle has completed, and the field still hasn't shown up in the Replication Key field, please reach out to support.