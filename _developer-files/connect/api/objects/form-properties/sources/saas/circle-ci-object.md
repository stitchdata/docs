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
key: "source-form-properties-circle-ci-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "CircleCI Source Form Property"
api-type: "platform.circle-ci"
display-name: "CircleCI"

source-type: "saas"
docs-name: "circle-ci" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "project_slugs"
    type: "string"
    required: true
    description: |
      Your project slugs. This is a space-separated list. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl | append: "#create-your-project-slugs" }}) for instructions on how to create a project slug.
    value: "<PROJECT_TYPE>/<ORG_NAME>/<REPO_NAME>"

  - name: "token"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} API token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl | append: "#create-api-token" }}) for instructions on how to create a one.
    value: "<API_TOKEN>"  
---