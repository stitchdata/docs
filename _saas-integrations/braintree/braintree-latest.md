---
title: Braintree (v1)
permalink: /integrations/saas/braintree
keywords: braintree, integration, schema, etl braintree, braintree etl, braintree schema
summary: "Connection instructions, replication info, and schema details for Stitch's Braintree integration."
layout: singer

key: "braintree-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "braintree"
display_name: "Braintree"

singer: true
repo-url: https://github.com/singer-io/tap-braintree

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://developers.braintreepayments.com/start/overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: https://status.braintreepayments.com/
whitelist-ips: true

api-type: "platform.braintree"

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to a Production Braintree account**. Stitch does not currently support connecting to Sandbox accounts."
  - item: "**Super Admin and API Access permissions in Braintree.** This is required to create the API access token in Braintree. [You can find info on Braintree user roles and permissions here](https://articles.braintreepayments.com/control-panel/basics/users-roles)."

requirements-info: |
  Additionally, Stitch's Braintree integration will only replicate transactions for the **default merchant account** in your Braintree instance. You can verify the merchant account set as the default by going to **Settings > Processing > Merchant Accounts** when signed into Braintree.

setup-steps:
  - title: "Whitelist Stitch's IP addresses in {{ integration.display_name }}"
    anchor: "whitelist-stitch-ips"
    content: |
      {% capture ip-restriction %}
      This step is only required if you [restrict IP access to your {{ integration.display_name }} account](https://articles.braintreepayments.com/reference/security/control-panel-whitelisting).

      If you don't use this feature, [skip to the next section](#retrieve-api-credentials).
      {% endcapture %}

      {% include note.html first-line="This step may not be required." content=ip-restriction %}

      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %} 

    substeps:
      - title: "Verify your Stitch account's data pipeline region"
        anchor: "verify-stitch-account-region"
        content: |
          {% include shared/whitelisting-ips/locate-region-ip-addresses.html %}

      - title: "Whitelist Stitch's IP addresses"
        anchor: "whitelist-stitch-ips-braintree"
        content: |
          1. Sign into your {{ integration.display_name }} account.
          2. Click **Settings > Security**.
          3. In the **Security Options** page, click **Edit** in the **IP and Hostname Restrictions** section.
          4. In the **IP Address or Hostname** field, paste one of the data pipeline region IP addresses you retrieved in the [previous step](#verify-stitch-account-region).
          5. Check the **Allow API Access** box.
          6. Click **Add Allowed Host**.
          7. Repeat steps 4-6 **for each Stitch IP address for your data pipeline region**.
          8. After all of Stitch's IP addresses have been added, click **Enable Restrictions**.

  - title: "Retrieve your {{ integration.display_name }} API credentials"
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

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Merchant ID** field, paste your Braintree Merchant ID.
      5. In the **Public Key** field, paste your Braintree Public Key.
      6. In the **Private Key** field, paste your Braintree Private Key.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/braintree

---
{% assign integration = page %}
{% include misc/data-files.html %}
