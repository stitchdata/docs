---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-campaign-manager-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Campaign Manager Source Form Property"
api-type: "platform.doubleclick-campaign-manager"
display-name: "Campaign Manager"

source-type: "saas"
docs-name: "campaign-manager"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: false

object-attributes:
  - name: "profile_id"
    type: "string"
    required: true
    description: |
      The ID of the {{ form-property.display-name }} profile you want to replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl | append: "#locate-your-profile-id" }}) for instructions on retrieving this info.
    value: "<CAMPAIGN_MANAGER_PROFILE_ID>"
---