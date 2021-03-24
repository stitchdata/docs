---
title: Extraction logs now available!
content-type: "changelog-entry"
date: 2017-11-16
entry-type: new-feature
entry-category: "replication, integration"
connections:
  - id: "aurora-rds"
    type: "integration"
    version: "1"

  - id: "autopilot"
    type: "integration"
    version: "1"

  - id: "braintree"
    type: "integration"
    version: "1"

  - id: "facebook-ads"
    type: "integration"
    version: "1"

  - id: "freshdesk"
    type: "integration"
    version: "1"

  - id: "gitlab"
    type: "integration"
    version: "1"

  - id: "cloudsql-mysql"
    type: "integration"
    version: "1"

  - id: "harvest"
    type: "integration"
    version: "1"

  - id: "hubspot"
    type: "integration"
    version: "1"

  - id: "mariadb"
    type: "integration"
    version: "1"

  - id: "mysql"
    type: "integration"
    version: "1"

  - id: "outbrain"
    type: "integration"
    version: "1"

  - id: "referral-saasquatch"
    type: "integration"
    version: "1"

  - id: "salesforce"
    type: "integration"
    version: "1"
    copy: "(v1 only)"

  - id: "shippo"
    type: "integration"
    version: "1"

  - id: "taboola"
    type: "integration"
    version: "1"

  - id: "urban-airship"
    type: "integration"
    version: "1"
---

Detailed [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }}) are now available for select integrations in Stitch. This new feature presents detailed information about the extraction process in these integrations, and lets you:

- Inspect, copy, and download extraction log files up to 50MB in size
- View historical logs over the past seven days
- Visualize how often extraction runs, how long it takes, and when it errors
- View logs for extraction jobs currently in progress

This feature is available for the following integrations:
  
{{ site.data.changelog.metadata.integration-list | flatify }}

We'll be working over the coming weeks to bring these logs to the rest of our integrations. Check out the [docs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }}) for more info on this new feature.