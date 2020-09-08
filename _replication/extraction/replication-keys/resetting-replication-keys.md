---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Resetting Replication Keys
permalink: /replication/extractions/replication-keys/resetting-replication-keys
keywords: replicate, replication, replication key, keys, stitch replicates data, rp
summary: "Replication Key resets clear saved Replication Key values for incremental tables and queue a full re-replication of data. Learn how resets work, what you should consider beforehand, and how to perform them."
layout: general

key: "reset-replication-keys"
content-type: "replication-keys, incremental-replication"
toc: true
weight: 7


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }} In this guide, we'll cover:

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
      Replication Keys can be reset for database and the majority of SaaS integrations, at either the table or integration level.

  - title: "How Replication Key resets work"
    anchor: "how-replication-resets-work"
    summary: "How Replication Key resets work"
    content: |
      Used to perform incremental replication (either [Key-based]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) or [Log-based]({{ link.replication.log-based-incremental | prepend: site.baseurl }})), [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) can be reset in two ways:

      - At the **integration** level, the reset will clear the Replication Key values and queue a full re-replication for all tables set to replicate.
      - At the **table** level, the reset will clear the Replication Key value and queue a full re-replication for that table only.

      When Replication Keys are reset, Stitch will:

      1. Clear the last saved Replication Key value for the table (if reset at the table level) or all incremental tables (if reset at the integration level)
      2. Queue a full re-replication of the affected data. **Note**: This step will vary depending on the integration type:

         - **Database integrations**: All records in the table or tables will be included in the re-replication
         - **SaaS integrations:** Records with Replication Key values **greater than or equal to** the **Start Date** defined for the integration will be included in the re-replication
         
      3. Delete or truncate the destination table. **Note**: This step will vary depending on the integration type:
         - **Database, NetSuite Suite Analytics, and Salesforce integrations**: The destination table will be deleted
         - **All other integrations**: The destination table will be truncated
      4. Load the fully re-replicated data into the destination

  - title: "Uses for resetting Replication Keys"
    anchor: "uses-for-resetting-replication-keys"
    summary: "Uses for resetting Replication Keys"
    content: |
      Now that you understand what the Replication Key reset process does, how might you use it in practice?

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Backfill existing records with new column data"
        anchor: "uses-for-resetting-replication-keys--backfill-columns"
        content: |
          If you've added a new source column and the Replication Key value hasn't increased for existing records, performing a reset will re-replicate the table in full and backfill the column where needed.

      - title: "Account for hard deletes or removed columns"
        anchor: "uses-for-resetting-replication-keys--hard-deletes"
        content: |
          While we strongly recommend using soft deletes whenever possible, Replication Key resets can be used to remove [hard-deleted records]({{ link.replication.deleted-records | prepend: site.baseurl }}) from your destination.

          **Note**: If resetting for this purpose, Stitch recommends **dropping the destination table(s) before performing the reset** and allowing it to be re-created. This will ensure that the hard deleted records are removed as expected.

      - title: "Troubleshoot data discrepancies"
        anchor: "uses-for-resetting-replication-keys--data-discrepancies"
        content: |
          **For SaaS integrations**, the integration's **Start Date** can sometimes be the root cause of missing data. If you're missing data from a specific timeframe, check if the records have Replication Key values that fall outside the **Start Date** for the integration.

          {% assign now = 'now' | date: "%s" %}

          For example: The default **Start Date** for most integrations is **1 year from the date the integration is created**. In this example, we'll assume it's a non-leap year, or **365 days**. 

          If created today (`{{ now | date: "%Y-%m-%d" }}`), records with Replication Key values **greater than or equal to** `{{ now | minus: 31622400 | date: "%Y-%m-%d" }}` would be selected for replication. Records with Replication Key values that are less than this date wouldn't be replicated.

          If this doesn't apply, check out the [Data discrepancy troubleshooting guide]({{ link.troubleshooting.discrepancy-guide | prepend: site.baseurl }}) for more data discrepancy troubleshooting tips.

  - title: "Considerations for resetting Replication Keys"
    anchor: "considerations"
    summary: "Things to think about before resetting your Replication Keys"
    content: |
      If you have any questions or concerns, reach out to support **before resetting Replication Keys**.

      1. **This process can't be reversed or interrupted once confirmed.**
      2. **Your row usage will increase.** The full re-replication triggered by a Replication Key reset will count towards your overall row usage.
      3. **Recent data may be re-replicated, which will count towards your row usage.** 
      4. **Data may be stale until the re-replication completes.** When a full re-replication is queued, replication begins with the oldest data and progresses towards the most recent. 
      5. **Data volume and the configuration of the source can impact how long the Extraction takes to complete.** Stitch is only able to extract data as fast as the source - whether database or API (SaaS) - allows. Contributing factors include, but aren't limited to the following:

         - **Overall volume of data to be replicated**, including the total number of records and columns set to replicate. In general, wider tables - that is, tables with many columns set to replicate - take longer to fully replicate.
         - **For database integrations**: 
            - Available database resources
         - **For SaaS integrations**:
            - Overall API design and speed
            - Available API quota
            - [Third-party downtime]({{ link.troubleshooting.third-party-downtime | prepend: site.baseurl }})
      6. **Your destination's available resources will impact how long Loading takes to complete.** Stitch is only able to load data as fast as the destination allows. If a small number of resources are available, loading time will likely increase.

  - title: "Resetting Replication Keys"
    anchor: "reset-replication-keys"
    summary: "How to reset Replication Keys"
    content: |
      {% include important.html type="single-line" content="**Resetting a table or integration's Replication Keys is an irreversible process once confirmed in Stitch.**" %}

      The process for resetting Replication Keys varies by integration type:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | replace:"Resetting d","D" | remove: "Resetting " |  remove:" and tables" | }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Resetting database integrations and tables"
        anchor: "reset-replication-keys--database-integrations"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Reset a database integration table"
            anchor: "reset-replication-keys--database-integrations--table-level"
            content: |
              {% capture reset-single-table %}
              To reset a single table:

              1. Click into the integration from the {{ app.page-names.dashboard }} page.
              2. Click the **Tables to Replicate** tab. 
              3. Navigate to and open the table you want to reset. 
              4. Click the **Table Settings** link, located near the top right corner of the page.
              5. Scroll down to the **Reset This Table** section.
              6. Click the **Reset Table** button.
              7. When prompted, click **OK** to confirm.
              {% endcapture %}

              {{ reset-single-table | flatify }}

          - title: "Reset an entire database integration"
            anchor: "reset-replication-keys--database-integrations--integration-level"
            content: |
              To reset the Replication Key values for all incrementally replicating tables and queue a full re-replication of the integration's data:

              1. Click into the integration from the {{ app.page-names.dashboard }} page.
              2. Click the {{ app.buttons.update-int-settings }} tab. 
              3. Scroll down to the **Reset This Integration** section.
              4. Click the **Reset This Integration** button.
              5. When prompted, click **OK** to confirm.

      - title: "Resetting SaaS integrations and tables"
        anchor: "reset-replication-keys--saas-integrations"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Reset a SaaS integration table"
            anchor: "reset-replication-keys--saas-integrations--table-level"
            content: |
              {% capture saas-support %}
              {% assign saas-with-table-level-resets = site.saas-integrations | where:"table-level-reset",true | sort:"display_name" %}
              {% assign integration-versions = site.data.taps.versions %}

              {% for integration in saas-with-table-level-resets %}
              {% assign this-version = integration-versions[integration.name]released-versions | where:"number",integration.this-version | first %}
              {% if this-version.status != "deprecated" or this-version.status != "sunset" %}

              - [{{ integration.display_name }} ({{ integration.this-version | prepend: "v" }})]({{ integration.url | prepend: site.baseurl }})
              {% endif %}
              {% endfor %}
              {% endcapture %}

              {% include note.html first-line="**Note**: Currently, only the following SaaS integrations support table-level Replication Key resets:" content=saas-support %}

              {{ reset-single-table | flatify }}

          - title: "Reset an entire SaaS integration"
            anchor: "reset-replication-keys--saas-integrations--integration-level"
            content: |
              Resetting a SaaS integration is accomplished by changing the **Start Date** defined in the {{ app.page-names.int-settings }} page.

              To reset the Replication Key values for all incrementally replicating tables and queue a full re-replication of the integration's data:

              1. Click into the integration from the {{ app.page-names.dashboard }} page.
              2. Click the {{ app.buttons.update-int-settings }} tab.
              3. Scroll to the **Sync Historical Data** section.
              4. In the **Start Date** section, click the **Change Date** link.
              5. Define the new starting date using the drop-down. 
              6. Next:
                 - If there's a **Reset Date** button, click it.
                 - Otherwise, click the **Update Settings** button.
              7. When prompted, click **OK** to confirm the change.
---