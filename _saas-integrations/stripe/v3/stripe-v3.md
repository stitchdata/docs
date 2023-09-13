---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Stripe (v3)
permalink: /integrations/saas/stripe
keywords: stripe, integration, schema, etl stripe, stripe etl, stripe schema
summary: "Connection instructions, replication info, and schema details for Stitch's Stripe integration."
layout: singer
# input: false

key: "stripe-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "stripe"
display_name: "Stripe"

singer: true
tap-name: "Stripe"
repo-url: https://github.com/singer-io/tap-stripe

this-version: "3"

api: |
  [{{ integration.display_name }} REST API](https://stripe.com/docs/api){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.stripe.com/"

api-type: "platform.stripe"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

extraction-logs: true
loading-reports: true

attribution-window: "600 days"
attribution-is-configurable: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## See the incompatibilities.yml files
## in _data/destinations for details.

has-incompatibilities: true


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
      **Administrator permissions in {{ integration.display_name }}.** This is required to grant Stitch access to {{ integration.display_name }}.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Lookback window** field, enter the number of historical days' worth of data you would like to replicate from the start date. The maximum lookback period is 600 days. This field is optional. Head to the [Lookback windows and data extraction](#lookback-windows-extraction) section to learn more about this.
      
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen explaining what you're authorizing will display. **Note**: Stitch will only ever read your {{ integration.display_name }} data, and cannot create charges or any other records in {{ integration.display_name }}.
      3. Click **Sign in with {{ integration.display_name }} to connect**.
      4. Sign into your {{ integration.display_name }} account.
      5. After the authorization process is successfully completed, you'll be directed back to Stitch.
      6. Click {{ app.buttons.finish-int-setup }}.
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
  - title: "Events table replication"
    anchor: "event-table-replication"
    content: |
      {{ integration.display_name }} will only provide 30 days of historical event data for the `events` table. Refer the the [{{ integration.display_name }} docs](https://stripe.com/docs/api/events){:target="new"} for more information about the `events` table.
  
  - title: "Objects and events"
    anchor: "objects-events"
    content: |
      In the {{ integration.display_name }} API, there are two concepts:

      - **Objects**, which are items like charges, invoices, customers, etc.
      - **Events**, which are changes to objects. For example: An invoice being created, or its status going from `draft` to `open`.

      Whenever an object is created or updated in {{ integration.display_name }}, a corresponding event is created. Because {{ integration.display_name }} creates and updates object records in this way, there are two types of tables in Stitch's {{ integration.display_name }} integration:

      - A table for **events**, which contains all events that have occurred for {{ integration.display_name }}'s [supported event types](https://stripe.com/docs/api/events/types){:target="new"}. This table acts as a history for an object record, showing how it has been changed over time.
      - Tables for **objects**, which contains the latest version of records. These are tables like [`customers`](#customers), [`charges`](#charges), [`invoices`](#invoices), etc.

      **Note**: Updates based on events is only applicable to the type of object the event is for. For example: If a dispute object is updated, only the corresponding record in the `disputes` table will be updated. The related `charge` in the `charges` table will **not** be updated. To retrieve related data for different objects, you'll need to use the `events` table. Refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/api/events/types){:target="new"} for info about event types and the objects they describe.
    subsections:
      - title: "Example event and object data replication over time"
        anchor: "event-object-data-over-time"
        content: |
          In the image below is an example of how records for the `events` and `invoices` tables will look as an invoice changes over time. **Click the image to enlarge.**

          [![Example showing how event and invoice records are replicated as an invoice changes over time]({{ site.baseurl }}/images/integrations/stripe-events.svg)]({{ site.baseurl }}/images/integrations/stripe-events.svg){:target="new"}

  - title: "Lookback windows and data extraction"
    anchor: "lookback-windows-extraction"
    content: |
      When Stitch runs a replication job for {{ integration.display_name }}, you can use a configurable lookback window of up to 600 days to query and extract data for your tables. A lookback window is a period of time for attributing shared files and the lookback period after those actions occur.

      While Stitch replicates data in this way to account for updates to records made during the lookback window, it can have a [substantial impact on your overall row usage](#lookback-window-row-count-impact).

      In the sections below are examples of how lookback windows impact how Stitch extracts data during historical and ongoing replication jobs.

      {% include integrations/saas/ads-append-only-replication.html %}
      {% include integrations/saas/attribution-window-examples.html %}      


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

## See this integration's folder in /_integration-schemas for details
## on the tables it contains.
---
{% assign integration = page %}
{% include misc/data-files.html %}