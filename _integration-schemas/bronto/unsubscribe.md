---
tap: "bronto"
# version: ""

name: "unsubscribe"
doc-link: http://dev.bronto.com/api/soap/objects/general/unsubscribeobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/endpoints/unsubscribe.py#L20
description: |
  The unsubscribe object contains data about unsubscribes. A contact can unsubscribed by you, or they can unsubscribe themselves via an Unsubscribe Webform or a Manage Preferences Webform.

replication-method: "Incremental"

api-method:
  name: "readUnsubscribes"
# How do we handle SOAP API endpoints?
#  doc-link: https://developer.github.com/v3/issues/assignees/#list-assignees

attributes:
  - name: "method"
    type: "string"
    description: "The method used by the contact to unsubscribe. The valid methods are: subscriber, admin, bulk, listcleaning, fbl (Feedback loop), complaint, account, api"

  - name: "complaint"
    type: "string"
    description: "Optional additional information about the unsubscribe."

  - name: "created"
    type: "string"
    description: "The date/time the unsubscribe was created."

  - name: "deliveryId"
    type: "string"
    description: "The unique ID of the delivery that resulted in the contact unsubscribing."

  - name: "contactId"
    type: "string"
    description: "The unique ID of the contact associated with the unsubscribe."
---
