---
title: Setting Up Your Stitch Data Pipeline
doc-type: "tutorial"
permalink: /getting-started/set-up-stitch-data-pipeline
keywords: getting started, get started, get set up, set up stitch, setup, guide

summary: "Get your Stitch data pipeline up and running."

layout: tutorial
toc: true

level: "guide"
key: "onboarding"
weight: 2


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Welcome to Stitch!

  This guide will help you get your Stitch data pipeline up and running. In this guide, you'll learn how to:

  - Connect a data warehouse (we call them **destinations**)
  - Connect an integration
  - Configure & monitor replication
  - Find additional resources and support

  In this guide, we'll walk you through setting up Stitch by demonstrating how to connect a **MySQL** database integration and replicate data from it to a **Panoply** destination.

  {% capture more-help %}If you have any questions not covered in this guide, check out the [rest of our documentation]({{ site.baseurl }}/ ) or reach out to our support team.{% endcapture %}

  {{ more-help }}

  Let's get started.

  A simple, powerful ETL service, Stitch connects to all your data sources -- from databases like MySQL and MongoDB, to SaaS tools like Salesforce and Zendesk -- and replicates that data to a data warehouse of your choosing. 

  With Stitch, developers can provision data to analysts and team members in minutes, not weeks. Stitch takes care of source management so your developers and analysts can get back to what they do best.


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **A Stitch account**. Don't have an account yet? [Sign up for your free trial here]({{ site.sign-in }}){:target="new"} before proceeding.
  - item: |
      **A destination.** 
  - item: |
      **An integration.**


# -------------------------- #
#         GUIDE STEPS        #
# -------------------------- #

steps:
  - title: "Choose and connect a destination"
    anchor: "choose-connect-a-destination"
    summary: "How to choose and connect a destination"
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
          - integration: "google-analytics"
            anchor: "prerequisites"
            requirements: |
              - Read & Analyze permissions
              - Recent data in the account

          - integration: "salesforce"
            anchor: "setup-requirements"
            requirements: |
              - A paid Stitch account (after free trial ends)
              - Web Service API access in Salesforce
              - [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#whitelist-stitch-ips" }}), depending on the account's setup
              - Access to the objects you want to replicate

          # - integration: "amazon-s3-csv"
          #   anchor: "setup-requirements"
          #   requirements: |
          #     - Privileges in Amazon Web Services (AWS) Identity Access Management (IAM) that allow you to create policies, roles, and attach policies to roles 
          #     - CSV files that contain a header row

          - integration: "netsuite"
            anchor: "setup-requirements"
            requirements: |
              - A paid Stitch account (after free trial ends)
              - Administrator permissions in NetSuite
              - [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#whitelist-stitch-ips" }}), depending on the account's setup
        content: |
          Before setting up a new integration, we recommend first checking the integration's documentation. This way, you can be sure you have everything you need to successfully complete the setup.

          Some integrations have requirements that must be met before you can connect it to Stitch. If you attempt to connect the integration without first completing the requirements, you'll run into issues either with the connection or replication.

          For example: The following table lists some of our most popular integrations and their setup requirements:

          <table class="attribute-list">
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
          <tr>
          <td class="attribute-name">
          <strong>
          <a href="{{ site.baseurl }}/integrations/databases">Most databases</a>
          </strong>
          </td>
          <td>
          {% capture database-setup %}
          - A database using a version supported by Stitch
          - Privileges that allow you to create a database user for Stitch
          - Privileges that allow you to grant privileges to database users
          - [Whitelisting Stitch's IP addresses]({{ integration.url | prepend: site.baseurl | append: "#connect-settings" }}), depending on the database server's connectivity settings
          {% endcapture %}

          {{ database-setup | flatify | markdownify }}
          </td>
          </tr>
          {% assign integrations = site.documents | where:"input",true %}

          {% for example in substep.examples %}
          {% for integration in integrations %}
          {% if example.integration == integration.name %}
          <tr>
          <td class="attribute-name">
          <strong>
          <a href="{{ integration.url | prepend: site.baseurl | append: "#" | append: example.anchor }}">{{ integration.display_name }}</a>
          </strong>
          </td>
          <td>
          {{ example.requirements | flatify | markdownify }}
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
    content: |
      {% assign all-extraction-docs = site.replication | where:"method",true %}

      The next steps will vary depending on the type of integration you connect. If you set up an Import API or [webhook]({{ site.baseurl }}/integrations/webhooks) integration, you're all done! These are considered "push" integrations, meaning that data is pushed to Stitch from the data source.

      For all other integrations, data is "pulled" from the source. An integration's replication settings define how, when, and what data is pulled from a source. 

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Understand the replication process"
        anchor: "familiarize-replication-process"
        content: |
          Before we walk you through how to define replication, you should familiarize yourself with Stitch's replication process. 

          [TODO]

# The Stitch replication process consists of three steps: extracting, preparing, and loading.

# During the **Extract** part of the replication process, Stitch will use the replication settings to determine how often to replicate data, what tables and columns to replicate, and whether to replicate data incrementally or fully from the data source. We'll go into more detail about these settings in the next section.

# Once the data has been extracted, it moves into the **Preparing** phase of the replication process. During this phase, Stitch will perform light transformations such as [de-nesting JSON]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) (if applicable to your destination), [column splitting for fields with multiple data types]({{ link.destinations.storage.structure-changes | prepend: site.baseurl }}), and data typing for some integrations to ready the data for the data warehouse.

# The last step is **Loading**. Stitch completes the replication process by writing the replicated data to your data warehouse in batches.

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

          [IMAGE?]

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
    content: |
      After you fully configure an integration, the integration might have a **Pending** status in the **Last Sync Completed** field on the {{ app.page-names.dashboard }} page:

      ![Newly connected integration with Pending Sync status.]({{ site.baseurl }}/images/getting-started/new-pending-integration.png)

      A **Pending** status indicates that Stitch is in the process of scheduling a replication job for the integration. To kick off a job sooner, you can use the [Force Extraction feature]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) in the integration's **Extractions** tab.

      When the status changes to **In Progress**, it means that the inital replication job has started. During this job, Stitch will replicate the integration's historical data.

    substeps:
      - title: "Monitor the initial replication job"
        anchor: "monitor-initial-replication-job"
        content: |
          Historical jobs tend to be larger in volume compared to subsequent jobs, and as a result may take longer to process and load into your destination. It's normal to see a large spike in replicated rows during this time, but you can expect your row usage to decrease and eventually level out.

      - title: "Monitor ongoing replication jobs"
        anchor: "monitor-ongoing-replication-jobs"
        content: |
          After the historical job completes, the time it takes Stitch to complete subsequent jobs should decrease. To keep an eye on where Stitch is in the replication process, you can use the integration's replication stats.

          Click on the integration from the {{ app.page-names.dashboard }} to open the {{ app.page-names.int-details }} page:

          ![Integration Replication Stats]({{ site.baseurl }}/images/replication/replication-stats.png)

          **Note**: These stats are not real-time and will update every few minutes. You'll need to refresh the page if you're eager to watch your data move through Stitch.

          To learn more about how info is displayed in these fields, check out the [Monitoring Replication Progress guide]({{ link.replication.rep-progress | prepend: site.baseurl }}).

          ---

next-steps: |
  Congratulations! You set up a destination, connected an integration, and configured replication settings. You're on your way to consolidating your data.

  So, what's next? Here's what we recommend:

  - **Get a handle on the basic concepts of Stitch**, if you haven't already. [This guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl }}) will provide you with the foundational knowledge you need to have the best experience with Stitch and set you up for success.
  - **Get to know your destination**. Every destination handles data differently, which will impact how Stitch loads and stores the data it replicates from your integrations. [Check out the Destination Data Loading guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for the specifics on your destination.
  - **Get to know your SaaS integrations**, if you plan on connecting any. Just like destinations, every SaaS integration structures its data differently. How Stitch replicates and loads SaaS data depends in part on how that data is created and structured. [Our extensive SaaS integration docs]({{ site.baseurl }}/integrations/saas/) cover what Stitch will replicate and how.
  - **Invite your team.** [Loop in your colleagues]({{ link.account.team-members | prepend: site.baseurl }}) to set up integrations and get the data flowing.
  - **Connect your analysis tool to your Stitch destination**. If your end-goal is to analyze or interact with the data Stitch replicates, you'll need an additional tool. Check out our [list of analysis tools]({{ site.baseurl }}/analysis-tools/) to find the visualization, analysis, or data science tool that's right for you.
---
{% include misc/data-files.html %}