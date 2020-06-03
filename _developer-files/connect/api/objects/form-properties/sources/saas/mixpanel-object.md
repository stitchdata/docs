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
key: "source-form-properties-mixpanel-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Mixpanel Source Form Property"
api-type: "platform.mixpanel"
display-name: "Mixpanel"

source-type: "saas"
docs-name: "mixpanel" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_secret"
    type: "string"
    required: true
    description: |
      The API secret of your project in your {{ form-property.display-name }} account. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-timezone-api-secret" }}) for instructions on obtaining this information. 
    value: "YOUR_API_SECRET"

  - name: "attribution_window"
    type: "string"
    required: true
    description: |
      Defines the number, in days, Stitch should use as an attribution window. To ensure your {{ form-property.display-name }} and Stitch settings align, we recommend using the same attribution window in Stitch that you use in {{ form-property.display-name }}. The default value for these attribution windows is five days. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#attribution-windows" }}) for more information about attribution windows for this integration.
    value: "XX"
  
  - name: "date_window_size"
    type: "string"
    required: true
    description: |
      Number of days for date window looping through transactional endpoints with `from_date` and `to_date`. The default `date_window_size` is 30 days.

      **Note**: If your project has large volumes of events, you may want to decrease the number of days to 14, 7, or even down to 1-2 days.
    value: "<XX>"
  
  - name: "project_timezone"
    type: "string"
    required: true
    description: |
      The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the {{ form-property.display-name }} console. For more information on Mixpanel's project timezones, [click here](https://help.mixpanel.com/hc/en-us/articles/115004547203-Manage-Timezones-for-Projects-in-Mixpanel).
    value: "US/Pacific"
  
  - name: "select_properties_by_default"
    type: "string"
    required: false
    description: |
      A confifguration parameter - the only accepted values are `true` and `false`. When set to `true`, this parameter captures new properties in the `events` and `engage` tables' records. If set to false, new properties will be ignored.
    value: "true"
---