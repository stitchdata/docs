---
tap-reference: "listrak"

# version: "1.0"

foreign-keys:
  - attribute: "ContactID"
    table: "subscribed_contacts"
    join-on: "id"

  - attribute: "MsgID"
    table: "messages"
    join-on: "MsgID"

  - attribute: "ListID"
    table: "lists"
    join-on: "ListsID"
---