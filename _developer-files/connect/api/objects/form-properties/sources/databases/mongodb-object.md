---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mongodb-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MongoDB Source Form Property"
api-type: "platform.mongodb"
display-name: "MongoDB"

source-type: "database"
docs-name: "mongodb"
db-type: "mongo"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
uses-feature-fields: true
uses-start-date: false

object-attributes:
  - name: "database"
    required: true
    internal: false
    type: "string"
    description: |
      The name of the authentication database for the `user` connecting the source.

      **Note**: For Atlas-based instances, this must be the `admin` database.
    value: "admin"

  - name: "replica_set"
    required: false
    internal: false
    type: "string"
    description: |
      The name of the replica set to be used for Log-based Incremental Replication.
    value: "<REPLICA_SET>"

  - name: "include_schemas_in_destination_stream_name"
    required: true
    internal: false
    type: "string"
    description: |
      If `true`, the name of the source schema will be included in the destination table name. For example: `<source_schema_name>__<table_name>`. This can help prevent table name collisions when two tables canonicalize to the same name.

      For more info, refer to the [Database Integration Table Name Collisions guide]({{ link.troubleshooting.database-table-name-collisions | prepend: site.baseurl }}).
    value: "false"
---