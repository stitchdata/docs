---
tap: "netsuite-suite-analytics"
version: "1"
key: "message-recipient"

name: "messagerecipient"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/messagerecipient.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "message_id"
    type: "integer"
    description: ""
    foreign-key-id: "message-id"
---