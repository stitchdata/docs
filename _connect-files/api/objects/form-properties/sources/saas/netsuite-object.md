---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-netsuite-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "NetSuite Source Form Property"
api-type: "platform.netsuite"
display-name: "NetSuite"

source-type: "saas"
docs-name: "netsuite"

## This is used to fill in the description that displays in the source form property rollup and under the object itself.

property-description: "the NetSuite SuiteTalk API"

## Full copy is: "NetSuite connections read data from [the NetSuite SuiteTalk API] and correspond to source type: platform.netsuite."


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "account"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} account ID. If the account ID includes a suffix, it should be included. For example: `1234567_sb2`

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#locate-netsuite-account-id" }}) for instructions on retrieving this info.
    value: "1234567_sb2"

  - name: "consumer_key"
    type: "string"
    required: true
    description: |
      The consumer key for Stitch's integration record in the user's {{ form-property.display-name }} account. This is used when performing token-based authentication to {{ form-property.display-name }}.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-stitch-integration-record" }}) for instructions on retrieving this info.
    value: "<{{ form-property.display-name | upcase }}_CONSUMER_KEY>"

  - name: "consumer_secret"
    type: "string"
    required: true
    description: |
      The consumer secret for Stitch's integration record in the user's {{ form-property.display-name }} account. This is used when performing token-based authentication to {{ form-property.display-name }}.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-stitch-integration-record" }}) for instructions on retrieving this info.
    value:  "<{{ form-property.display-name | upcase }}_CONSUMER_SECRET>"

  - name: "token_id"
    type: "string"
    required: true
    description: |
      The token ID, created as part of generating access tokens for Stitch's integration record in the user's {{ form-property.display-name }} account. This is used when performing token-based authentication to {{ form-property.display-name }}.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-tokens" }}) for instructions on retrieving this info.
    value: "<{{ form-property.display-name | upcase }}_TOKEN_ID>"

  - name: "token_secret"
    type: "string"
    required: true
    description: |
      The token secret, created as part of generating access tokens for Stitch's integration record in the user's {{ form-property.display-name }} account. This is used when performing token-based authentication to {{ form-property.display-name }}.

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-tokens" }}) for instructions on retrieving this info.
    value: "<{{ form-property.display-name | upcase }}_TOKEN_SECRET>"
---