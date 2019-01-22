---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-fullstory-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "FullStory Source Form Property"
api-type: "fullstory"
display-name: "FullStory"

source-type: "saas"
docs-name: "fullstory"

description: |
  **Note**: To use this integration, the user must have a FullStory account with the [FullStory Data Export Pack add-on](https://help.fullstory.com/technical-questions/data-export). This is a paid addition that allows users to export raw event data, and is required to use FullStory's Data Export REST API.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      A FullStory API key, used to authenticate to FullStory's Data Export API.
    value: "<API_KEY>"
---