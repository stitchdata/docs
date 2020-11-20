---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Changing Your Email Address and Password
permalink: /account-security/change-your-email-address-and-password
keywords: email address, password, change password, change email
summary: "Manage your user profile, email address, and update your password on the Your Profile page."

key: "change-email-password"

layout: general
toc: true

type: "manage-your-account"
weight: 1


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  Manage your user profile, email address, and update your password on the **Your Profile** page.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Update your email address"
    anchor: "update-your-email-address"
    summary: "How to update your email address"
    content: |
      {% capture email-requirements %}
      **Note**: An email address can only be associated with one Stitch account. If your email client supports using aliases, [you can use this workaround]({{ link.account.team-members | prepend: site.baseurl | append: "#add-to-multiple-accounts" }}) to associate an email with multiple accounts.
      {% endcapture %}

      {% include note.html type="single-line" content=email-requirements %}

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click **{{ app.page-names.user-profile }}**.
      3. Enter the new email address in the **Email Address** field.
      4. Click the {{ app.buttons.update-profile }} button.

  - title: "Change your password"
    anchor: "change-your-password"
    summary: "How to update your password"
    content: |
      {% capture password-requirements %}
      Passwords must contain:

      1. A minimum of eight characters,
      2. One number,
      3. One uppercase letter,
      4. One lowercase letter, and
      5. At least one special character. For example: `! $ % @ # ^ *` or `&`
      {% endcapture %}

      {% include note.html first-line="**Stitch password requirements:**" content=password-requirements %}

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click **{{ app.page-names.user-profile }}**.
      3. Enter your old password in the **Old Password** field.
      4. In the **New Password** and **Confirm New Password** fields, enter your new password.
      5. Click the {{ app.buttons.password }} button.
---