---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Single Sign-On
permalink: /account-security/single-sign-on
summary: "Tighten up and simplify your Stitch account's security with the Single Sign-on (SSO) feature."

input: false
layout: general
feedback: true

key: "single-sign-on"
type: "security"
weight: 1


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
  - title: "Single Sign-on (SSO) basics"
    anchor: "basics"
    summary: "Some Single Sign-on (SSO) basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What is Single Sign-on?"
        anchor: "basics--what-is-sso"
        content: |
          From [Wikipedia](https://en.wikipedia.org/wiki/Single_sign-on){:target="new"}:

          > Single Sign-on (SSO) is an authentication scheme that allows a user to log in with a single ID and password to any of several related, yet independent, software systems.

          SSO allows you to securely grant members of your team access to Stitch by internally managing their credentials through the [Identity Provider (IdP)](#basics--supported-identity-providers) of your choice.

      - title: "How does SSO work in Stitch?"
        anchor: "basics--how-sso-works"
        content: |
          {% capture sso-admin %}
          SSO can be enabled by any team member of a Stitch account with an Administrator role. The team member who initially enables SSO becomes an {{ user-roles.administrator.name }} user. To request that other users are added or removed as {{ user-roles.administrator.name | append: "s" }}, the {{ user-roles.administrator.name }} should contact support.
          {% endcapture %}

          When SSO is enabled in Stitch, non-{{ user-roles.administrator.name }} users must sign into Stitch using your organization's Identity Provider (IdP).

          Additionally, when SSO is enabled:

          - Upon initial enablement, all pending team member invitations are invalidated
          - Upon initial enablement, all existing team members in the account receive an email notification
          - Only {{ user-roles.administrator.name }} users are able to update their email addresses and passwords, or add, deactivate, or reactivate other team members
          - Team members access must be [managed in your IdP](#basics--how-is-user-access-managed)

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
          Only {{ user-roles.administrator.name }} users can modify an existing SSO configuration. This includes modifying any settings, disabling SSO, or reenabling SSO.

      - title: "How is team member access to Stitch managed?"
        anchor: "basics--how-is-user-access-managed"
        content: |
          When SSO is enabled, team member access must be managed in your IdP. If your colleague requires access to Stitch, a user with the required permissions in your IdP must grant them access through the IdP. This is also applicable if a team member no longer requires access to Stitch.

          **Note**: Team members removed from your IdP will still display in the **Team members** section of the **Account Settings** page, even though they no longer have access to Stitch. To clean up the list, click **Deactivate** to remove them.

      - title: "How can I access Stitch if my Identity Provider experiences downtime?"
        anchor: "basics--idp-downtime"
        content: |
          If SSO is enabled and your IdP is experiencing downtime, only {{ user-roles.administrator.name }} users will be able to access Stitch. These users can sign into Stitch using their password, ensuring a member of your team will always have access even if your Identity Provider is down.

      - title: "What happens when SSO is disabled in Stitch?"
        anchor: "basics--disable-sso"
        content: |
          Only an {{ user-roles.administrator.name }} can [disable SSO in Stitch](#disable-sso). When SSO is disabled, the following occurs:

          - All team members in the account receive an email notifying them that SSO has been disabled
          - All team members in the account receive a password reset email
          - Team members must sign in using Stitch credentials
          - Team members may be invited or removed directly in Stitch

          **Note**: This is also applicable when [switching to a different IdP](#switch-idp), as switching IdPs requires disabling the current SSO configuration.

  - title: "Enabling SSO"
    anchor: "enable-sso"
    summary: "How to enable in your Stitch account"
    content: |
      To enable SSO in your Stitch account:

      {% include shared/sso/stitch-sso-menu-path.html type="initial-setup" %}
      1. Follow the guide for your IdP to complete the setup. [Click here](#basics--supported-identity-providers) for links to the guides.

  - title: "Modifying SSO settings"
    anchor: "modify-sso"
    summary: "How to modify the SSO configuration in your Stitch account"
    content: |
      {% include note.html type="single-line" content="**Note**: The IdP used by your Stitch account can't be modified using these instructions. Refer to the [Switching to a different IdP section](#switch-idp) for more info." %}

      {% capture sso-edit %}
      1. Click {{ app.menu-paths.account-settings }}.
      2. Scroll down to the **Single Sign-on** section.
      3. Click **Edit**. The SSO Settings page will display.
      {% endcapture %}

      {{ sso-edit }}4. Make your changes, clicking **Save and Update** when finished.

  - title: "Disabling SSO"
    anchor: "disable-sso"
    summary: "How to disable in your Stitch account"
    content: |
      {{ sso-edit }}4. In the **Disable SSO** section, click **Disable SSO**.
      5. When prompted to confirm, click **Disable SSO** to continue.

      A **Success!** message will display in the **Account Settings** page if the configuration is disabled successfully. After SSO is disabled, team members in the account will receive an [email notification and a password reset email](#basics--disable-sso).

  - title: "Switching to a different IdP"
    anchor: "switch-idp"
    summary: "How to switch to a different IdP in your Stitch account"
    content: |
      As Stitch allows only one SSO configuration at a time, you'll need to disable the current configuration and then enable SSO again to switch to a different IdP.

      1. [Disable the current SSO configuration](#disable-sso).
      2. Re-enable SSO, following the guide for your IdP to complete the setup. [Click here](#basics--supported-identity-providers) for links to the guides.
---