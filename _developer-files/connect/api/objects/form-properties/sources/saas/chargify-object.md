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
key: "source-form-properties-chargify-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Chargify Source Form Property"
api-type: "platform.chargify"
display-name: "Chargify"

source-type: "saas"
docs-name: "chargify"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      A {{ integration.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-api-key" }}) for instructions on creating this credential.
    value: "<YOUR_{{ form-property.display-name | upcase }}_API_KEY>"

  - name: "subdomain"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} subdomain. For example: If the full URL of your {{ form-property.display-name }} site were `https://stitch.my-{{ form-property.display-name | downcase }}-site.com`, this value would be `stitch`.
    value: "<YOUR_{{ form-property.display-name | upcase }}_SUBDOMAIN>"
---