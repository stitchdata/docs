---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-yotpo-object"

title: "Yotpo Source Form Property"
description: |
  {{ api.form-properties.source-forms.yotpo.description }}

  **Note**: Creating a Yotpo source requires Yotpo API credentials. Retrieving these credentials requires Yotpo Account Administrator permissions. Refer to [Yotpo's documentation](https://support.yotpo.com/en/article/finding-your-app-key-and-your-secret-key){:target="new"} for more info.

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Yotpo" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date replace: "[INTEGRATION]","Yotpo" }}

  - name: "api_key"
    type: "string"
    required: true
    description: "The API Key for the Yotpo account Stitch should replicate data from. This is the **App Key** field in the Yotpo app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**."

  - name: "api_secret"
    type: "string"
    required: true
    description: |
      The API Secret for the Yotpo account Stitch should replicate data from. This is the **Secret Key** field in the Yotpo app, accessed by clicking **User menu (people icon) > Account Settings > Store tab**.

      **Note**: Yotpo Account Administrator permissions are required to retrieve this information.

examples: 
  - code: |
      {  
       "type":"platform.yotpo",
       "properties":{
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z",
          "api_key":"<YOTPO_API_KEY>",
          "api_secret":"<YOTPO_API_SECRET>"
        }
      }
---