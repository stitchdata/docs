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

title: Pendo (v1)
permalink: /integrations/saas/pendo
keywords: pendo, integration, schema, etl pendo, pendo etl, pendo schema
layout: singer
# input: false

key: "pendo-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pendo"
display_name: "Pendo"

singer: true
status-url: "https://status.pendo.io/"

tap-name: "Pendo"
repo-url: https://github.com/singer-io/tap-pendo

this-version: "1"

api: |
  [{{ integration.display_name }} v1 API](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.pendo"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

attribution-window: "10 days"
attribution-is-configurable: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin privileges in {{ integration.display_name }}.** These privileges are required to create an integration key, which Stitch needs to successfully connect to your {{ integration.display_name }} account.

setup-steps:
  - title: "Create a {{ integration.display_name }} integration key"
    anchor: "create-integration-key"
    content: |
      {% capture permissions-note %}
      **Note**: Admin privileges in {{ integration.display_name }} are required to complete this step.
      {% endcapture %}

      {% include note.html type="single-line" content=permissions-note %}

      1. Sign into your {{ integration.display_name }} account as a user with Admin privileges.
      2. Click **Settings > Integrations**.
      3. On the Integrations page, click the **Integration Keys** tab.
      4. Click **+ Add Integration Key**.
      5. In **Description** field of the window that displays, enter a description. For example: `Stitch`
      6. Click **Create**.

      The integration key will dispay in the **Key** column:

      ![Highlighted Key column and integration key in the Integration Keys tab of the {{ integration.display_name }} web app]({{ site.baseurl }}/images/integrations/pendo-integration-key.png)

      Keep the integration key handy - you'll need it to complete the setup in the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Lookback Window** field, enter the number of days' worth of data you want Stitch to replicate during each replication job for selected event tables. Refer to the [Event replication](#event-replication) section for more info.
      5. In the **Period** field, select how you want data for event tables to be aggregated:

         - **Day** - Data will be aggregated by day
         - **Hour** - Data will be aggregated by hour

         Refer to the [Event replication](#event-replication) section for more info.
      6. In the **X Pendo Integration Key** field, paste the integration key you created in [Step 1](#create-integration-key).

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#   Integration Replication  #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Event replication"
    anchor: "event-replication"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Applicable event tables"
        anchor: "event-replication--tables"
        content: |
          {% assign all-pendo-tables = site.integration-schemas | where:"tap",integration.name %}
          {% assign this-version-tables = all-pendo-tables | where:"version",integration.this-version %}
          {% assign event-tables = this-version-tables | where_exp:"table","table.name contains 'event'" | sort:"name" %}

          The info in this section applies to the following tables:

          {% for table in event-tables %}
          - [{{ table.name }}](#{{ table.name | slugify }})
          {% endfor %}

      - title: "Lookback windows for events"
        anchor: "event-replication--lookback-window"
        content: |
          The **Lookback Window** setting controls how many days' worth of data are replicated during each replication job for any selected [event tables](#event-replication--tables).

          For example: If you entered `10`, Stitch would replicate the past 10 days' worth of event tables during every replication job.

          Stitch replicates data in this way to account for changes that may occur to events over time.

      - title: "Data aggregation for events"
        anchor: "event-replication--period"
        content: |
          {{ integration.display_name }}'s API allows data for [event tables](#event-replication--tables) to be aggregated by day or by hour. In Stitch, this is controlled using the **Period** setting.

          When the **Period** setting is set to:

          - `Day`, each row of event data will pertain to a specific day
          - `Hour`, each row of event data will pertain to a specific hour of a given day


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pendo/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}