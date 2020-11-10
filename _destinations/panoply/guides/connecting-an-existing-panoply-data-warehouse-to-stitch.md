---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Connecting an Existing Panoply Destination to Stitch
permalink: /destinations/panoply/connecting-an-existing-panoply-data-warehouse-to-stitch
keywords: panoply, panoply.io, panoply data warehouse, panoply.io data warehouse etl to redshift, redshift etl, panoply etl
summary: "Connect your existing Panoply destination to Stitch."

content-type: "destination-setup"
order: 1

layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Panoply"
name: "panoply"

type: "panoply"

ssh: false
ssl: false
port: 5439


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture region-note %}
  {% assign north-america-region = site.data.stitch.regions | where:"id","north-america" | first %}

  **Data regions and {{ destination.display_name }}:** Use this process if you want your {{ destination.display_name }} destination to use a different region than `{{ north-america-region.region }}`. Reach out to [{{ destination.display_name }} support](https://panoply.io/docs/manage-data/custom-data-center-regions/){:target="new"} if you want to change your existing {{ destination.display_name }} destination's region.
  {% endcapture %}

  {% include note.html type="single-line" content=region-note %}


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: "**Admin permissions in {{ destination.display_name }}.**"

# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Locate the connection details in {{ destination.display_name }}"
    anchor: "locate-connection-info"
    content: |
      1. Sign into your {{ destination.display_name }} account.
      2. In the left panel menu, click **Connect**.
      3. The database connection info - the **host, port, database name**, and **username** - will display.

      Leave this page open - you’ll need it in the next step.

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}