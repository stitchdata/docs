---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Amplitude (v1)
permalink: /integrations/saas/amplitude
keywords: amplitude, integration, schema, etl amplitude, amplitude etl, amplitude schema
summary: "Connection instructions, replication info, and schema details for Stitch's Amplitude integration."
layout: singer
# input: false

key: "amplitude-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "amplitude"
display_name: "Amplitude"

singer: true 
tap-name: "Amplitude"
repo-url: https://github.com/singer-io/tap-amplitude

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "n/a"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.amplitude.com/"

api-type: "platform.amplitude"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration relies on the {{ integration.display_name }} [Query product add-on](#setup-requirements), which utilizes a Snowflake database to store data.

  {{ integration.display_name }} integrations can replicate event and merged user ID data. Refer to the [Schema](#schema) section for more info.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be on an {{ integration.display_name }} Enterprise or Growth plan**. Amplitude requires this to access the Query product add-on.  
  - item: |
      **To have purchased the {{ integration.display_name }} Query product add-on.** [Query](https://amplitude.zendesk.com/hc/en-us/articles/115001902492-Query-Snowflake){:target="new"} is an {{ integration.display_name }}-managed Snowflake database, which Stitch's integration replicates data from.

setup-steps:
  - title: "Retrieve your Snowflake credentials"
    anchor: "retrieve-snowflake-credentials"
    content: |
      Stitch's {{ integration.display_name }} integration connects to your {{ integration.display_name }}-managed Snowflake database to replicate data.

      To connect Stitch to {{ integration.display_name }}, you'll need to retrieve your Snowflake credentials from {{ integration.display_name }}. Reach out to [{{ integration.display_name }} support](https://amplitude.zendesk.com/hc/en-us/requests/new){:target="new"} or your {{ integration.display_name }} Success Manager to get your credentials.

      When you receive your credentials, you can move onto the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **{{ integration.display_name }} Snowflake Username** field, enter your Snowflake username.
      5. In the **{{ integration.display_name }} Snowflake Password** field, enter the Snowflake user's password.
      6. In the **{{ integration.display_name }} Snowflake Account** field, enter the Snowflake account.
      7. In the **{{ integration.display_name }} Snowflake Warehouse** field, enter the name of the Snowflake warehouse.
      8. In the **{{ integration.display_name }} Snowflake Database** field, enter the name of the Snowflake database.
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/amplitude

schema-sections:
  - content: |
      Stitch's {{ integration.display_name }} replicates two types of tables: Events and merged user IDs.

      For each project in your {{ integration.display_name }} account, a set of these tables will be available for replication. Stitch will append a project's ID to each table name to make them easily identifiable. For example: If a project has an ID of `168342`, the events table for the project will be named `events_168432`.

      You can identify which tables are for a specific project by comparing the ID in the table name to the projects in your {{ integration.display_name }} account. You can access this page in your {{ integration.display_name }} account by clicking the **User menu (top right corner) > Settings > Projects**.

      ![Highlighted project ID field in the Amplitude UI]({{ site.baseurl }}/images/integrations/amplitude-project-id.png)
---
{% assign integration = page %}
{% include misc/data-files.html %}