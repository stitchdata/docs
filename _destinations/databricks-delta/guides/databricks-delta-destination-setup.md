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

display_name: "Databricks Delta Lake"
name: "databricks-delta"

type: "databricks-delta"

hosting-type: "amazon"

this-version: "1"

ssh: true



# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      **An Amazon Web Services (AWS) account with a {{ destination.display_name }} deployment.** Instructions for configuring a {{ destination.display_name }} deployment are outside the scope of this tutorial; our instructions assume that you have {{ destination.display_name }} up and running. Refer to [Databricks' documentation]({{ site.data.destinations.databricks-delta.resource-links.configure-aws-account }}){:target="new"} for help configuring your AWS account with Databricks.
  - item: |
      **An existing Amazon S3 bucket.** This bucket must be in the same AWS account as the Databricks deployment or have a cross-account bucket policy that allows access to the bucket from the AWS account with the Databricks deployment.
  - item: |
      **Permissions to manage S3 buckets in AWS**. Your AWS user must be able to add and modify bucket policies in the AWS account or accounts where the S3 bucket and Databricks deployment reside.
  

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

steps:
  - title: "Grant Databricks access to your Amazon S3 bucket"
    anchor: "grant-databricks-access-to-s3"
    content: |
      {% capture databricks-access-note %}
      **Note**: You'll need the [**Allow Cluster Creation** privilege]({{ site.data.destinations.databricks-delta.resource-links.cluster-privileges | append: "#types-of-permissions" }}){:target="new"} in Databricks to complete this step.
      {% endcapture %}
      
      {% include note.html type="single-line" content=databricks-access-note %}

      First, you'll configure your AWS account to allow access from Databricks. This is required to complete loading data into {{ destination.display_name }}.  Refer to [Databricks' documentation]({{ site.data.destinations.databricks-delta.resource-links.databricks-s3-access }}){:target="new"} for help configuing AWS access for Databricks.

      **Note**: The Databricks cluster must have a **[Databricks Runtime]({{ site.data.destinations.databricks-delta.resource-links.databricks-runtime }}){:target="new"} Version of 6.3 or higher** to work with Stitch. When you reach the [**Launch a new cluster with the S3 IAM role** step]({{ site.data.destinations.databricks-delta.resource-links.databricks-s3-access | append: "#step-6-launch-a-cluster-with-the-s3-iam-role" }}){:target="new"} of Databricks' **Configuring S3 access** guide, make sure you select **version 6.3 or higher**:

      ![]({{ site.baseurl }}/images/destinations/databricks-runtime-version.png)

  - title: "Retrieve the Databricks' cluster JDBC URL"
    anchor: "retrieve-jdbc-url"
    content: |
      {% include layout/image.html type="right" file="/destinations/databricks-cluster-details-page.png" alt="The Advanced Options section of the Cluster Details page in Databricks" max-width="400" enlarge=true%}
      Next, you'll retrieve your [Databricks' cluster JDBC URL]({{ site.data.destinations.databricks-delta.resource-links.connect-bi-tools }}){:target="new"}. 

      1. Sign into your Databricks account, if you haven't already.
      2. Click the **Clusters** option in the menu on the left side of your Databricks workspace.
      3. Click the cluster you created in [Step 1](#grant-databricks-access-to-s3).
      4. On the cluster's details page, click **Advanced Options**.
      5. Click the **JDBC/ODBC** tab. 
      6. Locate the **JDBC URL** field and copy the value:

         ![The Advanced Options section of the Cluster Details page in Databricks]({{ site.baseurl }}/images/destinations/databricks-cluster-advanced-options.png)

      Keep this handy - you'll need it to complete the setup in Stitch.

  - title: "Generate a Databricks access token"
    anchor: "generate-databricks-api-access-token"
    content: |
      1. Click the **user profile icon** in the upper right corner of your Databricks workspace.
      2. Click **User Settings**.
      3. Click the **Access Tokens** tab:

         ![The Access Tokens tab in the User Settings page of Databricks]({{ site.baseurl }}/images/destinations/databricks-access-tokens-tab.png)

      4. In the tab, click the **Generate New Token** button. {% include layout/image.html type="right" file="/destinations/databricks-new-access-token.png" alt="The Generate New Token window in Databricks" max-width="400" %}
      {:start="5"}
      5. In the window that displays, enter the following: 
         - **Comment**: `Stitch destination`
         - **Lifetime (days)**: **Leave this field blank.** If you enter a value, your token will eventually expire and break the connection to Stitch.
      6. Click **Generate**. {% include layout/image.html type="right" file="/destinations/databricks-generated-token.png" alt="A newly generated access token in Databricks" max-width="400" %}
      {:start="7"}
      7. Copy the token somewhere secure. Databricks will only display the token once.
      8. Click **Done** after you copy the token.

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      {% include shared/database-connection-settings.html type="general" %}

      {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Grant Stitch access to your Amazon S3 bucket"
    anchor: "grant-stitch-access-to-s3"
    content: |
      {% for substep in step.substeps %}
      - [Step 5.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Copy the Stitch bucket policy"
        anchor: "copy-bucket-policy"
        content: |
          {% include destinations/amazon-s3/add-verify-bucket-policy.html type="bucket-example" %}

      - title: "Create the Stitch bucket policy in AWS"
        anchor: "add-bucket-policy"
        content: |
          {% include destinations/amazon-s3/add-verify-bucket-policy.html type="add-bucket-policy" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}