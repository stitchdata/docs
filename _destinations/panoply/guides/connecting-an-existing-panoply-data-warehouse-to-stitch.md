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
type: "panoply"

ssh: false
ssl: false
port: 5439


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture account-creation %}
  Stitch is in no way involved with the management of Panoply data warehouses. If you have billing questions or need help regarding your Panoply destination, [reach out to Panoply]({{ site.data.destinations.resource-links[destination.type]main-site }}){:target="new"}.
  {% endcapture %}

  {% include note.html first-line="**Panoply account management**" content=account-creation %}


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: "**Admin permissions in Panoply.**"

# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Locate the connection details in Panoply"
    anchor: "locate-connection-info"
    content: |
      1. Sign into your Panoply account.
      2. In the left panel menu, click **Connect**.
      3. The database connection info - the **host, port, database name**, and **username** - will display.

      Leave this page open - you’ll need it in the next step.

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

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