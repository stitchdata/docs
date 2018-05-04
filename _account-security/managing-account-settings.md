---
title: Managing Account Settings
permalink: /account-security/managing-account-settings
keywords: company information, email address, password, change password, change email
tags: [account]

summary: "Update your email address, change your password, and keep your company info up-to-date in Stitch."
type: "account"
toc: true
weight: 1

enterprise-cta:
  title: "Need HIPAA compliance?"
  url: "?utm_medium=docs&utm_campaign=hipaa-compliance"
  copy: |
    Activating this setting will not, by itself, make your Stitch account HIPAA compliant. As part of an Enterprise plan, Stitch can ensure PHI is handled in compliance with HIPAA. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).
---
{% include misc/data-files.html %}

## Personal settings

### Update your email address

1. Click the {{ app.menu-paths.account-settings }}.
2. Click **{{ app.page-names.user-profile }}**.
3. Enter the new email address in the **Email Address** field.
4. Click the {{ app.buttons.update-profile }} button.

### Update your password

1. Click the {{ app.menu-paths.account-settings }}.
2. Click **{{ app.page-names.user-profile }}**.
3. Enter your old password in the **Old Password** field.
4. In the **New Password** and **Confirm New Password** fields, enter your new password.
5. Click the {{ app.buttons.password }} button.

---

## Account settings

**Note**: The settings outlined in this section will affect the entire account.

### Update your account's company info

1. Click the {{ app.menu-paths.account-settings }}.
2. Enter your company name and website URL in the appropriate fields.
3. Select your **Time Zone** from the drop-down. **Note**: This won't affect how Stitch replicates your data, nor will it affect any timezone data in your data warehouse.
4. Click the {{ app.buttons.company-profile }} button.

### Update your account's notification settings

The {{ app.buttons.suppress-plaintext-notifications }} setting will do just that - suppress plain-text messages in email notifications. This setting is used in compliance with HIPAA requirements to prevent sensitive data from being sent via notifications.

1. Click the {{ app.menu-paths.account-settings }}.
2. Check the {{ app.buttons.suppress-plaintext-notifications }} box.
3. Click the {{ app.buttons.notification-settings }} button.

{% include enterprise-cta.html %}