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

title: Connecting an Amazon S3 Destination to Stitch
permalink: /destinations/amazon-s3/connecting-an-amazon-s3-data-warehouse-to-stitch
keywords: amazon s3 data warehouse, amazon s3 data warehouse, etl to amazon s3, postgres etl, amazon s3 etl

summary: "Connect an Amazon S3 bucket to your Stitch account as a destination."

content-type: "destination-setup"
key: "amazon-s3-destination-setup"
order: 1

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Amazon S3"
name: "amazon-s3"

type: "amazon-s3"

ssh: false
ssl: false

this-version: "1"

# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions to create and manage S3 buckets in AWS**. Your AWS user must be able to create a bucket (if one doesn't already exist), add/modify bucket policies, and upload files to the bucket.
  - item: |
      **An up and running Amazon S3 bucket**. Instructions for creating a bucket using the AWS console are in [Step 1 of this guide](#create-a-bucket).


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create an {{ destination.display_name }} bucket"
    anchor: "create-a-bucket"
    content: |
      {% include note.html type="single-line" content="Skip to [Step 2](#configure-stitch-settings) if there is an existing S3 bucket you want to connect to Stitch." %}

      {% include layout/inline_image.html type="right" file="destinations/amazon-s3-create-bucket-1.png" max-width="400px" alt="Adding an Amazon S3 bucket policy in the AWS console" %}

      1. Sign into AWS.
      2. Click **Services** near the top-left corner of the page.
      3. Under the **Storage** option, click **S3**. A page listing all buckets currently in use will display.
      4. Click the **+ Create Bucket** button.
      5. On the first screen, **Name and region**, complete the following:
         - **Bucket name**: Enter a DNS-compliant name for the bucket.
         - **Region**: Select the region you want the bucket to be located in.

      6. When finished, click **Next**.
      7. As Stitch doesn't require any particular configuration, how you define the settings in the **Set properties** and **Set permissions** screens are up to you. Follow the on-screen prompts to complete these steps.
      8. When you reach the **Review** screen, verify that all the bucket's information and settings are correct.
      9. When ready, click **Create bucket**.


  - title: "Define the bucket settings in Stitch"
    anchor: "configure-stitch-settings"
    content: ""
    substeps:
      - title: "Define the bucket name and data storage format"
        anchor: "define-bucket-name-and-data-storage-format"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define S3 Object Key"
        anchor: "define-s3-object-key"
        content: |
          In {{ destination.display_name }}, [Object Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys) are used to uniquely identify objects in a given bucket.

          The **Object Key** setting in Stitch determines the convention used to create Object Keys when Stitch writes to your bucket. For example: If the default Key is used:

          ```shell
          {{ site.data.ui.destination-settings.amazon-s3.object-keys.default }}
          ```

          This could create an object with an Object Key of:

          ```shell
          {{ site.data.ui.destination-settings.amazon-s3.object-keys.example-1 }}
          ```

          You can opt to use the default Key, which is pre-populated, or define your own using the elements in the next section.

          #### S3 Key Elements {#s3-key-elements}

          The following elements are available to construct an S3 Key:

          {% assign all-object-key-elements = site.data.ui.destination-settings.amazon-s3.object-keys.elements %}

          <table class="attribute-list">
          <tr>
          <td width="50%; fixed">
          <strong>Required Elements</strong>
          </td>
          <td>
          <strong>Optional Elements</strong>
          </td>
          </tr>
          <tr>
          <td>
          All of the following elements must be included in the S3 Key, in any order:
          <ul>
          {% for element in all-object-key-elements %}
          {% if element.required == true %}
          <li><code>[{{ element.name }}]</code>{{ element.description | strip_newlines }}</li>
          {% endif %}
          {% endfor %}
          </ul>
          </td>
          <td>
          The following elements are optional:
          <ul>
          {% for element in all-object-key-elements %}
          {% if element.required == false %}
          <li><code>[{{ element.name }}]</code></li>
          {% endif %}
          {% endfor %}
          </ul>
          </td>
          </tr>
          </table>

          Additionally, keep in mind that Keys cannot exceed **500 characters** or include spaces or special characters (`!@#$%^&*`).

          As you update the values in the **S3 Key** field, Stitch will validate the entry. If the Key doesn't include all required elements or contains spaces or special characters, you will be prompted to make corrections.

          After you've finished defining the Key, click **Continue**.

  - title: "Grant and verify bucket access"
    anchor: "grant-verify-bucket-access"
    content: |
      {% include important.html type="single-line" content="The challenge file name Stitch displays will only display once. Ensure you save this before moving on from this page." %}

      {% include destinations/amazon-s3/add-verify-bucket-policy.html type="bucket-example" %}

    substeps:
      - title: "Add the Stitch bucket policy"
        anchor: "add-bucket-policy"
        content: |
          {% include destinations/amazon-s3/add-verify-bucket-policy.html type="add-bucket-policy" %}

      - title: "Verify bucket access"
        anchor: "verify-bucket-access"
        content: |
          {% include destinations/amazon-s3/add-verify-bucket-policy.html type="verify-bucket-access" %}
---