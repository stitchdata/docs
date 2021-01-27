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
  {% assign user-roles = site.data.stitch.user-management.roles %}

  {{ page.summary }}

  In this guide:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - title: "Single sign-on (SSO) basics"
    anchor: "basics"
    summary: "Some single sign-on (SSO) basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What is single sign-on (SSO)?"
        anchor: "basics--what-is-sso"
        content: |
          From [Wikipedia](https://en.wikipedia.org/wiki/Single_sign-on){:target="new"}:

          > Single sign-on (SSO) is an authentication scheme that allows a user to log in with a single ID and password to any of several related, yet independent, software systems.

          SSO allows you to securely grant members of your team access to Stitch by internally managing their credentials through the [Identity Provider (IdP)](#basics--supported-identity-providers) of your choice.

      - title: "How does SSO work in Stitch?"
        anchor: "basics--how-sso-works"
        content: |
          {% capture sso-admin %}
          SSO can be enabled by any team member of a Stitch account. The team member who initially enables SSO becomes an {{ user-roles.sso-admin.name }} user; additional {{ user-roles.sso-admin.name | append: "s" }} can be added by contacting support.
          {% endcapture %}

          When SSO is enabled in Stitch, non-{{ user-roles.sso-admin.name }} users must sign into Stitch using your organization's Identity Provider. This means that new team members must be added to the Sttich account by an {{ user-roles.sso-admin.name }} user to be granted access.

          Additionally, when SSO is enabled:

          - Upon initial enablement, all pending team member invitations will be invalidated
          - Upon initial enablement, all team members on the account will receive an [email notification](TODO) explaining the change
          - Only {{ user-roles.sso-admin.name }} users will be able to update their email addresses and passwords, or add, deactivate, or reactivate other team members

      - title: "What Identity Providers (IdP) are supported by Stitch?"
        anchor: "basics--supported-identity-providers"
        content: |
          {% assign supported-identity-providers = site.account-security | where:"idp",true | sort_natural:"display-name" %}

          Stitch currently supports the following Identity Providers (IdP):

          {% for idp in supported-identity-providers %}
          - [{{ idp.display-name }}]({{ idp.url | prepend: site.baseurl }})
          {% endfor %}

      - title: "Who can enable SSO?"
        anchor: "basics--who-can-enable-sso"
        content: |
          {{ sso-admin }}

      - title: "Who can modify the SSO configuration?"
        anchor: "basics--who-can-modify-sso"
        content: |
          Only {{ user-roles.sso-admin.name }} users can modify an existing SSO configuration. This includes modifying any settings, disabling SSO, or reenabling SSO.

      - title: "How can I access Stitch if my Identity Provider experiences downtime?"
        anchor: "basics--idp-downtime"
        content: |
          If SSO is enabled and your Identity Provider is experiencing downtime, only {{ user-roles.sso-admin.name }} users will be able to access Stitch. These users can sign into Stitch using their password, ensuring a member of your team will always have access even if your Identity Provider is down.

  - title: "Enabling SSO"
    anchor: "enable-sso"
    summary: "How to enable in your Stitch account"
    content: ""

  - title: "Modifying SSO settings"
    anchor: "modify-sso"
    summary: "How to modify the SSO configuration in your Stitch account"
    content: ""

  - title: "Disabling SSO"
    anchor: "disable-sso"
    summary: "How to enable in your Stitch account"
    content: ""
---