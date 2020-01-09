---
title: Changing Stitch Destinations
keywords: destinations, compatibility, switch destination, switch redshift, switch, change redshift, change bigquery, change postgresql, change destination
summary: "Change your Stitch destination in just a few quick steps."

permalink: /destinations/switching-destinations

destination: false
content-type: "destination-general"
key: "switch-destinations"

toc: true
layout: general
type: "all"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  Sometimes, you may want to replicate data to a different location than what you initially connected to Stitch. 

  For example: You now want to replicate data from your integrations to a different database in your Redshift cluster, or you simply decide that Redshift isn't the destination for you.


# -------------------------- #
#         Instructions       #
# -------------------------- # 

sections:
  - title: "Prerequisites"
    anchor: "prerequisites"
    content: |
      The only prerequisite to changing destinations is that the **new** destination is ready to be connected to Stitch. This will minimize any downtime you may experience.

      If you need a refresher on how to spin up a destination for Stitch, check out the [destination setup guides]({{ site.baseurl }}/destinations#current-destinations).

  - title: "Considerations"
    anchor: "considerations"
    content: |
      Here's what you need to know to ensure a smooth switch:

      - **Some destinations may structure data differently than your current destination.** For example: if you're changing from Redshift to BigQuery, there will be some differences in how your data is stored. Detailed info about how Stitch loads data can be found in the [Data Loading Guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for each destination.

      - **Your integrations will be paused.** After the switch is complete, you’ll need to manually unpause the integrations you’d like to resume.

      - **We won’t delete or transfer any data from your current destination.** To get historical data into your new destination, you'll need to queue a full re-sync of all your integrations. 

         Re-syncing historical data will count towards your row usage and may take some time, depending on the volume of data and API limitations imposed by the provider.

      - **Some webhook data may be lost during this process.** Due to their continuous, real-time nature, some webhook data may be lost during the switch.

      - **Historical data from webhook-based integrations must be either manually backfilled or replayed.** Some webhook providers - such as Segment - allow customers on certain plans to 'replay' their historical data. This feature varies from provider to provider and may not always be available.

         If you don't have the ability to replay historical webhook data, then it must be manually backfilled after the switch is complete.

  - title: "Switch destinations"
    anchor: "switch-destinations"
    content: |
      To switch to a new destination, you'll need to: 

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Step 1: Select a historical data setting"
        anchor: "select-historical-data-setting"
        content: |
          {% include destinations/switching-destination-steps.html type="select-historical-data-setting" %}

      - title: "Step 2: Delete the current destination"
        anchor: "delete-current-destination"
        content: |
          {% include destinations/switching-destination-steps.html type="delete-current-destination" %}

      - title: "Step 3: Configure the new destination"
        anchor: "configure-new-destination"
        content: |
          1. On the next page, click the icon of the destination type you want to switch to.
          2. Follow the instructions for that destination type to complete the setup. If you need some help, refer to the destination's setup guide:
              {% assign destinations = site.destinations | where:"destination",true | sort:"display_name" %}
              {% for destination in destinations %}
              - [{{ destination.title | remove: " Destination Documentation" }}]({{ destination.url | prepend: site.baseurl | append: "#get-started" }})
             {% endfor %}

      - title: "Step 4: Unpause your integrations"
        anchor: "unpause-integrations"
        content: |
          {% include destinations/switching-destination-steps.html type="unpause-integrations" %}

  - title: "Troubleshooting"
    anchor: "troubleshooting"
    content: |
      If you encounter connection issues, check out the [Destination Connection Errors guide]({{ link.troubleshooting.dw-connection-errors | prepend: site.baseurl }}) for common problems and solutions.
---
{% include misc/data-files.html %}