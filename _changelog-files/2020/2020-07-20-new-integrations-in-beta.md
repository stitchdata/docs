---
title: New integrations in open beta
content-type: "changelog-entry"
date: 2020-07-20
entry-type: "beta"
entry-category: integration
connections:
  - id: "impact"
    type: "integration"
    version: "1"
    
  - id: "lever"
    type: "integration"
    version: "1"

  - id: "mailshake"
    type: "integration"
    version: "1"

  - id: "netsuite-suite-analytics"
    type: "integration"
    version: "1"

  - id: "outreach"
    type: "integration"
    version: "1"

  - id: "trello"
    type: "integration"
    version: "1"
---

Stitch is pleased to announce the release of several new integrations into open beta:

{{ site.data.changelog.metadata.integration-list | flatify }}

In addition to providing more tables, these integrations now include [table and column selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }}), [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }}), [Loading Reports]({{ site.data.urls.replication.loading-reports | prepend: site.baseurl | prepend: site.home }}) and full [Connect API compatibility]({{ site.data.urls.connect.overview | prepend: site.baseurl | prepend: site.home }})!