---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-zuora-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Zuora Source Form Property"
api-type: "platform.zuora"
display-name: "Zuora"

source-type: "saas"
docs-name: "zuora"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  # - name: "api_type"
  #   type: "string"
  #   description: "The {{ form-property.display-name }} API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/zuora#bulk-vs-rest-api)."

  - name: "european"
    type: "string"
    required: false
    description: "If `true`, the {{ form-property.display-name }} account being connected is based in Europe."
    value: "false"

  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the {{ form-property.display-name }} user authorizing the connection."
    value: "{{ sample-property-data.password }}"

  - name: "sandbox"
    type: "string"
    required: false
    description: "If `true`, the {{ form-property.display-name }} account being connected is a sandbox."
    value: "false"

  - name: "username"
    type: "string"
    required: true
    description: |
      The username of the {{ form-property.display-name }} user authorizing the connection. To successfully create a connection, this user must:

      1. **Have Standard user permissions across the board**,
      2. **Have two-factor authentication disabled**. Refer to this [{{ form-property.display-name }} article](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Two-Factor_Authentication) for assistance in disabling this setting.
      3. **Have credentials that don't expire**. This is only applicable if Password Expiration rules are enforced. Refer to [{{ form-property.display-name }}'s documentation](https://knowledgecenter.zuora.com/kb/How_do_I_prevent_my_API_user_login_from_expiring%3F) for a workaround.

      For more info, refer to our [{{ form-property.display-name }} integration documentation]({{ site.baseurl }}/integrations/saas/zuora#create-the-zuora-user).
    value: "{{ sample-property-data.user }}"
---