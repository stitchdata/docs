---
title: Extending Email Notifications
permalink: /account-security/notifications/extend-email-notifications
keywords: customize notifications, add recipients, notifications, pagerduty, datadog, slack, extend notifications, email alerts
summary: "Using the Custom notification list feature, extend Stitch's email notifications to external services like PagerDuty, Datadog, and Slack."

layout: general
key: "customize-notifications"
toc: true

type: "notifications"
weight: 2

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
  - title: "Uses for the custom notification list"
    anchor: "custom-notification-list-uses"
    summary: "The uses for the custom notification email list"
    content: |
      Using the custom notification list feature, you can:

      - **Integrate with external monitoring systems** like [PagerDuty](https://www.pagerduty.com/){:target="new"} or [Datadog](https://www.datadoghq.com/){:target="new"}. Send Stitch email notifications to your monitoring systems to get ahead of critical issues. Check out our [PagerDuty]({{ link.account.pagerduty-notifications | prepend: site.baseurl }}) and [Datadog]({{ link.account.datadog-notifications | prepend: site.baseurl }}) integration guides for more info.
      - **Post updates to Slack**. Make sure the right people are notified when there's an issue that needs intervention by sending Stitch notifications right to a [Slack](https://slack.com){:target="new"} channel. Check out our [Slack integration guide]({{ link.account.slack-notifications | prepend: site.baseurl }}) for more info.
      - **Trigger other apps** using [Zapier](https://zapier.com){:target="new"}.

      For details about the email notifications Stitch sends, refer to the [Notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}). This info can be used to create different alerts for individual notification types.

      For example: Your team wants to be notified when their Stitch account is nearing its row limit. Based on this, you can filter emails from Stitch with the subject [`Approaching Row Limit`]({{ link.account.notification-settings | prepend: site.baseurl }}#usage-nearing-limit), which are sent when an account is nearing its usage limit.

  - title: "Access to the custom notification list"
    anchor: "custom-notification-list-access"
    summary: "How to access the custom notification list feature"
    content: |
      The custom notification list feature is available during the Free Trial or on an Enterprise plan. Contact [Stitch Sales]({{ site.sales }}){:target="new"} for more info about Enterprise plans.

    subsections:
      - title: "Plan downgrades"
        anchor: "plan-downgrades"
        content: |
          If you decide to downgrade to a plan without custom notification list access, the feature will be disabled and notifications will no longer be sent to the email addresses in the custom notifications list.

          If you upgrade from a plan without custom notification list access to a plan that includes it, and you previously added custom notification email addresses in your account, you will need to [re-enable them](#disable-reenable-email-addresses) to allow Stitch to send notifications to the email address again.

  - title: "Custom notification list basics"
    anchor: "custom-notification-basics"
    summary: "Some custom notification list basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "How many email addresses can I add to the custom notification list?"
        anchor: "how-many-custom-notification-recipients"
        content: |
          An account's custom notification list may have a maximum of 10 email addresses.

      - title: "What emails are sent to the custom notification list?"
        anchor: "what-emails-are-sent-to-the-custom-list"
        content: |
          Any email notification that is sent to other team members of the account will also be sent to any custom notification recipient with an **Enabled** status.

          The only exception is the monthly invoice email. This will only be sent to [the user of the account who originally entered the account's payment information]({{ link.account.team-members | prepend: site.baseurl | append: "#who-will-receive-invoices" }}).

          Refer to the [Notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}) for details about each email notification Stitch can send, including subjects, content, triggers, etc.

      - title: "Can I specify the types of email notifications that are sent?"
        anchor: "can-i-specify-email-notification-types"
        content: |
          This feature is not currently supported. To work around this, you can set up rules or filters in your email client.

      - title: "What services can I use with the custom notification list?"
        anchor: "what-services-custom-notification-list"
        content: |
          Any service that supports receiving email can be used with the custom notification list.

          {% capture notice %}
          Check out the [Datadog]({{ link.account.datadog-notifications | prepend: site.baseurl }}), [PagerDuty]({{ link.account.pagerduty-notifications | prepend: site.baseurl }}), and [Slack integration guides]({{ link.account.slack-notifications | prepend: site.baseurl }}).
          {% endcapture %}

          {% include tip.html content=notice %}

      - title: "Who can add a custom notification email address?"
        anchor: "who-can-add-recipients"
        content: |
          Any team member in a Stitch account that has access to the custom notification list feature can create, delete, disable, or re-enable a notification email address.

  - title: "Add a custom notification recipient"
    anchor: "add-custom-notification-recipient"
    summary: "How to add a custom notification recipient"
    content: |
      {% include note.html type="single-line" content="**Note**: An account's custom notification list may have a maximum of 10 email addresses." %}

      To add a custom notification recipient:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.notification-tab }}** tab.
      3. Click the **Add email** button in the **Custom notification list** section.
      3. In the field that displays, enter an email address.
      4. Click the **Save Email** button.

  - title: "Delete a custom notification recipient"
    anchor: "delete-custom-notification-recipient"
    summary: "How to delete a custom notification recipient"
    content: |
      To delete a custom notification recipient:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.notification-tab }}** tab.
      3. Click the icon next to the **Status** column.
      4. Click **Delete this email**.
      5. You'll be prompted to confirm the deletion. Click **Delete** to continue and delete the email address.

  - title: "Disable or re-enable custom notification recipients"
    anchor: "disable-reenable-email-addresses"
    summary: "How to disable or re-enable a custom notification recipient"
    content: |
      If you want to temporarily disable a custom notification recipient, you can click the icon next to the email address and use the **Disable this email** option.

      To re-enable a disabled recipient, click the icon next to the **Status** column and select **Re-enable this email**.

  - title: "Guides for integrating popular services"
    anchor: "popular-service-integration-guides"
    summary: "Resources for integrating some popular services"
    content: |
      Ready to integrate Stitch notifications with your services? Check out our integration guides:

      - [Datadog]({{ link.account.datadog-notifications | prepend: site.baseurl }})
      - [PagerDuty]({{ link.account.pagerduty-notifications | prepend: site.baseurl }})
      - [Slack]({{ link.account.slack-notifications | prepend: site.baseurl }})
---