---
title: Loading Reports
permalink: /replication/integration-loading-reports
keywords: replication, load, loading, report
tags: [replication]
summary: "Loading reports provide detail about the loading portion of the replication process for a given integration." 
layout: general

key: "loading-reports"
content-type: "replication-progress"
toc: true
weight: 3

enterprise: true

enterprise-cta:
  title: "Get {{ site.data.stitch.subscription-plans.enterprise.reports }} of Loading Reports with Stitch Enterprise"
  utm: "?utm_medium=docs&utm_campaign=loading-report-retention"
  copy: "Enterprise plans come with {{ site.data.stitch.subscription-plans.enterprise.reports }} of Loading Reports, allowing you to view an integration's loading behavior over time, identify high volume tables, and quickly resolve errors if they arise."

intro: |
  {% include misc/data-files.html %}

  {% include note.html first-line="**Loading report availability**" content="Loading reports are available only for integrations powered by Singer taps. As integrations are converted to the Singer system, loading reports will be made available." %}

  The last phase of every Stitch replication job is called **Loading**. During Loading, Stitch loads [extracted data]({{ link.replication.extraction-logs | prepend: site.baseurl }}) into your destination. The **Loads** tab - accessed by clicking into the integration from the {{ app.page-names.dashboard }} - provides detail about the loading portion of the replication process for a given integration.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Report retention"
    anchor: "report-retention"
    summary: "How long reports are retained"
    content: |
      {% include misc/icons.html %}

      Loading reports are grouped by day. The number of days' worth of reports available to you depends on your Stitch plan:

      {% assign all-plans = site.data.stitch.subscription-plans.all-plans %}

      {% for plan in all-plans %}
      {% if plan.key %}
      {% assign this-plan = site.data.stitch.subscription-plans[plan.key] %}
      {% else %}
      {% assign this-plan = site.data.stitch.subscription-plans[plan.name] %}
      {% endif %}

      - **{{ plan.name | capitalize | replace:"-"," " }}**: {{ this-plan.reports }}
      {% endfor %}

    subsections:
      - title: "Reports and plan changes"
        anchor: "reports-and-plan-changes"
        content: |
          Changing your plan can impact reports currently available to you.

          {% assign enterprise-reports = site.data.stitch.subscription-plans.enterprise.reports | remove: " days" %}
          {% assign standard-reports = site.data.stitch.subscription-plans.standard.reports | remove: " days" %}

        sub-subsections:
          - title: "Plan downgrades"
            anchor: "plan-downgrades"
            content: |
              If you downgrade to a plan that offers fewer days' reports, you'll **lose** access to the difference between your current plan and your new plan.

              For example: If you downgrade to Standard from the Enterprise plan, you'll lose access to {{ enterprise-reports | minus: standard-reports }} days' worth of reports.

          - title: "Plan upgrades"
            anchor: "plan-upgrades"
            content: |
              Likewise, if you upgrade to a plan that offers more days' reports, you'll immediately **gain** access to the difference.

              For example: If you upgrade to Enterprise from the Standard plan, you'll gain access to an additional {{ enterprise-reports | minus: standard-reports }} days' worth of reports.

              {% include enterprise-cta.html %}

  - title: "Loading Report composition"
    anchor: "all-loading-reports"
    summary: "How to read and navigate the Loading Reports"
    content: |
      When the **Loading Reports** tab is first clicked, the loading reports for all tables will display first.

      Every row on this page corresponds to a single table that is set to replicate. The data in each table's row is updated upon every successful load to your destination, thus reflecting the loading state for the tables overall:

      ![Loading Reports for all tables in an integration]({{ site.baseurl }}/images/replication/loading-reports-for-all-tables.png)

      Clicking the name of the table in the **Tables to Replicate** column will open a page with a [loading report for that table](#loading-reports-by-table), enabling you to see loading behavior for the table over time.
    subsections:
      - title: "Loading data by time range"
        anchor: "data-by-time-range"
        content: |
          Use the toggle next to **Rows Loaded** to view a table's loading data based on the time range you select:

          - **24 hours**: Loading data for the past 24 hours
          - **This Billing**: Loading data for the current billing period
          - **Prev Billing**: Loading data for the previous billing period

          **Note**: A billing period is 30 days. To view the day the current billing period will end, navigate to the Billing page ({{ app.menu-paths.billing }}) and locate the **Next billing date** field.

        sub-subsections:
          - title: "Loading data for subtables"
            anchor: "loading-data-for-subtables"
            content: |
              Depending on the structure of your data in the source and the destination you're using, subtables may be created from a parent table.

              If a table contains subtables, a <i class="fa fa-plus-square" aria-hidden="true" ></i><span class="sr-only">Plus icon</span> icon will display next to its **Rows Loaded** value. Click the icon to view the number of rows loaded for its subtables.

              You can read more about subtables in the [Nested Data and Row Counts guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

          - title: "Loading data for non-replicating tables"
            anchor: "loading-data-for-non-replicating-tables"
            content: |
              {% include layout/inline_image.html type="right" file="replication/loading-reports-time-range.gif" alt="Rows Loaded time range selection" %}Loading data for tables not currently set to replicate may be available if the time of the last load is within the selected [time range](#data-by-time-range).

              For example: If the last load occurred less than 24 hours ago, the table's loading data will display when **24 hours** is selected. If it occurred more than 24 hours ago, select **This Billing** to see this table's loading stats for the current billing period.

          - title: "Loading Reports by table"
            anchor: "loading-reports-by-table"
            content: |
              The Loading Reports by Table page contains detailed loading stats for the selected table, broken down by day. The graph at the top of the page displays every time Stitch attempted to load data for the table into your destination for the selected date.

              To view loading reports for a specific day, use the date picker located above the graph. **Note**: The number of days' worth of logs varies by [plan type](#report-retention).

              ![Loading Reports for a single table]({{ site.baseurl }}/images/replication/loading-reports-by-table.png)

              In addition to displaying the time a load began, the tooltips also include how long the loading job ran and if any [errors](#loading-errors) arose during the job.

  - title: "Replication bookmarks in Loading Reports"
    anchor: "max-replication-bookmark-values"
    summary: "Understanding Replication bookmarks in Loading Reports"
    content: |
      {% include note.html type="single-line" content="The features in this section may not appear in the loading reports for some integrations. As we add this functionality to our integrations, bookmark columns in loading reports will be made available." %}

      Integration loading reports can contain information about the recency of your data. The **Max Replication Bookmark Value** column contains the highest or most recent [Replication Bookmark Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) value Stitch has loaded into your destination for a given table or replication job, displayed as `column_name: value`.

      Using the values in this column, you can identify how up-to-date the data in your destination is on a table-by-table basis or check the progress of a historical replication job.

      Keep in mind that:

      - **Replication Bookmark Key columns may not always be timestamps**. Some may be integers, like `id: 1234`.
      - For **SaaS integrations**, Stitch automatically selects the Replication Bookmark Key column. Refer to the [integration's schema documentation]({{ site.baseurl }}/integrations/saas) for the column(s) Stitch uses for each table.
      - For **Database integrations**, this is a column selected by you during [Replication Method setup]({{ link.replication.rep-methods | prepend: site.baseurl }})
      - **If the table is currently being loaded** (indicated by a {{ ui-icon.table-loading-in-progress | flatify }} icon), some data may load out of order. We suggest waiting until the load is complete to check the completeness of the data.  

    subsections:
      - title: "Replication Bookmark values, by page"
        anchor: "replication-bookmark-values-by-page"
        content: |
          On the [**Loading Reports for All Tables**](#all-loading-reports) page, the value in this column will reflect the highest or most recent value for the table **overall**:

          ![The highest Replication Bookmark Key value for a table, overall]({{ site.baseurl }}/images/replication/loading-reports-all-tables-max-bookmark.png)

          On the [**Loading Reports by Table**](#loading-reports-by-table) page, the value in this column will reflect the highest or most recent value for each **replication job** for the given table:

          ![Progessing Replication Bookmark Key values]({{ site.baseurl }}/images/replication/loading-reports-by-table-max-bookmark.png)

      - title: "Replication Bookmark unavailable"
        anchor: "replication-bookmark-unavailable"
        content: |
          For some tables, a **Bookmark Unavailable** message may display in the **Max Replication Bookmark Value** column in place of a value:

          ![Bookmark unavailable for integration table]({{ site.baseurl }}/images/replication/loading-reports-bookmark-unavailable.png)

          There are a few reasons this message may appear:

          - The table uses [Full Table Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#full-table-replication" }}) or [Log-based Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#log-based-incremental-replication" }}), replication methods which doesn't use a Replication Bookmark Key,
          - The column designated as the Replication Bookmark Key contains `NULL` values, or
          - The integration doesn't support this feature. As this functionality is added to eligible integrations, Replication Bookmark Key values in loading reports will become available.

  - title: "Loading errors"
    anchor: "loading-errors"
    summary: "How to handle errors during loading"
    content: |
      If an error occurs during the loading process, a {{ ui-icon.table-loading-error | flatify }} icon will display to the left of the affect table(s). To view the error for the table, hover over the error icon and then click the link in the tooltip.

      This will bring you to the Loading Report page for that table, where the error message will be expanded:

      {% include layout/inline_image.html type="normal" file="replication/table-loading-error-message.png" alt="Expanded error message on Loading Reports by Table page" %}

      If an error arises, check out the [Destination Loading Error Reference]({{ link.troubleshooting.dw-loading-errors | prepend: site.baseurl }}) for help.
---