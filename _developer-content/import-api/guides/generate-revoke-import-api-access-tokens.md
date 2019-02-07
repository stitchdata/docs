---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Generate and Revoke Import API Access Tokens in the Stitch App
permalink: /developers/import-api/guides/generate-revoke-import-api-access-tokens
redirect_from: /integrations/import-api/revoking-an-api-access-token

doc-type: "tutorial"

product-type: "import-api"
content-type: "guide"
content-id: "generate-revoke-import-api-access-tokens"

layout: general
sidebar: on-page

icon: table-selection
order: 1

summary: "A valid access token is required to use Stitch's Import API. Use this guide to generate a new access token or revoke an old one in the Stitch web app."
## This is used only on the /import-api/guides page.
description: "Generate and revoke Import API access tokens."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Import API reference"
    link: "{{ link.import-api.api }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% capture connect-api-notice %}
  **Note**: This guide focuses on generating Import API access tokens in the Stitch web application. For help creating Import API sources using Stitch Connect, refer to the [Create an Import API integration with Stitch Connect guide]({{ link.import-api.guides.create-import-api-with-stitch-connect | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=connect-api-notice %}

  {{ page.summary }}

  **Note**: Import API tokens allow you to send data directly to Stitch. As they have write access to the integration they are generated for, your access tokens should always be kept private. Compromised or lost tokens may be [revoked](#revoke-import-api-access-token) as needed. 


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **An active Stitch account.** To create an account, [sign up for a free one here]({{ site.home }}){:target="new"}.


# -------------------------- #
#         GUIDE STEPS        #
# -------------------------- #

sections:
  - title: "Access tokens and integrations"
    anchor: "access-tokens-integrations"
    content: |
      Each access token is associated with a unique Stitch Import API integration. Requests sent with a given access token will only ever update data for that integration in the destination.

      For example: You create an Import API integration named `Customer Records`, which has a corresponding destination schema named `customer_records`. Any [push requests]() made using the access token associated with the `Customer Records` integration will only affect the data in the `customer_records` schema.

  - title: "Generate a new Import API access token"
    anchor: "generate-import-api-access-token"
    content: |
      {% include layout/inline_image.html type="right" file="import-api/import-api-generated-access-token.png" max-width="400px" alt="A new Import API access token in the Stitch web app" %}

      1. [Sign into your Stitch account]({{ site.sign-in }}){:target="new"}.
      2. From the {{ app.page-names.dashboard }} page, click {{ app.buttons.add-integration }}.
      3. Click the **Import API** icon.
      4. Enter a name for the integration. This is the name that will display on the {{ app.page-names.dashboard }} for the integration; it'll also be used to create the schema in your destination.

         **Note**: Schema names cannot be changed after the integration has been saved.
      5. Click the **Save and Generate Token** button to generate and display the token.
      6. Copy the token.

      **Note**: Stitch will only display the access token once, so be sure to save it before clicking **Close and Continue**. If you forget to copy the token or misplace it, you can create a replacement and revoke the original token.

  - title: "Revoke an existing Import API access token"
    anchor: "revoke-import-api-access-token"
    content: |
      {% include note.html type="single-line" content="**Note**: If you need to revoke a token, we we recommend first [creating a second token](#generate-import-api-access-token) and updating your application with it to prevent interruptions. After you've updated the token in your application, you can revoke the old token." %}

      {% include layout/inline_image.html type="right" file="import-api/import-api-revoke-access-token.png" max-width="400px" alt="Import API access tokens in the Stitch web app" %}

      1. [Sign into your Stitch account]({{ site.sign-in }}){:target="new"}.
      2. From the {{ app.page-names.dashboard }} page, click the Import API integration you need to revoke a token from.
      3. On the {{ app.page-names.int-details }} page, click the **Settings** tab.
      4. Locate the **API Access Tokens** section.
      5. [If you've already generated a replacement token](#rotate-import-api-access-tokens), click the **Revoke** button next to the token you want to revoke.


  - title: "Rotate Import API access tokens"
    anchor: "rotate-import-api-access-tokens"
    content: |
      Each Import API integration is allowed a maximum of two active access tokens at a time.

      If you need to revoke a token, we recommend first [creating a second token](#generate-import-api-access-token) and updating your application with it to prevent interruptions. **Note**: Any requests you attempt to send to Stitch during the time an invalid token is in use must be re-sent once valid a token is in place.

      After you've updated the token in your application, you can [revoke the old token](#revoke-import-api-access-token).
---