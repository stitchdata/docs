---
title: Automating Post-Load Processing Using Webhooks
permalink: /account-security/notifications/post-load-notifications
keywords: loading notifications, load notification, post-load, webhook, notify load
summary: "Automate your post-load processing functions using the Post-load webhooks notification feature. With Post-load notifications, you can configure a webhook to fire each time Stitch loads data into your destination."

layout: general
key: "post-load-notifications"
toc: true

type: "notifications"
weight: 4

enterprise: true
enterprise-cta:
  feature: "Post-load notifications "
  title: "{{ site.data.strings.enterprise.title.are-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.are-an | prepend: page.enterprise-cta.feature | flatify }}"


# -------------------------- #
#       Introduction         #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  In the **{{ app.page-names.notification-tab }}** tab of the **{{ app.page-names.account-settings }}** page, you can configure webhooks to fire each time data is loaded into your destination. Using Stitch's post-load hooks feature, you can automate your post-load processing functions.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - title: "Uses for post-load hooks"
    anchor: "post-load-hook-uses"
    summary: "Some uses for post-load hooks"
    content: |
      Using post-load hooks, you can trigger:

      - Downstream processing in SQL
      - An [Amazon Web Services Lambda](https://aws.amazon.com/lambda/){:target="new"}
      - [Talend Cloud](https://help.talend.com/reader/6SB6Qfc014RWM4mEltupHA/5SzrIShpW6sCuQXlekpBNQ){:target="new"} workflows
      - Any other system that can be controlled with an HTTP request

      For technical details about post-load hooks, refer to the [Post-load webhooks reference]({{ link.webhooks.post-load | prepend: site.baseurl }}).

  - title: "Access to post-load hooks"
    anchor: "post-load-hooks-access"
    summary: "How to access post-load hooks"
    content: |
      The post-load hook feature is available during the Free Trial or on an Enterprise plan. Contact [Stitch Sales]({{ site.sales }}){:target="new"} for more info about Enterprise plans.

    subsections:
      - title: "Plan downgrades"
        anchor: "plan-downgrades"
        content: |
          If you decide to downgrade to a plan without post-load hook access, the feature will be disabled and notifications will no longer be sent to the webhook URLs in the post-load hook list.

          If you upgrade from a plan without post-load hook access to a plan that includes it, and you previously added post-load webhook URLs in your account, you will need to [re-enable them](#disable-reenable-webhook-urls) to allow Stitch to send webhooks to the webhook URLs again.

  - title: "Post-load hook basics"
    anchor: "post-load-hook-basics"
    summary: "Some post-load hook basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "How many post-load hooks can I have?"
        anchor: "how-many-post-load-hooks"
        content: |
          An account's post-load hook list may have a maximum of 10 webhook URLs.

      - title: "How are webhooks sent?"
        anchor: "how-are-webhooks-sent"
        content: |
          Post-load webhooks are sent on a per-integration, per-table basis.

          For example: You're tracking two tables (`orders` and `customers`) in a Shopify integration. Stitch will send two post-load webhooks for the Shopify integration - one for the `orders` table, and one for `customers`.

      - title: "When are webhooks sent?"
        anchor: "when-are-hooks-sent"
        content: |
          A post-load hook will be sent each time data for a tracked table is successfully loaded or rejected.

          **Note**: In the event that Stitch is unable to deliver the webhook to the URL(s) in the Post-load hook list, an [email notification]({{ link.account.notification-settings | prepend: site.baseurl | append: "#undeliverable-post-load" }}) will be sent.

      - title: "What services can I use with post-load hooks?"
        anchor: "what-services-post-load-hooks"
        content: |
          To be compatible with Stitch post-load hooks, the service must provide a properly formatted HTTPS webhook URL.

  - title: "Manage post-load hooks"
    anchor: "manage-post-load-hooks"
    summary: "How to add, disable, and delete post-load hooks in your account"
    content: |
      Any team member in a Stitch account that has access to the post-load webhook feature can create, delete, disable, or re-enable a post-load webhook URL.

      You can manage post-load webhooks in two ways:

      1. **In the Stitch app**:
         {% for subsection in section.subsections %}
         - [{{ subsection.title | remove: " in the Stitch app" }}](#{{ subsection.anchor }})
         {% endfor %}
      2. [**Via the Connect API**]({{ link.connect.api | prepend: site.baseurl | append: "#notifications--section" }}), if your Stitch plan includes API access.
      
    subsections:
      - title: "Add a post-load webhook URL in the Stitch app"
        anchor: "add-post-load-hook"
        content: |
          {% include note.html type="single-line" content="**Note**: An account's post-load hook list may have a maximum of 10 webhook URLs." %}

          To add a post-load webhook URL:

          1. Click the {{ app.menu-paths.account-settings }}.
          2. Click the **{{ app.page-names.notification-tab }}** tab.
          3. Click the **Add Webhook** button in the **Post-load hooks** section.
          3. In the field that displays, paste the webhook URL.

             **Note**: [The webhook URL must use HTTPS](#what-services-post-load-hooks), otherwise you'll receive an `Invalid URI` error and be unable to save the webhook.
          4. Click the **Save Webhook** button.

      - title: "Delete a post-load webhook URL in the Stitch app"
        anchor: "delete-post-load-hook"
        summary: "How to delete a post-load hook"
        content: |
          To delete a post-load webhook URL:

          1. Click the {{ app.menu-paths.account-settings }}.
          2. Click the **{{ app.page-names.notification-tab }}** tab.
          3. Scroll to the **Post-load hooks** section.
          4. Click the icon next to the **Status** column.
          5. Click **Delete this webhook**.
          6. You'll be prompted to confirm the deletion. Click **Delete** to continue and delete the webhook URL.

      - title: "Disable or re-enable post-load webhook URLs in the Stitch app"
        anchor: "disable-reenable-webhook-urls"
        summary: "How to disable or re-enable a post-load webhook URL"
        content: |
          If you want to temporarily disable a post-load webhook, you can click the icon next to the webhook URL and use the **Disable this webhook** option.

          To re-enable a disabled webhook URL, click the icon next to the **Status** column and select **Re-enable this webhook**.

  - title: "Post-load hook technical reference"
    anchor: "post-load-hook-technical-reference"
    summary: "Technical resources for post-load hooks"
    content: |
      Refer to the [Post-load webhooks reference]({{ link.webhooks.post-load | prepend: site.baseurl }}) for detailed info about:

      - Data included in request headers and bodies
      - Retries
      - Security
---