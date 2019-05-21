---
title: MongoDB
keywords: mongodb, mongo, database integration, etl mongo, mongodb etl
permalink: /integrations/databases/mongodb
summary: "Connect and replicate data from your MongoDB database using Stitch's Mongo integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mongodb"
display_name: "MongoDB"

hosting-type: "generic"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Paid"
port: 27017
db-type: "mongo"

## Stitch features

versions: "2.4 through 3.4"
ssh: true
ssl: true

## General replication features

anchor-scheduling: false
extraction-logs: false
loading-reports: true

table-selection: true
column-selection: false
table-level-reset: false

## Replication methods

define-replication-methods: false

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: false

view-replication: false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: "**A {{ integration.display_name }} server that uses Auth mode.** Auth mode requires every user who connects to Mongo to have a username and password. These credentials must be validated before the user will be granted access to the database."
  - item: |
      **To be using {{ integration.display_name }} version {{ integration.versions }}.** While older versions may be connected to Stitch, we may not be able to provide support for issues that arise due to unsupported versions.

      We recommend always keeping your version current as a best-practice. If you encounter connection issues or other unexpected behavior, verify that your {{ integration.display_name }} version is one supported by Stitch.


requirements-info: |
  Additionally, note that:

  - **If using SSL**, your server must require SSL connections. **Note**: SSL is **not** required to connect a {{ integration.display_name }} database to Stitch.
  - **If connecting via Atlas**, Stitch can only connect to instances using a **paid Atlas plan** with a **dedicated cluster**. The Free Atlas plan and shared clusters utilize a setup that Stitch doesn't currently support.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Index Replication Key fields"
    anchor: "index-replication-key-fields"
    content: |
      Before you jump into the actual setup, consider how the documents in your Mongo database are updated.

      Our Mongo integration uses [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) to replicate Mongo data, which means that only new and updated data will be replicated to your destination when a replication job runs. Stitch uses a field you designate - called a [Replication Key]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) - to identify new and updated data.

      There are two requirements for Mongo Replication Keys:

      1. **The field must be indexed**. Only indexed fields will display in the Replication Key drop-down.
      2. **The field must exist in the root of the document.** 

      Additionally, while this is not a strict requirement, **Replication Key fields should only contain a single, auto-incrementing data type**. If a field contains multiple data types or a data type that doesn't auto-increment, Stitch may have issues with detecting new/updated data.

      For a detailed look at Mongo Replication Keys, check out the [Selecting & Changing Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) before continuing.

  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include integrations/databases/setup/db-users/{{ integration.db-type }}.html %}

  - title: "Connect Stitch"
    anchor: "#connect-stitch"
    content: |
      {% capture mongo-conn %}
      Stitch uses a standalone server connection to connect to your MongoDB instance. What this means is that if you want Stitch to run on secondary instances, you have to give Stitch a host IP for one of your secondary instances.

      **In the case of Mongos (sharded Mongo)**, Stitch will always attempt to run data sync queries on your secondaries by default and you can provide the host IP for the master node.
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
  - title: "Supported Replication Methods"
    anchor: "supported-replication-methods"
    content: |
      Only Key-based Incremental Replication is supported for {{ integration.display_name }} integrations at this time. If a {{ object }} ever requires full replication - for example, to backfill existing rows with a new {{ col }}'s values - will require a full re-replication of the integration's data. Refer to the [Reset Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl | append: "#resetting-replication-keys" }}) for more info.

  - title: "{{ integration.display_name }} Replication Keys"
    anchor: "mongo-replication-keys"
    content: |
      Unlike Replication Keys for other database integrations, those for {{ integration.display_name }} have special considerations due to {{ integration.display_name }} functionality. For example: {{ integration.display_name }} allows multiple data types in a single field, which can cause records to be skipped during replication.

      Refer to the [{{ integration.display_name }} Replication Keys guide]({{ rep-key | prepend: site.baseurl }}) before you define the Replication Keys for your {{ object }}s, as incorrectly defining Replication Keys can cause data discrepancies.

  - title: "Data selection limitations"
    anchor: "data-selection-limitations"
    content: |
      {{ integration.display_name }} data can only be tracked at the collection level. This means that when a collection is set to replicate in Stitch, all documents in the collection will also be selected.

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
