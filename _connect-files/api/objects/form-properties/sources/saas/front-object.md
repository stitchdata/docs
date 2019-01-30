---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


content-type: "api-form"
form-type: "source"
key: "source-form-properties-frontapp-object"

title: "Front Source Form Property"
api-type: "frontapp"
display-name: "Front"

source-type: "saas"
docs-name: "frontapp"

description: |
  **Note**: To use this integration, the user must have a [Premium or Enterprise {{ form-property.display-name }} plan](https://frontapp.com/pricing){:target="new"}. These plans include API access, which is required to use Stitch's {{ form-property.display-name }} integration.

object-attributes:
  - name: "incremental_range"
    type: "string"
    required: true
    description: |
      Defines how data will be aggregated. Accepted values are `daily` or `hourly`.
    value: "daily"

  - name: "token"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API token. Refer to the [{{ form-property.display-name }} setup guide]({{ doc-link }}) for instructions on how to generate this token.
    value: "<API_TOKEN>"
---