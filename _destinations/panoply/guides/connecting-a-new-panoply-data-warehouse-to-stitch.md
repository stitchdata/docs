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

title: Connecting a New Panoply Destination to Stitch
permalink: /destinations/panoply/connecting-a-new-panoply-data-warehouse-to-stitch
keywords: panoply, panoply.io, panoply data warehouse, panoply.io data warehouse etl to redshift, redshift etl, panoply etl
summary: "Spin up and connect a new Panoply destination to Stitch."

content-type: "destination-setup"
key: "panoply-destination-setup"
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

this-version: "2"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture account-creation %}
  The email address you used to sign into Stitch will be used to create your Panoply data warehouse.

  Additionally, Stitch is in no way involved with the management of Panoply data warehouses. If you have billing questions or need help regarding your Panoply destination, [reach out to Panoply]({{ site.data.destinations[destination.type]resource-links.main-site }}){:target="new"}.
  {% endcapture %}

  {% include note.html first-line="**Panoply account creation and management**" content=account-creation %}


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a {{ destination.display_name }} account"
    anchor: "create-panoply-account"
    content: |
      1. Click the {{ app.menu-paths.destination-settings }}.
      2. Click the **Panoply.io** icon.
      3. A page explaining what’s included in a Panoply account will display. Click the **Create an Account** button.
      4. Click the **Create My Account** button when a pop-up explaining the use of your email address displays.

  - title: "Wrap up and save your Panoply credentials"
    anchor: "wrap-up-save-credentials"
    content: |
      It may take a few minutes, but after your Panoply destination is successfully created, the Panoply connection info will display in Stitch:
      
      ![Panoply connection information.]({{ site.baseurl }}/images/destinations/panoply-connection-info.png)
      
      Make sure to copy your password as Stitch won’t display it again.
      
      After you’ve copied your password, click the **View Your Dashboard** button to wrap things up.

      The Panoply destination connection settings will automatically populate in the {{ app.page-names.dw-settings }} page. If you need to update the settings at any point, click the {{ app.menu-paths.destination-settings }}.

next-steps: |
  After the account is created, you can manage your Panoply settings by signing into [Panoply]({{ site.data.destinations[destination.type]resource-links.main-site }}){:target="new"}.
---
{% include misc/data-files.html %}
{% assign destination = panoply %}