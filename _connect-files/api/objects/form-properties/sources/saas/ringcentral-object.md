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
key: "source-form-properties-ringcentral-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "RingCentral Source Form Property"
api-type: "platform.ringcentral"
display-name: "RingCentral"

source-type: "saas"
docs-name: "ringcentral"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_url"
    type: "string"
    required: true
    description: |
      The API URL used by the {{ form-property.display-name }} developer application. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on generating this info.
    value: "https://platform.ringcentral.com"

  - name: "client_id"
    type: "string"
    required: true
    description: |
      The client ID for the {{ form-property.display-name }} developer application. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on generating this credential.
    value: "<CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: |
      The client secret for the {{ form-property.display-name }} developer application. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on generating this credential.
    value: "<CLIENT_SECRET>"

  - name: "password"
    type: "string"
    required: true
    description: |
      The password for the {{ form-property.display-name }} developer application.
    value: "<PASSWORD>"

  - name: "username"
    type: "string"
    required: true
    description: |
      The username for the {{ form-property.display-name }} application. This is typically the phone number used to create the app.
    value: "9991234567"
---