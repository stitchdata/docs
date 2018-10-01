---
title: Connecting an Amazon S3 Data Warehouse to Stitch
permalink: /destinations/amazon-s3/connecting-an-amazon-s3-data-warehouse-to-stitch
tags: [amazon-s3_destination]
keywords: amazon s3 data warehouse, amazon s3 data warehouse, etl to amazon s3, postgres etl, amazon s3 etl
summary: "Ready to spin up an Amazon S3 data warehouse and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."
toc: true
layout: destination-setup-guide

type: "amazon-s3"
display_name: "Amazon S3"

# enterprise-cta:
#   title: "Need loading notifications?"
#   url: "?utm_medium=docs&utm_campaign=s3-webhook-notifications"
#   copy: |
#     As part of an Enterprise plan, you can set up configurable webhooks to notify you when fresh data has finished loading into your destination. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions to create and manage S3 buckets in AWS**. Your AWS user must be able to create a bucket (if one doesn't already exist), add/modify bucket policies, and upload files to the bucket.
  - item: |
      **An up and running Amazon S3 bucket**. Instructions for creating a bucket using the AWS console are in [Step 1 of this guide](#create-a-bucket).

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
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


  - title: "Configure Stitch settings"
    anchor: "configure-stitch-settings"
    content: |
      In this step, you'll define the file and object key format Stitch will use to load data into {{ destination.display_name }}.

      First, enter the name of the bucket in the **Bucket Name** field. Enter only the bucket name: No URLs, `https`, or S3 parts.

      For example: `this-is-a-test-bucket-stitch-dev`

    substeps:
      - title: "Select data storage format"
        anchor: "select-data-storage-format"
        content: |
          The data storage format defines the type of file Stitch will write to your {{ destination.display_name }} bucket. Supported options are:

          - **JSON**: Data will be stored as JSON files (`.jsonl`)
          - **CSV**: Data will be stored as CSV files (`.csv`)

          For examples of how data in each format will be stored, [click here]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl | append: "#data-storage-formats" }}).

          #### CSV-specific Settings

          If CSV is selected, there are a few additional configuration options for the files Stitch will write to your bucket:

          - **Delimiter**: Select the delimiter you want to use. Stitch will use the **comma** (`,`) option by default, but you may also use **pipes** (`|`) and **tabs** (`\t`).
          - **Quote all elements in key-value pairs**: If selected, Stitch will place all elements of key-value pairs in quotes. For example: Numerical fields will appear as `"123"` instead of `123`.

# Commenting out, since we aren't doing this right now.
      # - title: "Define Webhook Loading Notifications"
      #   anchor: "define-webhook-loading-notifications"
      #   content: |
      #     {% include enterprise-cta.html %}

      #     Webhooks allow external services to be notified when an event happens. If you choose, you can configure a webhook for Stitch to notify you when data is successfully loaded into your bucket.

      #     Webhook notifications are sent on a per-integration basis. This means that every time Stitch successfully loads data for an integration, a summary webhook will be sent to the URL you define.

      #     To enable this feature, check the **Post to a webhook URL each time loading to S3 completes** box and paste a webhook URL in the **Webhook URL** field.

      #     More info about webhook loading notifications, including a list of attributes and sample use cases, [can be found here]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl | append: "#webhook-loading-notifications" }}).

      - title: "Define S3 Object Key"
        anchor: "define-s3-object-key"
        content: |
          In {{ destination.display_name }}, [Object Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys) are used to uniquely identify objects in a given bucket.

          The S3 Key setting determines the convention Stitch uses to create Object Keys when it writes to your bucket. For example: If the default Key is used:

          ```shell
          {{ destination.default-key }}
          ```

          This could create an object with an Object Key of:

          ```shell
          {{ destination.example-key-1 }}
          ```

          You can opt to use the default Key, which is pre-populated, or define your own using the elements in the next section.

          #### S3 Key Elements {#s3-key-elements}

          The following elements are available to construct an S3 Key:

          <table width="100%">
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
          {% for element in destination.key-elements %}
          {% if element.required == true %}
          <li>[{{ element.name }}]{{ element.description | strip_newlines }}</li>
          {% endif %}
          {% endfor %}
          </ul>
          </td>
          <td>
          The following elements are optional:
          <ul>
          {% for element in destination.key-elements %}
          {% if element.required == false %}
          <li>[{{ element.name }}]</li>
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
      {% include important.html type="single-line" content="The bucket policy and challenge file name Stitch displays will only display once. Ensure you save them before moving on from this page." %}

      Next, Stitch will display a **Grant & Verify Access** page. This page contains the info you need to configure bucket access for Stitch, which is accomplished via a bucket policy. [A bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) is JSON-based access policy language to manage permissions to bucket resources.

      **Note**: The policy Stitch provides is an auto-generated policy unique to the specific bucket you entered in the setup page. It allows Stitch to assume a role and access the bucket. An example might look like this:

      ```json
      {
        "Version": "2012-10-17",
        "Id": "",
        "Statement": [
          {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
              "AWS": [
                "arn:aws:iam::218546966473:role/LoaderS3"
              ]
            },
            "Action": [
              "s3:PutObject",
              "s3:GetObject",
              "s3:ListBucket"
            ],
            "Resource": [
              "arn:aws:s3:::<YOUR_S3_BUCKET_NAME>",
              "arn:aws:s3:::<YOUR_S3_BUCKET_NAME>/*"
            ]
          }
        ]
      }
      ```

      For more info about the top-level permissions the Stitch bucket policy grants, click the link below.

      <div class="panel-group" id="accordion">
        <div class="panel panel-default">
            
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapse-s3-bucket-permissions">{{ destination.display_name }} Bucket Permissions</a>
                </h4>
            </div>
            
            <div id="collapse-s3-bucket-permissions" class="panel-collapse collapse noCrossRef">
                <div class="panel-body">
                    <table width="100%" class="table-hover">
                      <tr>
                      <td width="18%; fixed">
                      <strong>Permission Name</strong>
                      </td>
                      <td width="25%; fixed">
                      <strong>Operation</strong>
                      </td>
                      <td>
                      <strong>Operation Description</strong>
                      </td>
                      </tr>
                      {% for permission in destination.permissions %}
                      {% for operation in permission.operations %}
                      {%- capture rowspan -%}
                      {{ forloop.length }}
                      {%- endcapture -%}
                      {% endfor %}
                      <tr>
                      <td rowspan="{{ rowspan }}">
                      <strong>{{ permission.name }}</strong>
                      </td>
                      {% for operation in permission.operations %}
                      {% case forloop.first %}
                      {% when true %}
                      <td>
                      <strong><a href="{{ operation.link }}">{{ operation.name }}</a></strong>
                      </td>
                      <td>
                      {{ operation.description | flatify | markdownify }}
                      </td>
                      </tr>
                      {% else %}
                      <tr>
                      <td>
                      <strong><a href="{{ operation.link }}">{{ operation.name }}</a></strong>
                      </td>
                      <td>
                      {{ operation.description | flatify | markdownify }}
                      </td>
                      </tr>
                      {% endcase %}
                      {% endfor %}
                      {% endfor %}
                      </table>
                    </div>
                </div>
            </div>
          </div>

    substeps:
      - title: "Add the Stitch Bucket Policy"
        anchor: "add-bucket-policy"
        content: |
          To allow Stitch to access the bucket, you'll need to add a bucket policy using the AWS console.

          1. Sign into AWS in another tab, if you aren't currently logged in.
          2. Click **Services** near the top-left corner of the page.
          3. Under the **Storage** option, click **S3**.
          4. A page listing all buckets currently in use will display. Click the **name of the bucket** you want to connect to Stitch.
          5. Click the **Permissions** tab.
          6. In the **Permissions** tab, click the **Bucket Policy** button.
          7. In the Bucket policy editor, paste the bucket policy code from Stitch.
          8. When finished, click **Save**.

          Leave this page open for now - you'll come back to it in the next step.

      - title: "Verify bucket access"
        anchor: "verify-bucket-access"
        content: |
          Next, to ensure that Stitch can access the bucket, you'll create a blank file that Stitch will use to test the permissions settings.

          1. In Stitch, just below the bucket policy code, is the **Verify your bucket** section. In this section is a field containing the unique name of the test file you need to create:

             ![Amazon S3 challenge file field in Stitch]({{ site.baseurl }}/images/destinations/amazon-s3-challenge-file-field.png)

             **Note**: This file name will only display once. If you navigate out of this screen without saving the file name, you'll need to start over.

          2. Create a blank file using the name displayed in this field. **Do not save the file with an extension (file type)** like `.csv` or `.txt`. In the image below, notice that there isn't any kind of file extension after the challenge file name:

             ![Saving the Amazon S3 challenge file without a file extension]({{ site.baseurl }}/images/destinations/amazon-s3-challenge-file-creation.png)

          3. Switch back to the AWS console and click the **Overview** tab.
          4. Click the **Upload** button and follow the prompts to upload the file.
          5. After the file has been uploaded to the bucket, switch back to where you have Stitch open.
          6. Click **Check and Save** to save and test the connection to {{ destination.display_name }}.

          {% include important.html type="single-line" content="The challenge file must remain in the bucket even after the initial setup is completed. Removing this file will connection and loading interruptions." %}
---