---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Stitch IP Address Reference
permalink: /account-security/stitch-ip-addresses
summary: "The IP addresses Stitch uses for each supported data pipeline region."

input: false
layout: general
feedback: true

key: "ip-addresses"
type: "security"
weight: TODO


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  To connect to some integrations and destinations, you'll need to grant Stitch access by whitelisting our IP addresses. The IP addresses you use depend on the [data pipeline region]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) your account is in.

  In this guide:

  {% for region in site.data.stitch.regions %}
  - [{{ region.name }} region IP addresses](#{{ region.id }}-ip-addresses)
  {% endfor %}


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - content: |
      {% for region in site.data.stitch.regions %}
      ## {{ region.name }} region IP addresses {#{{ region.id }}-ip-addresses}

      If your Stitch account uses the **{{ region.name }}** region, you'll use the following list of IP addresses when asked to perform any IP whitelisting:

      {% for ip in ip-addresses[region.id] %}
      - {{ ip.ip }}
      {% endfor %}

      {% unless forloop.last == true %}
      <hr>
      {% endunless %}
      {% endfor %}
---