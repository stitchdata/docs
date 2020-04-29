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

  For example: You now want to replicate data from your integrations to a different database in your Amazon Redshift cluster, or you simply decide that Amazon Redshift isn't the destination for you.


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
      {% include destinations/switching-destination-steps.html type="considerations" %}

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
              {% assign destinations = site.destinations | where:"destination",true | sort_natural:"display_name" %}
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