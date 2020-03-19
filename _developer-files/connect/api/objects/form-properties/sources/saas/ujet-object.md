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
key: "source-form-properties-ujet-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "UJET Source Form Property"
api-type: "platform.ujet"
display-name: "UJET"

source-type: "saas"
docs-name: "ujet"

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
  - name: "company_key"
    type: "string"
    required: true
    description: |
      The company key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-keys" }}) to retrieve this information.
    value: "<YOUR_COMPANY_KEY>"

  - name: "company_secret"
    type: "string"
    required: true
    description: |
      The company secret code. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-keys" }}) to retrieve this information.
    value: "<YOUR_COMPANY_SECRET_CODE>"

  - name: "date_window_size"
    type: "string"
    required: true
    description: "This is an internal field for Stitch use."
    value: ""
    
  - name: "domain"
    type: "string"
    required: true
    description: "The domain of your {{ form-property.display-name }} account's web address."
    value: "ujet"
    
  - name: "subdomain"
    type: "string"
    required: true
    description: "The subdomain of your {{ form-propery.display-name }} account's web address."
    value: "your-subdomain"        
---