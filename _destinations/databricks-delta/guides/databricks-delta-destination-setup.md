---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Connecting a Databricks Delta Lake Destination to Stitch
permalink: /destinations/databricks-delta/connecting-a-databricks-delta-destination-to-stitch

keywords: databricks-delta, databricks-delta data warehouse, databricks-delta data warehouse, databricks-delta etl, etl to databricks-delta, databricks-delta destination
summary: "Connect a Databricks Delta Lake destination to your Stitch account."

content-type: "destination-setup"
key: "databricks-delta-destination-setup"
order: 1

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "databricks-delta"
display_name: "Databricks Delta Lake"

hosting-type: "amazon"

this-version: "1"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [<PROVIDER>'s documentation](){:target="new"}.
  - item: ""


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

steps:
  - title: ""
    anchor: ""
    content: |
      TODO: https://www.stitchdata.com/docs/destinations/amazon-s3/connecting-an-amazon-s3-data-warehouse-to-stitch

  - title: "Grant Databricks access to your Amazon S3 bucket"
    anchor: "grant-databricks-access-to-s3"
    content: |
      TODO: https://docs.databricks.com/administration-guide/cloud-configurations/aws/iam-roles.html

  - title: "Generate a Databricks access token"
    anchor: "generate-databricks-api-access-token"
    content: |
      Next, you'll generate a [Databricks access token]({{ site.data.destinations.databricks-delta.resource-links.api-access-token }}){:target="new"}.

      1. Sign into your Databricks account, if you haven't already.
      2. Click the **user profile icon** in the upper right corner of your Databricks workspace.
      3. Click **User Settings**.
      4. Click the **Access Tokens** tab:

         ![]({{ site.baseurl }}/images/destinations/databricks-access-tokens-tab.png)

      5. In the tab, click the **Generate New Token** button. {% include layout/image.html type="right" file="/destinations/databricks-new-access-token.png" alt="todo" max-width="400" %}
      {:start="6"}
      6. In the window that displays, enter the following: 
         - **Comment**: `Stitch destination`
         - **Lifetime (days)**: **Leave this field blank.** If you enter a value, your token will eventually expire and break the connection to Stitch.
      7. Click **Generate**. {% include layout/image.html type="right" file="/destinations/databricks-generated-token.png" alt="todo" max-width="400" %}
      {:start="8"}
      8. Copy the token somewhere secure. Databricks will only display the token once.
      9. Click **Done** after you copy the token.
      

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate the {{ destination.display_name }} connection details"
        anchor: "locate-connection-details-aws"
        content: |
          {% include shared/connection-details/amazon.html type="connection-details" %}

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