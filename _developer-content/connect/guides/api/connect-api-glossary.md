---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch Connect Glossary
permalink: /developers/stitch-connect/guides/glossary
summary: ""

product-type: "connect"
content-type: "guide"
content-id: &key "connect-glossary"

key: "connect-glossary"

layout: general
sidebar: api


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "reference"
icon: file
order: 1

description: "Terms and definitions used throughout Stitch Connect."


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }}


# -------------------------- #
#         TERMINOLOGY        #
# -------------------------- #

all-terms:
  - name: "Partner ID"
    definition: |
      {{ site.data.connect.general.authentication.partner-id | flatify }}

      A partner ID is prefixed with `oc_` so as not to be confused with a [client account access token](#client-account-access-token-term).

  - name: "Partner key"
    definition: |
      {{ site.data.connect.general.authentication.partner-key | flatify }}

      A partner key is prefixed with `oc_` so as not to be confused with a [client account access token](#client-account-access-token-term).
      
  - name: "Partner"
    definition: "An organization that utilizes Stitch Connect to programmatically create and/or manage Stitch client accounts on behalf of their users."

  - name: "Partner credentials"
    definition: |
      A set of credentials specific to a Stitch [partner](#partner-term), consisting of a [partner ID](#partner-id-term) and [partner key](#partner-key-term), obtained after an [interest form]({{ site.data.connect.api.interest-form }}){:target="new"} is submitted to and approved by Stitch.

      Partner credentials are used only to create Stitch client accounts. After the Stitch client account is created, the account's [client access token](#client-account-access-token-term) is used to authenticate API requests.

  - name: "Stitch client account"
    definition: |
      {{ site.data.tooltips.stitch-client-account }}

  - name: "Client account access token"
    definition: |
      {{ site.data.connect.general.authentication.client-account-access-token }}

      A client account access token is prefixed with `ac_` so as not to be confused with [partner credentials](#partner-credentials-term).

  - name: "Ephemeral token"
    definition: |
      A token that is passed to the Connect JavaScript client to create a session in the Stitch web application. This credential is created by using the [Create a session endpoint]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sessions.section }}) in the Connect API.

      A session is for the user for whom the API access token was created. The session will expire once terminated or after 12 hours. 

  - name: "Destination"
    definition: |
      {{ site.data.tooltips.destination }}

  - name: "Session"
    definition: |
      {{ site.data.tooltips.session }}

  - name: "Source"
    definition: |
      {{ site.data.tooltips.source | flatify }}

  - name: "Stream"
    definition: |
      A table in a [data source](#source-term).

  - name: "Connection check"
    definition: |
      {{ site.data.tooltips.connection-check }}

  - name: "Replication job"
    definition: |
      {{ site.data.tooltips.replication-job }}

  - name: "Discovery"
    definition: |
      {{ site.data.tooltips.structure-sync | replace: "A structure sync","Discovery" }}

  - name: "Structure sync"
    definition: |
      {{ site.data.tooltips.structure-sync }} This is also referred to as [discovery](#discovery-term).


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #

sections:
  - content: |
      {% assign glossary-terms = page.all-terms | sort:"name" %}

      {% for term in glossary-terms %}
      <h4 data-swiftype-index='false' id="{{ term.name | slugify | append:"-term" }}">{{ term.name }}</h4>
        {{ term.definition | flatify | markdownify | replace:"<p>","<p class='glossary-definition'>" }}
      {% endfor %}
      
---