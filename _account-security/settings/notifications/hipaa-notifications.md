---
title: Managing Notification Content for HIPAA Compliance
permalink: /account-security/notifications/hipaa-compliant-notifications
keywords: notifications, hipaa, hipaa compliance, hipaa-compliant, blank emails, blank error emails
summary: "Suppress plain-text error messages in email notifications as part of making your Stitch account HIPAA-compliant."

layout: general
key: "hipaa-notifications"
toc: true

type: "notifications"
weight: 3

enterprise: true
enterprise-cta:
  feature: "HIPAA compliance "
  title: "{{ site.data.strings.enterprise.title.is-an | prepend: page.enterprise-cta.feature }}"
  copy: |
    {{ page.enterprise-cta.feature | flatify }} is an Enterprise feature. Before replicating any sensitive data, contact Stitch Sales to ensure all requirements for HIPAA compliance are completed.

intro: |
  {% include misc/data-files.html %}

  To ensure sensitive data isn't sent via email notifications, you can enable plain-text error suppression. This will remove raw error messages from email notifications, making them accessible only in the Stitch app.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Plain-text error suppression basics"
    anchor: "hipaa-compliance-notification-content"
    summary: "How plain-text error suppression works"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What does plain-text error suppression do?"
        anchor: "what-does-the-feature-do"
        content: |
          The {{ app.buttons.suppress-plaintext-notifications }} setting in the **Notifications** section will do just that - suppress plain-text messages in email notifications. This setting is used in compliance with HIPAA requirements to prevent sensitive data from being sent via email notifications.

          When enabled, the setting will apply to the entire account. This setting cannot be enabled for specific integrations or notification types.

      - title: "Does enabling plain-text error suppression make my account HIPAA compliant?"
        anchor: "does-the-feature-make-me-hipaa-compliant"
        content: |
          **No**. Activating this setting will not, by itself, make your Stitch account HIPAA compliant. There are other requirements that must be in place before your account is compliant with HIPAA.

          HIPAA compliance is available for Enterprise plans. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

      - title: "Who can use the plain-text error suppression feature?"
        anchor: "who-can-use-the-feature"
        content: |
          All Stitch accounts have access to the plain-text error suppression feature, regardless of plan the account uses.

      - title: "What do email notifications look like when suppression is enabled?"
        anchor: "what-do-notifications-look-like-when-enabled"
        content: |
          This is an example of an email notification that contains a plain-text error message.

          On the left is what the email notification looks like when suppression is **not** enabled.

          On the left is what the same email notification looks like when suppression **is** enabled. 
          <table class="attribute-list">
          <tr>
          <td><strong>Without suppression</strong></td>
          <td><strong>With suppression</strong></td>
          </tr>
          <tr>
          <td width="50%; fixed">
          <img src="{{ site.baseurl }}/images/account-security/notification-with-plain-text.png" alt="Email notification without plain-text notification suppression" style="max-height: 100%; max-width: 100%;">
          </td>
          <td width="50%; fixed">
          <img src="{{ site.baseurl }}/images/account-security/notification-without-plain-text.png" alt="Email notification with plain-text notification suppression" style="max-height: 100%; max-width: 100%;">
          </td>
          </tr>
          </table>

          When this setting is enabled, you'll need to sign into your Stitch account and open [the **Notifications** tab](#view-suppressed-error-messages) to see the full error message.

      - title: "What email notifications contain plain-text errors?"
        anchor: "what-email-notifications-contain-plain-text-errors"
        content: |
          Refer to the [Notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}) for the content each notification may contain.
  
  - title: "View plain-text error messages in Stitch"
    anchor: "view-suppressed-error-messages"
    summary: "How to view suppressed error messages from emails"
    content: |
      While plain-text error messages won't be sent in email notifications when suppression is enabled, you can still view them in Stitch.

      When you receive an email notification that contains a suppressed error message, sign into Stitch, open the [**Notifications** tab]({{ link.account.notification-settings | prepend: site.baseurl }}), and click the **View details** link next to the notification to view the plain-text error:

      ![A plain-text error message for an Outbrain integration in the Notifications tab in the Stitch app]({{ site.baseurl }}/images/account-security/notification-tab-plain-error-example.png)

  - title: "Enable plain-text error message suppression"
    anchor: "enable-plain-text-error-suppression"
    summary: "How to enable plain-text error message suppression"
    content: |
      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.notification-tab }}** tab.
      3. In the **Notification Content** section, check the {{ app.buttons.suppress-plaintext-notifications }} checkbox.
      4. Click the {{ app.buttons.notification-settings }} button.
---