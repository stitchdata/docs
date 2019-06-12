---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Structuring Data for the Stitch Import API
permalink: /developers/import-api/guides/structure-data-for-the-import-api

doc-type: "concept"

product-type: "import-api"
content-type: "guide"
content-id: "structure-data"

layout: general
sidebar: on-page

icon: todo
order: 3

summary: ""
## This is used only on the /import-api/guides page.
description: ""


# -------------------------- #
#            INTRO           #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}



# -------------------------- #
#           CONTENT          #
# -------------------------- #

sections:
  - title: "Define tables"
    anchor: "define-tables"
    content: |
      When you push data to an arbitrary table name using the {{ integration.display_name }}, the table will be generated dynamically in your data warehouse. When creating requests, keep the following in mind:

      1. **The {{ integration.display_name }} doesn't enforce any limitation on the hierarchy of your tables.**
      2. **There aren't any commands to create or destroy a table in the {{ integration.display_name }}.**
      3. **You should create one table for each type of data point that you'll push.** For example: if you have customer and product data, you should create `customer` and `product` tables.
      4. **Each data point pushed to a single table should have the same data structure.** For example: if a `customers` table contains `customer_id`, `name`, and `email` columns, every customer record pushed into this table should contain those columns.
      5. **You can push more than one table using the same API access token.** Think of it this way: one schema for each API access token. All tables pushed using the same API access token will be housed in the same schema in your data warehouse.

  - title: "Define record sequences"
    anchor: "define-record-sequences"
    content: |
      Sequence properties communicate the order in which data points should be considered – newer data points can replace older ones, but not vice versa. 

      Every data point pushed to the Import API must have a `sequence` property.

      A simple solution is just to use the current timestamp, but before doing so, consider the following:

      1. **Are the rows being considered frequently updated?**
         Rows that are updated every few milliseconds can result in failure if records with identical key values are pushed simultaneously. This means that records with the same key values cannot be sent during the same clock resolution.

         For example: if the resolution is measured in milliseconds, records with identical key values cannot be sent during the same millisecond.
      2. **Are the records coming from multiple sources?**
         If records from multiple sources will be sent to the Import API, the time clocks of these sources must be synchronized. This is especially important if different sources are pushing rows to the same table.
---