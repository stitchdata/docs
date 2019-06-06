---
title: Managing Your Stitch API Keys
permalink: /account-security/managing-stitch-api-keys
keywords: api keys, create api key, stitch connect access
layout: general

summary: "Manage your Stitch API access keys."
toc: true

type: "account-settings"
weight: 3

enterprise-cta:
  title: "API access is an Enterprise feature"
  copy: |
    Access to the Stitch API is an Enterprise feature. [Contact Stitch Sales for more info]({{ site.sales }}){:target="new"}.

intro: |
  {% include misc/data-files.html %}

  {% include enterprise-cta.html %}

  With the Stitch API, you can programmatically control your Stitch account. This enables you to quickly create and configure integrations, select tables and columns for replication, connect Stitch with an external scheduler, and more.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "API key basics"
    anchor: "api-key-basics"
    summary: "Some API key basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "What does an API key do?"
        anchor: "api-key-actions"
        content: |
          A Stitch API key grants the user access to your Stitch account via the API. API keys should be handled like other credentials, such as a password. Stitch will display API keys only once, immediately after they are created.

          {% include important.html type="single-line" content="**Don't share your API key!** Not even with Stitch Support. Keep it secret; keep it safe." %}

          If an API key is lost or compromised, [delete the API key in Stitch](#delete-api-key) and then [create a new one](#create-api-key).

      - title: "How many API keys can I have?"
        anchor: "maximum-api-keys"
        content: |
          A single Stitch account may have up to 10 API keys at a time. This includes API keys that are currently enabled or disabled.

      - title: "Who can create an API key?"
        anchor: "who-can-create-keys"
        content: |
          Any team member in a Stitch account with API access can create, delete, disable, or re-enable an API key. While API keys are specific to the user who created them, all members of a Stitch account will be able to see high-level details about the API keys in use:

          ![An enabled API access key with a description]({{ site.baseurl }}/images/account-security/api-key-table.png)

      - title: "What Stitch plans include API access?"
        anchor: "plans-with-api-access"
        content: |
          Only the Stitch Enterprise plan includes access to the Stitch API. 

      - title: "What happens if I downgrade to a plan without API access?"
        anchor: "plan-downgrade"
        content: |
          If you decide to downgrade to a plan without API access, your API keys will be revoked (disabled).

          If you upgrade from a plan without API access to a plan that includes it, and you previously created API keys in your account, you will need to [re-enable the API keys](#disable-reenable-api-key) to utilize the API again.

  - title: "Create an API key"
    anchor: "create-api-key"
    summary: "How to create an API key"
    content: |
      To create an API key:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.account-settings }}** tab.
      3. In the **API access keys** section, click the {{ app.buttons.generate-api-key }} button. This will open the **Configure Your API Access Key** page.
      4. In the **Key Description** field, enter a description of what the API key will be used for. For example: `Used to create and configure Salesforce integrations`
      5. Click {{ app.buttons.save-api-key }}.
      6. The API key will be created and display on a new page. **Copy the API key before closing the page** - Stitch will only display the API key once.
      7. After you've copied the API key, click {{ app.buttons.close-continue }}.

      An entry for the API key will display in the **API access keys** section of the {{ app.page-names.account-settings }} page:

      ![An enabled API access key with a description]({{ site.baseurl }}/images/account-security/api-key-table.png)

  - title: "Delete an API key"
    anchor: "delete-api-key"
    summary: "How to delete an API key"
    content: |
      If an API key is lost or compromised, you should delete the key in Stitch and create a new one.

      To delete an API key:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. Click the **{{ app.page-names.account-settings }}** tab.
      3. Locate the API key you want to delete in the **API access keys** section.

         {% include tip.html type="single-line" content="**Not sure which key you need to delete?** If you know the last four characters of the key, you can match them to the value in the **Key (last 4)** column." %}
      4. Click the icon next to the **Status** column.
      5. Click **Delete this key**.
      6. You'll be prompted to confirm the deletion. Click **Delete** to continue and delete the API key.

  - title: "Disable or re-enable an API key"
    anchor: "disable-reenable-api-key"
    summary: "How to disable or re-enable an API key"
    content: |
      If you want to temporarily disable an API key, you can click the icon next to the key and use the **Disable this key** option.

      To re-enable a disabled key, click the icon next to the **Status** column and select **Re-enable this key**.

  - title: "Manage Stitch partner account access"
    anchor: "manage-stitch-partner-account-access"
    summary: "How to manage Stitch partner account access"
    content: |
      Refer to the [Manage Stitch partner account access guide]({{ link.account.manage-partner-access | prepend: site.baseurl }}) to learn more about managing partner account access.
---