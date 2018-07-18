---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Amazon S3 CSV
keywords: amazon-s3-csv, database integration, etl amazon-s3-csv, amazon-s3-csv etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-s3-csv
summary: "Connect and replicate data from CSV files in your Amazon S3 bucket using Stitch's Amazon S3 CSV integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "amazon-s3-csv"
display_name: "Amazon S3 CSV"

# this-version: "1.0"

# -------------------------- #
#       Stitch Supports      #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: "n/a"
db-type: "s3"
icon: /images/integrations/icons/amazon-s3-csv.svg

versions: "n/a"
ssh: false
ssl: false
sync-views: false
whitelist:
  tables: true
  columns: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

binlog-replication: false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions to manage S3 buckets in AWS**. Your AWS user must be able to add/modify bucket policies. During the setup process, Stitch will provide you with a bucket policy which will allow Stitch to access the bucket. This must be added to the bucket for Stitch to connect successfully.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "add integration"
    content: |
      4. In the **S3 Bucket** field, enter the name of bucket. Enter only the bucket name: No URLs, `https`, or S3 parts.

         For example: `com-test-stitch-bucket`

  - title: "Configure tables"
    anchor: "configure-tables"
    content: |
      Next, you'll indicate which CSV file(s) you want to include for replication. A table can be made up of a single CSV file or several CSV files.

      For the best results:

      - **The names of files should adhere to your destination's limits for table names.** File names will be used to create a name for the table in the destination.

         Table name limits will vary by destination type. For example: Redshift table names cannot exceed 127 characters.
      - **Each file should have a header row with names that adhere to your destination's limits for column names.** This will vary by destination type. For example: Redshift column names cannot exceed 115 characters. 
      - **If including multiple files in a table, each file should have the same header row.** Including multiple files in a single table depends on the search pattern you define in the next step.

        **Note**: This is not the same as configuring multiple tables. See the [search pattern](#define-table-search-pattern-and-name) section below for examples.

      In the following sections, we'll walk you through how to configure a table in Stitch.

    substeps:
      - title: "Define the table's search pattern and name"
        anchor: "define-table-search-pattern-and-name"
        content: |
          The **Search Pattern** field accepts the name of a single file (ex: `customers.csv`) or a regular expression, which can be used to include multiple files. What you enter into this field depends on how data for a particular entity is updated.

          If a single file is replaced in your S3 bucket at some interval, it would make sense to enter location of the file:

          ```
          customers.csv

          /analytics/customers.csv
          ```

          In other cases, there may be multiple files meant for a single table. For example: Every day a new CSV file is generated with updated customer data, and it follows the naming convention of `customers-YYYY-MM-DD.csv`.

          To ensure data is correctly captured, you'd want to enter a search pattern that would match all files beginning with `customer`, regardless of the date in the file name.

          To match `customers-2018-07-01.csv`, `customers-2018-07-02.csv`, and `customers-2018-07-03.csv`, you could use either of search patterns:

          ```
          customers.*\csv

          /analytics/customers.*\csv
          ```

      - title: "Define the table's Primary Key"
        anchor: "define-table-primary-key"
        content: |
          {% include note.html content="This step is optional." %}

          In the **Primary Key** field, enter one or more header fields (separated by commas) Stitch can use to identify unique rows. For example:

          ```
          account_id,date
          ```

          If undefined, Stitch will load data into the table in an append-only fashion. This means that existing rows in the destination won't be updated, but will be appended to the end of the table. Refer to the [Primary Keys and Append-Only Replication](#primary-keys-append-only) section below for more info and examples.

      - title: "Specify datetime fields"
        anchor: "specify-datetime-fields"
        content: |
          {% include note.html content="This step is optional." %}

          In the **Specify datetime fields** field, enter one or more header fields (separated by commas) that should appear in the destination table as `datetime` fields instead of strings. For example:

          ```
          created_at,updated_at
          ```

          If undefined, Stitch will load all columns into the destination as strings.

      - title: "Configure additional tables"
        anchor: "configure-additional-tables"
        content: |
          If you want to add another table, click the **Configure another table?** link below the **Specify datetime fields** field. Otherwise, move onto the [Sync historical data](#define-historical-sync) section.

           Stitch doesn't enforce a limit on the number of tables that you can configure for a single integration.

  - title: "historical sync"
    ## For this, we should note that setting this date will replicate all files in full that have been modified since the date set here

  - title: "replication frequency"

  - title: "Grant bucket access to Stitch"
    anchor: "grant-bucket-access-to-stitch"
    content: |
      Next, Stitch will display a **Grant & Verify Access** page. This page contains the info you need to configure bucket access for Stitch, which is accomplished via a bucket policy. [A bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) is JSON-based access policy language to manage permissions to bucket resources.

      **Note**: The policy Stitch provides is an auto-generated policy unique to the specific bucket you entered in the setup page.

      For more info about the top-level permissions the Stitch bucket policy grants, click the link below.

      [TODO- PERMISSIONS MIGHT BE HERE]

    substeps:
      - title: "Add the Stitch Bucket Policy"
        anchor: "add-bucket-policy"
        content: |
          To allow Stitch to access the bucket, you'll need to add a bucket policy using the AWS console.
          {% include layout/inline_image.html type="right" file="destinations/amazon-s3-bucket-policy.png" max-width="500px" alt="Adding an Amazon S3 bucket policy in the AWS console" %}

          1. Sign into AWS in another tab, if you aren't currently logged in.
          2. Click **Services** near the top-left corner of the page.
          3. Under the **Storage** option, click **S3**.
          4. A page listing all buckets currently in use will display. Click the **name of the bucket** you want to connect to Stitch.
          5. Click the **Permissions** tab.
          6. In the **Permissions** tab, click the **Bucket Policy** button.
          7. In the Bucket policy editor, paste the bucket policy code from Stitch.
          8. When finished, click **Save**.
      
      - title: "Check and save the connection"
        anchor: "check-save-connection"
        content: |
          1. Switch back to the tab where Stitch is open.
          2. Click the **Check and Save** button.

          Stitch will check if bucket access has been correctly granted. If successful, [TODO]

  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Mapping files to a single table"
    anchor: "mapping-files-to-table"
    content: |
      [CONTENT]

  - title: "[Use of file modified as Replication Key]"
    anchor: ""
    content: |
      [CONTENT]

  - title: "Primary Keys and Append-Only Replication"
    anchor: "primary-keys-append-only"
    content: |
      [CONTENT]

---
{% assign integration = page %}
{% include misc/data-files.html %}