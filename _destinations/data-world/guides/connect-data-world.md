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

title: Connecting a data.world Destination to Stitch
permalink: /destinations/data-world/connecting-a-data-world-data-warehouse-to-stitch
keywords: data-world, data-world, data-world data warehouse, etl to s3, s3 etl, data-world etl, amazon s3
summary: "Connect a data.world account to your Stitch account as a destination."

content-type: "destination-setup"
order: 1

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "data.world"
type: "data-world"

ssh: false
ssl: true

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture account-management %}
  **data.world account management**: Stitch is not involved with the management of {{ destination.display_name }} destinations. If you have billing questions or need help regarding your {{ destination.display_name }} destination, [reach out to {{ destination.display_name }}]({{ site.data.destinations[destination.type]resource-links.documentation }}){:target="new"}.
  {% endcapture %}

  {% include note.html type="single-line" content=account-management %}

  {{ destination.description | flatify }} With just a few clicks, you can connect your {{ destination.display_name }} account to Stitch and get the data flowing.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      1. Click the {{ app.menu-paths.destination-settings }}.
      2. Click the **{{ destination.display_name }}** icon.
      3. Click the **Sign in with {{ destination.display_name }}** button.
      4. At the prompt, sign into your {{ destination.display_name }} account.

  - title: "Authorize with {{ destination.display_name }}"
    anchor: "authorize-with-data-world"
    content: |
      Next, you'll be asked to authorize Stitch to access your {{ destination.display_name }} account. Stitch will request permission to perform the following:
         - **Access your profile information**: This is required to identify and connect to your account.
         - **Read datasets and projects**: This is required to load replicated data into your destination.
         - **Write to datasets and projects**: This is required to load replicated data into your destination.
      
      Click **Authorize Stitch**.

  - title: "Verify your {{ destination.display_name }} account ID"
    anchor: "verify-account-id"
    content: |
      After the authorization process is successfully completed, you'll be directed back to Stitch to verify your {{ destination.display_name }} account ID.

      Stitch will use your {{ destination.display_name }} Account ID by default, but you can use a different ID if desired. For example: For a user named `stitch-data-world`, Stitch would default to using `stitch-data-world` as the Account ID.

      To use a different ID, click the link and enter the ID in the **Use This Account ID** field:

      ![Changing the data.world Account ID in Stitch]({{ site.baseurl }}/images/destinations/data-world-s3-change-account-id.gif)
      
      When finished, click **Save Settings** to save and test the connection.
---
{% include misc/data-files.html %}
{% assign destination = page %}