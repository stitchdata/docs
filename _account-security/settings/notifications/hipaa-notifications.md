---
title: Managing Notification Content for HIPAA Compliance
permalink: /account-security/hipaa-compliant-notifications
keywords: notifications, hipaa, hipaa compliance, hipaa-compliant
summary: ""

layout: general
key: "hipaa-notifications"
toc: true

type: "account-settings"
weight: 5

enterprise: true
enterprise-cta:
  title: "Need HIPAA compliance?"
  url: "?utm_medium=docs&utm_campaign=hipaa-compliance"
  copy: |
    Activating this setting will not, by itself, make your Stitch account HIPAA compliant. As part of an Enterprise plan, Stitch can ensure PHI is handled in compliance with HIPAA. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

sections:
  - title: "Update account notification content"
    anchor: "update-account-notification-content"
    summary: "How to manage your account's notification settings"
    content: |
      The {{ app.buttons.suppress-plaintext-notifications }} setting in the **Notifications** section will do just that - suppress plain-text messages in email notifications. This setting is used in compliance with HIPAA requirements to prevent sensitive data from being sent via notifications.

      Check the {{ app.buttons.suppress-plaintext-notifications }} checkbox and click the {{ app.buttons.notification-settings }} button to enable plain-text suppressions in notification emails.
---