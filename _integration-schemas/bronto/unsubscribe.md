---
tap: "bronto"
# version: ""

name: "unsubscribe"
doc-link: http://dev.bronto.com/api/soap/objects/general/unsubscribeobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/endpoints/unsubscribe.py#L20
description: |
  The `unsubscribe` table contains info about unsubscribe events. Contacts may be unsubscribed by you, or they can unsubscribe themselves via an Unsubscribe or Manage Preferences Webform.

replication-method: "Key-based Incremental"

api-method:
  name: "readUnsubscribes"
  doc-link: http://dev.bronto.com/api/soap/objects/general/unsubscribeobject/

attributes:
  - name: "contactId"
    type: "string"
    primary-key: true
    description: "The unique ID of the contact associated with the unsubscribe."

  - name: "deliveryId"
    type: "string"
    primary-key: true
    description: "The unique ID of the delivery that resulted in the contact unsubscribing."

  - name: "created"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The time the unsubscribe event was created."

  - name: "method"
    type: "string"
    description: |
      The method used by the contact to unsubscribe. Possible values are:

      - `subscriber`
      - `admin`
      - `bulk`
      - `listcleaning`
      - `fbl` (feedback loop)
      - `complaint`
      - `account`
      - `api`

  - name: "complaint"
    type: "string"
    description: "Optional additional information about the unsubscribe."
---
