---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Import API Access Tokens
permalink: /developers/import-api/guides/import-api-access-tokens
redirect_from: /integrations/import-api/revoking-an-api-access-token

doc-type: "concept"

product-type: "import-api"
content-type: "guide"
content-id: "import-api-access-tokens"

layout: general
sidebar: on-page

icon: todo
order: 2

summary: "A valid API access token is required to use Stitch's Import API. Use this guide manage your Import API access tokens in the Stitch web app."
## This is used only on the /import-api/guides page.
description: "Manage your Stitch Import API access tokens."


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% capture connect-notice %}
  **Note**: This guide is specific to Import API access tokens. For info about Stitch Connect API credentials, refer to the [Connect API documentation]({{ link.connect.guides.api-credentials | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=connect-notice %}

  {{ page.summary }}


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #

sections:
  - title: "API access tokens and integrations"
    anchor: "access-tokens-integrations"
    content: |
      API access tokens are specific to the Import API integration they are created for. This means that data successfully pushed using a given API access token will only ever be loaded into the schema or dataset created for that integration.

      For example: You create an Import API integration named `Customer Records`, which has a corresponding destination schema named `customer_records`. Any [push requests]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.api.core-objects.push.anchor }}) made using the access token associated with the `Customer Records` integration will only affect the data in the `customer_records` schema.

      Each Import API integration is allowed a maximum of two active API access tokens at a time. This ensures that you can [rotate your API access tokens](#secure-your-api-access-tokens) when needed without interrupting replication.

  - title: "Generate a new API access token"
    anchor: "generate-import-api-access-token"
    content: |
      {% capture token-methods %}
      There are two ways to [TYPE] new Import API access tokens:

      1. [In the Stitch web app](#[TYPE]-token-stitch-web-app), or
      2. [Via the Connect API](#[TYPE]-token-via-the-connect-api). **Note**: This method requires access to Stitch Connect. Refer to the [Connect API documentation]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.api.access-api }}) for more info on getting access.
      {% endcapture %}

      {{ token-methods | replace:"[TYPE]","generate" }}

    subsections:
      - title: "In the Stitch web app"
        anchor: "generate-token-stitch-web-app"
        content: |
          {% include developers/import-api/obtaining-credentials.html type="generate-new-access-token" %}

      - title: "Via the Connect API"
        anchor: "generate-token-via-the-connect-api"
        content: |
          {% capture connect-guide %}
          Refer to the [Create and configure an Import API source with Stitch Connect guide]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl | append: "#rotate-import-api-access-tokens" }}) to [TYPE] an Import API access token using the Connect API.
          {% endcapture %}

          {{ connect-guide | replace:"[TYPE]","generate" }}

  - title: "Secure your API access tokens"
    anchor: "secure-your-api-access-tokens"
    content: |
      Import API access tokens allow you to send data directly to Stitch. As they have write access to the integration they are generated for, your access tokens should always be kept private. Compromised or lost tokens may be [revoked](#revoke-import-api-access-token) as needed. 

    subsections:
      - title: "Rotate your API access tokens"
        anchor: "rotate-your-api-access-tokens"
        content: |
          If you need to revoke a token, we recommend first [creating a second token](#generate-import-api-access-token) and updating your application with it to prevent interruptions. **Note**: Any requests you attempt to send to Stitch during the time an invalid token is in use must be re-sent once valid a token is in place.

          After you've updated the token in your application, you can [revoke the old token](#revoke-import-api-access-token).

      - title: "Revoke an existing API access token"
        anchor: "revoke-import-api-access-token"
        content: |
          {{ token-methods | replace:"[TYPE]","revoke" }}
          
        sub-subsections:
          - title: "In the Stitch web app"
            anchor: "revoke-token-stitch-web-app"
            content: |
              {% include developers/import-api/obtaining-credentials.html type="revoke-access-token" %}

          - title: "Via the Connect API"
            anchor: "revoke-token-via-the-connect-api"
            content: |
              {{ connect-guide | replace:"[TYPE]","revoke" }}
---