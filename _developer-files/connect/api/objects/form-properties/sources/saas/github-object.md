---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-github-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "GitHub Source Form Property"
api-type: "platform.github"
display-name: "GitHub"

source-type: "saas"
docs-name: "github"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: |
      An access token which allows access to any project the user wants to replicate data from. **Note**: This access token must have the `repo` scope at a minimum. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-token" }}) for more info.
    value: "<ACCESS_TOKEN>"

  - name: "repository"
    type: "string"
    required: true
    description: |
      The path or paths of the repository or repositories to be tracked. A repository path is relative to `https://github.com`. For example: The path for the Stitch Docs repository is `stitchdata/docs`

      To track multiple repositories, this value should be a space delimited list of the repository paths. For example:

      ```
      stitchdata/docs stitchdata/docs-about-docs
      ```
    value: "stitchdata/docs stitchdata/docs-about-docs"
---