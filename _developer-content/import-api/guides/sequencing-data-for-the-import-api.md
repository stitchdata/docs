---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Sequencing Data for the Stitch Import API
permalink: /developers/import-api/guides/sequencing-data-for-the-import-api

doc-type: "concept"

product-type: "import-api"
content-type: "guide"
content-id: "sequence-data"

layout: general
sidebar: on-page

icon: todo
order: 4

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