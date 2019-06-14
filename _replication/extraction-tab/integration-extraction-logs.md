---
title: Extraction Logs
permalink: /replication/extractions/integration-extraction-logs
redirect_from: /replication/integration-extraction-logs
keywords: replication, extract, extraction, logs, report
summary: "Extraction logs provide detail about the extraction portion of the replication process for a given integration."

layout: general
content-type: "replication-progress"
toc: true
weight: 2

enterprise: true

enterprise-cta:
  title: "Get 60 days of Extraction Logs with Stitch Enterprise"
  utm: "?utm_medium=docs&utm_campaign=extraction-log-retention"
  copy: "Enterprise plans come with 60 days of Extraction Logs, allowing you to view an integration's extraction behavior over time, identify patterns, and quickly resolve errors when they arise."

intro: |
  {% include note.html first-line="**Extraction log availability**" content="Extraction logs are available only for integrations powered by Singer taps. As integrations are converted to the Singer system, extraction logs will be made available." %}

  {{ page.summary }} In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Log retention"
    anchor: "log-retention"
    summary: "How long logs are retained"
    content: |
      {% include misc/icons.html %}

      Extraction logs are grouped by day. The number of days' worth of logs available to you depends on your Stitch plan:

      {% assign subscription-plans = stitch.subscription-plans.all-plans | where:"legacy",false %}

      <table class="attribute-list">
          <tr>
              {% for plan in subscription-plans %}
              <td>
                  <strong>{{ plan.name }}</strong>{% if plan.name == "Standard" %}{{ notice-icon | replace:"TOOLTIP","The Standard plan replaces the Starter, Basic, and Premier plans." }}{% endif %}
              </td>
              {% endfor %}
          </tr>
          <tr>
              {% for plan in subscription-plans %}
              <td>
                  {{ plan.logs }}
              </td>
              {% endfor %}
          </tr>
      </table>

    subsections:
      - title: "Logs and plan changes"
        anchor: "logs-and-plan-changes"
        content: |
          Changing your plan can impact logs currently available to you.

          #### Plan downgrades

          If you downgrade to a plan that offers fewer days' logs, you'll **lose** access to the difference between your current plan and your new plan.

          For example: If you downgrade to Free from the Standard plan, you'll lose access to six days' worth of logs.

          #### Plan upgrades

          Likewise, if you upgrade to a plan that offers more days' logs, you'll immediately **gain** access to the difference.

          For example: If you upgrade to Standard from the Free plan, you'll gain access to an additional six days' worth of logs.

          {% include enterprise-cta.html %}

  - title: "Log composition"
    anchor: "log-composition"
    summary: "How to read the logs"
    content: |
      The graph at the top of the Extractions tab displays every time Stitch connected to the integration by day, based on the integration's [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}).

      {% include layout/inline_image.html type="normal" file="replication/extraction-graph-rep-frequency.gif" alt="Extraction graph with intervals of 30 minutes" %}

      In addition to displaying the time an extraction began, the tooltips also include how long the extraction ran for and if any errors arose.

      To view the raw logs for a specific extraction, click the **View Logs** link in the tooltip or the bar in the graph. This will open the logs for the job in the **Extraction Logs** section, located below the graph.

    subsections:
      - title: "Logs for in progress jobs"
        anchor: "logs-for-in-progress-jobs"
        content: |
          When a replication job is currently running, the job will have an **In Progress** status and a {{ app.buttons.stop-extraction }} button:

          ![An In Progress replication job and Stop Extraction button, highlighted]({{ site.baseurl }}/images/replication/stop-in-progress-job.png)

          You can use the {{ app.buttons.stop-extraction }} button to stop an in progress job, which is useful when the data source is experiencing issues. Refer to the [Start and stop extraction jobs documentation]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) for more info.

      - title: "Extraction log fields"
        anchor: "extraction-log-fields"
        content: |
          Lines in raw extraction logs are made up of four fields. Before we get into the field details, take a look at this example line:

          ```shell
          2017-11-17 16:44:41,159Z tap - INFO State update: adding bookmarks.ads.updated_time = "2017-11-06T13:29:23-05:00"
          ```

          In the table below, we'll break down each of the fields and explain what they mean.

          {% assign extraction-logs = site.data.ui.extraction-logs %}

          <table>
              <tr>
                  <th>
                      Order
                  </th>
                  <th width="15%; fixed">
                      Name
                  </th>
                  <th>
                      Example
                  </th>
                  <th width="50%; fixed">
                      Description
                  </th>
              </tr>
              {% for field in extraction-logs.fields %}
              <tr>
                  <td>
                      {{ forloop.index }}
                  </td>
                  <td>
                      {{ field.name }}
                  </td>
                  <td>
                      {{ field.example | markdownify }}
                  </td>
                  <td>
                      {{ field.description | markdownify }}
                  </td>
              </tr>
              {% endfor %}
          </table>

  - title: "Extraction log examples"
    anchor: "extraction-log-examples"
    summary: "Some examples of extraction logs"
    content: |
      When reading the extraction logs for your integrations, pay particular attention to the content of the message body. The message body will contain information about what's currently happening in the extraction process and errors, should they arise.

      Below are some examples of extraction logs, what they indicate, and how to read them.

    subsections:
      - title: "Replication Key values"
        anchor: "replication-key-values"
        content: |
          [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) are columns used to identify new and updated data in tables that use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}).

          The extraction logs contain information about the current Replication Key value for a given table, as well as the updated value detected during the extraction process.

          {% capture replication-keys-in-tables %}
          Unlike database integrations, Stitch automatically selects the field to use for Key-based Incremental Replication. This can make it difficult to remember which field extraction is based on.

          To see the Replication Keys for a given integration, check the **Schema** section of the [integration's documentation]({{ site.baseurl }}/integrations/saas). Look for fields with a {{ ui-icon.replication-key | flatify }} icon next to their names.
          {% endcapture %}

          {% include note.html first-line="**SaaS Integrations & Replication Keys**" content=replication-keys-in-tables %}

          #### Replication Key values and extraction

          The last saved maximum Replication Key value for a given table is used to detect new and updated data.

          For example: In this log line, Stitch will extract data from the `ads` endpoint that has an `updated_at` timestamp greater than or equal to `2017-11-06T12:48:15-05:00`:

          ```shell
          2017-11-21 18:16:08,389Z    tap - INFO found current bookmark for ads:  2017-11-06T12:48:15-05:00
          ```

          #### Updated Replication Key values

          During the extraction process, Stitch will update the Replication Key values for the tables set to replicate.

          Generally, the log line containing the saved Replication Key value for a table will be similar to this:

          ```shell
          2017-11-21 18:21:15,307Z   main - INFO State update: adding bookmarks.ads.updated_time = "2017-11-06T13:29:23-05:00"
          ```

          Beginning after `bookmarks`, read the following as `table_name.replication_key_field`. In this case, the table is `ads`, the Replication Key is `updated_time`, and the saved Replication Key value for the table is being updated to `2017-11-06T13:29:23-05:00`.

          **Note**: This line will not display in the logs for tables that have unchanged Replication Key values. This means if Stitch doesn't detect any new or updated data for a table, a line like the above will not appear in the logs for that table.

  - title: "Extraction errors"
    anchor: "extraction-errors"
    summary: "How to handle errors during extraction"
    content: |
      If an error occurs that terminates the extraction process, a line with a message type of `CRITICAL` will appear in the log. Generally, this will also display as the last line of the log.

      For example: During this extraction of Salesforce data, Stitch detected that there wasn't sufficient API quota available to continue replication:

      ```shell
      2017-11-20 07:48:45,410Z    tap - CRITICAL Salesforce has reported 32115/100000 (32.12%) total REST quota used across all Salesforce Applications. Terminating replication to not continue past configured percentage of 30.0% total quota.
      ```

      For the majority of errors, Stitch will parse out and display the messages separately from the raw extraction logs:

      {% include layout/inline_image.html type="normal" file="replication/extraction-log-error.png" alt="Error message from error that occurred during extraction" %}

      If an error arises, check out our [troubleshooting guides]({{ link.troubleshooting.main | prepend: site.baseurl }}) for help.
---
{% include misc/data-files.html %}