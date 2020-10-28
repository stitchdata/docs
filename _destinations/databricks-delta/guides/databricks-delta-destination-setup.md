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


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      **An Amazon Web Services (AWS) account with a {{ destination.display_name }} deployment.** Instructions for configuring a {{ destination.display_name }} deployment are outside the scope of this tutorial; our instructions assume that you have {{ destination.display_name }} up and running. Refer to [Databricks' documentation]({{ site.data.destinations.databricks-delta.resource-links.configure-aws-account }}){:target="new"} for help configuring your AWS account with Databricks.
  - item: |
      {% assign north-america-region = site.data.stitch.regions | where:"id","north-america" | first %}

      **An existing Amazon S3 bucket that must be:** 

      - In the **same region as your Stitch account**. For example: If your Stitch account uses the {{ north-america-region.name }} (`{{ north-america-region.region }}`) data pipeline region, your S3 bucket must also be in `{{ north-america-region.region }}`. [Here's how to verify your Stitch account's data pipeline region]({{ link.security.supported-operating-regions | prepend: site.baseurl | append: "#identify-data-pipeline-region" }}).
      - In the same AWS account as the Databricks deployment or have a cross-account bucket policy that allows access to the bucket from the AWS account with the Databricks deployment.
  - item: |
      **Permissions to manage S3 buckets in AWS**. Your AWS user must be able to add and modify bucket policies in the AWS account or accounts where the S3 bucket and Databricks deployment reside.
  

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

steps:
  - title: "Configure S3 bucket access in AWS"
    anchor: "configure-s3-bucket-access-in-aws"
    content: |
      {% capture s3-region-note %}
      The S3 bucket you use [must be in the same region as your Stitch account](#prerequisites). Using a bucket in another region will result [in errors in Stitch]({{ link.troubleshooting.dw-loading-errors | prepend: site.baseurl | append: "#s3-bucket-region-mismatch" }}).
      {% endcapture %}

      {% include important.html type="single-line" content=s3-region-note %}

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Grant Stitch access to your Amazon S3 bucket"
        anchor: "grant-stitch-access-to-s3"
        content: |
          {% include destinations/amazon-s3/add-verify-bucket-policy.html type="add-bucket-policy" %}
      - title: "Grant Databricks access to your Amazon S3 bucket"
        anchor: "grant-databricks-access-to-s3"
        content: |
          Next, you'll configure your AWS account to allow access from Databricks by creating an IAM role and policy. This is required to complete loading data into {{ destination.display_name }}.

          Follow steps 1-4 in [Databricks' documentation]({{ site.data.destinations.databricks-delta.resource-links.databricks-s3-access }}){:target="new"} to create the IAM policy and role for Databricks.

  - title: "Configure access in Databricks"
    anchor: "configure-access-in-databricks"
    content: |
      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Add the Databricks S3 IAM role to Databricks"
        anchor: "add-s3-iam-role-databricks"
        content: |
          Follow [step 5 in this Databricks guide]({{ site.data.destinations.databricks-delta.resource-links.databricks-s3-access | append: "#step-5-add-the-s3-iam-role-to-databricks" }}){:target="new"} to add  IAM role you created for Databricks in [Step 1.2](#grant-databricks-access-to-s3) to your Databricks account.

          After the Databricks IAM role has been added using the Databricks [Admin Console](https://docs.databricks.com/administration-guide/admin-console.html#admin-console){:target="new"}, proceed to the next step. 

      - title: "Create a Databricks cluster"
        anchor: "create-databricks-cluster"
        content: |
          {% capture databricks-access-note %}
          **Note**: You'll need the [**Allow Cluster Creation** privilege]({{ site.data.destinations.databricks-delta.resource-links.cluster-privileges | append: "#types-of-permissions" }}){:target="new"} in Databricks to complete this step.
          {% endcapture %}
          
          {% include note.html type="single-line" content=databricks-access-note %}

          1. Sign into your Databricks account.
          2. Click the **Clusters** option on the left side of the page.
          3. Click the **+ Create Cluster** button.
          4. In the **Cluster Name** field, enter a name for the cluster.
          5. In the **Databricks Runtime Version** field, select a version that's **6.3 or higher.** This is required for {{ destination.display_name }} to work with Stitch:

             ![Databricks Runtime Version field with version Runtime: 6.3 selected]({{ site.baseurl }}/images/destinations/databricks-runtime-version.png)
          6. In the **Advanced Options** section, locate the **IAM Role** field.
          7. In the dropdown menu, select the Databricks IAM role you added to your account [in the previous step](#add-s3-iam-role-databricks).
          8. When finished, click the **Create Cluster** button to create the cluster.

      - title: "Retrieve the Databricks cluster's JDBC URL"
        anchor: "retrieve-jdbc-url"
        content: |
          Next, you'll retrieve your [Databricks' cluster JDBC URL]({{ site.data.destinations.databricks-delta.resource-links.connect-bi-tools }}){:target="new"}.

          1. On the **Clusters** page in Databricks, click the cluster you created in the previous step.
          2. Open the **Advanced Options** section.
          3. Click the **JDBC/ODBC** tab. 
          4. Locate the **JDBC URL** field and copy the value:

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
---
{% include misc/data-files.html %}
{% assign destination = page %}