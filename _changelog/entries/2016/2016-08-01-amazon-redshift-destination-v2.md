---
title: "Amazon Redshift destination: New version (v2)"
content-type: "changelog-entry"
date: 2016-08-01
entry-type: new-feature
entry-category: destination 
connection-id: redshift
connection-version: 2
---

Now 50% Redshiftier, along with these improvements: 

- Faster loading for high volume data streams
- Transactional upserts
- **NO MORE VIEWS**! Data is materialized into tables directly in the target schema, and these tables are never dropped

Learn more in the [docs]({{ site.data.urls.destinations.overviews.redshift | prepend: site.baseurl }}).