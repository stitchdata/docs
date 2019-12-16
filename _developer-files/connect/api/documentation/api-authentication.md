---
title: Authentication
product-type: "connect"
content-type: "api-doc"
order: 3

sections:
  - content: |
      {% assign api = site.data.connect.api %}
      Authenticate your calls to the API by providing an access token in your requests. Each access token is associated with a single Stitch client account. Access tokens do not expire, but they may be revoked by the user at any time.

      Additionally, each request's permissions are limited to that Stitch client account.

      In the examples in this documentation, we use bearer auth:

      ```json
      curl -X GET {{ api.base-url }}{{ api.core-objects.sources.base }}
           -H "Authorization: Bearer <ACCESS_TOKEN>"
      ```

      All requests must be made over HTTPS or they will fail. API requests that don't contain authentication will also fail.

  - title: "Obtain an API access token"
    anchor: "obtain-access-token"
    content: |
      How you obtain an access token depends on the type of user you are:

      - **Individual Stitch user**: You will be using the API to programmatically control your own Stitch client account. You can create, revoke, and delete API access tokens on the [Account Settings page]({{ link.account.manage-api-keys | prepend: site.baseurl }}) of your Stitch client account.

      - **Stitch partner**: You will be performing actions in Stitch client accounts on behalf of users who authorize your API client. You'll need to [register as an API client]({{ site.data.connect.api.interest-form }}){:target="new"} and refer to the [Partner API Authentication guide]({{ link.connect.guides.partner-authentication | prepend: site.baseurl }}) for instructions.
---