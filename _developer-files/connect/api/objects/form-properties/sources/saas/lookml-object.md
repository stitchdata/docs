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
docs-name: "lookml" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


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
    description: "An API token which allows access to any project the user wants to replicate data from. **Note**: This access token must have the `repo` scope at a minimum. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-token" }}) for more info."
    value: "<API_TOKEN>"

  - name: "git_owner"
    type: "string"
    required: true
    description: "The owner of the GitHub repository you're replicating {{ form-property.display-name }} data from. You can find the owner in the URL of the repositories you want to replicate. Ex: `https://github.com/git-owner/git-repository`."
    value: "<GIT_OWNER>"  
  
  - name: "git_repositories"
    type: "string"
    required: true
    description: "The GitHub repository you're replicating {{ form-property.display-name }} data from. You can find the owner in the URL of the repositories you want to replicate. Ex: `https://github.com/git-owner/git-repository`. The repositories must be comma-delimited if replicating multiple repositories. Ex: `repository-1, repository-2`."
    value: "<GIT_REPOSITORY>"    
---