---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-lookml-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "LookML Source Form Property"
api-type: "platform.lookml"
display-name: "LookML"

source-type: "saas"
docs-name: "lookml"

## This is used to fill in the description that displays in the source form property rollup and under the object itself.

property-description: "GitHub repositories containing Looker {{ form-property.display-name }} code"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      A GitHub access token which allows access to any repository the user wants to replicate data from.
      
      **Note**: This access token must have the `repo` scope at a minimum. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-token" }}) for more info.
    value: "<API_TOKEN>"

  - name: "git_owner"
    type: "string"
    required: true
    description: |
      The name of owner of the GitHub repository to replicate {{ form-property.display-name }} data from. You can find the owner in the URL of the repositories you want to replicate. For example: If the URL of the repository is `https://github.com/stichdata/docs`, the repository owner would be `stitchdata`.
    value: "<GIT_REPOSITORY_OWNER>"  
  
  - name: "git_repositories"
    type: "string"
    required: true
    description: |
      A comma-delimited list of the GitHub repositories to replicate {{ form-property.display-name }} data from. The name of the repository is in its URL. For example: If the URL of the repository is `https://github.com/stichdata/docs`, the repository would be `docs`.
      
      - To track a single repository, this value should be just the name of the repository: `repository-1`
      - To track multiple repositories, this value should be comma-delimited: `repository-1, repository-2`, etc.
    value: "<GIT_REPOSITORY_NAME>"    
---
