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
key: "source-form-properties-pendo-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Pendo Source Form Property"
api-type: "platform.pendo"
display-name: "Pendo"

source-type: "saas"
docs-name: "pendo"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "lookback_window"
    type: "string"
    required: false
    description: |
      The number of historical days' worth of data to replicate from the `start_date` value for each replication job for event streams. The default is `10`.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#event-replication" }}) for more info.
    value: "10"

  - name: "period"
    type: "string"
    required: true
    description: |
      The time period by which data is aggregated for event streams. Accepted values are:

      - `dayRange`
      - `hourRange`

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#event-replication" }}) for more info.
    value: "dayRange"

  - name: "x_pendo_integration_key"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} integration key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-integration-key" }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_INTEGRATION_KEY>"
---