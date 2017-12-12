---
title: Replication Keys for Mongo Integrations
permalink: /replication/mongo-replication-keys
keywords: replicate, replication, replication key, keys, stitch replicates data, rp, mongo, mongodb, mongo database integration
tags: [replication]
summary: "Replication Keys for Mongo integrations have their own set of quirks and gotchas, owing to how Mongo itself is designed. In this guide, we'll explain what to watch out for and how to choose the best field for the job."

type: "settings"
toc: true
weight: 4
---
{% include misc/data-files.html %}

Replication Keys are columns that Stitch uses to identify new and updated data for replication. As Stitch's Mongo integration uses only [Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}), when you set a Mongo collection to sync, you'll also need to define a Replication Key.

Incorrectly setting a Replication Key can cause data discrepancies, latency, and high row counts. As Mongo Replication Keys have their own set of quirks, it's important to understand how they work and what makes a good key.

---

{% include replication/rep-keys-vs-primary-keys.html %}

---

{% include replication/rep-key-requirements.html %}

---

## Recommendations & Gotchas

While a field need only be indexed and exist in the root of the document to be a Mongo Replication Key, we have some recommendations (and things you should keep in mind) when selecting a field to be a Replication Key.

{% include replication/rep-key-recommendations.html %}

{% include replication/rep-key-gotchas.html %}

---

{% include replication/define-rep-keys.html %}

---

{% include replication/reset-rep-keys.html %}