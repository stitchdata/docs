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
key: "source-form-properties-looker-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Looker Source Form Property"
api-type: "platform.looker"
display-name: "Looker"

source-type: "saas"
docs-name: "looker" 


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_port"
    type: "string"
    required: true
    description: "The {{ form-property.display-name }} API Port number. This value will be `19999`, unless you host {{ form-property.display-name }} internally."
    value: "19999"

  - name: "api_version"
    type: "string"
    required: true
    description: "The {{form-property.display-name }} API version. This value will be `3.1`."
    value: "3.1"

  - name: "client_id"
    type: "string"
    required: true
    description: |
      The client ID portion of your {{ form-property.display-name }} API3 Key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-looker-api-keys" }}) for instructions on obtaining this information.
    value: "<YOUR_{{ form-property.display-name | upcase }}_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: |
      The client secret portion of your {{ form-property.display-name }} API3 Key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-looker-api-keys" }}) for instructions on obtaining this information.
    value: "<YOUR_{{ form-property.display-name | upcase }}_CLIENT_SECRET>"

  - name: "domain"
    type: "string"
    required: true
    description: "The domain of your {{ form-property.display-name }} URL. This value is typically `looker.com`, unless you have your own white-listed domain."
    value: "looker.com"
    
  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The subdomain of your {{ form-property.display-name }} URL. This is the leading part of your {{ form-property.display-name }} URL.

      For example: If the URL is `https://stitch.looker.com`, the value for this property would be `stitch`.
    value: "<YOUR_{{ form-property.display-name | upcase }}_SUBDOMAIN>"       
---