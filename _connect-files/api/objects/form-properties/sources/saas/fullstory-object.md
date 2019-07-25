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
api-type: "platform.fullstory"
display-name: "FullStory"

source-type: "saas"
docs-name: "fullstory"

description: |
  **Note**: To use this integration, the user must have a {{ form-property.display-name }} account with the [{{ form-property.display-name }} Data Export Pack add-on](https://help.fullstory.com/technical-questions/data-export). This is a paid addition that allows users to export raw event data, and is required to use {{ form-property.display-name }}'s Data Export REST API.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} API key, used to authenticate to {{ form-property.display-name }}'s Data Export API.
    value: "<API_KEY>"
---