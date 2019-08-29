---
title: MongoDB (v1)
keywords: mongodb, mongo, database integration, etl mongo, mongodb etl
permalink: /integrations/databases/mongodb/v1
summary: "Connect and replicate data from your MongoDB database using Stitch's Mongo integration."
input: false

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mongodb"
display_name: "MongoDB"

hosting-type: "generic"

this-version: "1.0"

driver: |
  [PyMongo 3.8.0](https://docs.mongodb.com/ecosystem/drivers/pymongo/){:target="new"}


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
ssh: true
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

view-replication: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Privileges in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: "**A {{ integration.display_name }} server that uses Auth mode.** Auth mode requires every user who connects to Mongo to have a username and password. These credentials must be validated before the user will be granted access to the database."
  - item: |
      **A {{ integration.display_name }} database using a version between {{ integration.versions | replace:"through","and" }}.** While older versions may be connected to Stitch, we may not be able to provide support for issues that arise due to unsupported versions.

      We recommend always keeping your version current as a best-practice. If you encounter connection issues or other unexpected behavior, verify that your {{ integration.display_name }} version is one supported by Stitch.


requirements-info: |
  Additionally, note that:

  - **If using SSL**, your server must require SSL connections. **Note**: SSL is **not** required to connect a {{ integration.display_name }} database to Stitch.
  - **If connecting via Atlas**, Stitch can only connect to instances using a **paid Atlas plan** with a **dedicated cluster**. The Free Atlas plan and shared clusters utilize a setup that Stitch doesn't currently support.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#connect-stitch)." %}
      
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      In this section:

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "todo"
        anchor: "todo"
        content: ""

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      {% capture mongo-conn %}
      Stitch uses a standalone server connection to connect to your MongoDB instance. What this means is that if you want Stitch to run on secondary instances, you have to give Stitch a host IP for one of your secondary instances.

      **In the case of Mongos (sharded Mongo)**, Stitch will always attempt to run data sync queries on your secondaries by default and you can provide the host address for the master node.
      {% endcapture %}

      {% include note.html first-line="**Stitch and MongoDB connections**" content=mongo-conn %}

      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" %}

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
      
  - title: "{{ integration.display_name }} Replication Keys"
    anchor: "mongo-replication-keys"
    content: |
      Unlike Replication Keys for other database integrations, those for {{ integration.display_name }} have special considerations due to {{ integration.display_name }} functionality. For example: {{ integration.display_name }} allows multiple data types in a single field, which can cause records to be skipped during replication.

      Refer to the [{{ integration.display_name }} Replication Keys guide]({{ rep-key | prepend: site.baseurl }}) before you define the Replication Keys for your {{ object }}s, as incorrectly defining Replication Keys can cause data discrepancies.

  - title: "Heavily nested data and destination column limits"
    anchor: "nested-data-replication-column-limits"
    content: |
      {{ integration.display_name }} documents can contain heavily nested data, meaning an attribute can contain many other attributes.

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

### SSL Connection Errors {#ssl-connection-errors}

{% assign ssl-error = site.data.errors.connection-checks.errors | where:"id","premature-file" %}

{% for error in ssl-error %}
```
{{ error.message }}
```

{{ error.meaning }}

{{ error.fix-it }}
{% for listitem in error.fix-it-list %}
- {{ listitem.item }}
{% endfor %}
{% endfor %}

### Fields Missing from Replication Key Menu

If fields you expect to see are missing from a collection's Replication Key menu, it may be that the fields aren't indexed. Refer to the [Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) for more info.
