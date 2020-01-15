---
title: Mandrill
permalink: /integrations/webhooks/mandrill
redirect_from: /integrations/saas/mandrill
## Some users may experience a blip while the redirect works - it's normal.

keywords: mandrill, integration, schema, etl mandrill, mandrill etl, mandrill schema, webhook, webhooks, stitch webhooks, incoming webhook
summary: "Connect your Mandrill data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."


# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mandrill"
display_name: "Mandrill"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "Webhook"
branded: false
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false
  field: 
tier: "Free"
status-url: "http://status.mandrillapp.com/"
icon: /images/integrations/icons/mandrill.svg

setup-name: "Incoming Webhooks"

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## TABLE NAME
  - name: "data"
    doc-link: https://mandrill.zendesk.com/hc/en-us/articles/205583287-Webhook-Format
    description: "attributes and data relevant to the events you select during the setup in the Mandrill app."
    notes: |
      If you're using a data warehouse that doesn't natively support nested structures, you may see more than one table in Mandrill's schema. These are subtables, which are a result of Stitch de-nesting the nested data structures in Mandrill's API so the data can be loaded into your data warehouse.

      Additionally, **this will result in a higher number of rows replicated than what's in the source.**

      Refer to Mandrill's Webhook documentation (linked below) for info about how their data is structured.
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    attribute-notes: |
      Depending on the events you selected during the setup in the Mandrill app, this table can contain data about the events in the list below.

      **For a full list of that event's attributes**, click the links to check out Mandrill's documentation.
    attributes:
      - name: <a href="http://help.mandrill.com/entries/58303976-Message-Event-Webhook-format" target="new">Message Events</a> - Sends, Deferrals, Hard/Soft Bounces, Opens, Click Spams, Unsubs, Rejects
      - name: <a href="http://help.mandrill.com/entries/57147393-Sync-Event-Webhook-format" target="new">Sync Events</a> - Whitelist and Blacklist Sync events
      - name: <a href="https://mandrill.zendesk.com/hc/en-us/articles/205583207-What-is-the-format-of-inbound-email-webhooks-" target="new">Inbound Messages</a>
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% capture notice-content %}
To set up Mandrill, you need:

1. [Admin permissions](http://kb.mailchimp.com/accounts/multi-user/manage-user-levels-in-your-account) in your MailChimp account.
2. To enable the [Mandrill add-on in MailChimp](http://kb.mailchimp.com/mandrill/add-or-remove-mandrill).
{% endcapture %}

{% capture prerequisites %}
{% include important.html first-line="**Setup prerequisites**" content=notice-content %}
{% endcapture %}

{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your MailChimp account. (Yes, you read that right!)
2. Click the **user menu (your icon) > Account**.
3. Click the **Transactional** tab.
4. Click **Launch Mandrill**.
5. Once you're in the Mandrill app, click the **Settings** icon in the left nav tab.
6. Click the **Webhooks** tab.
7. Click **Add a Webhook**.
8. **Check the events that you want to track**. Every time one of these events occurs, the webhook will be triggered and data will post to your webhook URL:

   ![Checking the events that will trigger the webhook]({{ site.baseurl }}/images/integrations/mandrill-webhook-setup.png)

9. In the **Post to URL** field, paste the Stitch-generated webhook URL.
10. Enter a brief **Description**.
11. When you're finished, click **Create Webhook**.
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}
{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}
