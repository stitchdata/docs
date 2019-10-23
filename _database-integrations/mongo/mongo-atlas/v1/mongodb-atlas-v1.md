---
title: MongoDB Atlas (v1)
keywords: mongodb, mongo, atlas, mongo atlas database integration, etl mongo, mongodb etl
permalink: /integrations/databases/mongodb-atlas/v1
summary: "Connect and replicate data from your MongoDB Atlas database using Stitch's MongoDB integration."
input: true
show-in-menus: true

key: "mongodb-atlas-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mongodb-atlas"
display_name: "MongoDB Atlas"

hosting-type: "mongodb-atlas"

this-version: "1.0"

driver: |
  [PyMongo 3.8.0](https://docs.mongodb.com/ecosystem/drivers/pymongo/){:target="new"}

setup-name: "MongoDB"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
singer: true
certified: true

frequency: "30 minutes"
tier: "Standard"
port: 27017
db-type: "mongo"

## Stitch features

versions: "2.6 through 4.0"
ssh: false
ssl: true

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true
set-default-replication-method: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: true
log-based-replication-read-replica: true

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: false

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.driver | flatify | strip }} driver.


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Privileges in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      **A {{ integration.display_name }} database using a version between {{ integration.versions | replace:"through","and" }}.** While older versions may be connected to Stitch, we may not be able to provide support for issues that arise due to unsupported versions.

      We recommend always keeping your version current as a best-practice. If you encounter connection issues or other unexpected behavior, verify that your {{ integration.display_name }} version is one supported by Stitch.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      In this step, you'll configure your {{ integration.display_name }} cluster to allow traffic from Stitch to access it. This is accomplished by whitelisting Stitch's IP addresses in the cluster's IP address whitelist in {{ integration.display_name }}.

      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include integrations/templates/create-database-user-tabs.html override-user-setup=true %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      In this section:

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Locate the database connection details in Mongo Atlas"
        anchor: "locate-database-connection-details"
        content: |
          {% include shared/connection-details/mongodb-atlas.html %}

      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          Click the **{{ defaults.field-names.ssl }}** checkbox. {{ integration.display_name }} requires SSL to connect successfully.

      - title: "Define Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#create-replication-schedule)." %}

          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}


# -------------------------- #
#    Replication Details     #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}
      
  - title: "{{ integration.setup-name }} Replication Keys"
    anchor: "mongo-replication-keys"
    content: |
      Unlike Replication Keys for other database integrations, those for {{ integration.setup-name }} have special considerations due to {{ integration.setup-name }} functionality. For example: {{ integration.setup-name }} allows multiple data types in a single field, which can cause records to be skipped during replication.

      Refer to the [{{ integration.setup-name }} Replication Keys guide]({{ rep-key | prepend: site.baseurl }}) before you define the Replication Keys for your {{ object }}s, as incorrectly defining Replication Keys can cause data discrepancies.

  - title: "Heavily nested data and destination column limits"
    anchor: "nested-data-replication-column-limits"
    content: |
      {{ integration.setup-name }} documents can contain heavily nested data, meaning an attribute can contain many other attributes.

      If your destination doesn't natively support nested data structures, Stitch will de-nest them to load them into the destination. Depending on how deeply nested the data is and the per table column limit of the destination, Stitch may encounter issues when loading heavily nested data.

      Refer to the [Nested Data Structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) for more info and examples.


# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## See _data/destinations/reference/incompatibilities.yml

has-incompatibilities: true
---
{% assign integration = page %}
{% include misc/data-files.html %}

## Troubleshooting

### Fields Missing from Replication Key Menu

If fields you expect to see are missing from a collection's Replication Key menu, it may be that the fields aren't indexed. Refer to the [Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) for more info.
