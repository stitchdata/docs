---
title: FormKeep
permalink: /integrations/webhooks/formkeep
redirect_from: /integrations/saas/formkeep
## Some users may experience a blip while the redirect works - it's normal.

tags: [stitch_webhooks]
keywords: formkeep, integration, schema, etl formkeep, formkeep etl, formkeep schema, stitch webhooks
summary: "Connect your FormKeep data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse." 

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "formkeep"
display_name: "FormKeep"
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
status-url: "https://twitter.com/formkeep"
icon: /images/integrations/icons/formkeep.svg

table-selection: false
column-selection: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link:  
    description: "The FormKeep table created by Stitch will contain all the fields in your form along with created at information."
    notes: |
      ### Primary Keys
      While FormKeep tables won't have a designated Primary Key, you can use all the columns in the table in conjunction with the `created_at` column to create a composite key that identifies unique records. Some forms will likely only be submitted once (such as for an email list) but others may be used multiple times. A feedback form is a good example of a form that a person may use multiple times.
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    attribute-notes: |
      Other than the `_sdc` columns and a `created_at` column, the attributes contained in this table will depend on the fields that exist in your FormKeep form.

      For example: you have a partner signup form on your website that asks for a first name, last name, company name, website, and email address. In this case, your table might look like this:
    attributes:
      - name: created_at
      - name: first_name
      - name: last_name
      - name: company_name
      - name: website
      - name: email_address
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% capture notice-content %}
There are two ways to set up webhooks in FormKeep: Via a custom URL in the FormKeep app or using Zapier's FormKeep integration.

If your form is already using a custom webhook URL in FormKeep, you'll need to:

1. **Use Stitch's Zapier integration** instead of **FormKeep**. This is because of how Primary Keys are defined between the Zapier and FormKeep integrations.
  
2. After generating your Stitch webhook URL, follow the instructions for [setting up a FormKeep integration in Zapier](#zapier-formkeep-integration).
{% endcapture %}

{% capture prerequisites %}
{% include important.html first-line="**Already using a FormKeep webhook URL?**" content=notice-content %}
{% endcapture %}

{% include integrations/webhooks/webhook-setup.html %}

**If another webhook URL is currently in use for your form**, you'll have to use [Zapier's FormKeep integration](#zapier-formkeep-integration) to complete the setup.

Otherwise, you can use the instructions in the **Using a Custom Webhook URL** section, below.

#### Via a Custom Webhook URL {#custom-webhook-url}

1. Sign into your FormKeep account.
2. Using the drop-down menu under the FormKeep logo, **select the form** you want to add the webhook to.
3. After the settings for that form open, click the **Webhooks** option.
4. Scroll to the bottom of the Webhooks page.
5. In the **Webhook URL** field, paste your Stitch-generated webhook URL:

    ![Setting up webhooks in FormKeep]({{ site.baseurl }}/images/integrations/formkeep-webhook-setup-custom-url.png)

6. Click **Save**.

#### Via Zapier's FormKeep integration {#zapier-formkeep-integration}

{% include note.html type="first-line" content="You only need to complete the following if you're not using a custom webhook URL in the FormKeep app." %}

1. In Zapier, click **Make a Zap!**
2. On the **Choose a Trigger App** page, click **FormKeep**.
3. On the **Select FormKeep Trigger** page, click **Save + Continue**.
4. On the **Select FormKeep Account** page, select the FormKeep account you want to use. 

   **If you haven't previously connected the account**, you can find your API token by [clicking here](https://formkeep.com/account/zapier-token) when you're signed into your FormKeep account.
5. Click **Save + Continue** after you've selected the correct FormKeep account.
6. In the drop-down, select the **form** you want to use and then click **Continue**.
7. To test the setup so far, click **Fetch & Continue**. When the test successfully completes, click **Continue**.
8. Next, you'll select the Action, or where Zapier will send your FormKeep data. On the **Choose an Action App** page, scroll down to the **Built-in Apps** section and click **Webhooks**:

   ![Selecting the Webhooks integration in Zapier]({{ site.baseurl }}/images/integrations/zapier-webhooks-integration.png)

9. On the **Select Webhooks by Zapier Action** page, select the **POST** option and click **Save + Continue**.
10. Fill in the following fields:
  - In the **URL** field, paste your Stitch-generated webhook URL.
  - In the **Payload Type** field, select **JSON** from the drop-down menu. **Note that Stitch only accepts data in JSON format at this time** - if anything else is selected, the integration won’t work:

        ![Setting up webhooks for FormKeep in Zapier]({{ site.baseurl }}/images/integrations/formkeep-zapier-webhook-setup.png)

11. When finished, click **Continue**.
12. If you want to test the setup so far, you can do so now. When finished, click **Continue** to wrap things up.
13. Lastly, enter a **name** for your Zap, use the drop-down to **select a folder**, and then toggle the Zap to **on**.
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