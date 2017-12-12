---
title: Stitch Incoming Webhooks FAQ
permalink: /integrations/webhooks/faq
keywords: incoming webhooks, integration, etl webhooks, webhooks etl, incoming webhooks, stitch webhooks, stitch webhook, schema
tags: [stitch_webhooks]
layout: page
toc: false
input: false
summary: "Have an Incoming Webhook question that wasn't covered in the Getting Started Guide? This FAQ may have exactly what you're looking for."
---
{% include misc/data-files.html %}

## General

### What is the Stitch Incoming Webhooks integration?
Stitch’s Incoming Webhooks integration provides a simple and flexible method to integrate any existing webhook API with Stitch. If Stitch doesn’t have a native integration for the webhook you want to integrate, then Stitch webhooks is your best bet.

### What services can I integrate using Stitch Incoming Webhooks?
With Stitch’s Incoming Webhooks integration, you have the ability to quickly and easily integrate with dozens of services that use webhook APIs. Some notable services include:

{% capture webhooks %}
{% assign saas-integrations = site.saas-integrations | where:"input","true" %}
{% for integration in saas-integrations %}
{% if integration.type == "Webhook" and integration.name != "incoming-webhooks" %}
- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl }})
{% endif %}
{% endfor %}
{% endcapture %}

{{ webhooks }}

### What do I need to use Stitch webhooks?


## Setup

### Do I have to provide a Primary Key?

{% include integrations/webhooks/primary-keys-replication.html %}

### Can I change the Primary Key after I’ve defined it?
We don’t recommend this, but yes, you can. Stitch uses Primary Keys to correctly replicate your data and prevent duplication; changing the Primary Key after the fact may result in fields not being updated correctly.

### How do I set up webhooks in [name] app?
For instructions on how to set up webhooks in your provider’s app, **refer to their documentation and reach out to their support team if you get lost**. Depending on the provider you’re using, the steps for implementing webhooks may differ.

However: you can find setup articles in our docs for a few of the most popular apps that the Stitch Incoming Webhooks integration is compatible with, such as:

{{ webhooks }}

## Webhook Data & Schema

### Does the Incoming Webhooks integration support historical data?
By design, most webhook-based integrations don’t retain historical data, as data is sent in real-time.

If the service you’re integrating with offers replay functionality, however, you may be able to send historical data to your Incoming Webhooks integration.

### What’s this {{ primary-key }} column?
When the Primary Key isn’t defined during the setup process, Stitch will automatically generate a Primary Key column called `{{ primary-key }}`. This is because Stitch requires Primary Keys to replicate and de-dupe data.

### What will the data from my Incoming Webhooks integration look like?

{% include integrations/webhooks/webhook-schema.html %}

### Why does the data table contain so many NULLs?
There are two reasons for this: one is the general nature of webhook data, and the other is how the Incoming Webhooks integration is designed.

The Stitch Incoming Webhook integration is designed to create only one top-level table. This single table will contain all the data that Stitch receives from your webhook, which can include several types of records. 

For example: if you set up Mandrill using Incoming Webhooks, your data table may contain records for whitelist events, click events, bounce events, and so on.

While each record type may contain some similar attributes (`id`, `created_at`, etc.), it's likely that each record type will have its own set of attributes, which will only be populated for that record or other specific record types.

As such, some columns in some records will contain `NULLs`. Here's an example with a Mandrill message send event, a whitelist add event, and a click event:

{% highlight markdown %}
| id | ts         | event | action | type      | ip          | url           |        
|----+------------+-------+--------+-----------+-------------+---------------|
| 1  | 1481730892 | send  | NULL   | NULL      | NULL        | NULL          |
| 2  | NULL       | NULL  | add    | whitelist | NULL        | NULL          |
| 3  | 1481732465 | click | NULL   | NULL      | 54.88.76.97 | http://hi.com |   

// record 1 is a message send event
// record 2 is a whitelist add event
// record 3 is a click event
{% endhighlight %}

### Why is there more than one table? You said there'd only be one table.
That's true; we did. 

**However**: if you're using a data warehouse that doesn't natively support nested structures, you may see multiple tables in your Incoming Webhooks integration schema. These are subtables, which a result of Stitch deconstructing nested data structures so the data can be loaded into your data warehouse. If the provider you integrate with uses nested data structures, you'll see subtables.

To learn more about this Stitch feature and how to tie subtables together in your queries, check out the [Handling of Nested Structures & Row Count Impact guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

## Miscellaneous

### Can you add Incoming Webhook docs for [integration?]
Our Technical Documentation Manager loves getting feedback and suggestions for docs. If you’re looking for something specific, **write into support**! We can’t promise that every suggestion will result in a new set of docs, but suggestions are welcomed and encouraged.

## Troubleshooting

If you’re encountering issues with your Stitch Webhooks integration or you have questions that weren’t covered in this guide, **please get in touch with us.**