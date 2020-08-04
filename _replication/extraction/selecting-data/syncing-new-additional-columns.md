---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Setting New and Additional Columns to Replicate
permalink: /replication/extractions/setting-new-additional-columns-to-replicate
redirect_from: /replication/syncing-new-additional-columns
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column, add new columns, sync new column, add additional columns, backfill data
summary: "Learn about setting new and additional columns to replicate in already replicating tables in Stitch."

# key: "new-additional-columns"

layout: general
content-type: "select-data"
toc: true
weight: 3


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  When you add a new column to a table in your data source, what happens in Stitch? What about replicating additional columns on already-replicating tables? Depending on the type of integration and the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) the table uses, there are a few possible outcomes.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: ""
    anchor: ""
    content: ""

  - title: "New columns in the data source"
    anchor: "new-columns-data-source"
    summary: ""
    content: |
      During a structure sync, Stitch will automatically detect new columns when they're added to a source. A structure sync is the first step in Extraction, and it detects the structure of and any changes to your data.

      If you don't see a recently added column available in Stitch, it's likely that a structure sync hasn't completed since the column was created. You can [manually kick off a replication job]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}), which, when finished, will display the column in Stitch.

      Note that:

      - The following applies to both database and non-webhook SaaS integrations.

      ### Already-Syncing Tables
      After the structure sync completes, the column will **be automatically synced** and, **if the [integration supports whitelisting columns]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }})**, display in the {{ app.page-names.int-details }} page. Data for the column will then replicate based on the table's Replication Method.

      **Keep in mind that for Incremental tables**, you may need to [backfill existing rows](#backfilling-existing-rows) if the addition of new data hasn't updated the table's [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}).

      ### Non-Syncing Tables
      If the table isn't currently selected to sync, the new column will display inside Stitch (if the [integration supports whitelisting columns]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }})) **but will have to be manually set to sync**.

  - title: "Selecting additional columns "
    anchor: ""
    summary: ""
    content: |
      In this case, we aren't talking about brand new columns in the data source, **but previously existing columns that have never been set to sync in Stitch**. How Stitch handles the syncing of additional rows depends on the table's Replication Method.

      ### Full Table Replication

      For tables using Full Table Replication, data in the newly-synced column will be available for **all rows** - including new and existing - the next time the table is successfully replicated.

      ### Incremental Replication

      For tables using Incremental Replication, data in the newly-synced column will be available **only for rows added AFTER the column is synced. Existing rows must be backfilled to make the data available.**

      Getting newly-synced column data into existing rows requires a full re-ync of the table. Because this can significantly impact your row count and we don't want to re-replicate data without your say-so, we leave inserting newly-synced column data into existing rows up to you.

      

---
{% include misc/data-files.html %}