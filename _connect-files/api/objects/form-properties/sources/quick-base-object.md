---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-quickbase-object"

title: "Quick Base Source Form Property"
description: "{{ api.form-properties.source-forms.quickbase.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Quick Base" }}

  - name: "qb_appid"
    type: "string"
    required: true
    description: |
      The ID of the Quick Base app the user wants to connect. This is a unique alpha-numeric string that can be found in the app's URL when the user is logged into Quick Base.

      For example: If the app URL is `https://stitchdata.quickbase.com/db/bngf9ix7e`, the app ID is `bngf9ix7e`.

  - name: "qb_url"
    type: "string"
    required: true
    description: |
      The URL of the user's Quick Base realm. This value must include the `https://` and the trailing backslash after `db/`.

      For example: If the realm URL is `https://stitchdata.quickbase.com/db/main?a=myqb`, the URL required is `https://stitchdata.quickbase.com/db/`.

  - name: "qb_user_token"
    type: "string"
    required: true
    description: |
      The user's Quick Base user token. [Refer to Stitch's Quick Base documentation for creation instructions]({{ site.baseurl }}/integrations/saas/quick-base#create-quick-base-user-token).

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Quick Base" }}

examples: 
  - code: |
      {  
       "type":"platform.quickbase",
       "properties":{  
          "frequency_in_minutes":"30",
          "qb_appid":"<APP_ID>",
          "qb_url":"https://your-company-name.quickbase.com/db/",
          "qb_user_token":"<USER_TOKEN>",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---