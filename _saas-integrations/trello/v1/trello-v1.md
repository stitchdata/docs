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

title: Trello (v1)
permalink: /integrations/saas/trello
keywords: trello, integration, schema, etl trello, trello etl, trello schema
layout: singer
# input: false

key: "trello-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "trello"
display_name: "Trello"

singer: true
status-url: "https://trello.status.atlassian.com/"

tap-name: "Trello"
repo-url: https://github.com/singer-io/tap-trello

this-version: "1"

api: |
  [{{ integration.display_name }} REST API](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

api-type: "platform.trello"

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be a member of every {{ integration.display_name }} board you want to replicate.** If a board is private and the user isn't a member, Stitch will be unable to access it. Before beginning the setup process, verify that the user setting up the integration has access to all the boards you want to replicate.

      Refer to the [Replication section](#data-replication-board-membership) for why this is required. 

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
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
      1. Next, you'll be redirected to {{ integration.display_name }}.
      2. Log into your {{ integration.display_name }} account and complete the authorization process.  When finished, you'll be redirected back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#    Replication Details     #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in integration.replication-sections %}
      {% if section.title %}
      - [{{ section.title }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Data replication via board membership"
    anchor: "data-replication-board-membership"
    content: |
      Stitch's {{ integration.display_name }} integration replicates data by first querying for the **boards** that the user authorizing the integration in Stitch is a member of. Specifically, Stitch uses the [Get boards that member belongs to endpoint](https://developer.atlassian.com/cloud/trello/rest/#api-members-id-boards-get){:target="new"} (`/1/members/{id}/boards`) to retrieve the boards the user is a member of.

      This means that to replicate data successfully, including [`boards`](#boards), the user who authorized the integration in Stitch must be a member of every board you want to replicate data from.

      Let's take a look at what Extraction might look like for `boards` and `cards` using some SQL queries.

      {% include note.html type="single-line" content="**Note**: The queries in this section aren't meant to be used to query replicated Trello data, and may not have parity with actual fields replicated by Stitch. They are for demonstration only." %}

      {% assign authorizing-user-id = "559be34bc1f1b3f3383671b7" %}
      {% assign board-id = "574f5d5202564aa4447e14a5" %}

      1. Stitch queries for boards that the authorizing user is a member of. In this example, the authorizing user's ID is `{{ authorizing-user-id }}`:

         ```sql
         SELECT id as user_id,
                idBoard
           FROM members
          WHERE id = '{{ authorizing-user-id }}'
         ```

         Which returns the following:

         ```markdown
         | id                       | idBoard                  |
         |--------------------------+--------------------------|
         | {{ authorizing-user-id }} | {{ board-id }} |
         ```

      2. Stitch queries for cards using the `idBoard` value returned in the first query:

         ```sql
         SELECT id as card_id,
                idBoard,
                <other card fields>
           FROM cards
          WHERE idBoard = '{{ board-id }}'
         ```

         Which returns the following:

         ```markdown
         | card_id                  | boardId                  |
         |--------------------------+--------------------------|
         | 5c26a3ce766676349d2f82d2 | {{ board-id }} |
         | 5c2e83a628ffe90351d0208b | {{ board-id }} |
         | 5c950cf7e1ad9b845171680b | {{ board-id }} |
         ```

      This approach is used for every table set to replicate. If you're missing data, verify that the authorizing user is a member of the board.

  - title: "Custom field support"
    anchor: "custom-field-support"
    content: |
      Custom fields are supported for the following tables:

      {% assign all-trello-tables = site.integration-schemas | where:"tap",integration.name | sort: name %}
      {% assign trello-this-version-tables = all-trello-tables | where:"version",integration.this-version %}
      {% assign tables-with-custom-field-support = trello-this-version-tables | where:"supports-custom-fields",true %}

      {% for table in tables-with-custom-field-support %}
      - [`{{ table.name }}`](#{{ table.name }})
      {% endfor %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/trello/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}