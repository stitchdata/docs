---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Single Sign-On
permalink: /account-security/single-sign-on
summary: ""

input: false
layout: general
feedback: true

key: "single-sign-on"
type: "security"
weight: 4

# enterprise: true ## TODO: Flip this when confirmed

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {{ page.summary }}

  In this guide:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - title: ""
    anchor: "basics"
    summary: ""
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

  - title: "Enabling and disabling SSO"
    anchor: "enable-disable-sso"
    summary: "How to enable and disable SSO in your Stitch account"
    content: ""
    subsections:
      - title: "Supported identity providers"
        anchor: ""
        content: ""

      - title: ""
        anchor: ""
        content: ""

---