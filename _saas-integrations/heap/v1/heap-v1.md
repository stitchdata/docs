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

title: Heap (v1)
permalink: /integrations/saas/heap
keywords: heap, integration, schema, etl heap, heap etl, heap schema
summary: "Connection instructions, replication info, and schema details for Stitch's Heap integration."
layout: singer
# input: false

key: "heap-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "heap"
display_name: "Heap"

singer: true 
tap-name: "Heap"
repo-url: https://github.com/singer-io/tap-heap

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.heapanalytics.com/"

api-type: "platform.heap"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from Avro files published to Amazon S3 via {{ integration.display_name }}'s **Connect** for Amazon S3 feature. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to {{ integration.display_name }} Connect using Amazon S3**. Stitch's {{ integration.display_name }} integration currently only replicates data from {{ integration.display_name }} Amazon S3 instances.
  - item: |
      **Permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles**. This is required to grant Stitch authorization to your S3 bucket.

setup-steps:
  - title: "Retrieve your Amazon Web Services account ID"
    anchor: "retrieve-aws-account-id"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="retrieve-account-id" %}

  - title: "add integration"
    content: |
      4. In the **S3 Bucket** field, enter the name of the bucket. Enter only the bucket name: No URLs, `https`, or S3 parts. For example: `heap-rs3-stitch-bucket`
      5. In the **AWS Account ID** field, paste the account ID you retrieve in [Step 1](#retrieve-aws-account-id).

  - title: "historical sync"

  - title: "replication frequency"

  - title: "Grant access to your bucket using AWS IAM"
    anchor: "grant-access-bucket-iam"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="aws-iam-access-intro" %}

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
      Replication in Stitch's {{ integration.display_name }} integration depends on two factors:

      1. [How {{ integration.display_name }} syncs data to your Amazon S3 bucket](#heap-data-syncs-to-amazon-s3), and
      2. [How Stitch identifies new data in {{ integration.display_name }} integrations](#incremental-replication-for-heap)
      

    subsections:
      - title: "{{ integration.display_name }} data syncs to Amazon S3"
        anchor: "heap-data-syncs-to-amazon-s3"
        content: |
          {{ integration.display_name }} dumps data into Amazon S3 periodically. [By default, this is on a nightly basis](https://help.heap.io/integrations/data-warehouses/s3/#process-overview){:target="new"}.

          According to {{ integration.display_name }}'s documentation:

          > Heap will provide a periodic dump of data into S3 (nightly by default). Data will be delivered in the form of Avro-encoded files, each of which corresponds to one downstream table (though there can be multiple files per table). Dumps will be incremental, though individual table dumps can be full resyncs, depending on whether the table was recently toggled or the event definition modified.

          This means that while files will only include new and updated data pertinent to that specific object (table), a full resync may be included.

      - title: "Key-based Incremental Replication using file modification timestamps"
        anchor: "incremental-replication-for-heap"
        content: |
          To identify new and updated data for replication, Stitch will use file modification timestamps as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) and store them on a per-table basis. This means that only files dumped from a new {{ integration.display_name }} data sync will be selected for replication.

          {% include replication/extraction/file-modification-replication-keys.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/heap

schema-sections:
  - title: "Custom attributes"
    anchor: "heap-custom-attributes"
    content: |
      {{ integration.display_name }}'s data model is dynamic, meaning it changes as custom attributes are added to object types in your account. For example: Adding new user attributes to the [`user`](#users) object.

      This means that the {{ integration.display_name }} schema in your destination may also change over time as you add new attributes in {{ integration.display_name }}. 

      When a new attribute is added to an object in {{ integration.display_name }}, it will display as a selectable field in the Stitch app. **Note**: To include the field in replication, you'll need to select it in Stitch. Stitch will not automatically select new fields.

      The schema documentation following this section outlines the default attributes for each object type according to [{{ integration.display_name }}'s documentation](). 

  - title: "Event tables"
    anchor: "event-tables"
    content: |
      For each event type you define in {{ integration.display_name }}, a table for that event will be available for selection in Stitch.

      For example: If there's a `Sign up - Click button` event, there will be a table named `sign_up_click_button`.

      Refer to the [`[event_type]`](#event_type) schema documentation for a list of default event attributes.

      **Note**: When new event types are added in {{ integration.display_name }}, you will need to select the table and fields in Stitch to include it in replication.

  # - title: "Data types"
  #   anchor: "data-types"
  #   content: |
  #     When {{ integration.display_name }} syncs data into Amazon S3, it does so using [Avro-encoded files](https://docs.heapanalytics.com/docs/heap-sql-retroactive-s3-specification#section-process-overview){:target="new"}. Data is typed by {{ integration.display_name }} according to the [Avro specification](https://avro.apache.org/docs/1.8.1/spec.html){:target="new"}.

---
{% assign integration = page %}
{% include misc/data-files.html %}