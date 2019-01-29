---
title: JIRA (v1.0)
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
singer: true
status-url: "http://status.atlassian.com/"
repo-url: "https://github.com/singer-io/tap-jira"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "1 hour"
tier: "Paid"
icon: /images/integrations/icons/jira.svg

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to the issues, projects, worklogs, etc. that you want to replicate.** Stitch is only able to access the same objects that the user authenticating the integration has access to. If this user doesn't have access to specific datasets or records, Stitch will be unable to replicate them from {{ integration.display_name }}. Refer to [{{ integration.display_name }}'s documentation](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html#Managingprojectpermissions-permission_schemes){:target="new"} for more info about permissions in {{ integration.display_name }}.

setup-steps:
  - title: "Verify self-managed configuration"
    anchor: "verify-self-managed-configuration"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is only required if your JIRA instance is self-managed (hosted). Otherwise, skip this step." %}
    substeps:
      - title: "Verify your protocol support"
        anchor: "verify-protocol-support"
        content: |
          To connect to a self-managed {{ integration.display_name }} instance, your server must use `HTTPs` as the protocol. Stitch does not support `HTTP` for security reasons.

          When you complete the JIRA setup in Stitch, you'll be asked to enter your JIRA base URL. If Stitch determines that the protocol is not `HTTPs`, connection errors will arise.

          Before proceeding, verify that your server uses `HTTPs` as the protocol.

      - title: "Whitelist Stitch's IP addresses"
        anchor: "whitelist-stitch-ips"
        content: |
          If your self-managed {{ integration.display_name }} instance is behind a firewall, you'll also need to whitelist Stitch's IP addresses before proceeding. This ensures that Stitch will be allowed to access the instance. If you're unsure how to do this, contact a member of your technical team for assistance.

          Whitelist the following IP addresses:

          {% for ip-address in ip-addresses %}
          - {{ ip-address.ip }}
          {% endfor %}

  - title: "Generate a {{ integration.display_name }} API token"
    anchor: "generate-jira-api-token"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is only required if your JIRA instance is cloud-hosted. Otherwise, skip this step." %}

      To authenticate with a cloud-hosted {{ integration.display_name }} instance, Stitch requires a {{ integration.display_name }} username and an API token. In this step, you'll generate an API token in {{ integration.display_name }}.

      {% include layout/inline_image.html type="right" file="integrations/jira-cloud-api-token-window.png" max-width="400px" %}

      1. Sign into your {{ integration.display_name }} account.
      2. Click the **user menu (your icon)** in the bottom right corner of the page.
      3. Click **Manage your account**.
      4. Click the **Security** tab.
      5. In the **API token** section, click the **Create and manage API tokens** link.
      6. On the page that displays, click the **Create API token** button.
      7. In the window that displays, enter a **Label** for the API token. For example: `Stitch`
      8. Click **Create**.
      9. A new window containing the API token will display. **Copy the token before closing the window**, as {{ integration.display_name }} will only display it once.

  - title: "add integration"
    content: |
      4. In the **Base URL** field, enter the base URL for your JIRA site. For example: `stitchdata.atlassian.net`

         **Note**: If you're connecting a self-managed instance, your server must use the `HTTPs` protocol or Stitch will be unable to successfully connect.
      5. In the **Username** field, enter the email address of the JIRA user you want to use to authenticate the integration.
         **Note**: Stitch will replicate only the issues, projects, worklogs, etc. that this user has access to. If this user doesn't have access to specific datasets or records, Stitch will be unable to replicate them from JIRA.
      6. In the **Password or Token** field:
         - **If connecting a self-managed {{ integration.display_name }} instance**, enter the password associated with the user in the **Username** field.
         - **If connecting a cloud-hosted {{ integration.display_name }} instance**, paste the API token you generated in [Step 2](#generate-jira-api-token).
  - title: "historical sync"
  - title: "replication frequency"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #


# -------------------------- #
#    Documentation Links     #
# -------------------------- #

project-permissions-doc: "https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html"

global-permissions-doc: "https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html"

---
{% assign integration = page %}
{% include misc/data-files.html %}