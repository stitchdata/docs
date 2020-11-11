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
key: "source-form-properties-ebay-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "eBay Source Form Property"
api-type: "platform.ebay"
display-name: "eBay"

source-type: "saas"
docs-name: "ebay" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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
  - name: "client_id"
    type: "string"
    required: true
    description: |
      This is your App ID in your {{ form-property.display-name }} developer account. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-ids" }}) for instructions on retrieving this credential.
    value: "YOUR_APP_ID"

  - name: "client_secret"
    type: "string"
    required: true
    description: |
      This is your Cert ID in your {{ form-property.display-name }} developer account. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-ids" }}) for instructions on retrieving this credential.
    value: "YOUR_CERT_ID"

  - name: "refresh_token"
    type: "string"
    required: true
    description: |
      The refresh token for your {{ form-property.display-name }} app. This token has an expiration date, so keep note of it so that you can enter a new token into the Stitch integration when the time comes. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#grant-access" }}) for instructions on retrieving this credential.
    value: "YOUR_REFRESH_TOKEN"
    
  - name: "scope"
    type: "string"
    required: true
    description: |
      This determines which access privileges Stitch will have to your {{ form-property.display-name }}. For this integration, the scope is `sell.fulfillment.readonly`.
    value: "sell.fulfullment.readonly"      
---