---
title: Getting Started with Stitch Incoming Webhooks
permalink: /integrations/webhooks
keywords: incoming webhooks, integration, etl webhooks, webhooks etl, incoming webhooks, stitch webhooks, stitch webhook
tags: [stitch_webhooks]
layout: page
input: false
summary: "Stitch’s Incoming Webhooks integration provides a simple and flexible method to integrate dozens of webhook APIs with Stitch. This Getting Started guide covers the basics of using Incoming Webhooks."
---
{% include misc/data-files.html %}

Stitch’s Incoming Webhooks integration provides a simple and flexible method to integrate dozens of webhook APIs with Stitch. If Stitch doesn’t have a native integration for the webhook you want to integrate, then Stitch webhooks is your best bet. Webhooks are handy for anything that requires a notification and follow-up response, including:

- Email events, such as bounces or spam
- Incoming support requests
- Incoming leads from a marketing website
- And so on!

---

## How Stitch Uses Webhooks

If you’ve never used a webhook before and this topic seems a little abstract, allow us to give you an example of how Stitch uses webhooks for many of its operations.

Every time one of the following events occur, we’re notified. This could be just a simple alert or something more detailed that includes actual data and a message:

- A new Stitch account is created or a customer changes their plan tier
- A new NPS (Net Promoter Score) response is received
- A customer submits an integration suggestion from our website or in the Stitch app

---

## Integrable Webhook Services

Webhooks are a simple, flexible way to keep everyone in the loop. With Stitch’s Incoming Webhooks integration, you have the ability to quickly and easily integrate with dozens of services that use webhook APIs. Some notable services include:

{% assign saas-integrations = site.saas-integrations | where:"input","true" %}
{% for integration in saas-integrations %}
{% if integration.type == "Webhook" and integration.name != "incoming webhooks" %}
- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl }})
{% endif %}
{% endfor %}

---

## Requirements for Using Stitch Incoming Webhooks

To use Stitch Incoming Webhooks:

1. You must have a Stitch account. The Incoming Webhooks integration is available to all Stitch users, whether you're on a Free or Paid tier.

2. The Webhook API you're integrating with meets the following requirements:
   - The data sent by the webhook API must come to Stitch in **JSON format**. This is currently the only format Stitch supports.
   - The payload (or delivery) of the data must come via a `POST` request.
   - The request body must be less than 4MB

You can determine if the webhook API you want to use meets the above criteria by checking out that provider's webhook API documentation.

---

## Setting Up Incoming Webhooks

If you’ve determined that the webhook API you want to use is compatible with Stitch Incoming Webhooks, there are four steps to getting the data flowing:

1. Add an Incoming Webhook integration in Stitch
2. Define the Primary Key
3. Generate a Stitch webhook URL
4. Complete the setup in your provider’s app

### Setting Up Webhooks in Stitch

To add Stitch Incoming Webhooks as an integration in your Stitch account, **look for the integration in the Add an Integration page.** Some integrations - like Contentful and Zapier - have their own dedicated pages in Stitch.

**If you don't see the webhook integration you want in Stitch,** don't worry! If you've determined that that provider's API meet's Stitch's requirement, you can use the **generic Incoming Webhooks integration** to complete the setup. For how-to instructions, check out the [Setting Up Stitch Webhooks guide]({{ link.integrations.webhooks | prepend: site.baseurl }}).

### Setting Up Webhooks in Your Provider’s App
Depending on the provider you’re using, the steps for implementing webhooks may differ. We recommend checking out your provider’s documentation for instructions and reaching out to their support team if necessary.

---

## Webhook Data

{% include integrations/webhooks/webhook-schema.html %}
For example: if the webhook API you integrate with only contains `id`, `event`, and `value` fields, these are the only fields that will be created in the `data` table.

---

## Troubleshooting

If you’re encountering issues with your Stitch Webhooks integration or you have questions that weren’t covered in this guide, check out the [Stitch Webhooks FAQ]({{ site.baseurl }}/integrations/webhooks/faq).

If your question still hasn’t been answered, please get in touch with us.