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
key: "source-form-properties-mambu-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Mambu Source Form Property"
api-type: "platform.mambu"
display-name: "Mambu"

source-type: "saas"
docs-name: "mambu"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 
object-attributes:
  - name: "subdomain"
    type: "string"
    required: true
    description: "The subdomain of the {{ form-property.display-name }} account."
    value: "stitch.mambu.com"

  - name: "username"
    type: "string"
    required: true
    description: "The {{ form-property.display-name }} username used for login."
    value: "<USERNAME>"

  - name: "password"
    type: "string"
    required: true
    description: "The password for the {{ form-property.display-name }} user account."
    value: "<PASSWORD>"  	
---