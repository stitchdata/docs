---
tap-reference: "github"

# version: "1.0"

foreign-keys:
  - attribute: "sha"
    table: "commits"
    join-on: "sha"

  - attribute: ""
    table: "collaborators"
    join-on: "id"

  - attribute: "commit_id"
    table: "commits"
    join-on: "id"
---