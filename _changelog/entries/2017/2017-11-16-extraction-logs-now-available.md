---
title: Extraction logs now available!
content-type: "changelog-entry"
date: 2017-11-16
entry-type: new-feature
entry-category: replication
connections:
  - id: "aurora-rds"
    version: 1
  - id: "autopilot"
    version: 1
  - id: "braintree"
    version: 1
  - id: "facebook-ads"
    version: 1
  - id: "freshdesk"
    version: 1
  - id: "gitlab"
    version: 1
  - id: "cloudsql-mysql"
    version: 1
  - id: "harvest"
    version: 1
  - id: "hubspot"
    version: 1
  - id: "mariadb"
    version: 1
  - id: "mysql"
    version: 1
  - id: "outbrain"
    version: 1
  - id: "referral-saasquatch"
    version: 1
  - id: "salesforce"
    version: 1
  - id: "shippo"
    version: 1
  - id: "taboola"
    version: 1
  - id: "urban-airship"
    version: 1
---

Detailed [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) are now available for select integrations in Stitch. This new feature presents detailed information about the extraction process in these integrations, and lets you:

- Inspect, copy, and download extraction log files up to 50MB in size
- View historical logs over the past seven days
- Visualize how often extraction runs, how long it takes, and when it errors
- View logs for extraction jobs currently in progress

We'll be working over the coming weeks to bring these logs to the rest of our integrations. 
In the meantime here are the currently supported integrations:

{% for connection in page.connections %}
{% assign integrations = site.saas-integrations | concat: site.database-integrations | where:"name",connection.id %}
{% assign integration = integrations | where:"this-version",connection.version | first %}

- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl }})
{% endfor %}