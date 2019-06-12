---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Connect API Credentials
permalink: /developers/stitch-connect/guides/connect-api-credentials

doc-type: "concept"

product-type: "connect"
content-type: "guide"
content-id: "connect-api-credentials"

layout: general
sidebar: on-page

icon: todo
order: 2

summary: ""
## This is used only on the /stitch-connect/guides page.
description: ""


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% capture connect-notice %}
  **Note**: This guide is specific to Connect API access tokens. For info about Stitch Import API credentials, refer to the [Import API documentation]({{ link.import-api.guides.access-tokens | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=connect-notice %}

  {{ page.summary }}


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #

sections:
  - title: ""
    anchor: ""
    content: |
      
---

- Partner credentials:
  + ID (partner_id)
  + Token (partner_key)

- Account access token: An API access token used to authenticate with the Connect API. This is specific to a single Stitch client account.

- Session ephemeral token: A token that is passed to the Connect JavaScript client to create a session in the Stitch web application. A session is for the user for whom the API access token was created. The session will expire once terminated or after 12 hours. 
