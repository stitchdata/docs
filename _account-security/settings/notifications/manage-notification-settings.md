---
title: Managing Your Email Notification Settings
permalink: /account-security/notifications/manage-email-notification-settings
keywords: notifications, manage email notifications, email, opt out, opt-out, suppress
summary: "Manage your Stitch email notification settings."

layout: general
key: "manage-notification-settings"
toc: true

type: "manage-your-account, notifications"
weight: 3

# In this guide, we'll cover:

# {% for section in page.sections %}
# - [{{ section.summary }}](#{{ section.anchor }})
# {% endfor %}

sections:
  - title: "Opting out of replication error notifications"
    anchor: "opt-out-replication-error-notifications"
    summary: ""
    content: |
      {% include misc/data-files.html %}

      By default, every user in a Stitch account will receive all email notifications with the exception of the monthly billing invoice.

      To opt out of receiving replication error email notifications:

      1. Click {{ app.menu-paths.your-profile }}.
      2. In the **Your user profile** section, uncheck the {{ app.buttons.replication-notification-opt-out }} checkbox.
      3. Click {{ app.buttons.update-profile }}.

      **Note**: You will still receive general email notifications, such as notifications about [Single Sign-on (SSO)]({{ link.security.single-sign-on | prepend: site.baseurl }}) changes or the account approaching its row limit. Refer to the [Notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}) each individual notification's opt out status.
---