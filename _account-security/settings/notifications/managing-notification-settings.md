---
title: Notifications
permalink: /account-security/notifications
keywords: notifications, manage notifications, email notifications, email messages, notify, notify me 
summary: ""

layout: general
key: "notification-settings"
toc: true

type: "account-settings"
weight: 5

intro: |
  {% include misc/data-files.html %}

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Email notifications"
    anchor: "email-notification-basics"
    summary: "Some email notification basics"
    content: |
      Email notifications [todo]

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Email notification from address"
        anchor: "notification-sent-from-address"
        content: |
          All email notifications from Stitch are sent from `{{ site.support }}`.

      - title: "Email notification subject lines"
        anchor: "email-notification-subject-lines"
        content: |
          Notifications from Stitch will have a subject line similar to the following: `Stitch Notification - <description of issue>`

      - title: "Email notification delays"
        anchor: "email-notification-delays"
        content: |
          Some notifications may not be sent immediately after the issue occurs. Stitch implements a delay for some notification types to provide transient issues the opportunity to resolve themselves. Ideally, this means your inbox won't be spammed with notifications for non-actionable items.

          The delay Stitch uses depends on the notification/issue type. Refer to the next section for the delay used by each notification type.

      - title: "Email notification types"
        anchor: "email-notification-types"
        content: |
          {% assign attributes = "description|delay|potential-causes|subject-lines" | split:"|" %}
          {% assign email-notifications = site.data.stitch.notifications.email | sort: "name" %}

          {% for notification in email-notifications %}
          - [{{ notification.name }}](#{{ notification.name | slugify }})
          {% endfor %}

          {% for notification in email-notifications %}
          #### {{ notification.name | append: " email notifications" }} {#{{ notification.name | slugify }}}

          <table class="attribute-list">
          {% for attribute in attributes %}
          <tr>
          <td class="attribute-name">
          <strong>{{ attribute | capitalize | replace: "-", " " }}</strong>
          </td>
          <td>
          {% if attribute == "subject-lines" or attribute == "potential-causes" %}
          {% assign count = notification[attribute] | size %}

          {% case count %}
          {% when 1 %}
          {% for item in notification[attribute] %}
          {{ item | flatify | markdownify }}
          {% endfor %}

          {% else %}
          <ul>
          {% for item in notification[attribute] %}
          <li>{{ item | flatify | markdownify }}</li>
          {% endfor %}
          </ul>
          {% endcase %}
          {% else %}
          {{ notification[attribute] | flatify | markdownify }}
          {% endif %}
          </td>

          </tr>
          {% endfor %}
          </table>
          {% endfor %}
---
