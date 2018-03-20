---
content-type: "api-endpoint"
endpoint: "accounts"
key: "create-an-account"
version: "3"
order: 1


title: "Create an account"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.accounts.create.short }}"
description: "{{ api.core-objects.accounts.create.description | flatify | markdownify }}"

arguments:
  - name: "company"
    required: true
    type: "string"
    description: "A name for the Stitch client. This is typically the name of the company using the Stitch client account."

  - name: "email"
    required: true
    type: "string"
    description: "The email address of the user signing up for a Stitch client account. Upon successful account creation, Stitch will send an email to this address with instructions for completing the setup."

  - name: "first_name"
    required: true
    type: "string"
    description: "The first name of the user signing up for a Stitch client account."

  - name: "last_name"
    required: true
    type: "string"
    description: "The last name of the user signing up for a Stitch client account."

  - name: "partner_id"
    required: true
    type: "string"
    description: "The unique ID for your API client, obtained when you register to use the API."

  - name: "partner_secret"
    required: true
    type: "string"
    description: "The secret for your API client, obtained when you registered to use the API."


returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an `access_token` property containing an API access token for the Stitch client's account will be returned.

  Otherwise, an error will be returned. For example: If a Stitch client account associated with the user already exists, the request will return `This email address is already associated with an active user.` See the **Errors** tab below for additional possibilities.

examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "email": "stitch-api-test@stitchdata.com",
                "last_name": "Product Team",
                "partner_id": "<PARTNER_ID>",
                "first_name": "Stitch",
                "partner_secret": "<PARTNER_SECRET>",
                "company": "Stitch Product Team"
              }"
  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      {
        "access_token":"<ACCESS_TOKEN>"
      }

  - type: "errors"
---