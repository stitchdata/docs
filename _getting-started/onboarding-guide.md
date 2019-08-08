---
title: Setting Up Your Stitch Data Pipeline
doc-type: "tutorial"
permalink: /getting-started/set-up-stitch-data-pipeline
keywords: getting started, get started, get set up, set up stitch, setup, guide

summary: "Get your Stitch data pipeline up and running."

layout: tutorial
toc: false

level: "guide"
key: "onboarding"
weight: 2


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Basic concepts and system overview"
    link: "{{ link.getting-started.basic-concepts | prepend: site.baseurl }}"

  - title: "Understand your Stitch row usage"
    link: "{{ link.getting-started.row-usage | prepend: site.baseurl }}"

  # - title: "Stitch feature overview"
  #   link: "{{ link.getting-started.feature-overview | prepend: site.baseurl }}"

  - title: "All Getting Started guides"
    link: "{{ link.getting-started.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Welcome to Stitch!

  This guide will help you get your Stitch data pipeline up and running. In this guide, we'll cover:

  - [The requirements for using Stitch](#prerequisites)
  {% for step in page.steps %}
  - [{{ step.summary }}](#{{ step.anchor }})
  {% endfor %}
  - [What to do when you're all set up](#next-steps)

  {% capture more-help %}If you have any questions not covered in this guide, check out the [rest of our documentation]({{ site.baseurl }}/ ) or reach out to our support team.{% endcapture %}

  {{ more-help }}

  Let's get started.


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **A Stitch account**. Don't have an account yet? [Sign up for your free trial here]({{ site.sign-in }}){:target="new"} before proceeding.
  - item: |
      **A destination.** Typically a database or data warehouse, this is where Stitch will load data replicated from your data sources.
  - item: |
      **An integration**, like a database or SaaS application. 


# -------------------------- #
#         GUIDE STEPS        #
# -------------------------- #

steps:
  - title: "Choose and connect a destination"
    anchor: "choose-connect-a-destination"
    summary: "Choosing and connecting a destination"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %} 
    substeps:
      - title: "Choose a destination"
        anchor: "choose-a-destination"
        content: |
          If you already have a destination in mind, [skip to the next step](#connect-the-destination).

          The first step is to choose the destination you want to use with Stitch. As your destination determines how data is loaded and structured, we recommend familiarizing yourself with our destinations before replicating any data.

          Additionally, while Stitch currently allows one destination per account, you can change the type of destination you're using at any time.

          If you're new to data warehousing or you want to see how Stitch's destination offerings compare to each other, check out our [Choosing a Destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}). This guide will help you choose the best Stitch destination for your data warehousing needs, from ensuring your data sources are compatible to staying within your budget.

      - title: "Connect the destination"
        anchor: "connect-the-destination"
        content: |
          After you've chosen the destination you want to use, you can connect it to Stitch. The setup for some destinations requires technical expertise, such as familiarity with running SQL commands or using the command line. If you're unsure about how to proceed, we recommend looping in a member of your technical team before proceeding.

          For setup requirements and instructions, refer to our destination setup guides:

          {% assign destinations = site.destinations | where:"destination",true | sort:"title" %}

          {% for destination in destinations %}
          - [{{ destination.title | remove:" Destination" }}]({{ destination.url | prepend: site.baseurl | append:"#stitch-details-setup-info" }})
          {% endfor %}

  - title: "Connect an integration"
    anchor: "connect-an-integration"
    summary: "Connecting an integration"
    content: |
      After you've set up a destination, you can start connecting your integrations.

      An integration is what we call a data source. Using Stitch's native integrations, you can replicate data from [databases]({{ site.baseurl }}/integrations/databases/), [SaaS applications]({{ site.baseurl }}/integrations/saas/), and [webhooks]({{ site.baseurl }}/integrations/webhooks/) into your destination.

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

      **Don't see a data source you want?** Don't worry - there are options! Check out the [Connecting other data sources guide]({{ link.integrations.other-data-sources | prepend: site.baseurl }}) for more info.

    substeps:
      - title: "Verify integration setup requirements"
        anchor: "verify-integration-setup-requirements"
        examples:
          - integration: "any-database"
            requirements:
              - item: "A database using a version supported by Stitch"
              - item: "Privileges that allow you to create a database user for Stitch"
              - item: "Privileges that allow you to grant privileges to database users"
              - item: |
                  [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#connect-settings" }}), depending on the database server's connectivity settings

          - integration: "google-analytics"
            anchor: "prerequisites"
            requirements:
              - item: "Read & Analyze permissions"
              - item: "Recent data in the account"

          - integration: "salesforce"
            anchor: "setup-requirements"
            requirements:
              - item: "A paid Stitch account (after free trial ends)"
              - item: "Web Service API access in Salesforce"
              - item: |
                  [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#whitelist-stitch-ips" }}), depending on the account's setup
              - item: "Access to the objects you want to replicate"

          - integration: "netsuite"
            anchor: "setup-requirements"
            requirements:
              - item: "A paid Stitch account (after free trial ends)"
              - item: "Administrator permissions in NetSuite"
              - item: |
                  [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#whitelist-stitch-ips" }}), depending on the account's setup
        content: |
          Before setting up a new integration, we recommend first checking the integration's documentation. This way, you can be sure you have everything you need to successfully complete the setup.

          Some integrations have requirements that must be met before you can connect it to Stitch. If you attempt to connect the integration without first completing the requirements, you'll run into issues either with the connection or replication.

          For example: The following table lists some of our most popular integrations and their setup requirements:

          <table class="attribute-list table-hover">
          <tr>
          <td class="attribute-name">
          <strong>
          Integration
          </strong>
          </td>
          <td>
          <strong>Setup requirements</strong>
          </td>
          </tr>
          {% assign databases = site.database-integrations | where:"name","any-database" %}
          {% assign saas = site.saas-integrations | where:"input",true %}
          {% assign integrations = databases | concat: saas %}

          {% for example in substep.examples %}
          {% for integration in integrations %}
          {% if example.integration == integration.name %}
          <tr>
          <td class="attribute-name">
          <strong>
          <a href="{{ integration.url | prepend: site.baseurl | append: "#" | append: example.anchor }}">{{ integration.display_name | replace:"Any database","Most databases" }}</a>
          </strong>
          </td>
          <td>
          <ul>
          {% for requirement in example.requirements %}
          <li style="margin: 0px;">{{ requirement.item | flatify | markdownify }}</li>
          {% endfor %}
          </ul>
          </td>
          </tr>
          
          {% endif %}
          {% endfor %}
          {% endfor %}
          </table>

          For the setup requirements and instructions for all of Stitch's integrations, refer to our [library of integration documentation]({{ site.baseurl }}/integrations).

      - title: "Connect the integration"
        anchor: "connect-the-integration"
        content: |
          After you've verified that you meet the integration's setup requirements, you can connect it to Stitch.

          **Note**: The setup for some integrations - usually databases - requires technical expertise, such as familiarity with running SQL commands or using the command line. If you're unsure about how to proceed, we recommend looping in a member of your technical team before proceeding.

          Use the [setup guide for your integration]({{ site.baseurl }}/integrations) to complete the setup.

  - title: "Define replication settings"
    anchor: "define-replication-settings"
    summary: "Configuring replication"
    content: |
      {% assign all-extraction-docs = site.replication | where:"method",true %}

      The next steps will vary depending on the type of integration you connect. If you set up an Import API or [webhook]({{ site.baseurl }}/integrations/webhooks) integration, you're all done! These are considered "push" integrations, meaning that data is automatically pushed to Stitch from the data source.

      For all other integrations, data is "pulled" from the source. An integration's replication settings define how, when, and what data is pulled from a source. 

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Understand the replication process"
        anchor: "familiarize-replication-process"
        content: |
          Before we walk you through how to define replication, you should familiarize yourself with Stitch's replication process. This will ensure settings are defined appropriately and replication is efficient.

          Check out the [Replication section]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append:"#replication" }}) in the [Basic concepts and system overview guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl }}) for a quick overview.

      - title: "Create the replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% assign extraction-scheduling-docs = all-extraction-docs | where:"content-type","replication-scheduling" | sort:"title" %}

          When you initially set up an integration, you'll be asked to create a replication schedule. Replication schedules affect the time that replication jobs begin and how often they occur. Specifically, replication scheduling controls the frequency and start time of the Extraction phase of the replication process, which is when Stitch extracts data from the data source.

          Refer to the [Replication Scheduling guide]({{ link.replication.rep-scheduling | prepend: site.baseurl }}) for more info about replication scheduling and the scheduling methods Stitch currently offers.

          After you've selected the replication scheduling method you want to use, use the appropriate settings in the **{{ app.page-names.int-settings }}** page to create the schedule.

      - title: "Set data to replicate"
        anchor: "set-tables-columns-to-replicate"
        selection-scenarios:
          - table-selection: true
            column-selection: true
            result: "Only selected tables and columns are replicated"

          - table-selection: true
            column-selection: false
            result: "All available columns in selected tables are automatically selected for replication"

          - table-selection: false
            column-selection: false
            result: "All available tables and columns are automatically selected for replication"
        content: |
          {% include misc/icons.html %}

          Next, you'll tell Stitch what data you want to replicate from the integration. This is called [**table and column selection**]({{ link.replication.syncing | prepend: site.baseurl }}).

          The majority of Stitch's integrations offer some level of data selection, but there are some that don't. The level of data selection support determines not only the data you can choose to replicate, but how Stitch behaves when data selection isn't fully supported.

          The following table outlines how Stitch will behave for each level of data selection support:

          {% assign table-fields = "table-selection|column-selection|result" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for field in table-fields %}
          <td>
          <strong>{{ field | replace:"-"," " | capitalize }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for scenario in substep.selection-scenarios %}
          <tr>
          {% for field in table-fields %}
          {% case scenario[field] %}
          {% when true %}
          <td width="20%; fixed">
          {{ supported }}
          {% when false %}
          <td width="20%; fixed">
          {{ not-supported }}
          {% else %}
          <td>
          {{ scenario[field] }}
          {% endcase %}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

          For SaaS integrations, you can see what data is available through Stitch in each [integration's Schema documentation]({{ site.baseurl }}/integrations/saas).

          If selecting tables and columns is required to finish setting up an integration, Stitch will direct you to do so after the connection has been saved. Additionally, the integration's status will be **Not Configured** in the dashboard until this has been completed:

          ![An AppsFlyer integration with a Not Configured status on the Stitch Dashboard page.]({{ site.baseurl }}/images/getting-started/integration-not-configured.png)

      - title: "Define table Replication Methods"
        anchor: "define-table-replication-methods"
        content: |
          All tables you set to replicate must have a Replication Method associated with them. A table's Replication Method tells Stitch how data from the table should be extracted.

          {% for sub-substep in substep.sub-substeps %}
          - [Step 3.4.{{ forloop.index }}: {{ sub-substep.title }}](#{{ sub-substep.anchor }})
          {% endfor %}

        sub-substeps:
          - title: "Understand Stitch's Replication Methods"
            anchor: "understand-replication-methods"
            content: |
              The Replication Method setting is the single most important replication setting in Stitch for your data. It determines not only how records from a table are replicated, but **what** records are replicated.

              **Incorrectly defining this setting can lead to data discrepancies, latency, and increased row usage**. For this reason, we recommend reading the [Replication Method guide]({{ link.replication.rep-methods | prepend: site.baseurl }}) before defining methods for your tables.

          - title: "Choose a Replication Method"
            anchor: "choose-a-replication-method"
            content: |
              Now that you understand how Replication Methods work, you can choose one for your table. Replication Methods are defined on a table-by-table basis. 

              Stitch offers the following Replication Methods:

              {% for replication-method in site.data.taps.extraction.replication-methods.all %}
              - [**{{ site.data.taps.extraction.replication-methods[replication-method.id]display-name }}**]({{ site.data.taps.extraction.replication-methods[replication-method.id]documentation | flatify }}): {{ site.data.taps.extraction.replication-methods[replication-method.id]description | flatify }}
              {% endfor %}

              Keep in mind that the Replication Method that works for one table may not be suitable for another. If you're not sure which method to choose, refer to the [comparison table in the Replication Method guide]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#compare-replication-methods" }}).

          - title: "Set the table's Replication Method"
            anchor: "set-table-replication-method"
            content: |
              After you set a table to replicate, the **{{ app.page-names.table-settings }}** page will display. On this page, select the Replication Method you want to use, a Replication Key (if applicable), and click {{ app.buttons.save-table-settings }}.

  - title: "Monitor replication jobs"
    anchor: "monitor-replication-process"
    summary: "Monitoring replication progress"
    content: |
      After you fully configure an integration, the integration might have a **Pending** status in the **Last Sync Completed** field on the {{ app.page-names.dashboard }} page:

      ![Newly connected integration with Pending Sync status.]({{ site.baseurl }}/images/getting-started/new-pending-integration.png)

      A **Pending** status indicates that Stitch is in the process of scheduling a replication job for the integration. When the status changes to **In Progress**, it means that the replication job has started. To kick off a job sooner, you can use the [Force Extraction feature]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) in the integration's **Extractions** tab. 

      In this case, the job will replicate all historical data for the integration. Historical jobs tend to be larger in volume compared to subsequent jobs, and as a result may take longer to process and load into your destination. It's normal to see a large spike in replicated rows during this time, but you can expect your row usage to decrease and eventually level out.

      To keep an eye on where Stitch is in the replication process, you can use the integration's replication stats, Extraction Logs, and Loading Reports.

    substeps:
      - title: "Integration replication stats"
        anchor: "integration-replication-stats"
        no-number: true
        content: |
          Click on the integration from the {{ app.page-names.dashboard }} to open the **{{ app.page-names.int-details }}** page:

          {% include layout/image.html file="/replication/replication-stats.png" caption="Integration replication stats. These stats are not real-time and will update every few minutes. You'll need to refresh the page if you're eager to watch your data move through Stitch." alt="Integration Extracted, Preparing, and Loading replication stats." %}

          To learn more about how info is displayed in these fields, check out the [Monitoring Replication Progress guide]({{ link.replication.rep-progress | prepend: site.baseurl }}).

      - title: "Extraction Logs"
        anchor: "extraction-logs"
        no-number: true
        content: |
          [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) detail the **Extract** phase of Stitch's replication process. In the logs, you can see how data is queried and extracted, along with any errors that may occur.

          Click the **Extractions** tab in the integration to open its Extraction Logs.

      - title: "Loading Reports"
        anchor: "loading-reports"
        no-number: true
        content: |
          [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}) detail the **Loading** phase of Stitch's replication process. In the reports, you can see the status of loads for individual tables, the number of rows loaded for the table, and any errors that occurred during the load.
          
          Click the **Loads** tab in the integration to open its Loading Reports.

  - title: "Check out your data"
    anchor: "check-out-your-data"
    summary: "Checking out your Stitch-replicated data"
    content: |
      Now that Stitch has loaded your data, it's time to check it out! 

      To analyze or interact with the data Stitch replicates, you'll need an additional tool. Check out our [list of analysis tools]({{ site.baseurl }}/analysis-tools/) to find the visualization, analysis, or data science tool that's right for you.

      {% include tip.html type="single-line" content="If an integration's stats or Loading Reports indicate that data was loaded but you don't see any, make sure you're **directly querying your destination with a SQL client**. Some analysis tools, such as Mode or Tableau, have refresh lags on their reports. This means that even if data is in the destination, it may not immediately show up in the app you're using." %}

      ---

next-steps: |
  Congratulations! You set up a destination, connected an integration, and configured replication settings. You're on your way to moving your data.

  So, what's next? Here's what we recommend:

  - **Get a handle on the basic concepts of Stitch**, if you haven't already. [This guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl }}) will provide you with the foundational knowledge you need to have the best experience with Stitch and set you up for success.
  - **Get to know your destination**. Every destination handles data differently, which will impact how Stitch loads and stores the data it replicates from your integrations. [Check out the Destination Data Loading guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for the specifics on your destination.
  - **Get to know your SaaS integrations**, if you plan on connecting any. Just like destinations, every SaaS integration structures its data differently. How Stitch replicates and loads SaaS data depends in part on how that data is created and structured. [Our extensive SaaS integration docs]({{ site.baseurl }}/integrations/saas/) cover what Stitch will replicate and how.
  - **Invite your team.** [Loop in your colleagues]({{ link.account.team-members | prepend: site.baseurl }}) to set up integrations and get the data flowing.

  {{ more-help }}
---
{% include misc/data-files.html %}