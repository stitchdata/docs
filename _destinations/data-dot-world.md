---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: data.world Destination
permalink: /destinations/data-world
layout: destination-overview
tags: [bigquery_destination]
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3, data.world, data.world etl, data.world data warehouse, etl to data.world
summary: &summary "Data.world helps you host and share your data, collaborate with your team, and capture context and conclusions as you work."
toc: true
destination: true
data-loading: false


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "data.world"
type: "data-world"
db-type: "s3"
pricing_tier: "standard"
status: "Released"
description: *summary
pricing_model: "Varies" ## provider model
free_option: "Yes"
fully-managed: true
pricing_notes: "Data.world plans vary depending on the number of private projects/data sets, size limits per project/dataset, external integrations, and total number of team members that can belong to an account. All plans, however, include unlimited public projects/datasets, API access, joins, queries, activity alerts, and other standard features." 
icon: /images/destinations/icons/data-world.svg


# -------------------------- #
#           Support          #
# -------------------------- #
replication-methods: ""
connection-methods: "SSH, SSL"
supported-versions: "n/a"

nested-structures: true ## if true, natively supports nested structures
case: "Case Insensitive"
table-name-limit: "n/a" ## max # of characters
column-name-limit: "n/a" ## max # of characters
column-limit: "" ## max # of columns allowed in tables
timestamp-range: ""
timezones:
  supported: false
  storage: ""
varchar-limit: "" ## max width for varchars
decimal-limit: ""
decimal-range: ""
reserved-words: ""


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0



# -------------------------- #
#            Links           #
# -------------------------- #
status-url: https://dataworld.statuspage.io/
sign-up: &data-world https://data.world/
main-site: *data-world
documentation: https://help.data.world/hc/en-us
pricing: https://data.world/pricing


# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: "{{ destination.description | flatify | markdownify }}"

sections:
  - title: "pricing"
    content: |
      {{ destination.pricing_notes | flatify }}

      While Stitch is compatible with all of {{ destination.display_name }} plans, keep in mind that the number of private projects/datasets and the size maximum of those projects varies by plan.

      For more information on {{ destination.display_name }}'s plans, refer to their [pricing page]({{ destination.pricing }}).

  - title: "setup"
    content: |
      With just a few clicks, you can [connect your {{ destination.display_name }} account to Stitch]({{ link.destinations.setup.data-world | prepend: site.baseurl }}) and get the data flowing.

  - title: "replication"
    content: |
      A Stitch replication job consists of three stages: Extraction, Preparation, and Loading.

      The diagram below outlines the replication process for {{ destination.display_name }} destinations. In the following sections is more detail about what occurs during each stage in the replication process.

      <a href="{{ site.baseurl }}/images/destinations/data-world-replication-process.png" alt="Diagram of Stitch's replication process with data.world (Click to enlarge)"><img src="{{ site.baseurl }}/images/destinations/data-world-replication-process.png"></a>
      <p class="caption">Click to enlarge</p>

    subsections:
      - title: "Extraction"
        anchor: "extraction"
        content: |
          During the **Extraction** phase, Stitch will check for structural changes to your data, query for data according to the integration's replication settings, and extract the appropriate data.

          Replication settings include the integration's [Replication Schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}), the [data set to replicate]({{ link.replication.syncing | prepend: site.baseurl }}), and the selected tables' [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}).

      - title: "Preparation"
        anchor: "preparation"
        content: |
          During the **Preparation** phase, Stitch applies some light transformations to the extracted data to ensure compatibility with the destination.

          In the case of {{ destination.display_name }}, the only transformation Stitch performs is inserting a few [system columns]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}) into every table.

      - title: "Loading"
        anchor: "loading"
        content: |
          During **Loading**, Stitch loads the extracted data into the destination. Instead of loading data directly into your {{ destination.display_name }} account, Stitch will load the raw JSON data into an Amazon S3 bucket shared between Stitch and {{ destination.display_name }}.

          After Stitch successfully finishes loading into S3, a webhook notification is sent to {{ destination.display_name }} to trigger the retrieval process. {{ destination.display_name }} will extract the data destined for your account and load it into your {{ destination.display_name }} account. Refer to the [Schema](#schema) section below for more info on how your data will be structured in {{ destination.display_name }}.

      - title: "Replication Activity Report and Logs"
        anchor: "replication-activity-reports"
        content: |
          To check in on the replication progress of your integrations, use the [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) and [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}) features, which are visible after clicking into the integration from the dashboard.

          These logs and reports provide transparency into Stitch's replication process such as info the progress of historical jobs and errors that occur during replication.

          **Note**: Extraction Logs and Loading Reports are only available for certain integrations. Refer to the documentation linked above for info on supported integrations.

    # subsections:
    #   - title: "De-duping and Upserting Data"
    #     anchor: "de-dupe-and-upserts"
    #     content: |


  - title: "schema"
    content: |
      When {{ destination.display_name }} retrieves an integration's data from the Amazon S3 bucket, it will be loaded into your {{ destination.display_name }} account as a project with child datasets.

      {% include layout/inline_image.html type="right" file="destinations/data-world-workspace.png" max-width="250px" %}

      For each integration you connect to Stitch, a project with the same name will be created in data.world. The tables you set to replicate will be stored as JSON datasets within the project.

      For example: If you named an integration `HubSpot` in Stitch and selected the `companies`, `contact_lists`, and `contacts` tables to replicate, your workspace in your {{ destination.display_name }} account would be the same as the image on the right.
    subsections:
      - title: "Dataset Attributes"
        anchor: "dataset-attributes"
        content: |
          The dataset schema will contain the attributes you set to replicate in Stitch along with a few `_sdc` columns. These are [system columns generated by Stitch]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}) for replicating data.

          For information about the data available in SaaS integrations - including column descriptions and potential data values - refer to the [**Schema** section of any of our integrations docs]({{ site.baseurl }}/integrations/saas).

      - title: "Nested Data Structures"
        anchor: "nested-data-structures"
        content: |
          All replicated data is stored as JSON, both in Amazon S3 and in {{ destination.display_name }} after the final load is complete. This means that nested structures are stored intact.

---
{% assign destination = page %}
{% include misc/data-files.html %}