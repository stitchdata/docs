---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Post-Load Webhook Reference
permalink: /developers/webhooks/post-load-webhooks
redirect_from: /developers/webhooks
keywords: loading notifications, load notification, post-load, webhook, notify load
summary: "Automate your post-load processing functions using the Post-load webhooks notification feature. With Post-load notifications, you can configure a webhook to fire each time Stitch loads data into your destination."

sidebar: on-page
layout: general
key: "post-load-webhooks-reference"
toc: true

enterprise: true
enterprise-cta:
  feature: "Post-load notifications "
  title: "{{ site.data.strings.enterprise.title.are-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.are-an | prepend: page.enterprise-cta.feature | flatify }}"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Manage post-load hooks in Stitch"
    link: "{{ link.account.post-load-notifications | prepend: site.baseurl }}"

  - title: "Post-load hooks API reference"
    link: |
      {{ link.connect.api | prepend: site.baseurl | append: "#notifications--section" }}

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign post-load-hooks-data = stitch.notifications.post-load-webhooks %}

  Post-load hooks allow you to configure a webhook that fires each time data is loaded into your destination.

  Using post-load hooks, you can extend Stitch and automate dependent processes. For example: Trigger downstream processing in SQL, an Amazon Web Services Lambda function, Talend Cloud jobs, or any other system that can be controlled with an HTTP request.


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Set up a post-load hook"
    anchor: "set-up-post-load-hook"
    content: |
      You can configure a post-load hook in two ways:

      1. [In the Stitch app]({{ link.account.post-load-notifications | prepend: site.baseurl | append: "#manage-post-load-hooks" }})
      2. [Via the Connect API]({{ link.connect.api | prepend: site.baseurl | append: "#notifications--section" }}), if your Stitch plan includes API access

      You can configure up to 10 post-load hooks.

  - title: "Webhook triggers"
    anchor: "webhook-triggers"
    content: |
      Post-load hooks are sent on a per-integration, per-table basis to each configured post-load webhook URL. The post-load webhook must have a status of **Enabled** in order for Stitch to send requests.

      If multiple tables are set to replicate for an integration, Stitch will send a request for each table every time data is successfully loaded or rejected.

      If the load for a table fails, a post-load webhook will not be sent. For example: The Stitch database user has insufficient database privileges. In this scenario, Stitch will send an [email notification]({{ link.account.notification-reference | prepend: site.baseurl }}).

  - title: "Security"
    anchor: "security"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Webhook URL requirements"
        anchor: "webhook-url-requirements"
        content: |
          To be compatible with Stitch post-load hooks, the service must provide a properly formatted HTTPS webhook URL. For example: `https://your-webhook-provider.com/webhooks`

          If the URL doesn't use HTTPS, you'll receive an `Invalid URI` error when you attempt to add the webhook in Stitch. 

      - title: "IP whitelisting"
        anchor: "ip-whitelisting"
        content: |
          Post-load notification webhook requests will originate from one of the following of Stitch's IP addresses:

          {% for ip-address in ip-addresses %}
          - {{ ip-address.ip }}
          {% endfor %}

          To add an additional layer of security, or if the service you're using requires it, you can whitelist Stitch's IP addresses. This ensures that only requests sent from Stitch will be accepted and processed by the webhook service you're using.

  - title: "Retries"
    anchor: "retries"
    content: |
      If the service you've configured to receive post-load hooks encounters problems, **Stitch will attempt to re-send the notification up to five times**. Stitch will re-try when the following occurs:

      - The request fails to connect
      - The request doesn't receive a response after 30 seconds (timeout)
      - The request recieves a response code other than `2xx`

      If the notification can't be delivered after the maximum number of retries, Stitch will send an [email notification]({{ link.account.notification-settings | prepend: site.baseurl | append: "#undeliverable-post-load" }}) immediately after the last retry fails. Replaying post-load hooks isn't currently supported.

      **Note**: A load is still considered successful even if the post-load notification webhook fails.

  - title: "Webhook payload"
    anchor: "webhook-payload"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Header"
        anchor: "payload-header"
        content: |
          Post-load notification webhook requests are `POST` requests with a `User-Agent` of `StitchLoadingWebhook`. For example:

          ```curl
          -X "POST" "https://your-webhook-service.com/webhook"
          -H 'Content-Type: application/json'
          -H 'User-Agent: StitchLoadingWebhook'
          ```

          **Note**: At this time, custom request headers are not supported.

      - title: "Request format"
        anchor: "request-format"
        content: |
          Post-load notification webhook requests have a JSON payload in the body, similar to the following example.

          Refer to the [Request body properties section](#request-body-properties) for attribute descriptions:

          ```json
          {{ stitch.notifications.post-load-webhooks.request-bodies.example-data.no-nested-tables }}
          ```

  - title: "Request body properties"
    anchor: "request-body-properties"
    content: |
      A post-load notification webhook object is composed of the following:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Top-level properties"
        anchor: "post-load-webhook-object-top-level-properties"
        content: |
          A post-load notification webhook object contains the following top-level properties:

          {% include templates/attribute-display.html type="table" table=post-load-hooks-data.request-bodies.top-level-attributes %}

      - title: "Table object properties"
        anchor: "post-load-webhook-table-object"
        content: |
          {{ post-load-hooks-data.descriptions.table-object | flatify }}

          **Note**: If using a destination [that doesn't natively support nested structures]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl | append: "#nested-data-structures" }}), this list will include subtables created as a result of denesting JSON arrays. Refer to the [Nested JSON data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) for more info.

          A `table` object contains the following properties:

          {% include templates/attribute-display.html table=post-load-hooks-data.request-bodies.table-attributes %}

      - title: "Bookmark metadata object properties"
        anchor: "post-load-webhook-bookmark-metadata-object"
        content: |
          {{ post-load-hooks-data.descriptions.bookmark-metadata-object | flatify }}

          A `bookmark_metadata` object contains the following properties:

          {% include templates/attribute-display.html table=post-load-hooks-data.request-bodies.bookmark-metadata-attributes %}
---
{% include misc/data-files.html %}