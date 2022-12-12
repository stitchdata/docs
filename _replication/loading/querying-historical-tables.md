---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Querying Historical Tables
permalink: /replication/loading/querying-historical-tables
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, historical
summary: "Learn how Historical Loading works and how to account for it in your queries."

key: "historical-querying"
type: ""

layout: general
toc: true
order: 1
content-type: "guide"


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% capture note %}
  - [Destinations configured to use Historical Loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append:"#reference--destinations-loading-behavior" }})
  {% endcapture %}

  {% include note.html first-line="**This guide is applicable to:**" content=note %}

  When data is loaded using [Historical Loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append:"#reference--destinations-loading-behavior" }}), records are appended to the end of the table as new rows. Only the `_sdc_end_date` column is updated in existing rows, to indicate when a new version was added. Multiple versions of a row can exist in a table, creating a log of how a record has changed over time.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Before using this guide"
    anchor: "before-using-guide"
    summary: "Things to know before using this guide"
    content: |
      Before using this guide, note that:

      - You may need to modify the queries in this guide to use them yourself
      - Stitch Support's expertise lies in replicating data, and as such does not provide data analysis or querying assistance. We can, however, help with data discrepancies.

         If you'd like assistance with analysis or business intelligence solutions, we recommend reaching out to one of our [analytics partners]({{ site.partners }}){:target="new"}.

  - title: "Retrieving the latest version of every record"
    anchor: "latest-version"
    summary: "A querying strategy that retrieves the latest version of every record"
    content: |
      {% include note.html type="single-line" content="**Note**: The queries in this section are only intended to demonstrate one approach to querying. You may need to modify the queries to use them yourself." %}

      Let's take a look at an example. Assume we have an `orders` table that contains:

      - A Primary Key of `id`,
      - The system `{{ system-column.prefix }}` columns added by Stitch, and
      - Other order attribute columns

      If you wanted to get all current records, you could use the following query:

      {% capture code %}
          SELECT * FROM orders
          WHERE
            _sdc_end_date = "9999-12-31 0:00 +00:00"
      {% endcapture %}

      {% assign description = "Querying all current records" %}

      {% include layout/code-snippet.html code=code code-description=description %}
      
      {% include note.html type="single-line" content="**Note**: Since the `_sdc_end_date` value for current records is set to `9999-12-31` UTC, it is recommended to use `9999-12-31 0:00 +00:00` in your queries to make sure you get the correct result regardless of your local time." %}


  - title: "Retrieving the version of every record for a specific date"
    anchor: "specific-date"
    summary: "A querying strategy that retrieves the version of every record for a specific date"
    content: |
      {% include note.html type="single-line" content="**Note**: The queries in this section are only intended to demonstrate one approach to querying. You may need to modify the queries to use them yourself." %}

      Let's take a look at an example. Assume we have an `orders` table that contains:

      - A Primary Key of `id`,
      - The system `{{ system-column.prefix }}` columns added by Stitch, and
      - Other order attribute columns

      If you wanted to get all records valid on December 1st 2022, you could use the following query:

      {% capture code %}
          SELECT * FROM orders
          WHERE
            _sdc_start_date <= "2022-12-01"
            AND _sdc_end_date > "2022-12-01"
      {% endcapture %}

      {% assign description = "Querying all records for a specific date" %}

      {% include layout/code-snippet.html code=code code-description=description %}

  - title: "Retrieving the version of a specific record for a date range"
    anchor: "date-range"
    summary: "A querying strategy that retrieves the version of a specific record for a date range"
    content: |
      {% include note.html type="single-line" content="**Note**: The queries in this section are only intended to demonstrate one approach to querying. You may need to modify the queries to use them yourself." %}

      Let's take a look at an example. Assume we have an `orders` table that contains:

      - A Primary Key of `id`,
      - The system `{{ system-column.prefix }}` columns added by Stitch, and
      - Other order attribute columns

      If you wanted to get the version of a record with the ID `694` valid in all of December 2022, you could use the following query:

      {% capture code %}
          SELECT * FROM orders
          WHERE
            id = 694
            AND _sdc_start_date <= "2022-12-01"
            AND _sdc_end_date >= "2022-12-31"
      {% endcapture %}

      {% assign description = "Querying the version of a specific record valid for a date range" %}

      {% include layout/code-snippet.html code=code code-description=description %}

  - title: "Create views in your destination"
    anchor: "create-destination-views"
    summary: "How to simplify querying by creating a view in your destination"
    content: |
      To make this easier, you can turn queries like the one above into a view. We recommend this approach because a view will encapsulate all the logic and simplify the process of querying against the latest version of your data.

      Refer to the documentation for your destination for more info on creating views:

      - [Snowflake]({{ site.data.destinations.snowflake.resource-links.create-views }}){:target="new"}
---