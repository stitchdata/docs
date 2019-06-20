---
title: Extending Email Notifications
permalink: /account-security/extend-email-notifications
keywords: customize notifications, add recipients, notifications, pagerduty, datadog, slack, extend notifications, email alerts
summary: ""

layout: general
key: "customize-notifications"
toc: true

type: "account-settings"
weight: 5

enterprise: true
enterprise-cta:
  feature: "The custom notification list "
  title: "{{ site.data.strings.enterprise.title.is-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.is-an | prepend: page.enterprise-cta.feature | flatify }}"

intro: |
  {% include misc/data-files.html %}

  In the **{{ app.page-names.notification-tab }}** tab of the **{{ app.page-names.account-settings }}** page, you can extend Stitch's email notifications to include additional email addresses outside of the current account users.

  With the custom notification list, you can integrate services like PagerDuty, Datadog, or Slack to receive email alerts from Stitch. 

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Custom notification basics"
    anchor: "custom-notification-basics"
    summary: "Some custom notification list basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      
          
      - title: "What emails are sent to the custom notification list?"
        anchor: "what-emails-are-sent-to-the-custom-list"
        content: |
          Any email notification that is sent to other team members of the account will also be sent to any custom notification recipient with an **Enabled** status.

          The only exception is the monthly invoice email. This will only be sent to [the user of the account who originally entered the account's payment information]({{ link.account.team-members | prepend: site.baseurl | append: "#who-will-receive-invoices" }}).

      - title: "Can I specify the types of email notifications that are sent?"
        anchor: "can-i-specify-email-notification-types"
        content: |
          This feature is not currently supported. [TODO - should we ask folks to contact support and submit feedback?]

      - title: "What services can I use with the custom notification list?"
        anchor: "what-services-custom-notification-list"
        content: |


      - title: "Who can add a custom notification email address?"
        anchor: "who-can-add-recipients"
        content: |
          Any team member in a Stitch account that has access to the custom notification list feature can create, delete, disable, or re-enable a notification email address.

      - title: "What happens if I downgrade to a plan without custom notification list access?"
        anchor: "plan-downgrade"
        content: |
          If you decide to downgrade to a plan without custom notification list access, the feature will be disabled and notifications will no longer be sent to the email addresses in the custom notifications list.

          If you upgrade from a plan without custom notification list access to a plan that includes it, and you previously added custom notification email addresses in your account, you will need to [re-enable them](#disable-reenable-email-addresses) to allow Stitch to send notifications to the email address again.

  - title: "Add a custom notification recipient"
    anchor: "add-custom-notification-recipient"
    summary: "How to add a custom notification recipient"
    content: |
      To add a custom notification recipient:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.notification-tab }}** tab.
      3. In the **Custom notification list** section, **Add Email**





---