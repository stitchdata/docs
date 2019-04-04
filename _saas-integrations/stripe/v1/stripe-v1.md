---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Stripe (v1.0)
permalink: /integrations/saas/stripe
keywords: stripe, integration, schema, etl stripe, stripe etl, stripe schema
summary: "Connection instructions, replication info, and schema details for Stitch's Stripe integration."
layout: singer
# input: false

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "stripe"
display_name: "Stripe"

singer: true
tap-name: "Stripe"
repo-url: https://github.com/singer-io/tap-stripe

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://status.stripe.com/"

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## See _data/destinations/reference/incompatibilities.yml

has-incompatibilities: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in {{ integration.display_name }}.** This is required to grant Stitch access to {{ integration.display_name }}.

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen explaining what you're authorizing will display. **Note**: Stitch will only ever read your {{ integration.display_name }} data, and cannot create charges or any other records in {{ integration.display_name }}.
      3. Click **Sign in with {{ integration.display_name }} to connect**.
      4. Sign into your {{ integration.display_name }} account.
      5. After the authorization process is successfully completed, you'll be directed back to Stitch.
      6. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


# -------------------------- #
#     Replication Details     #
# -------------------------- #

replication-sections:
  - content: |
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


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

## See this integration's folder in /_integration-schemas for details
## on the tables it contains.
---
{% assign integration = page %}
{% include misc/data-files.html %}