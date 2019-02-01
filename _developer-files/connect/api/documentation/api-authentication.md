---
title: Authentication
type: "connect"
content-type: "api-doc"
order: 3

sections:
  - content: |
      {% assign api = site.data.connect.api %}
      Authenticate your calls to the API by providing an access token in your requests. Each access token is associated with a single Stitch client account. Access tokens do not expire, but they may be revoked by the user at any time.

      Additionally, each request's permissions are limited to that Stitch client account.

      In the examples in this documentation, we use bearer auth:

      ```curl
      curl -X GET {{ api.base-url }}{{ api.core-objects.sources.base }}
           -H "Authorization: Bearer <ACCESS_TOKEN>"
      ```

      Before you can make requests, you must complete [this form]({{ site.data.connect.api.interest-form }}){:target="new"}. Once approved, you'll receive the credentials required to authenticate your API calls.

      All requests must be made over HTTPS or they will fail. API requests that don't contain authentication will also fail.

  - title: "Generate access tokens"
    anchor: "generate-access-tokens"
    content: |
      Access tokens are obtained by performing an OAuth2 handshake with an existing Stitch client account or by creating a new account via the API.

    subsections:
      - title: "New Stitch clients"
        anchor: "generate-access-token-new-stitch-client"
        content: |
          As an API client, you can create a new Stitch client account with the [Create Account endpoint]({{ api.core-objects.accounts.create.section }}):

          ```curl
          curl -X {{ api.core-objects.accounts.create.method | upcase }} {{ api.core-objects.accounts.create.name | prepend: api.base-url | flatify | strip_newlines }}
               -H "Content-Type: application/json"
               -d "{
                    "email": "stitch-api-test@stitchdata.com",
                    "last_name": "Product Team",
                    "partner_id": "<PARTNER_ID>",
                    "first_name": "Stitch",
                    "partner_secret": "<PARTNER_SECRET>",
                    "company": "Stitch Product Team"
                  }"
          ```

          When successful, this endpoint returns a status of `200 OK` and an access token:

          ```json
          {
            "access_token":"<ACCESS_TOKEN>"
          }
          ```

          The created account is owned and managed by the user it is created for, and that user will be able to login to the Stitch web interface and receive emails from Stitch.

      - title: "Existing Stitch clients, using OAuth2"
        anchor: "existing-stitch-clients-oauth2"
        content: |
          You can connect to a user's existing Stitch client account by having the user complete a standard OAuth flow. Before generating OAuth tokens, registering your application with Stitch. 

          Then, follow these steps to complete the OAuth flow:

          {% for step in subsection.steps %}
          - [Step {{ forloop.index }}: {{ step.title }}](#{{ step.anchor }})
          {% endfor %}

        steps:
          - title: "Send the user to Stitch"
            anchor: "authentication--send-user-to-stitch"
            content: |
              To initiate the authorization flow, the user will click a link to Stitch that includes your application's API client ID. This is the `partner_id` you obtained when you registered your application:

              ```shell
              https://app.stitchdata.com/oauth/authorization?client_id={CLIENT_ID}
              ```

              While only your `client_id` (`partner_id`) is required, the URL may also include the following parameters:

              {% assign all-connect-docs = site.developer-files | where:"type","connect" %}
              {% assign auth = all-connect-docs | where:"content-type","api-url-parms" %}

              <table class="attribute-list">
              {% for item in auth %}
              {% for parameter in item.parameters %}
              <tr>
              <td class="attribute-name">
              <strong>{{ parameter.name }}</strong>
              <br>

              {% case parameter.required %}
              {% when true %}
              <font color="#cc3399">REQUIRED</font>
              {% else %}
              OPTIONAL
              {% endcase %}

              </td>

              <td class="description">
              {{ parameter.description | flatify | markdownify }}
              </td>

              </tr>
              {% endfor %}
              {% endfor %}
              </table>

          - title: "Get consent"
            anchor: "authentication--get-consent"
            content: |
              If the user isn't already logged into their Stitch client account, they will be prompted to do so or create a new account, if need be.

              Once logged in, the user will be shown a screen explaining that your application has requested access to their Stitch account. They will be prompted to accept or reject this request.

          - title: "Callback to your application"
            anchor: "authentication--callback-to-app"
            content: |
              When the user accepts or denies the request, they will be re-directed to the callback URL you provided when you registered your application with Stitch.

              If the user denies the request, Stitch will include error details:

              ```shell
              https://yourapplication.com/callback?error=access_denied
              ```

              If the user accepts the request, the callback will include a temporary authorization code to be used in the next step:

              ```shell
              https://yourapplication.com/callback?code=AUTHORIZATION_CODE
              ```


          - title: "Exchange tokens"
            anchor: "authentication--exchange-tokens"
            content: |
              Lastly, when your application receives the user's request to the callback URL, it should make a request to the Stitch OAuth URL to exchange the temporary authorization code for a permanent access token:

              ```curl
              curl {{ api.base-url }}/oauth/token 
                   -d client_secret=<CLIENT_SECRET>
                   -d code=<AUTHORIZATION_CODE>
                   -d grant_type=authorization_code
              ```

              **Note**: Each temporary authorization code can only be used once and will expire five minutes after creation.

              If successful, Stitch will respond with the following:

              ```json
              {
                "token_type": "bearer",
                "access_token": <ACCESS_TOKEN>,
                "stitch_account_id": <STITCH_ACCOUNT_ID>
              }
              ```

              Your application should store the `access_token` and `stitch_account_id` somewhere secure, and use them to make calls to the API:

              ```curl
              curl {{ api.core-objects.sources.list.method | upcase }} {{ api.core-objects.sources.list.name | prepend: api.base-url | flatify }}
                   -H 'Authorization: Bearer <ACCESS_TOKEN>'
              ```
---