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
  {% capture region-note %}
  **Not sure which data pipeline region your account uses?** [Click here for help]({{ link.security.supported-operating-regions | prepend: site.baseurl | append: "#identify-data-pipeline-region" }}).
  {% endcapture %}
  {% include note.html type="single-line" content=region-note %}

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

      **Need a comma-delimited list of these IP addresses?** Click **Copy** to copy the list to your clipboard:

      {% capture ip-list %}
      {% for ip in ip-addresses[region.id] %}{{ ip.ip }}{% unless forloop.last == true %},{% endunless %}{% endfor %}
      {% endcapture %}

      {% capture code %}{{ ip-list | strip }}
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="markdown" %}

      {% unless forloop.last == true %}
      <hr>
      {% endunless %}
      {% endfor %}
---