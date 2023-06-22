---
title: Iterable Core (v1)
permalink: /integrations/saas/iterable-core
keywords: iterable, integration, schema, etl iterable, iterable etl, iterable schema
layout: singer
# input: false

key: "iterable-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "iterable-core"
display_name: "Iterable"

singer: true
status-url: "https://status.iterable.com/"

tap-name: "Iterable"
repo-url: https://github.com/singer-io/tap-iterable

this-version: "1"

api: |
  [Iterable API 1.8](https://api.iterable.com/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.iterable"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      You must be an **org admin** or a user with **API and Webhook configuration permissions** in your {{ integration.display_name }} account.

setup-steps:
  - title: "Generate an {{ integration.display_name }} API key"
    anchor: "generate-api-key"
    content: |
      1. Sign into you {{ integration.display_name }} account.
      2. Navigate to **Integrations**>**API Keys**.
      3. Click **New API Key**.
      4. In the **Create a new API key** window, name your API key and select **read-only**.
      5. Click **Create**.
      6. Copy your new API key and have it ready for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Iterable API Key** field, paste the API key you copied in [step 1](#generate-api-key).
      5. In the **API Window in Days** field, enter a value. This parameter should be set to an optimum value to improve historical sync performance. Setting this value too low will take longer to complete historical sync and setting it larger may result in request timeouts or memory overflow issues.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/iterable


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}
