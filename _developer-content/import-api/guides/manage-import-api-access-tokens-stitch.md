---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Managing and Revoking Import API Access Tokens in Stitch
permalink: /developers/import-api/guides/manage-import-api-access-tokens
redirect_from: 
  - /integrations/import-api/revoking-an-api-access-token
  - /developers/import-api/guides/import-api-access-tokens
summary: "Learn to create and manage Import API access tokens in the Stitch web app."

product-type: "import-api"
content-type: "guide"
content-id: "import-api-access-tokens"
key: "import-api-access-tokens-stitch"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /import-api/guides page.
doc-type: "tutorial"
icon: lock
order: 2

display-title: "Managing Import API Access Tokens in Stitch"
description: "Manage and revoke Import API access tokens in Stitch."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Stitch Import API Quick Start"
    link: "{{ link.import-api.guides.quick-start | prepend: site.baseurl }}"

  - title: "Structuring and typing data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Sequencing data for the Import API"
    link: "{{ link.import-api.guides.sequence-data | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "Manage Import API access tokens with the Connect API"
    link: "{{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl }}"



# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% capture connect-notice %}
  **Note**: This guide is specific to the Stitch app. Refer to the [Managing and Revoking Import API Access Tokens via the Connect API]({{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl }}) for info about managing Import API access tokens using the Connect API.
  {% endcapture %}

  {% include note.html type="single-line" content=connect-notice %}

  {{ page.summary }}

  **Note**: This guide is specific to Import API access tokens. For info about Stitch Connect API credentials, refer to the [Connect API documentation]({{ link.connect.guides.api-credentials | prepend: site.baseurl }}).


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #

sections:
  - title: "Import API access tokens and integrations"
    anchor: "access-tokens-integrations"
    content: |
      {% include developers/import-api/obtaining-credentials.html type="general" %}

  - title: "Generate a new Import API access token"
    anchor: "generate-import-api-access-token"
    content: |
      {% include developers/import-api/obtaining-credentials.html type="generate-new-access-token" %}

  - title: "Revoke an existing Import API access token"
    anchor: "revoke-import-api-access-token"
    content: |
      If you need to revoke a token, we recommend first [creating a second token](#generate-import-api-access-token) and updating your application with it to prevent interruptions. **Note**: Any requests you attempt to send to Stitch during the time an invalid token is in use must be re-sent once valid a token is in place.

      After you've updated the token in your application, you can revoke the old token.

      {% include developers/import-api/obtaining-credentials.html type="revoke-access-token" %}
---