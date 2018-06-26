---
title: MongoDB
keywords: mongodb, mongo, database integration, etl mongo, mongodb etl
tags: [database_integrations]
permalink: /integrations/databases/mongodb
summary: "Connect and replicate data from your MongoDB database using Stitch's Mongo integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mongodb"
display_name: "MongoDB"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Premium"
port: 27017
db-type: "mongo"
icon: /images/integrations/icons/mongodb.svg

versions: "2.4 through 3.4"
ssh: true
ssl: true
sync-views: false
whitelist:
  tables: true
  columns: false

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

  - **If using SSL**, your server must require SSL connections. Note that SSL is **not** required to connect a {{ integration.display_name }} database to Stitch.
  - **If connecting via Atlas**, Stitch can only connect to instances using a **paid Atlas plan**. The Free Atlas plan utilizes a setup that Stitch doesn't currently support.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Index Replication Key Fields"
    anchor: "index-replication-key-fields"
    content: |
      Before you jump into the actual setup, consider how the documents in your Mongo database are updated.

      Our Mongo integration uses [Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}) to replicate Mongo data, which means that only new and updated data will be replicated to your data warehouse when a sync runs. Stitch uses a field you designate - called a [Replication Key]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) - to identify new and updated data.

      There are two requirements for Mongo Replication Keys:

      1. **The field must be indexed**. Only indexed fields will display in the Replication Key drop-down.
      2. **The field must exist in the root of the document.** 

      Additionally, while this is not a strict requirement, **Replication Key fields should only contain a single, auto-incrementing data type**. If a field contains multiple data types or a data type that doesn't auto-increment, Stitch may have issues with detecting new/updated data.

      For a detailed look at Mongo Replication Keys, check out the [Selecting & Changing Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) before continuing.

  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "create db user"

  - title: "connect stitch"
    content: |

      {% capture mongo-conn %}
      **Stitch & Mongo Connections**<br>

      Stitch uses a standalone server connection to connect to your MongoDB instance. What this means is that if you want Stitch to run on secondary instances, you have to give Stitch a host IP for one of your secondary instances.<br><br>

      **In the case of Mongos (Sharded Mongo)**, Stitch will always attempt to run data sync queries on your secondaries by default and you can provide the host IP for the master node.
      {% endcapture %}

      {% include note.html content=mongo-conn %}

  - title: "replication frequency"

  - title: "sync data"

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

incompatible:
  redshift: "sometimes"
  reason: "As a result of the de-nesting Stitch performs on nested structures, deeply nested data in Mongo may result in tables that exceed Redshift's 1,600 column limit."

  panoply: "sometimes"
  reason: "As a result of the de-nesting Stitch performs on nested structures, deeply nested data in Mongo may result in tables that exceed Panoply's 1,600 column limit."
---
{% assign integration = page %}
{% include misc/data-files.html %}

---

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
