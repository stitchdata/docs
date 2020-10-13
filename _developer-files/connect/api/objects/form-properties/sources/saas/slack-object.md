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
      The number of days to replicate for each request made for applicable streams during a replication job. The default is `7`.

      This property applies to the following streams: 

      - `files`
      - `messages`
      - `remote_files`

      For example: If this value is `7`, Stitch will replicate 7 days' worth of data for each request made for the `files` stream.

      **Note:** This doesn't mean only seven days' worth of data is replicated for each replication job, as Stitch can make several API requests for the same stream over the course of a job. This is implemented to more efficiently replicate data and prevent issues with {{ form-property.display-name }}'s API.
    value: "7"

  - name: "lookback_window"
    type: "string"
    required: false
    description: |
      The number of historical days' worth of data to replicate from the `start_date` value for each replication job for the `files` and `remote_files` streams. The default is `14`.
    value: "7"

  - name: "token"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} app bot user OAuth access token, generated after you create a {{ form-property.display-name }} app, assign the required scopes, and install the app in your {{ integration.display_name }} workspace. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#verification-token" }}) for instructions on retrieving this information.
    value: "<YOUR_APP_BOT_USER_OAUTH_ACCESS_TOKEN>"

  - name: "join_public_channels"
    type: "string"
    required: false
    description: |
      If `true`, then the integration will have your {{ form-property.display-name }} app join all public channels in your {{ form-property.display-name }} workspace and not just the ones you have personally joined. The default is `true`.
    value: "true"

  - name: "private_channels"
    type: "string"
    required: false
    description: |
      If `true`, then the integration will replicate data for private channels in your {{ form-property.display-name }} workspace. The default is `true`.
    value: "true"

  - name: "exclude_archived"
    type: "string"
    required: false
    description: |
      If `false`, then the integration will replicate data for archived channels in your {{ form-property.display-name }} workspace. The default is `false`.
    value: "false"  
---