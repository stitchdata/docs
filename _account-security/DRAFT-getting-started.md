---
title: Getting Started with Stitch
permalink: /getting-started/draft
keywords: getting started, get started, get set up, set up stitch, setup, guide

summary: "In just minutes, you can get your Stitch data pipeline up and running. Here's everything you need to know to get started."

layout: general
sidebar: on-page
toc: true

level: "category"
icon: "clock"
display-title: "Get started with Stitch"
display-summary: "Get your Stitch data pipeline up and running."

key: "getting-started"
type: "getting-started"
weight: 1

intro: |
  {% include misc/data-files.html %}

  A simple, powerful ETL service, Stitch connects to all your data sources -- from databases like MySQL and MongoDB, to SaaS tools like Salesforce and Zendesk -- and replicates that data to a destination of your choosing. 

  With Stitch, developers can provision data to analysts and team members in minutes, not weeks. Stitch takes care of source management so your developers and analysts can get back to what they do best.

sections:
  - title: "Basics"
    anchor: "basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Use cases"
        anchor: "uses-for-stitch"
        summary: "What Stitch can be used for"
        content: |
          - todo

          That being said, keep in mind that Stitch isn't:

          - **A data analysis service**. We have many [analytics partners]({{ site.partners }}){:target="new"} who can help here, however.
          - **A data visualization or querying tool.** Stitch only replicates data. To analyze it, you'll need an additional tool. Refer to our list of [analysis tools]({{ site.baseurl | append: "/analysis-tools" }}) for some suggestions.
          - **A data warehouse**. A destination is required to use Stitch. While we can't create one for you, you can use our [Choosing a destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) if you need some help picking the right destination for your needs.

      - title: "Requirements"
        anchor: "requirements"
        summary: "What you need to use Stitch"
        content: |
          To use Stitch, you need:

          - **A Stitch account**. Don't have an account yet? [Sign up here for your free trial]({{ site.sign-in }}){:target="new"}.
          - **A destination**. [Destinations]({{ site.baseurl }}/destinations) are the databases and warehouses where Stitch loads data replicated from your integrations.
          - **An integration**. [Integrations]({{ site.baseurl }}/integrations) are data sources. This can be a database, API, or other data application that Stitch replicates data from.

          **Note**: Stitch works best when viewed on a desktop or laptop computer. To ensure the app works properly, we also recommend temporarily **pausing any ad blocking software** and **enabling pop-ups**.

      # - title: "Terminology"
      #   anchor: "terminology"
      #   summary: "todo"
      #   terms:
      #     - name: "ETL"
      #       id: "etl"
      #       definition: |
      #         Short for extract, transform, load, ETL is a process that consolidates data from multiple sources into a central repository.
      #     - id: "destination"
      #     - id: "integration"
      #       definition: |
      #         A database, API, or other data application that Stitch replicates data from. Stitch offers three types of integrations:

      #         - Databases
      #         - SaaS
      #         - Webhooks
      #     - id: "replication-job"
      #     - id: "object"
      #       definition: |
      #         An item in a database. Depending on the context, this can be a schema, table, or column.
      #     - id: "analysis-integration"
      #   content: |
      #     <table class="attribute-list">
      #     {% for term in subsection.terms %}
      #     <tr>
      #     <td class="attribute-name">
      #     <strong>{% if term.name %}{{ term.name }}{% else %}{{ term.id | replace:"-"," " | capitalize }}{% endif %}</strong>
      #     </td>
      #     <td>
      #     {% if term.definition %}
      #     {{ term.definition | flatify | markdownify }}
      #     {% else %}
      #     {{ site.data.tooltips[term.id] | flatify | markdownify }}
      #     {% endif %}
      #     </td>
      #     </tr>
      #     {% endfor %}
      #     </table>

      # - title: "Destinations"
      #   anchor: "destinations-overview"
      #   content: |
      #     A [**destination**]({{ site.baseurl }}/destinations/) - or data warehouse - is a central repository of integrated data from disparate sources. When Stitch replicates your data, we'll load it into the destination of your choosing.

      #     **Note**: Nearly everything Stitch does is dependent on the destination you’re using: How data is loaded, what integrations, if any, have incompatibilities, and even your row usage.

      #     If you're new to data warehousing or you want to see how Stitch's destination offerings compare to each other, check out our [Choosing a Destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}). This guide will help you choose the best Stitch destination for your data warehousing needs, from ensuring your data sources are compatible to staying within your budget.

      # - title: "Integrations"
      #   anchor: "integrations-overview"
      #   content: |
      #     An [**integration**]({{ site.baseurl }}/integrations) is the Stitch word for **data source**. Using Stitch's native integrations, you can replicate data from [**databases**]() and  like PostgreSQL, MongoDB, Salesforce, Zendesk, Segment, Autopilot, and more.

      #     During your Free Trial, you'll have access to all of the integrations we offer. After your trial ends, some integrations - for example, MongoDB or Salesforce - will only be available if you select a **paid** plan.

      #     Stitch has three types of integrations:

      #     - **SaaS**: These include [SaaS applications]({{ site.baseurl }}/integrations/saas) like Salesforce, Zendesk, Google Analytics, and more.
      #     - **Databases**: These include [popular database engines]({{ site.baseurl }}/integrations/databases) such as PostgreSQL, MongoDB, MySQL, and more.
      #     - **Webhooks**: [Webhooks send data to Stitch as it occurs]({{ site.baseurl }}/webhooks), meaning it's sent in real time. Stitch's webhook integrations include services such as Segment, Delighted, FormKeep, and Zapier.

      #     **Don't see an integration you need?** If Stitch doesn't have a native integration for one of your sources, don't worry - there are still options:

      #     - Use the [**Import API**]({{ link.integrations.import-api | prepend: site.baseurl }}) integration to push arbitrary data into your data warehouse. You can use the Import API to replicate data from CSV files, Google Sheets, and more.
      #     - Use the [**Stitch Incoming Webhooks**]({{ link.integrations.stitch-incoming-webhooks | prepend: site.baseurl }}) integration to pull event data from a webhook-based service. This generic integration can be used with dozens of services.
      #     - Check out (and contribute to) [**Singer**]({{ site.singer }}), our open-source, community-driven ETL platform. 
      #     - Use the **Suggest Integration** button on the Integrations page in the Stitch app. We're always looking to add new integrations to our offerings.

  - title: "Replication"
    anchor: "replication"
    content: |
      Stitch's replication process consists of three distinct phases:

      1. **Extraction**: Stitch pulls data from your data sources and validates it using our Stitch's Import API.
      2. **Preparing**: Data is [lightly transformed](#transformations) to ensure compatibility with the destination. 
      3. **Loading**: Stitch loads the data into your destination.

      You can keep an eye on a replication job's progress on any [integration's **Summary** page]({{ link.replication.rep-progress | prepend: site.baseurl }}).

    subsections:
      - title: "Performance"
        anchor: "replication-performance"
        content: |
          Because our process is performed in steps, it's important to note that Stitch replication isn't real-time. This means that there will be some time between data extracted and data loaded.

          Additionally, the speed of Extraction and Loading is largely dependent on the resources available in your data sources and destination.

## [TODO- do we have any recommendations for optimizing performance?]

# We pride ourselves on the speed and scalability of the Stitch system, [which you can read more about here](todo).

      - title: "Deleted records"
        anchor: "replication--never-delete"
        content: |
          Stitch will never delete data from your destination, even if records have been hard deleted from the source. Refer to the [Deleted Record Handling guide]({{ link.replication.deleted-records | prepend: site.baseurl }}) for more info and examples.

      - title: "Settings"
        anchor: "replication--settings"
        content: |
          When you set up an integration in Stitch, you'll also need to define its replication settings. These settings define [how often Stitch should schedule replication jobs]({{ link.replication.rep-scheduling | prepend: site.baseurl }}), [what data should be replicated]({{ link.replication.syncing | prepend: site.baseurl }}), and [how data is replicated]({{ link.replication.rep-methods | prepend: site.baseurl }}).

# For the majority of integrations, you can:

# - Select only the schemas, tables, and columns you want to replicate
# - Define how individual tables are replicated
# - Specify when and how often data should be replicated

  - title: "Transformations"
    anchor: "transformations"
    content: |
      Stitch's goal is to get data from your data sources to your destination [in a useful, raw format](https://www.stitchdata.com/blog/why-our-etl-tool-doesnt-do-transformations/){:target="new"}:

      > _Useful_ means with types and structures that make the data easy to work with, and _raw_ means staying as close to the original representation as possible.

      This doesn't mean that Stitch doesn't perform transformations during the replication process. Stitch just doesn't perform _arbitrary_ transformations - Stitch will perform only the transformations required to ensure the loaded data is useful and compatible with your destination.

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

## todo: confirm how we handle data that doesn't have timezone info in the source
---