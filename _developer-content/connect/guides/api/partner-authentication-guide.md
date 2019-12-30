---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Partner API Authentication Guide
permalink: /developers/stitch-connect/guides/stitch-partner-authentication-guide
redirect_from: /stitch-connect/guides/stitch-partner-authentication-guide

summary: "As an API client, you'll need to obtain an API access token before you can make API requests on behalf of a user's Stitch client account. In this guide, we'll cover the available methods for obtaining an access token and authenticating to the API."

product-type: "connect"
content-type: "guide"
content-id: "partner-authentication"

key: "connect-partner-auth"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: lock
order: 2

description: "Learn about the API authentication methods available to Stitch Partners."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Authentication reference"
    link: "{{ site.data.connect.api.authentication | prepend: link.connect.api | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% capture applicable-to-notice %}
  **Note**: This guide is applicable only to Stitch partners, or API clients. If you aren't a Stitch partner - meaning you only want to use the API to manage your own Stitch account(s) - refer to the [Authentication reference]({{ site.data.connect.api.authentication | prepend: link.connect.api | prepend: site.baseurl }}).
  {% endcapture %}
  {% include note.html type="single-line" content=applicable-to-notice %}

  Stitch authenticates API requests using an API access token. {{ page.summary }}

  For more info about API access tokens, refer to the [API reference]({{ site.data.connect.api.authentication | prepend: link.connect.api | prepend: site.baseurl }}).

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Stitch partner credentials.** To use the Stitch API as a partner, complete [this form]({{ site.data.connect.api.interest-form }}){:target="new"}. Once approved, you'll receive the credentials required to authenticate requests made from your API client.


# -------------------------- #
#         GUIDE STEPS        #
# -------------------------- #

sections:
  - title: "Generate tokens for a new Stitch account with the API"
    anchor: "generate-tokens-new-account"
    content: |
      This approach will create a new Stitch client account using the API. When a new Stitch client account is successfully created, the response will include an access token, which you can use to authenticate API calls to other endpoints:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Step 1: Create a Stitch account and generate a token"
        anchor: "create-stitch-account-generate-token"
        content: |
          Using your API client credentials, create a new Stitch client account using the [Create Account endpoint]({{ site.data.connect.core-objects.accounts.create.anchor | prepend: link.connect.api | prepend: site.baseurl }}).

          In the body of the request, include your `partner_id` and `partner_secret`, along with [the other properties required to create a Stitch client account]({{ site.data.connect.core-objects.accounts.object | prepend: link.connect.api | prepend: site.baseurl }}):

          ```json
          curl -X {{ site.data.connect.core-objects.accounts.create.method | upcase }} {{ site.data.connect.core-objects.accounts.create.name | prepend: site.data.connect.api.base-url | flatify | strip_newlines }}
               -H 'Content-Type: application/json'
               -d "{
                    "partner_id": "<YOUR_PARTNER_ID>",
                    "partner_secret": "<YOUR_PARTNER_SECRET>",
                    "first_name": "<USER'S_FIRST_NAME>",
                    "last_name": "<USER'S_LAST_NAME>",
                    "company": "<USER'S_COMPANY>",
                    "email": "<USER'S_EMAIL>@<DOMAIN>"
                  }"
          ```

          The account that will be created will be owned and managed by the user provided in the Create Account request. This user can then log into the Stitch web interface, receive emails from Stitch, etc.

          When successful, this endpoint returns a status of `200 OK` and an object with `access_token` and `stitch_account_id` properties:

          ```json
          {
            "access_token": "<ACCESS_TOKEN>",
            "stitch_account_id": <STITCH_CLIENT_ID>
          }
          ```

          Your application should store the `access_token` and `stitch_account_id` somewhere secure, as these credentials will be used to make calls to the API.

      - title: "Step 2: Authenticate your API requests"
        anchor: "authenticate-your-api-requests"
        content: |
          {% capture authenticate-calls %}
          Lastly, use the `access_token` in the header of your API requests to authenticate to the API:

          ```json
          curl {{ site.data.connect.api.core-objects.sources.list.method | upcase }} {{ site.data.connect.api.core-objects.sources.list.name | prepend: site.data.connect.api.base-url | flatify }}
               -H 'Authorization: Bearer <ACCESS_TOKEN>'
          ```
          {% endcapture %}

          {{ authenticate-calls | flatify }}

  - title: "Generate tokens and authenticate using OAuth2"
    anchor: "generate-tokens-existing-account"
    content: |
      If you prefer to use OAuth, or to connect to a user's existing Stitch client account, you can also use this approach:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Step 1: Send the user to Stitch from your application"
        anchor: "send-user-to-stitch"
        content: |
          To initiate the authorization flow, the user will click a link to Stitch that includes your application's API client ID. This is the `partner_id` you obtained when you registered your application. For example:

          ```shell
          https://app.stitchdata.com/oauth/authorization?client_id={PARTNER_ID}
          ```

          While only your `partner_id` is required, the URL may also include the following parameters:

          {% assign all-connect = site.developer-files | where:"product-type","connect" %}

          {% assign auth = all-connect | where:"content-type","api-url-parms" %}

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

      - title: "Step 2: Get the user's consent"
        anchor: "get-users-consent"
        content: |
          If the user isn't already signed into their Stitch client account, they will be prompted to do so or create a new account, if need be.

          Once signed in, the user will be shown a screen explaining that your application has requested access to their Stitch account. They will be prompted to accept or reject this request.

      - title: "Step 3: Callback to your application"
        anchor: "callback-to-your-application"
        content: |
          When the user accepts or denies the request, they will be redirected to the callback URL (`redirect_uri`) you provided when you registered your application with Stitch.

          If the user denies the request, Stitch will include error details:

          ```shell
          https://yourapplication.com/callback?error=access_denied
          ```

          If the user accepts the request, the callback will include a temporary authorization code to be used in the next step:

          ```shell
          https://yourapplication.com/callback?code=<STITCH_AUTHORIZATION_CODE>
          ```

          **Note**: Each temporary authorization code can only be used once and expires five minutes after creation.

      - title: "Step 4: Exchange tokens"
        anchor: "exchange-tokens"
        content: |
          Lastly, when your application receives the user's request to the callback URL, it should make a request to the Stitch OAuth endpoint to exchange the temporary authorization code for a permanent access token:

          ```json
          curl {{ site.data.connect.api.base-url }}/oauth/token 
               -d client_secret=<CLIENT_SECRET>
               -d code=<STITCH_AUTHORIZATION_CODE>
               -d grant_type=authorization_code
          ```

          If successful, Stitch will respond with the following:

          ```json
          {
            "token_type": "bearer",
            "access_token": "<ACCESS_TOKEN>",
            "stitch_account_id": <STITCH_ACCOUNT_ID>
          }
          ```

          Your application should store the `access_token` and `stitch_account_id` somewhere secure, as these credentials will be used to make calls to the API.

      - title: "Step 5: Authenticate your API requests"
        anchor: "authenticate-api-calls"
        content: |
          {{ authenticate-calls | flatify }}

  - title: "Next steps"
    anchor: "next-steps"
    content: |
      To learn more about the Stitch API, refer to the [API reference]({{ link.connect.api | prepend: site.baseurl }}).
---