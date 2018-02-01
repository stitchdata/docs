---
content-type: "embed-endpoint"
endpoint: "accounts"
key: "create-an-account"
version: "3"
order: 1


title: "Create an account"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  Create a new Stitch client account and receive an API access in return.

  Before creating a Stitch account, you'll need to register as an API client by contacting [{{ page.contact-email }}](mailto:{{ page.contact-email }}).


arguments:
  - name: "company"
    required: true
    description: "A name for the Stitch client. This is typically the name of the company using the Stitch client account."

  - name: "email"
    required: true
    description: "The email address of the user signing up for a Stitch client account. Upon successful account creation, Stitch will send an email to this address with instructions for completing the setup."

  - name: "first_name"
    required: true
    description: "The first name of the user signing up for a Stitch client account."

  - name: "last_name"
    required: true
    description: "The last name of the user signing up for a Stitch client account."

  - name: "partner_id"
    required: true
    description: "The unique ID for your API client, obtained when you register to use the {{ page.api-name }}."

  - name: "partner_secret"
    required: true
    description: "The secret for your API client, obtained when you registered to use the {{ page.api-name }}."


returns: "An `access_token` property containing an API access token for the Stitch client's account."

examples:
  - type: "request"
    language: ""
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "email": "{{ page.contact-email }}",
                "last_name": "Product Team",
                "partner_id": "<PARTNER_ID>",
                "first_name": "Stitch",
                "partner_secret": "<PARTNER_SECRET>",
                "company": "Stitch Product Team"
              }"
  - type: "response"
    language: ""
    code: |
      
      
---