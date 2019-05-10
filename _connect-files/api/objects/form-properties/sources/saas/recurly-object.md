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

content-type: "api-form"
form-type: "source"
key: "source-form-properties-recurly-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Recurly Source Form Property"
api-type: "platform.recurly"
display-name: "Recurly"

source-type: "saas"
docs-name: "recurly"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on generating this credential.
    value: "<API_KEY>"

  - name: "quota_limit"
    type: "string"
    required: true
    description: |
      The percentage of the API rate limit that should be allocated to Stitch replicating from {{ form-property.display-name }}. For example: A value of `30` would be `30%` of the rate limit. Refer to [{{ form-property.display-name }}'s documentation](https://dev.recurly.com/docs/rate-limits){:target="new"} for more info.
    value: "30"

  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} subdomain. For example: If the full URL were `https://stitchdata.recurly.com`, the value of this property would be `stitchdata`.
    value: "<RECURLY_SUBDOMAIN>"
---