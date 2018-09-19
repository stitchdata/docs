---
tap: "integration_name"

name: "table_name"
doc-link: ## link to source's API docs
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
<<<<<<< HEAD
  The `{{ table.name }}` table contains 
=======
  The `table_name` table contains info about 
>>>>>>> master

replication-method: "Incremental / Full Table"

api-method:
  name: 
  doc-link: 

attributes:
  - name: ""
    type: ""
    primary-key: true ## remove if this column isn't part of the table's PK
    description: ""
    doc-link:

  - name: ""
    type: 
    description: ""

  - name: ""
    type: "array"
    description:
    array-attributes:

  - name: ""
    type: "object"
    description:
    object-attributes:

---