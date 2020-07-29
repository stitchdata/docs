---
tap: "codat"
version: "1"
key: "event"

name: "events"
doc-link: "https://docs.codat.io/reference/reports#reports_companyevents"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/events.json"
description: |
  The {{ table.name }} table contains information about a given company's events in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get events"
  doc-link: "https://docs.codat.io/reference/reports#reports_companyevents"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "eventTimeUtc"
    type: "string"
    primary-key: true
    description: "The time of the event."
    foreign-key-id: "event-time" 

  - name: "description"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---