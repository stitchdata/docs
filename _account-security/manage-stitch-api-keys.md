---
title: Managing Your Stitch API Keys
permalink: /account-security/managing-stitch-api-keys
keywords: api keys, create api key, stitch connect access
layout: general

summary: "Manage your Stitch API access keys."
type: "settings"
toc: true
weight: 2

enterprise-cta:
  title: "API access is an Enterprise feature"
  copy: |
    Access to the Stitch API is an Enterprise feature. [Contact Stitch Sales for more info]({{ site.sales }}){:target="new"}.

intro: |
  {% include misc/data-files.html %}

  {% include enterprise-cta.html %}

  With the Stitch API, you can programmatically control your Stitch account. This enables you to quickly create and configure integrations, select tables and columns for replication, connect Stitch with an external scheduler, and more.

  API key management and access to the Stitch API are Enterprise features.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "API key basics"
    anchor: "api-key-basics"
    summary: "Some API key basics"
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
          Any team member in a Stitch account can create, delete, disable, or re-enable an API key. While API keys are specific to the user who created them, all members of a Stitch account will be able to see high-level details about the API keys in use:

          [TODO-image example]

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

      [TODO-image example]

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
      4. Click the [TODO] icon next to the **Status** column.
      5. Click **Delete this key**.
      6. You'll be prompted to confirm the deletion. Click **Delete** to continue and delete the API key.

  - title: "Disable or re-enable an API key"
    anchor: "disable-reenable-api-key"
    summary: "How to disable or re-enable an API key"
    content: |
      If you want to temporarily disable an API key, you can click the [TODO] icon next to the key and use the **Disable this key** option.

      To re-enable a disabled key, [TODO]
---