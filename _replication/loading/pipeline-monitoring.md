---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Pipeline Monitoring Overview
permalink: /replication/pipeline-monitoring
keywords: data structure, schema, data load, loading data, observability, monitoring, pipeline monitoring

summary: "Learn how Stitch can help your monitor your data's reliability."

destination: false
content-type: "general"
type: "all"
key: "data-observability"

layout: general
toc: true

# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  Learn how Stitch can help you monitor your data's reliability and minimize data downtime. In this guide you will learn everything you need to know on how to fully utilize the Pipeline Monitoring features.


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Monitoring basics"
    anchor: "basics"
    summary: "Some Pipeline Monitoring basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What can I monitor with these features?"
        anchor: "basics--what-is-pipeline-monitoring"
        content: |
          Stitch will display key ingestion indicators and a timeline of schema events for all tables ingested. An **ingestion metric**  is a metric on the Stitch ingestrion process. A **schema event** is when an underlying table structure changes in a way that could break downstream processes or cause silent errors as old columns stop being populated.

      - title: "Who can use these monitoring features?"
        anchor: "basics--who-can-use-pipeline-monitoring"
        content: |
          Anyone on a paid plan, trial, and pre-trial can see ingestion metrics. If you are on an expired trial, a deactivated account, or a billing hold Stitch will only show data from tables ingested in the past 30 days.


  - title: "Data ingestion"
    anchor: "ingestion-general"
    summary: "An overview on ingestion metrics"
    content: |
      This functionality is available to all eligible clients across all destinations. Metrics and events information will also include table data from sources that are currently paused and/or without a target destination.

      Whenever data is present in your Stitch account, you will be able to see metrics for tables that have been ingested within the past 30 days.

    subsections:
      - title: "Time between loads"
        anchor: "ingestion-time-between-loads"
        content: |
          The **Time between loads** chart shows the time since data was last loaded. To view this chart, you must select a table. You can also see the average time between loads accross all days where data exists.

      - title: "Rows loaded"
        anchor: "ingestion-rows-loaded"
        content: |
          The **Rows loaded** chart shows how many rows have been loaded into a given table. This metric is aggregated as a sum of all rows loaded into your tables for that day. You can also filter this chart by loaded table.
        
  - title: "Schema event"
    anchor: "ingestion-schema-event"
    content: |
      This functionality is available to all eligible clients across all destinations. Displayed schema events information will also include table data from sources that are currently paused and/or without a target destination.
      
      A **Schema event** is when a column is loaded for the first time within the past 30 days. The only exception to this is when an entirely new table is being loaded for the first time.

      Schema events are displayed as a timeline ordered from most recent to least. Multiple new columns in the same load are registered as a single event. Each  schema event shows the **table name**, **list of new columns** in the load, and the **date** and **timestamp** of the load.
---
{% include misc/data-files.html %}