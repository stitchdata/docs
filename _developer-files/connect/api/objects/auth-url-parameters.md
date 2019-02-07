---
product-type: "connect"
content-type: "api-url-parms"

parameters:
  - name: "client_id"
    required: true
    description: |
      Your application's client ID. This is the `partner_id` that is obtained when your [API access request]({{ api.access-api }}) is approved.

  - name: "redirect_uri"
    required: false
    description: |
      The callback URL for your application, which will be used in [Step 3](#authentication--callback-to-app).

      **Note**: If provided in Step 1 as a URL parameter, then the value must match one of the redirect URIs provided with your application's registration.

      If **not** provided in Step 1 as a URL parameter, Stitch will fallback to the first `redirect_uri` associated with your API client.

  - name: "email"
    required: false
    description: "The email address of the Stitch client owner. If provided, this value will be used to pre-populate the signup form."

  - name: "first_name"
    required: false
    description: "The user's first name. If provided, this value will be used to pre-populate the signup form."

  - name: "last_name"
    required: false
    description: "The user's last name. If provided, this value will be used to pre-populate the signup form."

  - name: "company"
    required: false
    description: "The name of the company or organization to associate with the Stitch client account. If provided, this value will be used to pre-populate the signup form."
---