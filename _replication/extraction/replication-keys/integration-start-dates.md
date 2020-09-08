---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Integration Start Dates
permalink: /replication/extractions/replication-keys/understanding-integration-start-dates
keywords: replicate, replication, replication key, keys, stitch replicates data, rp, saas, historical data, reset bookmark, reset replication key
summary: "An integration's Start Date defines how far back Stitch should query for historical data. Learn how Start Dates work, how to define a custom Start Date, and how to change an existing integration's Start Date." 

layout: general

key: "define-integration-start-date"
content-type: "replication-keys, incremental-replication"
toc: true
weight: 6

# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  An integration's Start Date defines how far back Stitch should query for historical data. While the Start Date setting allows you to define historical data loads, it can also reset an integration's Replication Keys when you need to re-replicate data. In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Applicable integrations"
    anchor: "applicable-integrations"
    summary: "The integrations this guide applies to"
    content: |
      This guide is applicable to:

      <table>
      <tr>
      <td width="50%; fixed">
      <strong>SaaS integrations</strong>
      </td>
      <td>
      <strong>Database integrations</strong>
      </td>
      </tr>
      <tr>
      <td>
      {% capture saas %}
      All SaaS integrations **with the exception of the following**:

      {% assign saas-sources = site.developer-files | where:"source-type","saas" %}
      {% assign sources-without-start-date = saas-sources | where:"uses-start-date",false | sort_natural:"display-name"%}

      {% for source in sources-without-start-date %}
      {% assign source-doc = site.saas-integrations | where:"name",source.docs-name | first %}
      - [{{ source.display-name }}]({{ source-doc.url | prepend: site.baseurl }})
      {% endfor %}
      {% endcapture %}

      {{ saas | markdownify | flatify }}
      </td>
      <td>
      {% capture database %}
      The following database integrations:

      {% assign database-sources = site.developer-files | where:"source-type","database" %}
      {% assign databases-with-start-date = database-sources | where:"uses-start-date",true | sort_natural:"display-name"%}

      {% for source in databases-with-start-date %}
      {% assign source-doc = site.database-integrations | where:"name",source.docs-name | first %}
      - [{{ source.display-name }}]({{ source-doc.url | prepend: site.baseurl }})
      {% endfor %}
      {% endcapture %}

      {{ database | markdownify | flatify }}
      </td>
      </tr>
      </table>

  - title: "How historical Start Dates work"
    anchor: "how-start-dates-work"
    summary: "How historical Start Dates work"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "How Start Dates are used during Extraction"
        anchor: "start-date-usage"
        summary: "How Start Dates are used during Extraction"
        content: |
          When you connect an integration, Stitch will begin the process of replicating not only that integration’s recent data, but the historical data as well. During the setup of the integration, you can choose the start date by using Stitch's default starting date or defining your own custom date.

          The **Start Date** sets the initial [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) value for tables using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}). This tells Stitch how far back in time to query for historical data.

          When Stitch replicates a table using Key-based Incremental Replication and a **Start Date**, a few things will happen:

          1. During the initial replication job, Stitch uses the **Start Date** as the initial Replication Key value to query for historical data. All records with a Replication Key value **greater than or equal to`*`** the **Start Date** will be replicated.

             If this were a SQL query, it would look similar to this:

          {% capture code %}
          SELECT replication_key_column,
                 column_you_selected_1,
                 column_you_selected_2,
                 [...]
            FROM table
          WHERE replication_key_column >= 'start_date_value'
          {% endcapture %}

             {% include layout/code-snippet.html use-code-block=false %}

             ```sql
          {{ code | lstrip | rstrip }}
             ```

          {:start="2"}
          2. Stitch stores the new maximum value of the Replication Key column for the table.
          3. During the **next** replication job, Stitch compares the saved value from the previous job to Replication Key column values in the source.
          4. Any records in the table with a Replication Key **greater than or equal`*` to the stored value** are replicated.
          5. Stitch stores the new maximum value from the table's Replication Key column.
          6. Repeat.

          `*` Some integrations may not use Replication Keys inclusively. In this case, records with Replication Key values that are **greater than** the last saved value are extracted.

      - title: "Impact on Full Table Replication"
        anchor: "start-dates-full-table-replication"
        summary: "Impact on Full Table Replication"
        content: |
          Start Dates don't have any impact on historical data extraction in tables using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}). These tables  will replicate in full during every replication job, including historical jobs.

      - title: "Understanding default Start Dates"
        anchor: "understanding-default-start-dates"
        summary: "Understanding default Start Dates"
        content: |
          Stitch will use the integration's default starting date for historical replication unless you define a [custom Start Date](#define-a-custom-start-date).

          The majority of integrations have a default starting date of **-1 year** from the date the integration is created.

          For example: You create an integration on {{ "now" | date: '%B %d, %Y' }} and use the default **Start Date** of `-1 year`. The **Start Date** would be calculated as follows:

          {% assign start-date = 'now' | date: "%s" | minus: 31556926 | date: '%B %d, %Y' %}

          `{{ "now" | date: '%B %d, %Y' }} - 1 year = {{ start-date }}`

          When querying for historical data, Stitch will use **{{ start-date }}** as the initial Replication Key value. This means that in tables using Key-based Incremental Replication, records with a Replication Key value **greater than or equal to {{ start-date }}** will be replicated.

  - title: "Defining a custom Start Date for a new integration"
    anchor: "define-a-custom-start-date"
    summary: "How to define a custom Start Date for a new integration"
    content: |
      {% include layout/inline_image.html type="right" file="/replication/saas-historical-start-date-default.gif" alt="Selecting a custom start date in the Integration Settings page of the Stitch app" max-width="450px" %}

      1. In the integration's settings page, scroll to the **Sync Historical Data** section.
      2. Uncheck the **Uses integration default** box.
      3. In the **Start Date** dropdown that displays, use the calendar to select the desired start date.
      4. Continue the integration setup, clicking **Save Integration** when finished.

  - title: "Changing an integration's defined Start Date"
    anchor: "change-integrations-start-date"
    summary: "How to change an integration's defined Start Date"
    content: |
      While you can change the **Start Date** after the integration has been created, doing so will:

      1. Clear all saved Replication Key values, and 
      2. Queue a full re-replication of all selected tables in the integration, including those using Full Table Replication

      This will essentially reset the entire integration and can be used to replicate additional historical data or troubleshoot data discrepanciees.

      Changing an integration's **Start Date** can impact your row usage and downstream reporting. Refer to the [Resetting Replication Keys guide]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) for more info and instructions.
---
{% include misc/data-files.html %}