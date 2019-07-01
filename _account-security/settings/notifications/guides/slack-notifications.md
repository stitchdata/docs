---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Integrate Stitch Notifications with Slack
permalink: /account-security/notifications/integrate-notifications-with-slack
summary: "Integrate Stitch notifications with Slack using Stitch's Custom email notification list feature."

input: false
layout: general

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

  Using the [Custom email notification list feature]({{ link.account.customize-notifications | prepend: site.baseurl }}), you can integrate Stitch notifications with your [Slack workspace](https://www.slack.com){:target="new"}.

  In this guide, we'll walk you through integrating your Stitch notifications with Slack using Slack's email integration features: Email forwarding and the Email app.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **A Stitch Enterprise plan.** The Custom email notification list is available only on a Stitch Enterprise plan.
  - item: |
      **An existing Slack account.** Depending on ]the method you want to use to integrate with Slack](#configure-slack), you may need a Slack Standard or Plus plan.


# -------------------------- #
#        Instructions        #
# -------------------------- #

sections:
  - title: "Step 1: Configure Slack"
    anchor: "configure-slack"
    content: |
      Using one of the two following methods, you can integrate Stitch email notifications with Slack:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Option {{ forloop.index }}: Integrate using a forwarding address"
        anchor: "integrate-using-forwarding-address"
        content: |
          Slack's [forwarding address feature](https://get.slack.help/hc/en-us/articles/206819278-send-emails-to-slack#set-up-a-forwarding-email-address){:target="new"} enables you to forward emails to your Slack workspace. Emails sent to the forwarding address are received in your direct message with Slackbot.

          {% include layout/inline_image.html type="right" file="account-security/notifications-slack-workspace.png" alt="Stitch workspace menu in Slack" max-width="200px" %}

          1. From your desktop Slack app, click your workspace name in the top left.
          2. Click **Preferences**.
          3. Click **Messages & Media**.
          4. In the **Bring Emails into Slack** section, click the **Get a forwarding Address** button.
          5. Copy the email address that displays:

             ![Slack forwarding email address]({{ site.baseurl }}/images/account-security/notifications-slack-forwarding-email-address.png)

      - title: "Option {{ forloop.index }}: Integrate using the Slack Email app"
        anchor: "integrate-using-email-app"
        content: |
           {% include note.html type="single-line" content="**Note**: The Email app requires a Standard or Plus Slack plan." %}

           Slack's [Email app](https://get.slack.help/hc/en-us/articles/206819278-send-emails-to-slack#connect-the-email-app-to-your-workspace){:target="new"} automatically routes emails to the channel or direct message in Slack that you specify.

           {% include layout/inline_image.html type="right" file="account-security/notifications-slack-email-app.png" alt="Slack Email App integration settings with the Email Address field highlighted" max-width="450px" %}

           1. Navigate to the [Email app page](https://my.slack.com/apps/A0F81496D-email){:target="new"} in the Slack App Directory.
           2. Click **Install**, or **Add Configuration** if the app has already been installed in your workspace.
           3. In the **Post to Channel** section, select the channel or direct message you want to post emails to.
           4. Click **Add Email Integration** to add the integration.
           5. After the integration has been successfully created, you can further define the integration's settings. Update the label, name, icon, or preview message as desired, clicking **Save Integration** when finished.
           6. Copy the **Email Address** from the top of the page.

  - title: "Step 2: Add the Slack email address to your Stitch custom notification list"
    anchor: "add-slack-email-to-stitch"
    content: |
      1. Sign into your Stitch account.
      2. Click the {{ app.menu-paths.account-settings }}.
      3. Click the **{{ app.page-names.notification-tab }}** tab.
      4. Click the **Add email** button in the **Custom notification list** section.
      5. In the field that displays, paste the Slack email address you created in [Step 1](#configure-slack), either by creating a forwarding address or using the Email app.
      6. Click the **Save Email** button.
---