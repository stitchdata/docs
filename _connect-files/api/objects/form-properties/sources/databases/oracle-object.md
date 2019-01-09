---
# content-type: "api-form"
# form-type: "source"
# key: "source-form-properties-oracle-object"

title: "Oracle Source Form Property"
api-type: "oracle"
display-name: "Oracle"

# source-type: "database"
#docs-name: "oracle"
# db-type: "oracle"

description: ""

uses-common-fields: true
uses-feature-fields: true

object-attributes:
  - name: "default_replication_method"
    type: "string"
    required: false
    description: |
      The Replication Method type to be used as the default method for tables set to replicate. Accepted values are:

      - `FULL_TABLE` - [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}) will be the default
      - `LOG_BASED` - [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) will be the default
    value: "LOG_BASED"

  - name: "filter_schemas"
    type: "string"
    required: false
    description: "**This is an internal field and is for Stitch use only.**"
    value: ""

  - name: "sid"
    type: "string"
    required: false
    description: "The site identifier associated with the Oracle instance."
    value: "<ORACLE_SID>"
---