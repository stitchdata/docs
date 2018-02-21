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
  - title: "Create an {{ destination.display_name }} Bucket"
    anchor: "create-a-bucket"
    content: |
      {% include note.html content="Skip to [Step 2](#configure-stitch-settings) if there is an existing S3 bucket you want to connect to Stitch." %}

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


  - title: "Configure Stitch Settings"
    anchor: "configure-stitch-settings"
    content: |
      In this step, you'll define the file and object key format Stitch will use to load data into {{ destination.display_name }}.

      First, enter the name of the bucket in the **Bucket Name** field.

    substeps:
      - title: "Select Data Storage Format"
        anchor: "select-data-storage-format"
        content: |
          The data storage format defines the type of file Stitch will write to your {{ destination.display_name }} bucket. Supported options are:

          - **JSON**: Data will be stored as JSON files (`.jsonl`)
          - **CSV**: Data will be stored as CSV files (`.csv`)

          Refer to [SOME SECTION HERE]() for more information and examples.

          #### CSV-specific Settings

          If CSV is selected, there are a few additional configuration options for the files Stitch will write to your bucket:

          - **Delimiter**: Select the delimiter you want to use. Stitch will use the **comma** (`,`) option by default, but you may also use **pipes** (`|`) and **tabs** (`\t`).
          - **Quote all elements in key-value pairs**: If selected, Stitch will place all elements of key-value pairs in quotes. For example: `{a: 123}` will be stored as `"a","123"`

      - title: "Define S3 Object Key"
        anchor: "define-s3-object-key"
        content: |
          In {{ destination.display_name }}, [Object Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys) are used to uniquely identify objects in a given bucket.

          The S3 Key setting determines the convention Stitch uses to create Object Keys when it writes to your bucket. For example: If the default Key is used:

          ```shell
          [integration_name]/[table_name]/[table_version]_[timestamp_loaded]
          ```

          This could create an object with an Object Key of:

          ```shell
          salesforce-prod/accounts/1_2018-01-01[somethinghere]
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
          <li>[{{ element.name }}]</li>
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

  - title: "Grant and Verify Bucket Access"
    anchor: "grant-verify-bucket-access"
    content: |
      {% include important.html content="The bucket policy and challenge file name Stitch displays will only display once. Ensure you save them before moving on from this page." %}

      To wrap things up, you'll grant Stitch access by adding a bucket policy. [A bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) is JSON-based access policy language to manage permissions to bucket resources.

      In the table below are the top-level permissions the Stitch bucket policy grants, the operations each permission allows, and a description of the operation.

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

    substeps:
      - title: "Add a Bucket Policy"
        anchor: "add-bucket-policy"
        content: |
          To allow Stitch to access the bucket, you'll need to add a bucket policy using the AWS console.
          {% include layout/inline_image.html type="right" file="destinations/amazon-s3-bucket-policy.png" max-width="500px" alt="Adding an Amazon S3 bucket policy in the AWS console" %}

          1. Sign into AWS, if you aren't currently logged in.
          2. Click **Services** near the top-left corner of the page.
          3. Under the **Storage** option, click **S3**.
          4. A page listing all buckets currently in use will display. Click the **name of the bucket** you want to connect to Stitch.
          5. Click the **Permissions** tab.
          6. In the **Permissions** tab, click the **Bucket Policy** button.
          7. In the Bucket policy editor, paste the bucket policy code from Stitch.
          8. When finished, click **Save**.

          Leave this page open for now - you'll come back to it in the next step.

      - title: "Verify Bucket Access"
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


# {% capture console-hierarchy %}
# Though the {{ destination.display_name }} data model is flat - meaning that there isn't a hierarchy - the {{ destination.display_name }} console supports the concept of folders.

# The example Object Key above would create this folder structure: `salesforce > accounts` with the individual objects contained within the `accounts` folder. Refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-key-guidelines-safe-characters) for more info.
# {% endcapture %}


# {% include note.html content=console-hierarchy %}
---


