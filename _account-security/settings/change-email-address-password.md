---
title: Changing Your Email Address and Password
permalink: /account-security/change-your-email-address-and-password
keywords: email address, password, change password, change email
summary: "Manage your user profile, email address, and update your password on the Your Profile page."

layout: general
toc: true

type: "account-settings"
weight: 1

intro: |
  {% capture sso-notice %}
  If [Single Sign-on (SSO)]({{ link.security.single-sign-on | prepend: site.baseurl }}) is enabled, only {{ site.data.stitch.user-management.roles.sso-admin.name | append: "s" }} will have the ability to change their email address and/or password in Stitch. All other users will need to make changes through their Identity Provider (IdP).
  {% endcapture %}

  {% include note.html first-line="**Single Sign-on (SSO) can impact these features**" content=sso-notice %}

  Manage your user profile, email address, and password on the **Your Profile** page.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Update your email address"
    anchor: "update-your-email-address"
    summary: "How to update your email address"
    content: |
      {% capture email-requirements %}
      An email address can only be associated with one Stitch account. If your email client supports using aliases, [you can use this workaround]({{ link.account.team-members | prepend: site.baseurl | append: "#add-to-multiple-accounts" }}) to associate an email with multiple accounts.

      **Note**: If [SSO]({{ link.security.single-sign-on | prepend: site.baseurl }}) is enabled, this workaround won't work unless configured through your Identity Provider (IdP).
      {% endcapture %}

      {% include note.html first-line="**Adding an email to multiple accounts**" content=email-requirements %}

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click **{{ app.page-names.user-profile }}**.
      3. Enter the new email address in the **Email Address** field.
      4. Click the {{ app.buttons.update-profile }} button.

  - title: "Change your password"
    anchor: "change-your-password"
    summary: "How to update your password"
    content: |
      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click **{{ app.page-names.user-profile }}**.
      3. Enter your old password in the **Old Password** field.
      4. In the **New Password** and **Confirm New Password** fields, enter your new password.
      5. Click the {{ app.buttons.password }} button.
---