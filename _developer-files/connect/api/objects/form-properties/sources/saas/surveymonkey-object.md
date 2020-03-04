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
key: "source-form-properties-surveymonkey-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "SurveyMonkey Source Form Property"
api-type: "platform.surveymonkey"
display-name: "SurveyMonkey"

source-type: "saas"
docs-name: "surveymonkey" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads



# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: "The access token. This access token allows Stitch to access your {{ form-property.display_name }} account's API. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-access-token" }}) for instructions on locating this info."
    value: "<YOUR_ACCESS_TOKEN>"

  - name: "survey_id"
    type: "string"
    required: false
    description: "The survey ID. These survey IDs are used to pull simplified responses for specific surveys. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-survey-id" }}) for instructions on locating this info."
    value: "<YOUR_SURVEY_ID"  
---