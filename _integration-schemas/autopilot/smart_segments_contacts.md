---
tap: "autopilot"
version: 

name: "smart_segments_contacts"
doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-contacts-on-smart-segment/get-contacts-on-smart-segment
singer-schema: https://github.com/singer-io/tap-autopilot/blob/master/tap_autopilot/schemas/smart_segments_contacts.json
description: |
  The `smart_segments_contacts` table contains segment and contact pairs, or the segments your contacts are associated with.

replication-method: "Full Table"
api-method:
  name: "getContactsOnSmartSegment"
  doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-contacts-on-smart-segment/get-contacts-on-smart-segment

attributes:
  - name: segment_id
    type: "string"
    primary-key: true
    description: "The ID of the segment."
    foreign-key-id: "segment-id"

  - name: contact_id
    type: "string"
    primary-key: true
    description: "The ID of the contact that belongs to the segment."
    foreign-key-id: "contact-id"
---