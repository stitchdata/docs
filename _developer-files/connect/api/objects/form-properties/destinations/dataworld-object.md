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

## AUGUST 2020: Removing data.world from the API
## As per Mark, we're temporarily removing this destination from the API
## until we can figure out the best way to allow users to
## configure it. 

## It won't show up in the Connect docs unless the section
## below is uncommented:

# product-type: "connect"
# content-type: "api-form"
# form-type: "destination"
# key: "destination-form-properties-dataworld-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "data.world Destination Form Property"
api-type: "dataworld"
display-name: "data.world"

docs-name: "data-world"
db-type: "data-world"

property-description: |
  a {{ form-property.display-name }} account dataset


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} Account ID. Refer to the [{{ form-property.display-name }} documentation]({{ link.destinations.setup.data-world | prepend: site.baseurl | append: "#verify-account-id" }}) for more info.
    value: |
      "<YOUR_DATA_WORLD_ACCOUNT_ID>"

  - name: "output_file_format"
    type: "string"
    required: true
    description: |
      Defines the type of file Stitch will write to the bucket. Possible values are:

      - `csv`, which will use CSV (`.csv`) files
      - `jsonl`, which will use JSON (`.jsonl`) files
    value: |
      "jsonl"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://apidocs.data.world/toolkit/oauth"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The {{ form-property.display-name }} access token to use in future requests to the {{ form-property.display-name }} API, created after a successful OAuth handshake with {{ form-property.display-name }}.
    value: |
      "<ACCESS_TOKEN>"

  - name: "s3_bucket"
    type: "string"
    required: true
    credential: false
    description: |
      **This property is provided by Stitch and should not be set when creating or updating a {{ form-property.display-name }} destination.**
    value: "<S3_BUCKET>"

  - name: "s3_key_format_string"
    type: "string"
    required: true
    credential: false
    description: |
      **This property is provided by Stitch and should not be set when creating or updating a {{ form-property.display-name }} destination.**
    value: |
      "<S3_KEY_FORMAT_STRING>"
---