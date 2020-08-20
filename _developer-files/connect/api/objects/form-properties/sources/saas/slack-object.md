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
key: "source-form-properties-slack-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Slack Source Form Property"
api-type: "platform.slack"
display-name: "Slack"

source-type: "saas"
docs-name: "slack" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "date_window_size"
    type: "string"
    required: false
    description: |
      The number of days of {{ form-property.display-name }} data to replicate during each replication. The default number of days to replicate is seven.
    value: "7"

  - name: "lookback_window"
    type: "string"
    required: false
    description: |
      The number of historical days worth of data to replicate from the start date, for each replication. Lookback windows can only be applied to the `files` and `remote_files` tables in your {{ form-property.display-name }} integration.
    value: "7"

  - name: "token"
    type: "string"
    required: true
    description: |
      The verification token to connect your {{ form-property.display-name }} workspace to Stitch. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#verification-token" }}) for instructions on retrieving this information.
    value: "<YOUR_VERIFICATION_TOKEN>"

  - name: "join_public_channels"
    type: "string"
    required: false
    description: |
      This allows you to join all public channels in your {{ form-property.display-name }} workspace so that you can replicate data from them, and not just the ones that you have personally joined.
    value: "true/false"

  - name: "private_channels"
    type: "string"
    required: false
    description: |
      This allows you to include data from private channels in your {{ form-property.display-name }} workspace.
    value: "true/false"

  - name: "exclude_archived"
    type: "string"
    required: false
    description: |
      This allows you to exclude data from archived channels in your {{ form-property.display-name }} workspace.
    value: "true/false"  
---