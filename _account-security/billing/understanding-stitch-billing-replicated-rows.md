---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding and Reducing Your Row Usage
permalink: /account-security/understanding-stitch-billing-replicated-rows
keywords: billing, bill info, payment history, tier, plan, charge, row usage, replicated row, replicated rows, usage, row count
layout: general

key: "understanding-row-usage"

summary: "Learn the basics of Stitch billing, how to view & understand your usage, and keep your row count low."

toc: true

type: "billing"
weight: 1


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Much like the data part of a cell phone plan, each Stitch plan is allotted a certain number of replicated rows per month. For detailed info on pricing and what's included in each plan, refer to the [pricing page]({{ site.pricing }}){:target="new"} on our website.

  In this guide, we'll cover the basics of Stitch billing, how to check and understand your usage, and some tips for keeping your row count low.


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Billing basics"
    anchor: "billing-basics"
    content: |
      {% include billing/replicated-row-definition.html %}

  - title: "Check your usage in Stitch"
    anchor: "viewing-rows-replicated-in-stitch"
    content: |
      {% include billing/view-usage.html %}

      The **reset date** - or the day your row count will reset to zero - can be found in the **Plan Details** section of your {{ app.page-names.billing }} page, accessed by clicking the {{ app.menu-paths.billing }}.

    subsections:
      - title: "Understand your usage"
        anchor: "understanding-your-usage"
        content: |
          When viewing the number of replicated rows in Stitch, you may be surprised by the totals. You may ask yourself: _"How did Stitch replicate this many rows? There aren't that many in my source or destination!"_

          Keep in mind that the total reported by Stitch is the number of **replicated** rows. The number of rows Stitch replicates is directly impacted by:

          {% include replication/replicated-rows-calculation.html %}

          Because Stitch counts updated rows, copies of existing rows, and rows created from de-nesting towards your total usage, the total of replicated rows and the total number of rows in your data sources or destination may not be equal.

  - title: "Reduce your usage"
    anchor: "reducing-your-usage"
    content: |
      While you can change your plan at any time to accommodate changing volume needs, below are some tried-and-true tips for reducing your row usage and staying within your plan's row allotment:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Reduce your integrations' Replication Frequency"
        anchor: "reduce-replication-frequency"
        content: |
          {{ site.data.tooltips.replication-frequency }} Generally, the more often an integration is scheduled to replicate, the higher the number of rows Stitch replicates for the inetgration.

          If you're able to get by without the freshest data, consider changing your integrations' [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}) to something less frequent. For example: Every hour or six hours.

          Keep in mind that the Replication Frequency setting applies to the **entire integration**, not individual tables. This is especially important if there are a lot of tables that use <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.full-table-rep }}">Full Table Replication</a> in the integration.

      - title: "Understand Stitch's Replication Methods"
        anchor: "check-table-replication-methods"
        content: |
          Stitch uses one of three [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) to replicate data from your data sources. To keep your row usage down, Stitch recommends familiarizing yourself with each of these methods before selecting tables for replication. This will ensure you set Stitch up to accurately and efficiently replicate your data.

          - [**Key-based Incremental Replication**]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) - {{ site.data.tooltips.key-based-incremental-rep }}
          - [**Log-based Incremental Replication**]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) - {{ site.data.tooltips.log-based-incremental-rep }}
          - [**Full Table Replication**]({{ link.replication.full-table | prepend: site.baseurl }}) - {{ site.data.tooltips.full-table-rep }}

          For integrations that allow you to configure Replication Methods for selected tables, Stitch recommends using an incremental method whenever possible. This can significantly reduce the amount of redundant data that's replicated by Stitch.

      - title: "Get to know your SaaS integrations"
        anchor: "get-to-know-saas-integrations"
        content: |
          While we try to use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) for SaaS integrations whenever possible, replicating high numbers of rows is sometimes unavoidable. This can be because:

          - **The integration generates massive amounts of data.** Mixpanel, for example, typically contains large amounts of data.
          - **Some tables require Full Table Replication or querying for a time range** (attribution window) during each replication job to ensure accuracy. 
          - **The integration contains nested data structures.** If you're using a destination that doesn't natively support nested structures, Stitch will de-nest these structures and create sub-rows which will result in a higher number of replicated rows.

             For an in-depth walkthrough of how JSON arrays are deconstructed in Stitch, as well as what arrays are in the first place, check out the [Handling of Nested Data Structures & Row Count Impact]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) guide.

          To find out more about your SaaS integrations' data structure and replication methods, we recommend checking out our extensive [SaaS integration docs]({{ site.baseurl }}/integrations/saas). Every SaaS integration has detailed info about the tables Stitch will replicate and the methods used to do so.

      - title: "De-select unnecessary data"
        anchor: "deselect-unnecessary-data"
        content: |
          To keep your row count down and your destination tidy, you can also de-select any tables or columns you don't need.

          For example: If a column contains nested data, additional sub-rows may be created to accommodate loading the data to certain destination types. This will increase the total row count, as [Stitch counts sub-rows towards usage](#billing-basics). If this column is no longer needed, you could de-select it and lower your usage.

          **Note**: This is only applicable to the [integrations that support table and/or column selection]({{ link.replication.syncing | prepend: site.baseurl | append: "#table-column-selection-support" }}).

      - title: "Pause integrations"
        anchor: "pause-integrations"
        content: |
          If all else fails, you can temporarily pause the integration to keep from going over your row limit.

          **Note**: Pausing an integration will only prevent the extraction of additional records. Loading will continue for records that have been extracted prior to the pause.

          For example: If there are records currently in **Preparing** when an integration is paused, Stitch will continue to load these records, complete the current replication job, and count them towards your usage.
---
{% include misc/data-files.html %}