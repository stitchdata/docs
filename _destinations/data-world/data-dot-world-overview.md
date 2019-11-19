---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: data.world Destination
permalink: /destinations/data-world/reference
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3, data.world, data.world etl, data.world data warehouse, etl to data.world
summary: "Reference documentation for Stitch's data.world destination, including info about Stitch features, replication, and transformations."

content-type: "destination-overview"
key: "data-world-reference"

layout: general
sidebar: on-page
toc: false

data-loading: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.data-world | prepend: site.baseurl }}"

  - title: "Official {{ page.display_name }} documentation"
    link: "{{ site.data.destinations.data-world.resource-links.documentation }}"

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "data.world"
type: "data-world"
db-type: "s3"

this-version: "1"

## Resource links can be found in _data/destinations/data-world/resource-links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.data-world.destination-details.description }}

  This guide serves as a reference for version {{ destination.this-version }} of Stitch's {{ destination.display_name }} destination.

sections:
  - title: "Details and features"
    anchor: "details-and-features"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Stitch features"
        anchor: "stitch-features"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="stitch-details" %}

      - title: "Destination details"
        anchor: "destination-details"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="destination-details" %}

      - title: "data.world pricing"
        anchor: "pricing"
        content: |
          {{ site.data.destinations.data-world.destination-details-info.pricing-details | flatify }}

          While Stitch is compatible with all of {{ destination.display_name }} plans, keep in mind that the number of private projects/datasets and the size maximum of those projects varies by plan.

          For more information on {{ destination.display_name }}'s plans, refer to their [pricing page]({{ site.data.destinations[destination.type]resource-links.pricing }}){:target="new"}.

  - title: "Replication"
    anchor: "replication"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Replication process overview"
        anchor: "replication-process-overview"
        content: |
          <a href="{{ site.baseurl }}/images/destinations/data-world-replication-process.png" alt="Diagram of Stitch's replication process with data.world (Click to enlarge)"><img src="{{ site.baseurl }}/images/destinations/data-world-replication-process.png"></a>
          <p class="caption">Click to enlarge</p>
        sub-subsections:
          - title: "Steps 1 & 2: Data extraction"
            anchor: "replication--data-extraction"
            content: |
              {% include replication/replication-process-phases.html phase="data-extraction" %}

          - title: "Step 3: Load data into shared S3 bucket"
            anchor: "replication--load-data-shared-s3"
            content: |
              Stitch will loads the raw JSON data into an Amazon S3 bucket shared between Stitch and {{ destination.display_name }}.

          - title: "Step 4: Notify data.world"
            anchor: "replication--notify-data-world"
            content: |
              After Stitch successfully finishes loading into Amazon S3, a webhook notification is sent to {{ destination.display_name }} to trigger the retrieval process.

          - title: "Steps 5 & 6: data.world retrieves data from S3"
            anchor: "replication--data-world-retrieves-data"
            content: |
               {{ destination.display_name | capitalize }} retrieves the data destined for your account from the shared Amazon S3 bucket.

          - title: "Step 7: data.world loads your data"
            anchor: "replication--"
            content: |
              {{ destination.display_name | capitalize }} loads the data into your {{ destination.display_name }} account. Refer to the [Loading behavior](#loading-behavior) section below for more info on how your data will be structured in {{ destination.display_name }}.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          When {{ destination.display_name }} retrieves an integration's data from the Amazon S3 bucket, it will be loaded into your {{ destination.display_name }} account as a project with child datasets.

          {% include layout/inline_image.html type="right" file="destinations/data-world-workspace.png" max-width="250px" %}

          For each integration you connect to Stitch, a project with the same name will be created in data.world. The tables you set to replicate will be stored as JSON datasets within the project.

          For example: If you named an integration `HubSpot` in Stitch and selected the `companies`, `contact_lists`, and `contacts` tables to replicate, your workspace in your {{ destination.display_name }} account would be the same as the image on the right.

          The dataset schema will contain the attributes you set to replicate in Stitch along with a few `_sdc` columns.

      - title: "Incompatible sources"
        anchor: "replication--incompatible-sources"
        content: |
          {% include shared/incompatibilities/destination-version-incompatibilities.html %}

  - title: "Transformations"
    anchor: "transformations"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "System columns"
        anchor: "system-columns"
        content: |
          The dataset schema will contain the attributes you set to replicate in Stitch along with a few `_sdc` columns. These are [system columns generated by Stitch]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}) for replicating data.

          For information about the data available in SaaS integrations - including column descriptions and potential data values - refer to the [**Schema** section of any of our integrations docs]({{ site.baseurl }}/integrations/saas).

      - title: "JSON structures"
        anchor: "json-structures"
        content: |
          All replicated data is stored as JSON, both in Amazon S3 and in {{ destination.display_name }} after the final load is complete. This means that nested structures are stored intact.
---
{% assign destination = page %}
{% include misc/data-files.html %}