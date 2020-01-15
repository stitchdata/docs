---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "accounts"
key: "create-an-account"
version: "3"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create an account"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.accounts.create.short }}"
description: "{{ api.core-objects.accounts.create.description | flatify | markdownify }}"

## This endpoint uses partner credentials for authorization
## No access token is required.
## Notes are in _includes/developers/api-resource-list.html
access-token-required: false


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "company"
    required: true
    type: "string"
    description: "A name for the Stitch client. This is typically the name of the company using the Stitch client account."
    example-value: |
      "Stitch Data"

  - name: "email"
    required: true
    type: "string"
    description: "The email address of the user signing up for a Stitch client account. Upon successful account creation, Stitch will send an email to this address with instructions for completing the setup."
    example-value: |
      "stitch@stitchdata.com"

  - name: "first_name"
    required: true
    type: "string"
    description: "The first name of the user signing up for a Stitch client account."
    example-value: |
      "Stitch"

  - name: "last_name"
    required: true
    type: "string"
    description: "The last name of the user signing up for a Stitch client account."
    example-value: |
      "Data"

  - name: "partner_id"
    required: true
    type: "string"
    description: "The unique ID for your API client, obtained when you register to use the API."
    example-value: |
      "<PARTNER_ID>"

  - name: "partner_secret"
    required: true
    type: "string"
    description: "The secret for your API client, obtained when you registered to use the API."
    example-value: |
      "<PARTNER_SECRET>"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and an object with `access_token` and `stitch_account_id` properties.

  Otherwise, an error will be returned. For example: If a Stitch client account associated with the user already exists, the request will return `This email address is already associated with an active user.` See the **Errors** tab below for additional possibilities.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Content-Type: application/json"
           -d "{
                "partner_id": "<PARTNER_ID>",
                "partner_secret": "<PARTNER_SECRET>",
                "first_name": "Stitch",
                "last_name": "Product Team",
                "company": "Stitch Product Team",
                "email": "stitch-api-test@stitchdata.com"
              }"
  - type: "Response"
    language: "json"
    code: |
      {
        "access_token": "at_<ACCESS_TOKEN>",
        "stitch_account_id": 136715
      }

  - type: "Errors"
---