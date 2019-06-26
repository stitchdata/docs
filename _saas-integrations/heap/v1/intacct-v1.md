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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to {{ integration.display_name }} Data Delivery Service**. Stitch's {{ integration.display_name }} integration currently only replicates data from Amazon S3 buckets used by this {{ integration.display_name }} feature.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Company ID** field, enter the company ID you use to sign into {{ integration.display_name }}.
      4. In the **S3 Bucket** field, enter the name of the bucket where the {{ integration.display_name }} Data Delivery Service (DDS) outputs data. Enter only the bucket name: No URLs, `https`, or S3 parts. For example: `intacct-stitch-bucket`
      5. **Optional**: In the **Path** field, enter the path configured in {{ integration.display_name }} for use in the S3 bucket.

  - title: "historical sync"

  - title: "replication frequency"

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