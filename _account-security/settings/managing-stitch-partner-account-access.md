---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Managing Stitch Partner Account Access
permalink: /account-security/managing-stitch-partner-account-access
keywords: stitch partner, partner access, partner keys, partner api, partner
summary: "View and manage the Stitch partners you have authorized to access your Stitch account."

key: "manage-partner-account-access"

layout: general
toc: true

type: "manage-your-account"
weight: 5


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% capture notice %}
  **Note**: Partner keys are different than API access keys. Refer to the [API access keys documentation]({{ link.account.manage-api-keys | prepend: site.baseurl }}) if you want to use the Stitch API yourself.
  {% endcapture %}

  {% include note.html type="single-line" content=notice %}

  In the **Partner keys** section of the **{{ app.page-names.account-settings }}** page, you can view and manage the Stitch partners that have access to your Stitch account. The partners in this list with an **Enabled** status have authorization to access your Stitch account via the Stitch API.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "How a Stitch partner is granted account access"
    anchor: "how-stitch-partner-get-account-access"
    summary: "How a Stitch partner is granted account access"
    content: |
      Stitch partners are granted access to your account when you create a connection to Stitch from their application. If there aren't any Stitch partners that have access to your account, this section will say **No current partner keys**.

      For example: If you created a Stitch account through your [Snowflake](http://snowflakecomputing.com){:target="new"} account, Snowflake would be listed as an authorized partner for your Stitch account:

      ![A Snowflake partner listed in the Partner keys table in Stitch]({{ site.baseurl }}/images/account-security/partner-access-keys-table.png)

  - title: "Revoke a partner's account access"
    anchor: "revoke-partner-account-access"
    summary: "How to revoke a partner's account access"
    content: |
      You can revoke access to partners at any time. When you revoke access, the affected partner will no longer be able to perform actions for Stitch on your behalf.

      For example: If you revoke access to Snowflake, Stitch will no longer be able to load replicated data into your Snowflake destination.

      ![Disabling a partner key in Stitch]({{ site.baseurl }}/images/account-security/partner-access-keys-disable-menu.png)

  - title: "Restore a partner's account access"
    anchor: "restore-partner-account-access"
    summary: "How to restore a partner's account access"
    content: |
      If you accidentally revoke a partner's access by deleting their access key, you can re-authorize the connection to Stitch from the partner's application.

      To perform the re-authorization, you'll need to sign into the partner's application and complete the re-authorization process.

      The partner will be listed in the **Partner keys** section with a status of **Enabled** when the connection is successfully reestablished.
---