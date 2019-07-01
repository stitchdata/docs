---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Integrate Stitch Notifications with PagerDuty
permalink: /account-security/notifications/integrate-notifications-with-pagerduty
summary: "Integrate Stitch notifications with PagerDuty using Stitch's Custom email notification list feature."

input: false
layout: tutorial
use-tutorial-sidebar: true

type: "notifications"
weight: 5

enterprise: true
enterprise-cta:
  feature: "The custom notification list "
  title: "{{ site.data.strings.enterprise.title.is-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.is-an | prepend: page.enterprise-cta.feature | flatify }}"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Extend Stitch email notificatons"
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

  Using the [Custom email notification list feature]({{ link.account.customize-notifications | prepend: site.baseurl }}), you can integrate Stitch notifications with your [PagerDuty account](https://www.pagerduty.com){:target="new"}.

  In this guide, we'll walk you through integrating your Stitch notifications with PagerDuty using [PagerDuty's email integration feature](https://www.pagerduty.com/docs/guides/email-integration-guide/){:target="new"}.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **A Stitch Enterprise plan.** The Custom email notification list is available only on a Stitch Enterprise plan.
  - item: |
      **An existing PagerDuty account.**


# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Create a new service in PagerDuty"
    anchor: "create-new-service-in-pagerduty"
    content: |
      1. Sign into your PagerDuty account.
      2. Click **Configuration > Services**.
      3. Click **+ Add Services**.
      4. In the **General Settings** section, enter a **Name** and a **Description**.
      5. In the **Integration Settings** section:
         - **Integration Type** - Click **Integrate via email**.
         - **Integration Email** - Enter the PagerDuty email address that will receive Stitch notifications.
      6. In the **Incident Settings**, **Incident Behavior**, and **Alert Grouping** sections, define what PagerDuty should do when it receives a notification from Stitch.
      7. When finished, click the **Add Service** button.

  - title: "Optional: Configure PagerDuty email management rules"
    anchor: "configure-pagerduty-email-management-rules"
    content: |
      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Configure email filter rules"
        anchor: "configure-email-filter-rules"
        content: |
          PagerDuty supports using regular expressions (regex) to create email filter rules. These rules determine whether an email is accepted or disregarded in PagerDuty. Messages that don't pass the filter(s) are silently discarded.

          This feature can be helpful if there are Stitch notifications that you don't want to trigger PagerDuty incidents.

          For example: If you only want to be notified about [critical data loading errors]({{ link.account.notification-settings | prepend: site.baseurl | append: "#loading-error" }}), you could set up an email rule that matches the subject `We're having trouble writing to your data warehouse`.

          {% capture notification-reference %}
          Use the [email notification reference]({{ link.account.notification-reference | prepend: site.baseurl }}) to help create email filters in PagerDuty.
          {% endcapture %}

          {% include tip.html type="single-line" content=notification-reference %}

          Refer to [PagerDuty's documentation](https://support.pagerduty.com/docs/email-management-filters-and-rules#section-advanced-email-management-extracting-information-with-regular-expressions){:target="new"} for more info and instructions.

      - title: "Configure incident creation settings"
        anchor: "configure-incident-settings"
        content: |
          Using the integration settings in PagerDuty, you can control when new incidents are created in response to email notifications.

          Refer to [PagerDuty's documentation](https://support.pagerduty.com/docs/email-management-filters-and-rules#section-trigger-and-resolve-alerts-with-email-management-rules){:target="new"} for more info and instructions.

  - title: "Add the PagerDuty email address to your Stitch custom notification list"
    anchor: "add-pagerduty-email-to-stitch"
    content: |
      1. Sign into your Stitch account.
      2. Click the {{ app.menu-paths.account-settings }}.
      3. Click the **{{ app.page-names.notification-tab }}** tab.
      4. Click the **Add email** button in the **Custom notification list** section.
      5. In the field that displays, paste the Pagerduty **Integration Email** from [Step 1](#create-new-service-in-pagerduty).
      6. Click the **Save Email** button.
---