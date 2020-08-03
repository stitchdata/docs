---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Sequencing Data for the Stitch Import API
permalink: /developers/import-api/guides/sequencing-data-for-the-import-api
summary: &summary "Learn how to sequence data for the Import API."

doc-type: "concept"

product-type: "import-api"
content-type: "guide"
content-id: "sequence-data"

key: "import-api-sequence-data"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /import-api/guides page.
icon: replication
order: 4

display-title: "Sequencing data for the Import API"
description: *summary


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "Structuring data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Understanding loading behavior"
    link: "{{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}"


# -------------------------- #
#            INTRO           #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Stitch uses record sequencing to determine in what order extracted records are considered for loading. This practice, along with de-duping data using Primary Keys, ensures that only the most recent version of a record is loaded into a destination. Newer data points can replace older ones, but not vice versa.

  Stitch uses the `sequence` property on records pushed to the Import API to accomplish this. Every record in a request must have this property.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#           CONTENT          #
# -------------------------- #

sections:
  - title: "Understanding record sequencing"
    anchor: "understand-record-sequencing"
    summary: "The basics of record sequencing"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Sequencing and Replication Keys"
        anchor: "sequence-replication-keys"
        content: |
          Think of `sequence` like a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}), but on a record-by-record basis.

          For the Import API, sequence functions similarly to an `updated_at` property: Only records that have a `sequence` value greater than an existing record with the same Primary Key will be replicated and loaded.

          For example: The record below has a `sequence` value of `1574800199000`:

          {% capture code %}{
             "action":"upsert",
             "sequence":1574800199000,
             "data":{
                "id":1,
                "name":"Finn",
                "age":15,
                "has_magic":false
             }
          }
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

          In this example, `sequence` is a Unix epoch in milliseconds that translates to `Tuesday, November 26, 2019 8:29:59 PM GMT-05:00`.

      - title: "Record sequencing, Primary Keys, and loading"
        anchor: "record-sequencing-primary-keys"
        content: |
          {% capture append-only-notice %}
          If the destination uses or only supports Append-Only loading, data will not be de-duplicated using Primary Keys. The version of the record with the greatest sequence value will be loaded, but it will be appended to the destination table as a new row. This means that a table can contain several versions of a single record, showing how it has changed over time.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info.
          {% endcapture %}

          {% include note.html first-line="**Note**: This section only applies if the destination isn't configured to use Append-Only loading." content=append-only-notice %}

          Every record sent to the Import API must have a `sequence` property. If Primary Keys are defined for the table records are sent to, Stitch will use the provided `sequence` value and the record's Primary Key to de-duplicate data. This process ensures that only the most recent version of a record is loaded into a destination.

          For example: Below is a single request containing two data points, both for the same record (`id: 2`). Only data point 1 would be loaded into the destination, as it has a greater `sequence` value than data point 2:

          {% capture code %}{
             "action":"upsert",           /* Data point 1 */
             "sequence":1574807445000,    /* 11/26/2019 10:30:45 PM */
             "data":{
                "id":2,
                "name":"Jake",
                "has_magic":false
             }
          },
          {
             "action":"upsert",           /* Data point 2 */
             "sequence":1574807395000,    /* 11/26/2019 10:29:55 PM */
             "data":{
                "id":2,
                "name":"Jake",
                "has_magic":true
             }
          }
          
          {% endcapture %}

          {% include layout/code-snippet.html language="json" code=code %}

  - title: "Defining record sequences"
    anchor: "define-record-sequences"
    summary: "How to define a record's sequence"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Generating sequence values"
        anchor: "generate-sequence-values"
        content: |
          When developing your Import API script, you'll need to define how values for the `sequence` property are generated. 

          A simple solution is just to use the current timestamp, but before doing so, consider the following:

          - **How frequently are the records being updated?** If records with identical Primary Key values are updated every few milliseconds and pushed simultaneously, the correct version of a record may not be loaded successfully. This means that records with the same Primary Key values can't be sent during the same clock resolution.

             For example: If the resolution is measured in milliseconds, records with identical Primary Key values cannot be sent during the same millisecond.

          - **Are records being pushed from multiple sources?** If so, the time clocks of these sources must be synchronized. This is especially important if different sources are pushing records to the same table.

      - title: "Tracking a record's maximum sequence"
        anchor: "track-record-maximum-sequence"
        content: |
          In addition to generating sequence values for records, you'll also need to track the maximum sequence value for each record being pushed to the Import API. Sequence values need to continually increase or records in the destination won't be updated with new data.

  - title: "Example request"
    anchor: "examples"
    summary: "An example request"
    content: |
      This request for [POST {{ site.data.import-api.core-objects.batch.url }}]({{ link.import-api.api | append: site.data.import-api.core-objects.batch.anchor | prepend: site.baseurl }}) the contains three data points: One for record `id: 1`, and two for `id: 2`.

      If these data points were received in this order, only data points 1 and 2 would continue to Stitch.

      Data point 3 would not, as its `sequence` value is less than the `sequence` value for data point 2, which also has a Primary Key value of `id: 2`.

      {% capture code %}{
         "table_name":"customers",
            "messages":[
            {
               "action":"upsert",           /* Data point 1 */
               "sequence":1574807356000,    /* 11/26/2019 10:29:16 PM */
               "data":{
                  "id":1,
                  "name":"Finn",
                  "has_magic":false
               }
            },
            {
               "action":"upsert",           /* Data point 2 */
               "sequence":1574807445000,    /* 11/26/2019 10:30:45 PM */
               "data":{
                  "id":2,
                  "name":"Jake",
                  "has_magic":false
               }
            },
            {
               "action":"upsert",           /* Data point 3 */
               "sequence":1574807395000,    /* 11/26/2019 10:29:55 PM */
               "data":{
                  "id":2,
                  "name":"Jake",
                  "has_magic":true
               }
            }
         ],
         "key_names":[
            "id"
         ],
         "schema":{
            "properties":{
               "id":{
                  "type":"integer"
               },
               "name":{
                  "type":"string"
               },
               "has_magic":{
                  "type":"boolean"
               }
            }
         }
      }
      {% endcapture %}

      {% assign description = "Example request for POST " | append: site.data.import-api.core-objects.batch.url %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}
---