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
whitelist-ips: true
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

  - title: "Create a Stitch JIRA user"
    anchor: "create-jira-user"
    content: |
      {% include note.html content="This step is optional. You may use your own credentials to create the integration in the next step if you don't want to create a Stitch JIRA user." %}

      **Note**: Depending on the permissions structure your JIRA organization uses, [Administrator permissions may be required to create a user](https://confluence.atlassian.com/get-started-with-jira-software/set-up-your-software-team-937185135.html).

      Creating a dedicated user for Stitch ensures that Stitch will be obvious in any logs or audits. To create a user, [follow the instructions in JIRA's documentation](https://confluence.atlassian.com/get-started-with-jira-software/set-up-your-software-team-937185135.html).

      #### User access and replication

      Stitch will replicate only the issues, projects, worklogs, etc. that the Stitch user has access to. After the Stitch user is created, verify that the user has access to all the issues, projects, worklogs, etc. that you want to replicate. If the Stitch user doesn't have access to specific datasets or records, Stitch will be unable to replicate them from JIRA.
  - title: "add integration"
    content: |
      4. In the **Base URL** field, enter the base URL for your JIRA site. **Remember**: If you're connecting a self-hosted instance, your server must use the `HTTPs` protocol or Stitch will be unable to successfully connect.
      5. In the **Username** field, enter the email address of the JIRA user you want to use to authenticate the integration.
         **Note**: Stitch will replicate only the issues, projects, worklogs, etc. that this user has access to. If this user doesn't have access to specific datasets or records, Stitch will be unable to replicate them from JIRA.
      6. In the **Password** field, enter the user's password.
  - title: "historical sync"
  - title: "replication frequency"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

---
{% assign integration = page %}
{% include misc/data-files.html %}