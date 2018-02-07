---
title: Authentication
content-type: "embed-doc"
order: 3

sections:
  - content: |
      Authenticate your calls to the {{ page.api-name }} by providing an access token in your requests. Each access token is associated with a single Stitch client account. Additionally, each request's permissions are limited to that Stitch client account.

      In the examples in this documentation, we use bearer auth:

      ```curl
      curl - X GET {{ page.api-base-url }}/v4/sources
           - H "Authorization: Bearer <ACCESS_TOKEN>"
      ```

      Before you can make requests, you must register as an API client by emailing [{{ page.contact-email }}](mailto:{{ page.contact-email }}).

      All requests must be made over HTTPS or they will fail. API requests that don't contain authentication will also fail.

  - title: "Generate Access Tokens"
    anchor: "generate-access-tokens"
    content: |
      Access tokens are obtained by performing an OAuth2 handshake with an existing Stitch client account or by creating a new account via the API.

    subsections:
      - title: "New Stitch Clients"
        anchor: "generate-access-token-new-stitch-client"
        content: |
          As an API client, you can create a new Stitch client account with the Create Account API endpoint, which will return an access token for that Stitch client account.

          The created account is still owned and managed by the user it is created for, and that user will be able to login to the Stitch web interface and receive emails from Stitch.

      - title: "Existing Stitch Clients, Using OAuth2"
        anchor: "existing-stitch-clients-oauth2"
        content: |
          You can connect to a user's existing Stitch client account by having the user complete a standard OAuth flow. Registering your application with Stitch is a prerequisite to generating tokens with OAuth, so do that first. Then, follow these steps to complete the OAuth flow:

        steps:
          - title: "Send the user to Stitch"
            anchor: "authentication--send-user-to-stitch"
            content: |
              To initiate the authorization flow, the user will click a link to Stitch that includes your application's API client ID. This is the `partner_id` you obtained when you registered your application:

              ```shell
              https://app.stitchdata.com/oauth/authorization?client_id={CLIENT_ID}
              ```

              While only your `client_id` (`partner_id`) is required, the URL may also include the following parameters:

              {% assign auth = site.api-files | where:"content-type","embed-url-parms" %}

              <table width="100%; fixed">
              {% for item in auth %}
              {% for parameter in item.parameters %}
              <tr>
              <td width="20%; fixed" align="right">
              <strong>{{ parameter.name }}</strong>
              <br>

              {% case parameter.required %}
              {% when true %}
              <font color="#cc3399">REQUIRED</font>
              {% else %}
              OPTIONAL
              {% endcase %}

              </td>

              <td>
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
              curl https://api.stitchdata.com/oauth/token 
                   -d client_secret={CLIENT_SECRET}
                   -d code={AUTHORIZATION_CODE}
                   -d grant_type=authorization_code
              ```

              **Note**: Each temporary authorization code can only be used once and will expire five minutes after creation.

              If successful, Stitch will respond with the following:

              ```json
              {
                "token_type": "bearer",
                "access_token": ACCESS_TOKEN,
                "stitch_account_id": STITCH_ACCOUNT_ID
              }
              ```

              Your application should store the `access_token` and `stitch_account_id` somewhere secure, and use them to make calls to the API:

              ```curl
              curl https://api.stitchdata.com/v4/sources
                   -H 'Authorization: Bearer ACCESS_TOKEN'
              ```

              Access tokens do not expire, but they can be revoked by the user at any time.
---