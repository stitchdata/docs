---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-yotpo-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Yotpo Source Form Property"
api-type: "yotpo"
display-name: "Yotpo"

source-type: "saas"
docs-name: "yotpo"

description: |
  **Note**: Creating a Yotpo source requires Yotpo API credentials. Retrieving these credentials requires Yotpo Account Administrator permissions. Refer to [Yotpo's documentation](https://support.yotpo.com/en/article/finding-your-app-key-and-your-secret-key){:target="new"} for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The API Key for the Yotpo account Stitch should replicate data from. This is the **App Key** field in the Yotpo app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**."
    value: "<API_KEY>"

  - name: "api_secret"
    type: "string"
    required: true
    description: |
      The API Secret for the Yotpo account Stitch should replicate data from. This is the **Secret Key** field in the Yotpo app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**.

      **Note**: Yotpo Account Administrator permissions are required to retrieve this information.
    value: "<API_SECRET>"
---