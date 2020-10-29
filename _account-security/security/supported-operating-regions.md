---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Supported Data Pipeline Regions
permalink: /account-security/supported-data-pipeline-regions
summary: "The data pipeline region feature, available to all Stitch plans, determines the region where Stitch-hosted data centers will process your replicated data."

input: false
layout: general
feedback: true

key: "supported-operating-regions"
type: "security"
weight: 4


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {{ page.summary }}

  In this guide:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#           Content          #
# -------------------------- #

# I'm pretty sure most of the bg is around GDPR and unlocking customers who can't/won't have their data move through the US. Another benefit would be performance - moving data over an ocean is expensive and slow

sections:
  - title: "Data pipeline region basics"
    anchor: "basics"
    summary: "How data pipeline regions work"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Understanding Stitch's infrastructure and data pipeline region impact"
        anchor: "basics--data-infrastructure-impact"
        content: |
          {% assign north-america-region = site.data.stitch.regions | where:"id","north-america" | first %}

          When you create a Stitch account, you'll need to define a data pipeline region. This setting defines the region where Stitch-hosted data centers will process your data.

          Stitch uses Amazon Web Services (AWS) to host and run its infrastructure. Each Stitch data pipeline region corresponds to an AWS region.

          For example: If `{{ north-america-region.name }}` is selected as the region in Stitch, Stitch's data centers in AWS' `{{ north-america-region.aws-name }} ({{ north-america-region.region }})` region will be used to process data.

## Some of this content is also used in the Security FAQ

      - title: "Understanding the processes impacted by data pipeline region selection"
        anchor: "basics--process-impact"
        content: |
          Now that you understand how the data pipeline region affects your Stitch account, we'll clarify what "data processing" means in the context of regions.

          Data pipeline regions only affect the replication of data in your Stitch account, specifically extracting, preparing, and loading data into your destination.

          All other processes and data, such as billing, reporting, and other metadata, are not affected by your account's data pipeline region. Metadata related to these processes will be processed using Stitch's `{{ north-america-region.name }}` region.

      - title: "Selecting a data pipeline region"
        anchor: "basics--selecting-a-region"
        content: |
          {% include important.html type="single-line" content="Data pipeline regions can't be changed after your account is created." %}

          Before selecting a data pipeline region for your account, consider the following:

          - **The distance between your location and the data pipeline region.** We recommend, whenever possible, using the region closest to your location.
          - **The destination you want to use.** Some destinations aren't available in all regions, though we hope to expand data pipeline region support in the future. Refer to the [Data pipeline region support by destination type](#region-support-by-destination) section for more info.
          - **Any data processing regulations that your country and/or company might have in place.** Keeping your data within your own region may make it easier to comply with these requirements.

      - title: "Supported data pipeline regions"
        anchor: "basics--supported-regions"
        content: |
          Refer to the [All supported data pipeline regions section](#all-supported-regions) for more info about the regions Stitch currently supports.

  - title: "Defining and changing data pipeline regions"
    anchor: "define-change-data-pipeline-regions"
    summary: "How to define and change an account's data pipeline region"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Defining your account's data pipeline region"
        anchor: "defining-a-data-pipeline-region"
        content: |
          Data pipeline regions are selected during the account creation process. Regions can't be changed after the account is created.

      - title: "Changing your account's data pipeline region"
        anchor: "changing-a-data-pipeline-region"
        content: |
          Data pipeline regions can't be changed after your Stitch account is created. If you want to change your region, you'll need to create a new Stitch account and select the desired region.

  - title: "Identifying your account's data pipeline region"
    anchor: "identify-data-pipeline-region"
    summary: "How to identify your account's data pipeline region"
    content: |
      Click {{ app.menu-paths.account-settings }} and locate the **Data pipeline region** section:

      ![The Data Pipeline Region section of the Stitch Account Settings page]({{ site.baseurl }}/images/account-security/data-pipeline-region.png)

  - title: "Supported data pipeline regions"
    anchor: "all-supported-regions"
    summary: "The data pipeline regions supported by Stitch"
    content: |
      The following table contains info about the data pipeline regions Stitch currently supports.

      <table class="attribute-list table-hover">
      <tr>
      <td>
      <strong>
      Stitch region
      </strong>
      </td>
      <td>
      <strong>
      AWS region
      </strong>
      </td>
      <td>
      <strong>
      Stitch IP addresses
      </strong>
      </td>
      <td>
      <strong>
      Stitch destinations
      </strong>
      </td>
      </tr>
      {% for region in site.data.stitch.regions %}
      <tr>
      <td>
      {{ region.name }}
      </td>
      <td>
      {{ region.region }}
      </td>
      <td>
      <a href="{{ link.security.ip-addresses | prepend: site.baseurl }}#{{ region.id }}-ip-addresses">See list</a>
      </td>
      <td>
      <a href="#region-support-by-destination">See list</a>
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "Data pipeline region support by destination type"
    anchor: "region-support-by-destination"
    summary: "Data pipeline region support for each of Stitch's destinations"
    content: |
      {% include misc/icons.html %}

      The following table contains info about the data pipeline regions each of Stitch's destinations currently support:

      - {{ supported | replace:"TOOLTIP","Supported" }} indicates that the destination supports the region
      - {{ not-supported | replace:"TOOLTIP","Not supported" }} indicates that the destination doesn't currently support the region

      <table>
      <tr>
      <td class="attribute-name">
      <strong>
      Destination
      </strong>
      </td>
      <td>
      <strong>
      Version
      </strong>
      </td>
      {% for region in site.data.stitch.regions %}
      <td>
      <strong>
      {{ region.name }}
      </strong>
      </td>
      {% endfor %}
      </tr>
      {% assign destinations = site.destinations | where:"destination",true | sort_natural:"display_name" %}

      {% for destination in destinations %}
      <tr>
      <td class="attribute-name">
      <strong>
      {{ destination.display_name }}
      </strong>
      </td>
      <td>
      {% assign destination-version = destination.this-version | prepend:"v" %}
      {{ destination-version }}
      </td>
      {% for region in site.data.stitch.regions %}
        {% if site.data.destinations[destination.type][destination-version]stitch-details %}
          {% assign region-support = site.data.destinations[destination.type][destination-version]stitch-details.stitch-supported-regions | where:"id",region.id | first %}
        {% else %}
          {% assign region-support = site.data.destinations[destination.type]stitch-details.stitch-supported-regions | where:"id",region.id | first %}
        {% endif %}

      <td>
      {% if region-support %}
      {% capture tooltip %}{{ destination.display_name }} ({{ destination-version }}) destinations support this region.{% endcapture %}
      {{ supported | replace:"TOOLTIP",tooltip }}
      {% else %}
      {% capture tooltip %}{{ destination.display_name }} ({{ destination-version }}) destinations don't currently support this region.{% endcapture %}
      {{ not-supported | replace:"TOOLTIP",tooltip }}
      {% endif %}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>
---