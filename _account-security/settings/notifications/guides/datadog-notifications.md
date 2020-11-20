---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Integrating Datadog with Stitch Notifications 
permalink: /account-security/notifications/integrate-notifications-with-datadog
summary: "Integrate Stitch notifications with Datadog using Stitch's Custom email notification list feature."

key: "datadog-email-notifications"

input: false
layout: tutorial

type: "notifications"
weight: 6

enterprise: true{:target="new"}
enterprise-cta:
  feature: "The custom notification list "
  title: "{{ site.data.strings.enterprise.title.is-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.is-an | prepend: page.enterprise-cta.feature | flatify }}"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Datadog email event documentation"
    link: "https://docs.datadoghq.com/graphing/event_stream/#events-email" 

  - title: "Extend Stitch email notifications"
    link: "{{ link.account.customize-notifications | prepend: site.baseurl }}"

  - title: "Notifications overview"
    link: "{{ link.account.notification-settings | prepend: site.baseurl }}"

  - title: "Notifications reference"
    link: "{{ link.account.notification-reference | prepend: site.baseurl }}"


# -------------------------- #
#       Introduction         #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Using the [Custom email notification list feature]({{ link.account.customize-notifications | prepend: site.baseurl }}), you can integrate Stitch notifications with your [Datadog account](https://www.slack.com){:target="new"}.

  When a Stitch email notification is sent to Datadog, it will display in the **Events** stream. For example: This is an email notification sent to Datadog about an issue with a Salesforce integration:

  ![Event email notification in the Datadog event stream]({{ site.baseurl }}/images/account-security/notifications-datadog-event-stream.png)

  In this guide, we'll walk you through integrating your Stitch notifications with Datadog using [Datadog's event email feature](https://docs.datadoghq.com/graphing/event_stream/#events-email){:target="new"}.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **A Stitch Enterprise plan.** The Custom email notification list is available only on a Stitch Enterprise plan.
  - item: |
      **An existing Datadog account.**


# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Create a Datadog event email address"
    anchor: "create-event-email-address"
    content: |
      1. Sign into your Datadog account.
      2. In the sidenav, click **Integrations > APIs**.
      3. On the page that displays, click **Events API Emails**.
      4. In the **New API Email** section, check that the **Format** is set to **Plain text**.
      5. Click **Create API Email**.
      6. Copy the email address that displays: 

         ![Events API Emails section in the Datadog app]({{ site.baseurl }}/images/account-security/datadog-email-event-address.png)

  - title: "Add the Datadog email address to your Stitch custom notification list"
    anchor: "add-datadog-email-to-stitch"
    content: |
      1. Sign into your Stitch account.
      2. Click the {{ app.menu-paths.account-settings }}.
      3. Click the **{{ app.page-names.notification-tab }}** tab.
      4. Click the **Add email** button in the **Custom notification list** section.
      5. In the field that displays, paste the Datadog email address you created in [Step 1](#create-event-email-address).
      6. Click the **Save Email** button.

      ---

next-steps: |
  After you've set up notifications in Datadog, use the [Notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}) to learn more about the notifications Stitch sends.
---