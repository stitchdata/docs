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
  {% capture region-note %}
  {% assign north-america-region = site.data.stitch.regions | where:"id","north-america" | first %}

  Using this process will create a {{ destination.display_name }} destination in the `{{ north-america-region.region }}` region. To use a different region, use the [Connecting an existing {{ destination.display_name }} destination to Stitch]({{ link.destinations.setup.panoply-ex | prepend: site.baseurl }}) guide.
  {% endcapture %}

  {% include important.html type="single-line" content=region-note %}


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a {{ destination.display_name }} account"
    anchor: "create-panoply-account"
    content: |
      {% include note.html type="single-line" content="**Note**: The email address you used to sign into Stitch will be used to create your Panoply destination." %}

      1. [Sign into your Stitch account]({{ site.sign-in }}){:target="new"}.
      2. Click the {{ app.menu-paths.destination-settings }}.
      3. Click the **Panoply.io** icon.
      4. A page explaining what’s included in a {{ destination.display_name }} account will display. Click the **Create an Account** button.
      5. Click the **Create My Account** button when a pop-up explaining the use of your email address displays.

  - title: "Wrap up and save your {{ destination.display_name }} credentials"
    anchor: "wrap-up-save-credentials"
    content: |
      It may take a few minutes, but after your {{ destination.display_name }} destination is successfully created, the {{ destination.display_name }} connection info will display in Stitch:
      
      ![Panoply connection information.]({{ site.baseurl }}/images/destinations/panoply-connection-info.png)
      
      Make sure to copy your password as Stitch won’t display it again.
      
      After you’ve copied your password, click the **View Your Dashboard** button to wrap things up.

      The {{ destination.display_name }} destination connection settings will automatically populate in the {{ app.page-names.dw-settings }} page. If you need to update the settings at any point, click the {{ app.menu-paths.destination-settings }}.

next-steps: |
  After the account is created, you can manage your {{ destination.display_name }} settings by signing into [{{ destination.display_name }}]({{ site.data.destinations[destination.type]resource-links.main-site }}){:target="new"}.
---
{% include misc/data-files.html %}
{% assign destination = panoply %}