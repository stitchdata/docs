---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zuora-object"

title: "Zuora Source Form Property"
api-type: "zuora"
display-name: "Zuora"

source-type: "saas"
docs-name: "zuora"

description: ""

object-attributes:
  # - name: "api_type"
  #   type: "string"
  #   description: "The zuora API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/zuora#bulk-vs-rest-api)."

  - name: "european"
    type: "string"
    required: false
    description: "If `true`, the Zuora account being connected is based in Europe."
    value: "false"

  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the Zuora user authorizing the connection."
    value: "{{ sample-property-data.password }}"

  - name: "sandbox"
    type: "string"
    required: false
    description: "If `true`, the Zuora account being connected is a sandbox."
    value: "false"

  - name: "username"
    type: "string"
    required: true
    description: |
      The username of the Zuora user authorizing the connection. To successfully create a connection, this user must:

      1. **Have Standard user permissions across the board**,
      2. **Have two-factor authentication disabled**. Refer to this [Zuora article](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication) for assistance in disabling this setting.
      3. **Have credentials that don't expire**. This is only applicable if Password Expiration rules are enforced. Refer to [Zuora's documentation](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F) for a workaround.

      For more info, refer to our [Zuora integration documentation]({{ site.baseurl }}/integrations/saas/zuora#create-the-zuora-user).
    value: "{{ sample-property-data.user }}"
---