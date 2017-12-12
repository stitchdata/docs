---
title: Zapier
permalink: /integrations/webhooks/zapier
redirect_from: /integrations/saas/zapier

tags: [stitch_webhooks]
keywords: zapier, integration, schema, etl zapier, zapier etl, zapier schema
summary: "Connect your Zapier data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zapier"
display_name: "Zapier"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "Webhook"
branded: true
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false
  field: 
tier: "Free"
status-url: "https://status.zapier.com/"
icon:  /images/integrations/icons/zapier.svg

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: 
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: 
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% capture intro %}
Zapier is incredibly useful, powerful, and flexible. Because Zapier gives you complete control over how your data is defined and sent, we'll walk you through the setup using a Zap we use at Stitch every day.

Whenever you provide feedback to us while chatting on Drift, we record it using a Google Form. We set up a Zap that sends new submissions to our data warehouse, where we can analyze them and determine what our top priorities for development are. Additionally, everyone is notified of a new submission via email and a notification in Slack.
{% endcapture %}

{% include integrations/webhooks/webhook-setup.html %}
[Zapier has detailed instructions](https://zapier.com/help/creating-zap/) that delve into the finer points of making a Zap, but for our purposes, we'll keep it high-level.

In this example, we'll demonstrate by walking you through how we set up our product feedback webhook using Zapier and Google Forms.

#### Define the Trigger
In this step, you'll define the event that will trigger the webhook.

1. Sign into your Zapier account.
2. Click **Make a Zap!** at the top of the page.
3. Select the appropriate app from the **Choose a Trigger App** page. For us, we chose Google Forms.
4. Next, you'll define the Trigger. We chose to use new responses in our spreadsheet as our trigger.
5. Depending on the app you've selected, you may be asked to select the account you want to use. Select the appropriate account and click **Continue** when finished.
6. If you want to test the set up before moving on, feel free to do so now.

#### Define the Action
Next, you'll define the action, or what happens once the webhook has been triggered.

1. Select **Webhooks** from the **Choose a Trigger App** page. It's in the **Built-in Apps** section.
2. On the **Action** page, click **POST. Note that Stitch Incoming Webhooks only accepts POST requests at this time** - if anything else is selected, the integration won't work.
3. Next, you'll define the template for the Zap:
   - In the **URL** field, paste the Stitch-generated webhook URL.
   - In the **Payload Type** field, select **JSON** from the drop-down menu. **Note that Stitch Incoming Webhooks only accepts data in JSON format at this time** - if anything else is selected, the integration won't work.
   - If you choose to, you can define data in the **Data** section. **Note that this section is optional; if left blank then the raw data from the previous step (from the app you chose) will be used instead**:

     ![Example of Stitch's Google Forms setup in Zapier]({{ site.baseurl }}/images/integrations/zapier-webhook-setup.png)
     
     We chose to re-define our form fields here, as using the raw data from the Google Form would result in columns named like this: `gsx$clientid`, which we felt wasn't query-friendly.
4. When you're finished defining the other options for the template, click **Continue**.
5. If you'd like to test the setup so far, do so now.
6. If you want to add more steps, click the **Add a step** button.
   Otherwise, if you're finished, click **Finish**.
8. If your testing was successful and you're happy with your setup, toggle the Zap to **On** to get the data flowing.
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