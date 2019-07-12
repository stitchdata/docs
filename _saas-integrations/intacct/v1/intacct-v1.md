---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Intacct (v1.0)
permalink: /integrations/saas/intacct
keywords: intacct, integration, schema, etl intacct, intacct etl, intacct schema
summary: "Connection instructions, replication info, and schema details for Stitch's Intacct integration."
layout: singer
# input: false

no-schema: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "intacct"
display_name: "Intacct"

singer: true 
tap-name: "Intacct"
repo-url: https://github.com/singer-io/tap-intacct

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://www.sageintacct.com/system-status"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#       Feature Summary      #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration relies on {{ integration.display_name }}'s [Data Delivery Service (DDS)](https://developer.intacct.com/data-delivery-service/){:target="new"} for Amazon S3. {{ integration.display_name }} DDS exports reports in CSV format to Amazon S3, which Stitch will then replicate using [Key-based Incremental Replication](#replication).

  While DDS supports other export targets, Stitch only supports replicating {{ integration.display_name }} data through Amazon S3 at this time.

  For more info about DDS, [refer to {{ integration.display_name }}'s documentation](https://www.intacct.com/ia/docs/help/More/Data_Delivery_Service/dds-overview.htm){:target="new"}.

  **Note**: This integration does not use the {{ integration.display_name }} API. Only data available via DDS will be available for replication through Stitch.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **An active subscription to {{ integration.display_name }}'s [Data Delivery Service (DDS)](https://developer.intacct.com/data-delivery-service/){:target="new"}**. Stitch's {{ integration.display_name }} integration currently only replicates data from Amazon S3 buckets used by this {{ integration.display_name }} feature.
  - item: "**An existing Amazon S3 bucket where {{ integration.display_name }} publishes data via DDS.** Stitch will not create a bucket for you."
  - item: |
      **Permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles**. This is required to grant Stitch authorization to your S3 bucket.

setup-steps:
  - title: "Set up an {{ integration.display_name }} Cloud Storage Target and automatic data delivery"
    anchor: "set-up-target-and-delivery"
    content: |
      In this step, you'll set up a Cloud Storage Target and automatic data delivery in {{ integration.display_name }}.

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Configure Amazon S3 access for {{ integration.display_name }}"
        anchor: "configure-amazon-s3-bucket-access"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if Inacct can already access your Amazon S3 bucket." %}

          1. Sign into your Amazon Web Services account.
          2. Navigate to the Amazon S3 bucket you want to use as the Cloud Storage Target for {{ integration.display_name }}.
          3. Follow the instructions in [Step 1 of {{ integration.display_name }}'s documentation](https://www.intacct.com/ia/docs/help/Reporting/Distribute_and_run_reports/Store_reports/cloud-storage-for-reports.htm?cshid=Reporting/Distribute_and_run_reports/Store_reports/cloud-storage-for-reports.htm#1.2){:target="new"} to enable {{ integration.display_name }} to access the bucket.

      - title: "Define a Cloud Storage Target in {{ integration.display_name }}"
        anchor: "define-target-in-intacct"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if a Cloud Storage Target for Amazon S3 is already set up in Inacct." %}

          1. Sign into your {{ integration.display_name }} account.
          2. Follow the instructions in [Step 2 of {{ integration.display_name }}'s documentation](https://www.intacct.com/ia/docs/help/Reporting/Distribute_and_run_reports/Store_reports/cloud-storage-for-reports.htm?cshid=Reporting/Distribute_and_run_reports/Store_reports/cloud-storage-for-reports.htm#1.){:target="new"} to create the target in {{ integration.display_name }}.

      - title: "Set up an automated data delivery in {{ integration.display_name }}"
        anchor: "set-up-automated-data-delivery"
        content: |
          In this step, you'll create an [automatic delivery schedule](https://www.intacct.com/ia/docs/help/More/Data_Delivery_Service/create-an-automated-delivery.htm#Config){:target="new"} in your {{ integration.display_name }} account.

          1. In your {{ integration.display_name }} account, navigate to **Company > Data Delivery Service > Automatic**.
          2. Click the **Add** button.
          3. In the **File attributes** section, define the settings as follows:
             - **Delimiter**: Commas
             - **Text qualifier (delimiter)**: Double quote (`"`)
             - **Encryption**: Do not encrypt
          4. In the **Delivery options** section, define the settings as follows:
             - **Cloud storage destination**: Select the Amazon S3 Cloud Storage Target you created in [Step 1.2](#define-target-in-intacct).
             - **Frequency**: Select the frequency you want to use to trigger a data export in {{ integration.display_name }}.
          5. In the **Objects** section, select the objects you want to include in the export. These objects will then be available for selection in Stitch.
          6. Save the schedule.

  - title: "Retrieve your Amazon Web Services account ID"
    anchor: "retrieve-aws-account-id"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="retrieve-account-id" %}

  - title: "add integration"
    content: |
      4. In the **Company ID** field, enter the company ID you use to sign into {{ integration.display_name }}.
      5. In the **S3 Bucket** field, enter the name of the bucket where the {{ integration.display_name }} Data Delivery Service (DDS) outputs data. Enter only the bucket name: No URLs, `https`, or S3 parts. For example: `intacct-stitch-bucket`
      6. In the **AWS Account ID** field, paste the AWS Account ID you retrieved in [Step 2](#retrieve-aws-account-id).
      7. **Optional**: In the **Path** field, enter the path configured in {{ integration.display_name }} for use in the S3 bucket.

  - title: "historical sync"

  - title: "replication frequency"

  - title: "Grant access to your bucket using AWS IAM"
    anchor: "grant-access-bucket-iam"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="aws-iam-access-intro" %}

      {% for substep in step.substeps %}
      - [Step 5.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Create an IAM policy"
        anchor: "create-iam-policy"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-iam-policy" %}
          
      - title: "Create an IAM role for Stitch"
        anchor: "create-stitch-iam-role"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-stitch-iam-role" %}

      - title: "Check and save the connection in Stitch"
        anchor: "check-save-stitch-connection"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="check-and-save" %}

  - title: "track data"

# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
  - content: |
      Stitch uses Key-based Incremental Replication to replicate data from {{ integration.display_name }} integrations. To identify new and updated data for replication, Stitch will use file modification timestamps as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) and store them on a per-table basis. This means that only files dumped from a new {{ integration.display_name }} data sync will be selected for replication.

      {% include replication/extraction/file-modification-replication-keys.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/intacct
---
{% assign integration = page %}
{% include misc/data-files.html %}