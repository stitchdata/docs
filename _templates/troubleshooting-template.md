---
title: 
keywords: 
permalink: /troubleshooting/MOST-RELEVANT-CATEGORY/page-title-here
tags: []

summary: ""
type: ""
toc: true
---
{% include misc/data-files.html %}

Directions for using this template:

1. `page.tags` acts as a way to categorize articles. When articles are tagged with a pre-created tag, they're added to the tag page for that category. For example: articles tagged with `troubleshooting_destinations` will [show up here](https://www.stitchdata.com/docs/tag_troubleshooting_destinations).

   In `/_data/tags.yml` is the list of allowed tags.

   To tag a page, enter the tag **exactly as it appears in this list** in the page's `tags` Frontmatter field. Use commas to separate multiple tags. For example:

   ```
   tags: [troubleshooting_destinations, replication]
   ```

2. `page.type` is used on the category pages in Troubleshooting (ex: `/troubleshooting/integrations`) to sort articles into specific buckets. A page can have more than one type - separate them using commas.

   The full list of Troubleshooting types:

   - account - for account-related issues
   - all-integrations - issue that applies to all integrations
   - connection - for connection issues, both destination and integration

   - database-integration - if used, make sure the integration's name is in `page.keywords`
   - saas-integration - if used, make sure the integration's name is in `page.keywords`

   - discrepancy - for data discrepancies
   - error
   - replication
   - replication-all - replication issue that applies to all integration types (ex: columns with NULL values)

   - **Destinations**
   	   - all-destinations - issue that applies to all destination types
   	   - bigquery-destination
	   - panoply-destination
	   - postgres-destination
	   - redshift-destination