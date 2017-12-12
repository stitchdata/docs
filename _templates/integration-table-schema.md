---
tap: "integration_name"

name: "table_name"
doc-link: ## link to source's API docs
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  ## description of the table

notes: 

replication-method: "Incremental / Full Table"

attributes:
  - name: ""
    type: ""
    primary-key: true ## remove if this column isn't part of the table's PK
    description: ""
    doc-link:

  - name: ""
    type: "array"
    description:
    array-attributes:

  - name: ""
    type: "object"
    description:
    object-attributes:

---