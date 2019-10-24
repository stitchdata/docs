---
tap: "autopilot"
version: 

name: "smart_segments"
doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/smart-segments/get-list-of-smart-segments
singer-schema: https://github.com/singer-io/tap-autopilot/blob/master/tap_autopilot/schemas/smart_segments.json 
description: |
  The `smart_segments` table contains info about the smart segments in your Autopilot account.

replication-method: "Full Table"
api-method:
  name: getListOfSmartSegments
  doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/smart-segments/get-list-of-smart-segments

attributes:
  - name: "segment_id"
    type: "string"
    primary-key: true
    description: "The ID of the segment."
    foreign-key-id: "segment-id"

  - name: title
    type: "string"
    description: "The title of the segment."
---