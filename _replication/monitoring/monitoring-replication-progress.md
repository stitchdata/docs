---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Monitoring Replication Progress
permalink: /replication/monitoring-replication-progress
keywords: replicate, replication, replication progress, stitch replicates data, how long, where is my data, time to dw, time to data warehouse
summary: "Keep track of your data as it moves through Stitch using integration Replication Stats."

key: "wheres-my-data"
category: "monitoring"
content-type: "basics, monitoring"

layout: general
toc: true
weight: 1

# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  It can be difficult to be patient when all you want is your data. In the Integration Details page for every integration, you can check out that integration's Replication Stats. This section will give you a better idea of where your data is in the replication process.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: |
      "Where's my data?"
    anchor: "wheres-my-data"
    summary: "When to expect data in your destination"
    content: |
      This is the most frequently asked question Stitch support receives.

      In short, **replication through Stitch is not real-time**. The reason for this is that Stitch's replication process contains three distinct phases, each of which takes time to complete.

      TODO: FILL THIS OUT

  - title: "Understanding an integration's replication stats"
    anchor: "understanding-replication-stats"
    summary: "Understanding an integration's replication stats"
    content: |
      {% include note.html type="single-line" content="**Note**: These stats are not real-time and will update every few minutes. You'll need to refresh the page if you're eager to watch your data move through Stitch." %}

      After an integration's initial replication job completes, the replication stats section will populate with info about the current or last replication job, if one isn't currently in progress:

      ![Integration replication stats]({{ site.baseurl }}/images/replication/replication-stats.png)

      The data in this section can help you determine where your data currently is and check up on recently loaded data:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Extracted stats"
        anchor: "progress--extracted"
        content: |
          {% capture iapi-webhooks %}
          For IAPI and webhook integrations, the **Extracted** section will look a little different:

          - **For Import API integrations**, this section will display the last time data was successfully received by Stitch with a **Last Rows Received** stat.
          - **For webhook integrations**, Extraction stats aren’t available due to the real-time nature of webhooks. In this case, **Never** will display alongside **Last Rows Received**.
          {% endcapture %}

          {% include note.html first-line="**Extracted stats for Import API and webhook integrations**" content=iapi-webhooks %}

          The **Extracted** section displays details about the extraction part of the replication process:

          - **Last Sync Started** - The time the last replication job began.
          - **Last Sync Completed** - The time the last replication job successfully completed.
          - **Sync Status** - The status of the replication job. **Note**: If the integration is **Paused** or **Not Configure**, a status of **Not Syncing** will display here.

             Additionally, there may be times where an integration is in an error state and still display an **In Progress** status. This means that Stitch is attempting to extract data despite the issue causing the error.
          - **Next Sync** - The estimated time of the next replication job. This estimate is based on the integration’s replication schedule and the completion time of the last replication job.

          **Looking for more detail about what happened during a specific Extraction**? Use the integration's [Extraction logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      - title: "Preparing stats"
        anchor: "progress--preparing"
        content: |
          The **Preparing** section shows the total number of rows and tables Stitch is currently preparing to load into your data warehouse for the integration you’re viewing.

          The **Rows to be Loaded** stat is the total sum of rows across all tables currently in preparation (**Tables to be Loaded**).

      - title: "Loading stats"
        anchor: "progress--loading"
        content: |
          The **Loaded** section displays details about:

          - **Rows Loaded Today** - The total number of rows published to your destination **since midnight UTC** of the current day.
          - **Last Table Loaded** - The name of the last table loaded into your destination. **Note**: This isn't limited to the current day.

             For example: If the integration encountered an issue that prevented successful replication for a day or two, the name of the table displayed here may be several days old.

          **Looking for more detail about what happened during a specific Load**? Use the integration's [Loading reports]({{ link.replication.loading-reports | prepend: site.baseurl }}).

  - title: "Getting additional info"
    anchor: "getting-additional-info"
    summary: "Where to get additional info about Extractions and Loads"
    content: |
      Integration replication stats can be helpful if you need a high level look at the current or last replication job, but if you need more detail:
      
      - [**Extraction logs**]({{ link.replication.extraction-logs | prepend: site.baseurl }}) provide info about the tables set to replicate, the Replication Key values used, and any errors that arose during the extraction.

      - [**Loading reports**]({{ link.replication.loading-reports | prepend: site.baseurl }}) provide info about the current loading status of selected tables, the number of loaded rows, and any errors that arose during the load.
---
{% include misc/data-files.html %}