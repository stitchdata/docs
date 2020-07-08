---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Notifications Overview and Reference
permalink: /account-security/notifications
keywords: notifications, manage notifications, email notifications, email messages, notify, notify me 
summary: "Learn about how in-app and email notifications work in Stitch."

key: "notification-settings"

layout: general
toc: true

type: "notifications"
weight: 1


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% include misc/icons.html %}
  {% assign notifications = site.data.stitch.notifications %}

  To ensure you're kept in the loop when Stitch encounters issues, Stitch will trigger in-app and email notifications.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Notification levels"
    anchor: "notification-levels"
    summary: "Notification urgency levels"
    content: |
      {% assign notification-levels = notifications.common.levels %}
      Stitch notifications are assigned levels of urgency as follows:

      {% for level in notification-levels.all %}
      - {{ level.icon | flatify | replace:"TOOLTIP",level.name }} **{{ level.name }}** - {{ level.description | flatify }} **For example:** {{ level.example | flatify }}
      {% endfor %}

      Refer to the [Notification reference section](#notification-reference) for more info about the issues that trigger notifications and the level assigned to each issue.

  - title: "Notification categories"
    anchor: "notification-categories"
    summary: "Stitch's notification categories"
    content: |
      {% assign notification-categories = notifications.common.categories %}

      Stitch notifications are grouped into the following categories:

      {% for category in notification-categories %}
      - **{{ category | capitalize }}** - {{ notifications[category]description | flatify }}
      {% endfor %}

      For more info about the notifications in each category, refer to the [Notification reference section](#notification-reference-section).

  - title: "In-app notifications"
    anchor: "in-app-notifications"
    summary: "How in-app notifications work"
    content: |
      When Stitch encounters an issue or something requires your attention, a notification will display in the **Notifications** tab of your account:

      ![The Notifications tab in the Stitch web app]({{ site.baseurl }}/images/account-security/notification-tab.png)
      
    subsections:
      - title: "In-app notification recipients"
        anchor: "in-app-notification-recipients"
        content: |
          In-app notifications are visible to all team members in a Stitch account.

      - title: "In-app notification visibility"
        anchor: "in-app-notification-visibility"
        content: |
          All notifications listed in the [Notification reference](#notification-reference) will display in the **Notifications** tab shortly after they're triggered.

          **Note**: Email notifications for some issues may not be sent immediately after the issue occurs. Refer to the [Email notification delays section](#email-notification-delays) for more info.

      - title: "In-app notification resolution"
        anchor: "in-app-notification-resolution"
        content: |
          Notifications in the **Notifications** tab will continue to display until the issue that triggered the notification is resolved.

          **Note**: At this time, manually clearing notifications is not supported.

  - title: "Email notifications"
    anchor: "email-notifications"
    summary: "How email notifications work"
    content: |
      For any issue listed in the [Notification reference](#notification-reference), Stitch will send an email version of the notification to all team members in a Stitch account.

    subsections:
      - title: "Email notification recipients"
        anchor: "email-notification-recipients"
        content: |
          Email notifications are sent to all team members in a Stitch account.

          If your account also has the [custom email notification list feature]({{ link.account.customize-notifications | prepend: site.baseurl }}) enabled, email notifications will also be sent to the email addresses in this list that have an **Enabled** status.

          **Note**: The only exceptions are:

          - **The monthly billing invoice**, which is sent only to the team member who originally entered the account's payment method details.
          - **If the user opts out of replication error notifications**. [Users who opt out of replication error notifications]({{ link.account.manage-notification-settings | prepend: site.baseurl }}) will still receive general email notifications. Refer to the [notification reference](#notification-reference) for each individual notification's opt out status.

      - title: "Email notification from address"
        anchor: "notification-sent-from-address"
        content: |
          All email notifications from Stitch are sent from `{{ site.support }}`.

      - title: "Email notification subject lines"
        anchor: "email-notification-subject-lines"
        content: |
          Notifications from Stitch will have a subject line similar to the following: `{{ notifications.common.subject-lines.prefix }} <description of issue>`

      - title: "Email notification delays"
        anchor: "email-notification-delays"
        content: |
          Some email notifications may not be sent immediately after the issue occurs. Stitch implements an email send delay for some notification types to provide transient issues the opportunity to resolve themselves. Ideally, this means your inbox or [external notification service]({{ link.account.customize-notifications | prepend: site.baseurl }}) won't be spammed with notifications for non-actionable items.

          The delay Stitch uses depends on the notification/issue type. Refer to the [Notification reference section](#notification-reference) for the delay used by each notification type.

  - title: "Notification reference"
    anchor: "notification-reference"
    summary: "A reference of Stitch's email notifications"
    content: |
      In this section is info about the email notifications Stitch will send to the users of your account. This includes a description of the issue triggering the notification, the email's subject, urgency level, send delay (if any), potential causes, and the content of the email notification.

      {% assign attributes = "email-subject|category|level|opt-out|email-delay|potential-causes|content" | split:"|" %}

      {% for level in notification-levels.all %}
      - [{{ level.name | append: " level notifications" }}](#{{ level.id }}-notification-reference)
      {% endfor %}

      {% for level in notification-levels.all %}
      ### {{ level.name | append: " level notifications" }} {#{{ level.id }}-notification-reference}

      When {{ level.name | downcase }} level notifications are sent, it means that {{ level.description | flatify | replace: "Data","data" }}

      {% for category in notification-categories %}
      {% for notification in notifications[category][level.id] %}
      - [{{ notification.name }}](#{{ notification.id }})
      {% endfor %}
      {% endfor %}

      {% for category in notification-categories %}
      {% for notification in notifications[category][level.id] %}

      #### {{ notification.name }} {#{{ notification.id | slugify }}}

      {{ notification.description | flatify }}

      <table class="attribute-list">
      {% for attribute in attributes %}
      {% if attribute == "level" %}
      <tr>
      <td class="attribute-name">
      <strong>{{ attribute | capitalize }}</strong>
      </td>
      <td>
      {{ level.name | capitalize }} {{ notification-levels[level.id]icon | flatify | replace:"TOOLTIP",notification-levels[level.id]description }}
      </td>
      </tr>

      {% elsif attribute == "category" %}
      <tr>
      <td class="attribute-name">
      <strong>{{ attribute | capitalize }}</strong>
      </td>
      <td>
      {{ category | capitalize }}
      </td>
      </tr>

      {% elsif attribute == "opt-out" %}
      <tr>
      <td class="attribute-name">
      <strong>Users can opt-out</strong> {{ info-icon | replace:"TOOLTIP","If Yes, this email notification will be suppressed when a user opts out of receiving error notifications about replication. If No, this email notification will always be sent." }}
      </td>
      <td>
      {% case notification[attribute] %}
        {% when true %}
          Yes

        {% when false %}
          No
      {% endcase %}
      </td>
      </tr>

      {% else %}

      {% if notification[attribute] %}
      <tr>
      <td class="attribute-name">
      <strong>{{ attribute | capitalize | replace: "-", " " }}</strong>
      </td>
      <td>
      {% if attribute == "email-subject" or attribute == "potential-causes" or attribute == "content" %}
      {% assign count = notification[attribute] | size %}

      {% case count %}
      {% when 1 %}
      {% for item in notification[attribute] %}
      {{ item | flatify }}
      {% endfor %}

      {% else %}
      <ul>
      {% for item in notification[attribute] %}
      <li style="margin-top: 0px;">{{ item | flatify | markdownify }}</li>
      {% endfor %}
      </ul>
      {% endcase %}

      {% else %}
      {{ notification[attribute] | flatify }}
      {% endif %}
      </td>

      </tr>
      {% endif %}
      {% endif %}
      {% endfor %}
      </table>

      
      {% endfor %}
      {% if forloop.last == true %}
      [Back to {{ level.name }} notification reference](#{{ level.id | append: "-notification-reference" }})
      {% endif %}

      
      {% endfor %}

      {% unless forloop.last == true %}
      ---
      {% endunless %}
      {% endfor %}
---