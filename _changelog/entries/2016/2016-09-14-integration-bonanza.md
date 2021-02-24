---
title: "New integration bonanza!"
content-type: "changelog-entry"
date: 2016-09-14
entry-type: new-feature
entry-category: integration
connections:
  - id: "google-analytics"
    version: "14-09-2016"
    copy: |
      We've opened up the beta for our new {{ this-connection.display_name }} integration. This new integration allows you to create custom datasets using {{ this-connection.display_name }}'s metrics and dimensions.

  - id: "intercom"
    version: "02-02-2016"
    copy: &leaving-beta |
      {{ this-connection.display_name }} is leaving beta

  - id: "pardot"
    version: "15-10-2015"
    copy: *leaving-beta

  - id: "recurly"
    version: "14-09-2016"
    copy: *leaving-beta

  - id: "segment"
    version: "1"
    copy: *leaving-beta

  - id: "trello"
    version: "15-12-2015"
    copy: *leaving-beta
---

Lots of integration related news today. Ready? Here we go:

{{ site.data.changelog.metadata.integration-list | flatify }}

Get out there and start moving some data.