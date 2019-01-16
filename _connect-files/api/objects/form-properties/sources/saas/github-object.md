---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-github-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "GitHub Source Form Property"
api-type: "github"
display-name: "GitHub"

source-type: "saas"
docs-name: "github"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: "An access token which allows access to any project the user wants to replicate data from."
    value: "<ACCESS_TOKEN>"

  - name: "repository"
    type: "string"
    required: true
    description: "The name of the repository to be tracked."
    value: "<REPOSITORY_NAME>"
---