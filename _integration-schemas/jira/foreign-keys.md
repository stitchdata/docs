---
tap-reference: "jira"

version: "1.0"

foreign-keys:
  - attribute: 
    table: "changelogs"
    join-on: "id"

  - attribute:  
    table: "issue_comments"
    join-on: "id"

  - attribute: "issueId"
    table: "issues"
    join-on: "id"

  - attribute: 
    table: "issue_transitions"
    join-on: "id"

  - attribute: "projectTypeKey"
    table: "project_types"
    join-on: "key"

  - attribute: ""
    table: "project_categories"
    join-on: "id"

  - attribute: "projectId"
    table: "projects"
    join-on: "id"

  - attribute: 
    table: "resolutions"
    join-on: "id"

  - attribute:  
    table: "roles"
    join-on: "id"

  - attribute:  
    table: "users"
    join-on: "key"

  - attribute: 
    table: "versions"
    join-on: "id"

  - attribute:  
    table: "worklogs"
    join-on: "id"
---