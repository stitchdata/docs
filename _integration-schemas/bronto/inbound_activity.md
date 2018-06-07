---
tap: "bronto"
# version: ""

name: "inbound_activity"
doc-link: http://dev.bronto.com/api/soap/objects/general/activityobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/schemas.py#L60
description: |
  The `inbound_activity` object contains activity info regarding contacts, messages, and deliveries.

replication-method: "Key-based Incremental"

api-method:
  name: "readRecentInboundActivities"
  doc-link: http://dev.bronto.com/api/soap/objects/general/activityobject/

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The activity ID."

  - name: "createdDate"
    type: "date-time"
    replication-key: true
    description: "The date the activity was recorded."

  - name: "skipReason"
    type: "string"
    description: "The detailed reason why the contact was skipped when attempting to send to them. The `skipReason` property is returned if the `activityType` is `contactskip`."

  - name: "deliveryId"
    type: "string"
    description: "The ID assigned to the delivery associated with the activity."

  - name: "deliveryType"
    type: "string"
    description: |
      The type of delivery associated with the activity. Possible values are:

      - `bulk`
      - `test`
      - `split`
      - `trigger`
      - `ftaf` (forward to a friend)

  - name: "workflowName"
    type: "string"
    description: "The name of the workflow associated with the activity. The `workflowName` property is returned if a `workflowId` is returned."

  - name: "listName"
    type: "string"
    description: "The name of the list associated with the activity. The `listName` property is returned if a `istId` is returned."

  - name: "messageName"
    type: "string"
    description: "The name of the message associated with the activity. The `messageName` property is returned if a `messageId` is returned."

  - name: "emailAddress"
    type: "string"
    description: "The email address of the contact associated with the activity. The `emailAddress` property is returned if a `contactId` is returned, and an email address is stored for the associated contact."

  - name: "orderId"
    type: "string"
    description: "The ID assigned to the order. The `orderId` property is returned if the `activityType` is `conversion`."

  - name: "webformAction"
    type: "string"
    description: "The activity performed on the webform. Valid values are: `submitted`, `view`. The webformAction property is returned if the activityType is webform."

  - name: "webformName"
    type: "string"
    description: "The name of the webform used. The `webformName` property is returned if the `activityType` is `webform`."

  - name: "listId"
    type: "string"
    description: "The ID assigned to the list that the delivery associated with the activity was sent to."
    foreign-key: true

  - name: "socialNetwork"
    type: "string"
    description: |
      The social network the activity was performed on. The `bounceType` property is returned if the `activityType` is `social`.

      The valid networks are: `facebook`, `twitter`, `linkedin`, `digg`, `myspace`.

  - name: "unsubscribeMethod"
    type: "string"
    description: |
      The method used by the contact to unsubscribe. The `unsubscribeMethod` property is returned if the `activityType` is `unsubscribe`.

      Possible values are: 

      - `subscriberadmin` 
      - `bulk`
      - `listcleaning`
      - `fbl` (Feedback Loop)
      - `complaint`
      - `account`
      - `api`
      - `unclassified`

  - name: "linkName"
    type: "string"
    description: "The name of the link that was clicked. The `linkName` property is returned if the `activityType` is `click`."

  - name: "segmentId"
    type: "string"
    description: "The ID assigned to the segment that the delivery associated with the activity was sent to."

  - name: "deliveryStart"
    type: "string"
    description: "The date/time the delivery associated with the activity was scheduled. The `deliveryStart` property is returned if a `deliveryId` is returned."

  - name: "contactId"
    type: "string"
    description: "The ID assigned to the contact associated with the activity."

  - name: "listLabel"
    type: "string"
    description: "The label assigned to the list associated with the activity. The label is the external (customer facing) name given to a list. The `listLabel` property is returned if a `listId` is returned."

  - name: "socialActivity"
    type: "string"
    description: "The activity performed. The valid activities are: `view`, `share`. The `socialActivity` property is returned if the `activityType` is `social`."

  - name: "automatorName"
    type: "string"
    description: "The name of the automator associated with the activity."

  - name: "webformId"
    type: "string"
    description: "The unique ID for a webform."

  - name: "bounceReason"
    type: "string"
    description: "The detailed reason why the bounce occurred. The `bounceReason` property is returned if the `activityType` is `bounce`."

  - name: "messageId"
    type: "string"
    description: "The ID assigned to the message associated with the activity."

  - name: "workflowId"
    type: "string"
    description: "The ID assigned to the workflow that sent the delivery associated with the activity."

  - name: "smsKeywordName"
    type: "string"
    description: "The name of the SMS keyword associated with the activity. The `smsKeywordName` property is returned if a `keywordId` is returned."

  - name: "keywordId"
    type: "string"
    description: "The ID assigned to the SMS keyword that the SMS delivery associated with the activity was sent to."

  - name: "activityType"
    type: "string"
    description: "The type of activity the object represents. For outbound activities, this can be `send` or `sms_send`."

  - name: "contactStatus"
    type: "string"
    description: |
      The status of the contact associated with the activity. Possible values are:

      - `active`
      - `onboarding`
      - `transactional`
      - `bounce`
      - `unconfirmed`
      - `unsub`

  - name: "bounceType"
    type: "string"
    description: |
      The type of bounce recorded. The `bounceType` property is returned if the `activityType` is `bounce`.

      The following types can be returned: 

      **Hard bounces**:
      - `bad_email`
      - `destination_unreachable`
      - `rejected_message_content`

      **Soft bounces:**
      - `temporary_contact_issue`
      - `destination_temporarily_unavailable`
      - `deferred_message_content`
      - `unclassified`

  - name: "ftafEmails"
    type: "string"
    description: "The emails that were used in the Forward To A Friend Delivery. The `ftafEmails` property is returned if the `activityType` is `friendforward`."

  - name: "mobileNumber"
    type: "string"
    description: "The mobile number of the contact associated with the activity. The `mobileNumber` property is returned if a `contactId` is returned, and a mobile number is stored for the associated contact."

  - name: "linkUrl"
    type: "string"
    description: "The URL of the link that was clicked. The `linkUrl` property is returned if the `activityType` is `click`."

  - name: "segmentName"
    type: "string"
    description: "The name of the segment associated with the activity. The `segmentName` property is returned if a `segmentId` is returned."
---
