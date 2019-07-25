---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Basic Concepts and System Overview
permalink: /getting-started/basic-concepts-system-overview
keywords: getting started, get started, get set up, set up stitch, setup, guide

summary: "The basic concepts and architecture of Stitch, including an overview of replication and the Stitch system."

layout: general
sidebar: on-page
toc: true

level: "guide"
key: "basic-concepts"
weight: 1


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Set up your Stitch data pipeline"
    link: "{{ link.getting-started.onboarding | prepend: site.baseurl }}"

  - title: "Understand your Stitch row usage"
    link: "{{ link.getting-started.row-usage | prepend: site.baseurl }}"

  - title: "Stitch feature overview"
    link: "{{ link.getting-started.feature-overview | prepend: site.baseurl }}"

  - title: "All Getting Started guides"
    link: "{{ link.getting-started.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Welcome to Stitch! 

  Stitch is a cloud-first, open source platform for rapidly moving data. A simple, powerful ETL service, Stitch connects to all your data sources -- from databases like MySQL and MongoDB, to SaaS applications like Salesforce and Zendesk -- and replicates that data to a destination of your choosing.

  In this guide, we'll cover the basic concepts and architecture of Stitch, including:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Basics"
    anchor: "basics"
    summary: "What Stitch does, how to get set up, and how usage is calculated"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What is Stitch?"
        anchor: "what-is-stitch"
        summary: "What does Stitch do?"
        content: |
          Stitch a cloud-based, ETL data pipeline. ETL is short for extract, transform, load, which is a process that replicates data from multiple data sources and loads it into a central repository, or destination.

          That being said, keep in mind that Stitch isn't:

          - **A data analysis service**. We have many [analytics partners]({{ site.partners }}){:target="new"} who can help here, however.
          - **A data visualization or querying tool.** Stitch only replicates data. To analyze it, you'll need an additional tool. Refer to our list of [analysis tools]({{ site.baseurl | append: "/analysis-tools" }}) for some suggestions.
          - **A data warehouse**. A data warehouse, or destination, is required to use Stitch. While we can't create one for you, you can use our [Choosing a destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) if you need some help picking the right destination for your needs.

      - title: "Get set up"
        anchor: "concepts--getting-set-up"
        summary: "Getting set up with Stitch"
        content: |
          In just a few minutes, you can set up your own data pipeline:

          1. **Sign up for a Stitch account**. Don't have an account yet? [Sign up here for your free trial]({{ site.sign-in }}){:target="new"}.
          2. **Connect a destination**. A destination is a database or warehouse where Stitch will load the replicated data, like Amazon Redshift or Google BigQuery.
          3. **Connect an integration**. Integrations are data sources, or where Stitch replicates data from. This includes SaaS applications like Google Analytics, databases like MySQL, and more.

          For a step-by-step look at setting up Stitch, refer to the [Setting up your Stitch data pipeline guide]({{ link.getting-started-onboarding | prepend: site.baseurl }}).

      - title: "Integrations and destinations"
        anchor: "concepts--integrations-destinations"
        summary: "What integrations and destinations are"
        content: |
          To use Stitch, you need a destination and at least one integration, or data source.

        sub-subsections:
          - title: "Destinations"
            anchor: "concepts--destinations"
            content: |
              Stitch offers some of the most popular data lakes, warehouses, and storage platforms as destinations, such as Amazon Redshift, Google BigQuery, and Microsoft Azure SQL Data Warehouse.

              The destination you choose determines how replicated data is loaded and structured. This is discussed in more detail in the [Transformations](#transformations) section.

              Refer to the [Destination]({{ site.baseurl }}/destinations) documentation for more info on each of Stitch's destination offerings. If you're new to data warehousing or you want to see how Stitch's destination offerings compare to each other, check out our [Choosing a Destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}). This guide will help you choose the best Stitch destination for your data warehousing needs, from ensuring your data sources are compatible to staying within your budget.

          - title: "Integrations"
            anchor: "concepts--integrations"
            content: |
              An integration is a data source. This can be a database, API, or other data application that Stitch replicates data from, such as Google Analytics or MySQL.

              During your free trial, you'll have access to all of Stitch's integrations. After the trial ends, some integrations - such as MongoDB or Salesforce - are only available if you select a paid plan.

              Refer to the [Integration]({{ site.baseurl }}/integrations) documentation for more info on each of Stitch's integrations, such as what data is available or what features are supported.

      - title: "Rows and Stitch usage"
        anchor: "concepts--rows-stitch-usage"
        summary: "How Stitch usage is calculated"
        content: |
          Stitch usage is volume-based. Much like the data part of a cell phone plan, each Stitch plan is allotted a certain number of replicated rows per month. 

          Your overall row usage can be affected by a variety of factors, including the destination you choose and number of integrations you have. For an in-depth walkthrough of how usage is calculated, the factors that affect it, and how you can reduce your usage, refer to the [Understanding and Reducing Your Usage guide]({{ link.getting-started.row-usage | prepend: site.baseurl }}).

      #     **Don't see an integration you need?** If Stitch doesn't have a native integration for one of your sources, don't worry - there are still options:

      #     - Use the [**Import API**]({{ link.integrations.import-api | prepend: site.baseurl }}) integration to push arbitrary data into your data warehouse. You can use the Import API to replicate data from CSV files, Google Sheets, and more.
      #     - Use the [**Stitch Incoming Webhooks**]({{ link.integrations.stitch-incoming-webhooks | prepend: site.baseurl }}) integration to pull event data from a webhook-based service. This generic integration can be used with dozens of services.
      #     - Check out (and contribute to) [**Singer**]({{ site.singer }}), our open-source, community-driven ETL platform. 
      #     - Use the **Suggest Integration** button on the Integrations page in the Stitch app. We're always looking to add new integrations to our offerings.

  - title: "Replication"
    anchor: "replication"
    summary: "An overview of data replication in Stitch"
    content: |
      Stitch's replication process consists of three distinct phases:

      1. **Extraction**: Stitch pulls data from your data sources and validates it using our Stitch's Import API.
      2. **Preparing**: Data is [lightly transformed](#transformations) to ensure compatibility with the destination. 
      3. **Loading**: Stitch loads the data into your destination.

      A single occurrence of these three phases is called a **replication job**. You can keep an eye on a replication job's progress on any [integration's **Summary** page]({{ link.replication.rep-progress | prepend: site.baseurl }}).

    subsections:
      - title: "Extraction settings"
        anchor: "replication--settings"
        content: |
          When you set up an integration in Stitch, you'll also need to define its replication settings. These settings control the Extraction phase of the replication process, including [how often Extraction occurs]({{ link.replication.rep-scheduling | prepend: site.baseurl }}), [what data should be extracted]({{ link.replication.syncing | prepend: site.baseurl }}), and [how data is extracted]({{ link.replication.rep-methods | prepend: site.baseurl }}).

      - title: "Time to data loaded"
        anchor: "replication-performance"
        content: |
          Because our process is performed in steps, it's important to note that Stitch replication isn't real-time. This means that there will be some time between data extracted and data loaded, which you can read more about in the [System architecture section](#system-architecture) of this guide.

          Additionally, the speed of Extraction and Loading is largely dependent on the resources available in your data sources and destination.

          > [TODO- do we have any recommendations for optimizing performance?]

      - title: "Deleted records"
        anchor: "replication--never-delete"
        content: |
          Stitch will never delete data from your destination, even if records have been hard deleted from the source. Refer to the [Deleted Record Handling guide]({{ link.replication.deleted-records | prepend: site.baseurl }}) for more info and examples.

  - title: "Transformations"
    anchor: "transformations"
    summary: "The data transformations Stitch performs"
    content: |
      Stitch's goal is to get data from your data sources to your destination [in a useful, raw format](https://www.stitchdata.com/blog/why-our-etl-tool-doesnt-do-transformations/){:target="new"}:

      > _Useful_ means with types and structures that make the data easy to work with, and _raw_ means staying as close to the original representation as possible.

      This doesn't mean that Stitch doesn't perform transformations during the replication process. Stitch just doesn't perform _arbitrary_ transformations - Stitch will perform only the transformations required to ensure the loaded data is useful and compatible with your destination. The transformations Stitch performs are dependent on the destination you choose. These can include:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

      Stitch's philosophy is that what you do with your data depends on your needs, and by keeping data close to its original form, Stitch enables you to manage and transform it as you see fit. While we don't support user-defined transformations inside of Stitch, you can take advantage of [Talend's transformation and data quality solutions](https://www.stitchdata.com/platform/datatransformation/){:target="new"} to design and integrate your own transformations.

    subsections:
      - title: "Data typing"
        anchor: "data-typing"
        example-data:
          - id: "1"
            boolean: "true"
            string: ""
          - id: "2"
            boolean: ""
            string: "yes"
          - id: "3"
            boolean: ""
            string: "no"
        content: |
          Stitch's data typing process consists of three steps which take place during replication:

          1. **Extraction**: Identify the data type in the source
          2. **Preparing**: Map the data type to a Stitch data type
          3. **Loading**: Convert the Stitch data type to a destination-compatible data type

          Stitch converts data types only where needed to ensure the data is accepted by your destination.

          With some exceptions, when a data type is changed in the source, Stitch will create an additional column in the destination to accommodate the new data type. This will look like the column has been "split". For example:

          {% assign column-headings = "id|has_magic__bo|has_magic__st" | split: "|" %}
          {% assign attributes = "id|boolean|string" | split: "|" %}

          <table class="attribute-list">
          <tr>
          {% for column-heading in column-headings %}
          <td>
          <strong>{{ column-heading }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for example in subsection.example-data %}
          <tr>
          {% for attribute in attributes %}
          <td>
          {{ example[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

          Stitch handles changed data types in this way to ensure previously loaded data is retained in its original format. We recommend using views to coerce data types when this occurs.

          Refer to the [Columns with mixed data types guide]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }}) for more info and examples.

      - title: "JSON structures"
        anchor: "json-structures"
        content: |
          The destination you're using determines how Stitch handles complex JSON structures such as arrays and objects.

          If your destination natively supports storing nested data, Stitch will store the data as a type appropriate for storing semi-structured data. You can then use the JSON functions supported by the destination to parse and analyze the data.

          If your destinaton doesn't natively support storing nested data, Stitch will "de-nest", or normalize, the data into relations. For JSON objects, attributes will be flattened into the table, while arrays will be unpacked into subtables. For more info and examples, refer to the [Nested JSON structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

      - title: "Object names"
        anchor: "object-names"
        content: |
          When you initially set up an integration, you'll define [the name of the schema in the destination]({{ link.destinations.storage.stitch-schema | prepend: site.baseurl | append: "#integration-schema-names" }}) where Stitch will load that integration's data.

          The names of the tables and columns you set to replicate, however, are automatically generated based on two factors:

          1. The name of the object in the source
          2. The object naming rules enforced by the destination

          During loading, Stitch will attempt to keep object names as close to the source as possible. Some transformations may occur to ensure that the object name conforms to the destination's naming rules.

          **Note**: Table and column names cannot be changed in Stitch.

      - title: "Timezones"
        anchor: "timezones"
        content: |
          Some of the destinations Stitch offers don't natively support timezones. To ensure accuracy and consistency, Stitch handles data with timezones in this manner:

          1. Extract the data from the source
          2. Convert the source data to UTC
          3. Load the data as UTC into your destination

          Depending on the destination you're using, the data may or may not be stored with the timezone information. This is dependent on whether the destination supports timezones.

          For more info, refer to the [loading reference]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for your destination.

          > TODO: confirm how we handle data that doesn't have timezone info in the source

  - title: "System architecture"
    anchor: "system-architecture"
    summary: "A step-by-step tour of the Stitch system, from data extracted to data loaded"
    content: |
      Now that you understand the basics of Stitch and how data replication works, let's take a look at the internal workings of the Stitch system.

      {% include layout/image.html type="inline" file="/system-architecture.jpg" enlarge=true %}

    subsections:
      - title: "Extraction"
        anchor: "system-architecture--extraction"
        content: |
          The first phase in the replication process is called **Extraction**. During this phase, data is extracted from an integration using the [replication settings you define](#replication--settings).

          The Extraction phase includes:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Step 1: The Singer-based replication engine"
            anchor: "system-architecture--singer-based-rep-engine"
            content: |
              For SaaS applications and databases, data is pulled on a schedule using the Singer-based replication engine that Stitch runs against data sources like APIs, databases, and flat files.

              During this step, two things happen:

              1. **A structure sync**. At the start of every extraction, Stitch will run what is called a structure sync. A structure sync detects the tables and columns available in the source, along with any changes to the structure of those tables and columns.

                 **Note**: New tables and columns detected during a structure sync will be available in Stitch after the current replication job ends. For the majority of integrations, new tables and columns won't be automatically set to replicate.
              2. **Data is extracted in JSON format.** Based on the schemas, tables, and columns set to replicate, Stitch extracts the data in JSON format and sends it to the Import API.

          - title: "Step 2: The Import API"
            anchor: "system-architecture--import-api"
            content: |
              The next step in the replication process is the Import API. 

              For data sent directly to Stitch through a webhook or Import API integration, this is the first step in the replication process. (**Note**: This is why webhook and Import API integrations don't have [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).)

              The [Import API]({{ link.import-api.getting-started | prepend: site.baseurl }}) is a [Clojure](https://clojure.org/){:target="new"} web service that accepts JSON and [Transit](https://github.com/cognitect/transit-format){:target="new"}, either in large batches or at a point in time. The Import API performs a validation check on the data before writing it to a central Apache Kafka queue.

              If the data fails validation or another critical error occurs, the extraction will fail and trigger an [in-app and email notification]({{ link.account.notification-settings | prepend: site.baseurl }}). The error can also be viewed in an integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) tab.

              ---

      - title: "Preparing"
        anchor: "system-architecture--preparing"
        content: |
          The second phase in the replication process is called **Preparing**. During this phase, the extracted data is replicated internally for redundancy, batched, and readied for loading.

          The Preparing phase includes:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Step 3: The Kafka queue"
            anchor: "system-architecture--kafka-queue"
            content: |
              Data sent from the Import API is immediately persisted to Kafka, using Amazon S3 as a fallback. The Kafka queue is used to ensure Stitch meets its most important service-level target: Don't lose data.

              During this step, Stitch replicates our Kafka cluster across three different data centers. Each data point in the extracted data must be written to two data centers before it's accepted. Should the write fail, Stitch will continue to try until it's successful.

              Data is stored encrypted, and deleted after no more than seven days.

          - title: "Step 4: The Streamery"
            anchor: "system-architecture--streamery"
            content: |
              Next, data is moved from Kafka into what is called the Streamery. A low-latency, multithreaded Clojure application, the Streamery's goal is to maximize throughput while guarding against data loss or data leaking between data sets.

              During this step, data is written to files on Amazon S3 in batches. Batches are separated by Stitch client, integration, and the tables the data is destined for.

              After reaching either a memory limit or an amount of time elapsed since the last batch, the Streamery cuts a batch.

          - title: "Step 5: The Spool"
            anchor: "system-architecture--spool"
            content: |
              After the Streamery writes batches to Amazon S3, those batches enter the Spool. The Spool is a queue of work waiting to be processed by a [Loader](#system-architecture--loaders). Data is stored in an encrypted Amazon S3 bucket by Stitch client, connection, and destination table and retained for no more than 30 days.

              ---

      - title: "Loading"
        anchor: "system-architecture--loading"
        content: |
          The last phase in the replication process is **Loading**. During this phase, the prepared data is transformed to be compatible with the destination, and then loaded.

          The Loading phase includes:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}
          
        sub-subsections:
          - title: "Step 6: The Loaders"
            anchor: "system-architecture--loaders"
            content: |
              A Loader reads data from the Streamery (Amazon S3) and performs the [transformations](#transformations) necessary - such as converting data into the appropriate data types or structure - before loading it into your destination. Disk is used as a temporary buffer, data is encrypted when written, and deleted immediately once loaded.

              If available, Stitch will attempt to use [verified SSL/TLS-based encryption]({{ link.security.encryption | prepend: site.baseurl | append: "#connections-ssl-default" }}). Otherwise, Stitch will use an SSH tunnel for encryption, [if one is configured for the destination]({{ link.security.encryption | prepend: site.baseurl | append: "#ssh-tunnel-connections" }}).

              If a critical error occurs, the load will fail and trigger an [in-app and email notification]({{ link.account.notification-settings | prepend: site.baseurl }}). The error can also be viewed in an integration's [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}) tab.

          - title: "Step 7: Your destination"
            anchor: "system-architecture--destination"
            content: |
              Data is finally loaded into your destination! At this point, you can use an [analysis tool]({{ site.baseurl }}/analysis-tools) to interact with your data.

  - title: "Next steps"
    anchor: "next-steps"
    summary: "Some next steps"
    content: |
      Now that you've mastered the basics, move onto:

      {% assign getting-started-guides = site.getting-started | where:"level","guide" | sort:"weight" %}

      {% for guide in getting-started-guides %}
      {% unless guide.url == page.url %}
      - [**{{ guide.title }}**]({{ guide.url | prepend: site.baseurl }}): {{ guide.summary }}
      {% endunless %}
      {% endfor %}

---