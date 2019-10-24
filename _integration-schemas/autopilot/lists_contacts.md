---
tap: "autopilot"
version: 

name: "lists_contacts"
doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-contacts-on-list/get-contacts-on-list
singer-schema: https://github.com/singer-io/tap-autopilot/blob/master/tap_autopilot/schemas/lists_contacts.json
description: |
  The `lists_contacts` table contains list and contact ID pairs, allowing you to create a list of all the contacts that belong to a given {{ integration.display_name }} list.

replication-method: "Full Table"
api-method:
  name: getContactsOnList
  doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-contacts-on-list/get-contacts-on-list

attributes:
  - name: "list_id"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "contact_id"
    type: "string"
    primary-key: true
    description: "The ID of the contact that belongs to the list."
    foreign-key-id: "contact-id"
---