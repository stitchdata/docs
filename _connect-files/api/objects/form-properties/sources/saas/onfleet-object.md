---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## PLEASE REMOVE COMMENTS WHEN FINISHED


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-onfleet-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Onfleet Source Form Property"
api-type: "platform.onfleet"
display-name: "Onfleet"

source-type: "saas"
docs-name: "onfleet"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

# uses-common-fields: true/false
# See these fields in _data/connect/common/all-sources.yml
# May also include applicable fields in _data/connect/common/all-sources.yml

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_API_KEY>"

  - name: "quota_limit"
    type: "string"
    required: true
    description: |
      The percentage of the {{ form-property.display-name }} API quota Stitch is allowed to use for this connection.

      [{{ form-property.display-name }} limits API requests](http://docs.onfleet.com/docs/throttling){:target="new"} to 20 requests per second across all API keys in a given {{ form-property.display-name }} account.

      For example: If this value is `10`, Stitch would be allowed to use 10% of the API quota, or 2 requests per second.
    value: "10"
---