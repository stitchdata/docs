---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding and Reducing Your Row Usage
permalink: /getting-started/understanding-stitch-usage
redirect_from: /account-security/understanding-stitch-billing-replicated-rows
keywords: billing, bill info, payment history, tier, plan, charge, row usage, replicated row, replicated rows, usage, row count
layout: general

summary: "Learn the basics of Stitch billing, how to view and understand your usage, and keep your row count low."

toc: false

level: "guide"
key: "row-usage"
weight: 3


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Basic concepts and system overview"
    link: "{{ link.getting-started.basic-concepts | prepend: site.baseurl }}"

  - title: "Set up your Stitch data pipeline"
    link: "{{ link.getting-started.onboarding | prepend: site.baseurl }}"

  # - title: "Stitch feature overview"
  #   link: "{{ link.getting-started.feature-overview | prepend: site.baseurl }}"

  - title: "All Getting Started guides"
    link: "{{ link.getting-started.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  In this guide, we'll cover the basics of Stitch billing, how to check and understand your usage, and some tips for keeping your row count low.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Stitch billing basics"
    anchor: "billing-basics"
    summary: "The basics of Stitch billing"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "How does Stitch billing work?"
        anchor: "how-does-billing-work"
        content: |
          Much like the data part of a cell phone plan, each Stitch plan is allotted a certain number of replicated rows per month. For detailed info on pricing and what's included in each plan, refer to the [pricing page]({{ site.pricing }}){:target="new"} on our website.

      - title: "What's a replicated row?"
        anchor: "what-is-a-replicated-row"
        content: |
          {% include billing/replicated-row-definition.html %}

  - title: "Understand your usage"
    anchor: "understanding-your-usage"
    summary: "Understanding your row usage"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
      
    subsections:
      - title: "Source rows ≠ replicated rows"
        anchor: "source-rows-not-equal-to-replicated-rows"
        content: |
          When viewing the number of replicated rows in Stitch, you may be surprised by the totals. You may ask yourself:

          > "How did Stitch replicate this many rows? There aren't that many in my source or destination!"

          We understand that this can be confusing. **Keep in mind that row usage in Stitch is the total number of replicated rows.** This means that the number of rows in the source won't necessarily be equal to your row usage in Stitch.

          Because Stitch counts updated rows, copies of existing rows, and rows created from de-nesting towards your total usage, the total of replicated rows and the total number of rows in your data sources or destination may not be equal.

          Take the following example. As you can see in the second replication job, the total replicated rows reported by Stitch are cumulative, or the total rows replicated across all replication jobs. 

          {% include layout/image.html file="/getting-started/source-to-destination-replicated-rows.png" alt="Example demonstrating how source, Stitch-reported, and destination rows are not always equal." enlarge=true caption="Click to enlarge." %}

      - title: "Impacts on usage"
        anchor: "impacts-on-usage"
        content: |
          The number of rows Stitch replicates is directly impacted by:

          {% include replication/replicated-rows-calculation.html %}

      - title: "Usage examples"
        anchor: "usage-examples"
        example-one:
          description: |
            In this example, we'll look at how different replication frequencies can affect the total number of replicated rows.

            Below are the total number of replicated rows for a table with **100 rows** using **Full Table Replication**:

          attributes:
            - frequency: "30 minutes"
              daily-total: "4,800"
              billing-period-total: "144,000"

            - frequency: "1 hour"
              daily-total: "2,400"
              billing-period-total: "72,000"

            - frequency: "6 hours"
              daily-total: "400"
              billing-period-total: "12,000"

            - frequency: "12 hours"
              daily-total: "200"
              billing-period-total: "6,000"

            - frequency: "24 hours"
              daily-total: "100"
              billing-period-total: "3,000"

        example-two:
          description: |
            **Note**: This example is applicable only to destinations that don't natively support nested data, such as Amazon Redshift or PostgreSQL-based destinations.

            In this example, we'll look at how data structured using JSON arrays can affect the total number of replicated rows.

            For destinations that don't natively support storing nested data, Stitch will "de-nest", or normalize, complex JSON structures into relations. For JSON arrays, data is unpacked into subtables, where each sub-record is counted as a replicated row.
          attributes:
            - frequency: "30 minutes"
              daily-total: "192"
              billing-period-total: "5,760"

            - frequency: "1 hour"
              daily-total: "96"
              billing-period-total: "2,880"

            - frequency: "6 hours"
              daily-total: "16"
              billing-period-total: "480"

            - frequency: "12 hours"
              daily-total: "8"
              billing-period-total: "240"

            - frequency: "24 hours"
              daily-total: "4"
              billing-period-total: "120"
          data: |
            ```json
            {
               "id":1,
               "name":"Finn",
               "type":"human",
               "best_friends":[
                  {
                     "id":2,
                     "name":"Jake",
                     "type":"dog"
                  },
                  {
                     "id":3,
                     "name":"Bubblegum",
                     "type":"princess"
                  },
                  {
                     "id":4,
                     "name":"BMO",
                     "type":"robot"
                  }
               ]
            }
            ```
          destination:
            names:
              top-level: "people"
              subtable: "people__best_friends"

            descriptions:
              top-level: "The top-level table will contain a single record:"
              subtable: "The subtable will contain three records, one for each item in the `best_friends` array:"

            top-level:
              - id: "1"
                name: "Finn"
                type: "human"
            subtable:
              - _sdc_source_key_id: "1"
                _sdc_level_0_id: "0"
                id: "2"
                name: "Jake"
                type: "dog"

              - _sdc_source_key_id: "1"
                _sdc_level_0_id: "1"
                id: "3"
                name: "Bubblegum"
                type: "princess"

              - _sdc_source_key_id: "1"
                _sdc_level_0_id: "2"
                id: "4"
                name: "BMO"
                type: "robot"

        content: |
          Next, we'll look at some examples of how certain factors can affect row usage in Stitch.

          When looking at the examples, note the differences between the source rows and row totals reported in Stitch.

          <ul id="profileTabs" class="nav nav-tabs">
            <li class="active">
                <a href="#all-examples" data-toggle="tab">Examples</a>
            </li>
            <li>
                <a href="#example-one" data-toggle="tab">Replication Frequency</a>
            </li>
            <li>
                <a href="#example-two" data-toggle="tab">Data structure</a>
            </li>
          </ul>
          <div class="tab-content">
          <div role="tabpanel" class="tab-pane active" id="all-examples">
          {% capture example-tab-copy %}
          In each tab is an example of how certain factors can affect row usage in Stitch.

          For these examples, assume that:

          - The tables are using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}). This means the table is replicated in full during every replication job.
          - That Extraction has completed without issue for every scheduled replication job.
          {% endcapture %}

          {{ example-tab-copy | flatify | markdownify }}

          </div>

              <div role="tabpanel" class="tab-pane" id="example-one">
                {{ subsection.example-one.description | flatify | markdownify }}

                {% assign rows = "daily-total|billing-period-total" | split:"|" %}

                  <table class="attribute-list">
                    <tr>
                      <td>
                        <strong>Replication Frequency</strong>
                      </td>
                      {% for attribute in subsection.example-one.attributes %}
                        <td>
                          <strong>{{ attribute.frequency }}</strong>
                        </td>
                      {% endfor %}
                    </tr>

                    {% for row in rows %}
                      <tr>
                        <td>
                          <strong>{{ row | replace:"-"," " | capitalize }}</strong>
                        </td>
                        {% for attribute in subsection.example-one.attributes %}
                          <td>
                            {{ attribute[row] }}
                          </td>
                        {% endfor %}
                      </tr>
                    {% endfor %}
                  </table>

                <p>
                  As you can see, slightly reducing the Replication Frequency can greatly reduce the number of replicated rows overall.
                </p>
                <p>
                  While this example only demonstrates row usage for a single table, think about how row usage will increase when there are multiple tables like this one set to replicate.
                </p>
              </div>

              <div role="tabpanel" class="tab-pane" id="example-two">
                {{ subsection.example-two.description | flatify | markdownify }}

                <strong>Source record in JSON format</strong>

                <p>
                  When Stitch extracts data from a source, it's done by putting the data into JSON format. Below is a sample record from a table named <code>people</code>. Note the <code>best_friends</code> array:
                </p>

                {{ subsection.example-two.data | markdownify }}

                <p>
                  When Stitch loads this record into the destination, two tables will be created: <code>people</code> and <code>people__best_friends</code>. This is due to Stitch unpacking the JSON arrays.
                </p>

                {% assign tables = "top-level|subtable" | split:"|" %}

                {% for table in tables %}
                    <strong>{{ table | capitalize }}: 
                    <code>{{ subsection.example-two.destination.names[table] }}</code></strong>

                  {{ subsection.example-two.destination.descriptions[table] | markdownify }}

                  {% case table %}
                    {% when 'top-level' %}
                      {% assign columns = "id|name|type" | split:"|" %}
                    {% when 'subtable' %}
                      {% assign columns = "_sdc_source_key_id|_sdc_level_0_id|id|name|type" | split:"|" %}
                  {% endcase %}

                  <table class="attribute-list">
                    <tr>
                      {% for column in columns %}
                        <td>
                          <strong>{{ column }}</strong>
                        </td>
                      {% endfor %}
                    </tr>
                  {% for record in subsection.example-two.destination[table] %}
                    <tr>
                      {% for column in columns %}
                        <td>
                          {{ record[column] }}
                        </td>
                      {% endfor %}
                    </tr>
                  {% endfor %}
                  </table>
                {% endfor %}

                {% assign rows = "daily-total|billing-period-total" | split:"|" %}

                <strong>Row usage totals</strong>

                <p>
                  This example assumes the table is using <strong>Full Table Replication</strong>. Below are the total number of replicated rows for the <code>people</code> (one record) and <code>people__best_friends</code> (three records) tables:
                </p>

                  <table class="attribute-list">
                    <tr>
                      <td>
                      </td>
                      {% for attribute in subsection.example-two.attributes %}
                        <td>
                          <strong>{{ attribute.frequency }}</strong>
                        </td>
                      {% endfor %}
                    </tr>

                    {% for row in rows %}
                      <tr>
                        <td>
                          <strong>{{ row | replace:"-"," " | capitalize }}</strong>
                        </td>
                        {% for attribute in subsection.example-two.attributes %}
                          <td>
                            {{ attribute[row] }}
                          </td>
                        {% endfor %}
                      </tr>
                    {% endfor %}
                  </table>

                  <p>
                    This example demonstrates that while there is only one record in the source, the number of rows replicated and loaded through Stitch will be four due to de-nesting.
                  </p>

                  <p>
                    While the example totals may not appear to be significant, think about this as it might relate to real data. Tables can contain dozens or hundreds of records, which will exponentially increase overall row usage.
                  </p>
              </div>
          </div>


  - title: "Check your row usage"
    anchor: "check-your-usage"
    summary: "How to check your row usage in Stitch"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Row usage for all integrations"
        anchor: "row-usage-all-integrations"
        content: |
          On the {{ app.page-names.dashboard }} page, you can view the total number of replicated rows for all of your integrations for the current billing period:

          ![Row usage graph on the Stitch Dashboard page for all integrations]({{ site.baseurl }}/images/account-security/all-row-usage-dashboard.png)

      - title: "Row usage for an integration"
        anchor: "row-usage-for-an-integration"
        content: |
          To take a closer look at an individual integration's usage for the current billing period, click on the integration to open the {{ app.page-names.int-details }} page, and check out the **Rows Loaded Over Time** section:

          ![Rows loaded over time for an integration]({{ site.baseurl }}/images/account-security/integration-row-usage.png)

      - title: "Row usage reset date"
        anchor: "row-usage-reset-date"
        content: |
          The reset date - or the day your row count will reset to zero - can be found in the **Your Usage** section of your {{ app.page-names.billing }} page, accessed by clicking the {{ app.menu-paths.billing }}:

          ![Row usage reset date in the Your Usage section of the Stitch Billing page]({{ site.baseurl }}/images/account-security/billing-reset-date.png)

  - title: "Reduce your usage"
    anchor: "reducing-your-usage"
    summary: "Some tips for reducing your usage"
    content: |
      While you can change your plan at any time to accommodate your data volume needs, below are some tried-and-true tips for reducing your row usage and staying within your plan's row allotment:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Identify high usage integrations"
        anchor: "integrations-known-to-be-high-usage"
        row-hog-reasons:
          - name: "data-structure"
            flat-on-page: false
            problem-if: true
            summary: "Data contains many nested structures. This is applicable to row usage only when a destination doesn't natively support nested JSON structures."
            copy: |
              Data contains many [nested structures]({{ row-hog.url | prepend: site.baseurl | append:"#schema" }})

          - name: "data-volume"
            flat-on-page: false
            problem-if: true
            summary: "Source generates large amounts of data"
            copy: "High data volume"

          - name: "lots-of-full-table"
            flat-on-page: false
            problem-if: true
            summary: "Integration has a high number of tables using Full Table Replication"
            copy: |
              [High number of tables]({{ row-hog.url | prepend: site.baseurl | append:"#schema" }}) using Full Table Replication

          - name: "table-selection"
            problem-if: false
            summary: "Integration doesn't currently support table selection"
            copy: "No table selection"

          - name: "attribution-window"
            problem-if: true
            summary: |
              Integration uses an {{ site.data.tooltips.word-format | replace:"TOOLTIP",site.data.tooltips.attribution-window-replication | replace:"DISPLAY-WORD","attribution window" }} for extraction
            copy: |
              Integration uses an [attribution window of {{ attribution-days }}]({{ row-hog.url | prepend: site.baseurl | append:"#replication" }}) for extraction

        content: |
          For many of Stitch's integrations, row usage shouldn't be an issue. We attempt to use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) for SaaS integrations whenever possible.

          There are, however, times when high row usage may be unavoidable. For example:

          {% for reason in subsection.row-hog-reasons %}
          - {{ reason.summary | flatify }}
          {% endfor %}

          **Click below to display integrations known to be heavy row users, and the potential reasons for their increased usage.** If you're using any of these integrations, you can use the remaining tips in this section to keep your usage down.

          {% capture integration-table %}
          <p style="margin: 10px;">To find out more about your SaaS integrations' data structure and replication methods, we recommend checking out our extensive <a href="{{ site.baseurl }}/integrations/saas">SaaS integration docs</a>. Every SaaS integration has detailed info about the tables Stitch will replicate and the methods used to do so.</p>

          {% assign databases = site.database-integrations | where:"row-usage-hog",true %}
          {% assign saas = site.saas-integrations | where:"row-usage-hog",true %}

          {% assign all-row-hogs = databases | concat: saas | sort:"display_name" %}

          <div class="table-responsive">
          <table class="attribute-list table-hover" style="margin-top: 0px; margin-bottom: 0px;">
          <tr>
          <td class="attribute-name">
          <strong>Integration</strong>
          </td>
          <td>
          <strong>Reasons</strong>
          </td>
          </tr>
          {% for row-hog in all-row-hogs %}
          <tr>
          <td class="attribute-name">
          <strong>
          <a href="{{ row-hog.url | prepend: site.baseurl }}">{{ row-hog.display_name }}</a>
          </strong>
          </td>
          <td>
          <ul>
          {% for reason in subsection.row-hog-reasons %}
          {% if reason.flat-on-page == false %}
            {% assign reason-value = row-hog.row-usage-hog-reasons[reason.name] %}
          {% else %}
            {% if reason.name == "attribution-window" %}
              {% if row-hog.attribution-window contains "days" %}
                {% assign reason-value = true %}
                {% assign attribution-days = row-hog.attribution-window %}
              {% else %}
                {% assign reason-value = false %}
              {% endif %}
            {% else %}
              {% assign reason-value = row-hog[reason.name] %}
            {% endif %}
          {% endif %}

          {% if reason.problem-if == reason-value %}
          <li style="margin: 0px;">{{ reason.copy | flatify | markdownify }}</li>
          {% endif %}

          {% endfor %}
          </ul>
          </td>
          </tr>
          {% endfor %}
          </table>
          </div>
          {% endcapture %}

          {% include layout/expandable-heading.html no-body=true anchor="integrations-that-use-up-rows" title="Integrations with known high row usage" content=integration-table %}

      - title: "Reduce Replication Frequencies"
        anchor: "reduce-replication-frequency"
        content: |
          Generally, the more often an integration is scheduled to replicate, the higher the number of rows Stitch replicates for the inetgration.

          If you're able to get by without the freshest data, consider changing your integrations' [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}) to something less frequent. For example: Every hour or six hours.

          Keep in mind that the Replication Frequency setting applies to the **entire integration**, not individual tables. This is especially important if there are a lot of tables that use [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}) in the integration.

      - title: "Use an incremental Replication Method"
        anchor: "use-incremental-replication"
        content: |
          For integrations that support Replication Method configuration, we recommend using either [Key-based]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) or [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) whenever possible.

      

      - title: "De-select unnecessary data"
        anchor: "deselect-unnecessary-data"
        content: |
          **Note**: This is only applicable to the [integrations that support table and/or column selection]({{ link.replication.syncing | prepend: site.baseurl | append: "#table-column-selection-support" }}).

          To keep your row count down and your destination tidy, you can also de-select any tables or columns you don't need.

          For example: If a column contains nested data, additional sub-rows may be created to accommodate loading the data to certain destination types. This will increase the total row count, as [Stitch counts sub-rows towards usage](#billing-basics). If this column is no longer needed, you could de-select it and lower your usage.

      - title: "Pause integrations"
        anchor: "pause-integrations"
        content: |
          If all else fails, you can temporarily pause the integration to keep from going over your row limit.

          **Note**: Pausing an integration will only prevent the extraction of additional records. Loading will continue for records that have been extracted prior to the pause.

          For example: If there are records currently in **Preparing** when an integration is paused, Stitch will continue to load these records, complete the current replication job, and count them towards your usage.
---
{% include misc/data-files.html %}