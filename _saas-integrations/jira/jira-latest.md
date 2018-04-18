---
title: JIRA
permalink: /integrations/saas/jira
tags: [saas_integrations]
keywords: jira, integration, schema, etl jira, jira etl, jira schema
summary: "Connection instructions and schema details for Stitch's JIRA integration."
layout: singer
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "jira"
display_name: "JIRA"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://status.atlassian.com/"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/jira.svg
whitelist-ips: true ## if true, Stitch's IP addresses must be whitelisted to access this integration's data
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Adminstrator permissions in JIRA.** This is required to complete parts of the setup process."

setup-steps:
  - title: "Whitelist Stitch's IP addresses"
    anchor: "whitelist-stitch-ips"
    content: |
      {% include note.html content="This step is only required if your JIRA instance is both self-hosted and behind a firewall." %}
      
      Whitelist all of the following IP addresses:

      {% for ip-address in ip-addresses %}
      - {{ ip-address.ip }}
      {% endfor %}

      Be sure to do this before continuing through the rest of the setup or you may encounter errors when saving the integration.

  - title: "Verify your protocol support"
    anchor: "verify-protocol-support"
    content: |
      {% include note.html content="This step is only required if your JIRA instance is self-hosted." %}

      If your JIRA instance is self-hosted, you'll also need to verify that your server uses `HTTPs` as the protocol. Stitch does not support `HTTP` for security reasons.

      When you complete the JIRA setup in Stitch, you'll be asked to enter your JIRA base URL. If Stitch determines that the protocol is not `HTTPs`, connection errors will arise.

  - title: "Retrieve your Stitch public key"
    anchor: "retrieve-stitch-public-key"
    content: |
      {{ site.data.tooltips.public-key | flatify }} In this case, when you add the public key to your JIRA instance, it allows Stitch to access and extract data from the account.

      1. {{ app.menu-paths.add-integration | flatify }}
      2. Click the **JIRA** icon.
      3. Locate the **Public Key** field.

      Leave this page open for now - you'll need this to set up the application access in JIRA in the next step.

  - title: "Grant Stitch application access to {{ integration.display_name }}"
    anchor: "grant-stitch-access-to-jira"
    content: |
      **Note that you need Administrator permissions to complete the steps in this section**. If you're not an Admin, loop in someone who can help you before continuing.

      1. Sign into your JIRA account.
      2. Click the **Settings (gear)** icon in the top-right corner.
      3. In the drop-down menu, click **Applications**.
      4. Click the **Application** link in the **Integrations** section of the menu on the left side of the page.
      5. In the **Application** field, enter `stitchdata.com`.
      6. Click **Create new link**.

      A few ‘Configure Application URL’ messages might display after clicking the **Create new link** button. If you see these, don’t worry - everything is still on track.

      Click **Continue** to keep going.
    substeps:
      - title: "Define the first set of Link Application settings"
        anchor: "define-first-link-application-settings"
        content: |
          1. When the **Link Applications** window displays, enter `stitch` into the following fields:
             - Application Name
             - Service Provider Name
          2. Set the **Application Type** field to **Generic Application**.
          3. Enter `rjmetrics` into the following fields:
             - Consumer Key
             - Shared Secret
          4. Enter `stitchdata.com` into the following fields:
             - Request Token URL
             - Token URL
             - Authorize URL
          5. Check the **Create incoming link** box.
          6. Click the **Continue** button and a second Link Applications window will display.

      - title: "Define the second set of Link Application settings"
        anchor: "define-second-link-application-settings"
        content: |
          1. In the **Consumer Key** field, enter `rjmetrics`.
          2. In the **Consumer Name** field, enter `stitch`.
          3. In the **Public Key** field, paste the entire Public Key from the Stitch JIRA credentials page.
          4. Click the **Continue** button.

          If the link configuration was successful, you’ll see a **Success!** message on the Configure Application Links page.

  - title: "add integration"
    content: |
      4. In the **Base URL** field, enter the base URL for your JIRA site. **Remember**: If you're connecting a self-hosted instance, your server must use the `HTTPs` protocol or Stitch will be unable to successfully connect. 
  - title: "historical sync"
  - title: "replication frequency"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

---
{% assign integration = page %}
{% include misc/data-files.html %}