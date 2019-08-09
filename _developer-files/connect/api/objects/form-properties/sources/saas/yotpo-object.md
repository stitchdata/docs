---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-yotpo-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Yotpo Source Form Property"
api-type: "platform.yotpo"
display-name: "Yotpo"

source-type: "saas"
docs-name: "yotpo"

description: |
  **Note**: Creating a {{ form-property.display-name }} source requires {{ form-property.display-name }} API credentials. Retrieving these credentials requires {{ form-property.display-name }} Account Administrator permissions. Refer to [{{ form-property.display-name }}'s documentation](https://support.yotpo.com/en/article/finding-your-app-key-and-your-secret-key){:target="new"} for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The API Key for the {{ form-property.display-name }} account Stitch should replicate data from. This is the **App Key** field in the {{ form-property.display-name }} app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**."
    value: "<API_KEY>"

  - name: "api_secret"
    type: "string"
    required: true
    description: |
      The API Secret for the {{ form-property.display-name }} account Stitch should replicate data from. This is the **Secret Key** field in the {{ form-property.display-name }} app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**.

      **Note**: {{ form-property.display-name }} Account Administrator permissions are required to retrieve this information.
    value: "<API_SECRET>"
---