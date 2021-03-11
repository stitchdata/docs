---
title: Managing Account Settings
permalink: /account-security/managing-account-settings
keywords: company information, team members, account settings
summary: "Manage your company's info and team members on the Account Settings page."

layout: general
toc: true

type: "account-settings"
weight: 3

enterprise-cta:
  title: "Need HIPAA compliance?"
  url: "?utm_medium=docs&utm_campaign=hipaa-compliance"
  copy: |
    Activating this setting will not, by itself, make your Stitch account HIPAA compliant. As part of an Enterprise plan, Stitch can ensure PHI is handled in compliance with HIPAA. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).

intro: |
  {% include note.html type="single-line" content="**Note**: Updating the settings outlined in this guide will affect your entire Stitch account." %}

  On the **Account Settings** page, you can view and manage your company's info, data pipeline region, API and partner keys, and team members.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Update your company information"
    anchor: "update-company-information"
    summary: "How to update your company information"
    content: |
      1. Click the {{ app.menu-paths.account-settings }}.
      2. In the **Company Name** field, enter the name of your company.
      3. Click the {{ app.buttons.company-profile }} button.

  - title: "Identify your data pipeline region"
    anchor: "identify-data-pipeline-region"
    summary: "How to identify your data pipeline region"
    content: |
      Refer to the [Supported Data Pipeline Regions guide]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) for more info.

  - title: "Manage your API and partner keys"
    anchor: "manage-api-partner-keys"
    summary: "How to manage your account's API and partner keys"
    content: |
      Refer to the [Managing Your Stitch API Keys]({{ link.account.manage-api-keys | prepend: site.baseurl }}) and [Managing Stitch Partner Account Access]({{ link.account.manage-partner-access | prepend: site.baseurl }}) guides for more info.

  - title: "Manage Single Sign-on"
    anchor: "manage-single-sign-on"
    summary: "How to manage your account's Single Sign-on (SSO) settings"
    content: |
      Refer to the [Managing Single Sign-on (SSO)]({{ link.security.single-sign-on | prepend: site.baseurl }}) guide for more info.

  - title: "Manage account team members"
    anchor: "manage-account-team-members"
    summary: "How to manage your account's team members"
    content: |
      Refer to the [Managing account team members guide]({{ link.account.team-members | prepend: site.baseurl }}) for info on managing the users in your Stitch account.
---
{% include misc/data-files.html %}