---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_calendar_event"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/calendareventsearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId"
replication-key: "lastModifiedDate"

abstract: false

permissions:
  - name: "Calendar"
    level: "Lists"
    location: "Setup"
  - name: "Events"
    level: "Lists"
    location: "Setup"
---