---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "1"
key: "collaborator"

name: "collaborators"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/collaborators.json
description: |
  The `{{ table.name }}` table contains info about the users who contribute to the repositories specified for the integration.

  For organization-owned repositories, this will include outside collaborators, organization owners, organization members that are direct collaborators, who have access through team memberships, or have access through default organization permissions.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List collaborators"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-repository-collaborators"

replication-method: "Full Table"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The collaborator's ID."
    foreign-key-id: "collaborator-id"

  - name: "login"
    type: "string"
    description: "The collaborator's username."

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: "The collaborator's type."

  - name: "url"
    type: "string"
    description: "The profile URL associated with the collaborator."
---