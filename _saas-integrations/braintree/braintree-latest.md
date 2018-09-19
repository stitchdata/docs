---
title: Braintree
permalink: /integrations/saas/braintree
tags: [saas_integrations]
keywords: braintree, integration, schema, etl braintree, braintree etl, braintree schema
summary: "Connection instructions, replication info, and schema details for Stitch's Braintree integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "braintree"
display_name: "Braintree"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-braintree 

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://status.braintreepayments.com/
icon: /images/integrations/icons/braintree.svg
whitelist-ips: true ## if true, Stitch's IP addresses must be whitelisted to access this integration's data
whitelist:
  tables: false
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to a Production Braintree account**. Stitch does not currently support connecting to Sandbox accounts."
  - item: "**Super Admin and API Access permissions in Braintree.** This is required to create the API access token in Braintree. [You can find info on Braintree user roles and permissions here](https://articles.braintreepayments.com/control-panel/basics/users-roles)."

requirements-info: |
  Additionally, Stitch's Braintree integration will only replicate transactions for the **default merchant account** in your Braintree instance. You can verify the merchant account set as the default by going to **Settings > Processing > Merchant Accounts** when signed into Braintree.

setup-steps:
  - title: "Whitelist Stitch's IP addresses in Braintree"
    anchor: "whitelist-stitch-ips"
    content: |
      {% capture ip-restriction %}
      This step is only required if you [restrict IP access to your Braintree account](https://articles.braintreepayments.com/reference/security/control-panel-whitelisting).

      If you don't use this feature, [skip to the next section](#retrieve-api-credentials).
      {% endcapture %}

      {% include note.html first-line="This step may not be required." content=ip-restriction %}

      1. Sign into your Braintree account.
      2. Click **Settings > Security**.
      3. In the **Security Options** page, click **Edit** in the **IP and Hostname Restrictions** section.
      4. In the **IP Address or Hostname** field, paste one of the IP addresses from the following list:

         {% for ip-address in ip-addresses %}
         - {{ ip-address.ip }}
         {% endfor %}

      5. Check the **Allow API Access** box.
      6. Click **Add Allowed Host**.
      7. Repeat steps 4-6 **for each Stitch IP address in the list above**.
      8. After all of Stitch's IP addresses have been added, click **Enable Restrictions**.

  - title: "Retrieve your Braintree API credentials"
    anchor: "retrieve-api-credentials"
    content: |
      1. If you haven't already, sign into your Braintree account.
      2. Click **Account > My User**.
      3. Scroll down to the **API Keys, Tokenization Keys, Encryption Keys** section and click **View Authorizations**.
      4. In the **API Keys** section, click **Generate New API Key**.
      5. After the key has been generated, click the **View** link in the **Private Key** column.
      6. This will display the **Client Library Key** page, which contains your Braintree API credentials:

         ![Braintree API credentials.]({{ site.baseurl }}/images/integrations/braintree-api-credentials.png)

      Leave the Braintree Client Library Key page open for now - you'll need the **Public Key**, **Private Key**, and **Merchant ID** to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **Merchant ID** field, paste your Braintree Merchant ID.
      5. In the **Public Key** field, paste your Braintree Public Key.
      6. In the **Private Key** field, paste your Braintree Private Key.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/braintree

---
{% assign integration = page %}
{% include misc/data-files.html %}
