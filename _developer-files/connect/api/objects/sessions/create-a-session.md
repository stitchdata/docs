---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sessions"
key: "create-a-session"
version: "3"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a session"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/ephemeral
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sessions.create.short }}"
description: |
  {% capture deprecation-notice %}
  Stitch.js, which uses this endpoint, has been deprecated and may stop functioning at a future date. If you're currently using Stitch.js, you should begin transitioning to the Connect API. [Learn more]({{ link.changelog.main | prepend: site.baseurl | append: "#2021-07-14-stitch-connect-javascript-stitch-js-deprecation" }}).
  {% endcapture %}

  {% include important.html type="single-line" content=deprecation-notice %}

  {{ api.core-objects.sessions.create.description | flatify }}


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Session object]({{ api.core-objects.sessions.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: "{{ endpoint.short-url | flatify | strip_newlines }}"
    header: "{{ site.data.connect.request-headers.post.without-body | flatify }}"

  - type: "Response"
    language: "json"
    code: |
      {
        "ephemeral_token":"<EPHEMERAL_TOKEN>"
      }
---