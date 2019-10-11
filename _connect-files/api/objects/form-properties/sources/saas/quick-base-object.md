---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-quickbase-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Quick Base Source Form Property"
api-type: "platform.quickbase"
display-name: "Quick Base"

source-type: "saas"
docs-name: "quick-base"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "qb_appid"
    type: "string"
    required: true
    description: |
      The ID of the Quick Base app the user wants to connect. This is a unique alpha-numeric string that can be found in the app's URL when the user is logged into Quick Base.

      For example: If the app URL is `https://stitchdata.quickbase.com/db/bngf9ix7e`, the app ID is `bngf9ix7e`.
    value: "<APPID>"

  - name: "qb_url"
    type: "string"
    required: true
    description: |
      The URL of the user's Quick Base realm. This value must include the `https://` and the trailing backslash after `db/`.

      For example: If the realm URL is `https://stitchdata.quickbase.com/db/main?a=myqb`, the URL required is `https://stitchdata.quickbase.com/db/`.
    value: "https://<your-subdomain-here>.quickbase.com/db/"

  - name: "qb_user_token"
    type: "string"
    required: true
    description: |
      The user's Quick Base user token. [Refer to Stitch's Quick Base documentation for creation instructions]({{ site.baseurl }}/integrations/saas/quick-base#create-quick-base-user-token).
    value: "<QUICK_BASE_USER_TOKEN>"
---