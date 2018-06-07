  - name: "msgPref"
    type: "string"
    description: "The message preference for the contact. A contact can have a message preference of text or html."

  - name: "primaryEmailClient"
    type: "string"
    description: "The primary email client (Microsoft Outlook, Mozilla Thunderbird, Apple Mail, etc.) used by a contact."

  - name: "source"
    type: "string"
    description: "The source or where the contact came from. The source can manual, import, api, webform, or sforcereport (salesforce report)."

  - name: "numConversions"
    type: "number"
    description: "The total number of conversions made by the contact."

  - name: "numClicks"
    type: "number"
    description: "The total number of times deliveries were clicked by the contact. If a link is clicked multiple times, each click is included in this metric."

  - name: "customSource"
    type: "string"
    description: "A source you define that states where the contact came from."

  - name: "totalOrders"
    type: "number"
    description: "The total number of orders recorded for a contact."

  - name: "geoIPZip"
    type: "string"
    description: "The zip code recorded for the contact based on their last known non-mobile IP addresses."

  - name: "lastClickDate"
    type: "string"
    description: "The last date a click was recorded for the contact."

  - name: "totalRevenue"
    type: "number"
    description: "The total amount of revenue recorded for a contact."

  - name: "SMSKeywordIDs"
    type: "object"
    description: ""

    object-attributes: 
  - name: "SMSKeywordIDs"
    type: "string"
    description: ""

  - name: "lastOpenDate"
    type: "string"
    description: "The last date an open was recorded for the contact."

  - name: "created"
    type: "string"
    description: "The date the contact was created. This timestamp is immutable and cannot be changed"

  - name: "numBounces"
    type: "number"
    description: "The total number of times deliveries sent to the contact resulted in a bounce."

  - name: "lastOrderTotal"
    type: "number"
    description: "The total amount of revenue recorded for the most recent order."

  - name: "modified"
    type: "string"
    description: "The last time information about the contact was modified. This timestamp is immutable and cannot be changed."

  - name: "deleted"
    type: "boolean"
    description: "Set to true if the contact has been deleted."

  - name: "email"
    type: "string"
    description: "The email address assigned to the contact. The email address can be used to reference a specific contact when using the contact functions."

  - name: "operatingSystem"
    type: "string"
    description: "The operating system (MacOSX, WinXP, Win7, Android, iOS etc.) used by a contact."

  - name: "conversionAmount"
    type: "number"
    description: "The sum/total amount of conversions made by the contact."

  - name: "lastDeliveryDate"
    type: "string"
    description: "The last date a delivery was made to the contact."

  - name: "averageOrderValue"
    type: "number"
    description: "The average amount of revenue per order recorded for a contact."

  - name: "mobileBrowser"
    type: "string"
    description: "The mobile browser (Safari mobile, Firefox mobile, Chrome mobile) used by a contact."

  - name: "primaryBrowser"
    type: "string"
    description: "The primary browser (Firefox, Chrome, Safari, etc.) used by a contact."

  - name: "firstOrderDate"
    type: "string"
    description: "The date of the first order recorded for a contact."

  - name: "id"
    type: "string"
    description: "The unique id for the contact. The id can be used to reference a specific contact when using the contact functions."

  - name: "status"
    type: "string"
    description: "The status of the contact. Valid statuses are: active, onboarding, transactional, bounce, unconfirmed, unsub"

  - name: "geoIPCity"
    type: "string"
    description: "The city recorded for the contact based on their last known non-mobile IP addresses."

  - name: "numSends"
    type: "number"
    description: "The total number of deliveries sent to the contact."

  - name: "lastOrderDate"
    type: "string"
    description: "The date of the last order recorded for a contact."

  - name: "numOpens"
    type: "number"
    description: "The total number of times deliveries were opened by the contact. This metric includes multiple opens of the same delivery."

  - name: "geoIPCountryCode"
    type: "string"
    description: "The country code recorded for the contact based on their last known non-mobile IP addresses."

  - name: "mobileEmailClient"
    type: "string"
    description: "The mobile email client (Gmail mobile, Yahoo Mail for mobile, etc.) used by a contact."

  - name: "geoIPStateRegion"
    type: "string"
    description: "The state/region recorded for the contact based on their last known non-mobile IP addresses."

  - name: "mobileNumber"
    type: "string"
    description: "The mobile number stored for the contact. A valid country code must be included when adding or updating a mobile number for a contact."

  - name: "listIds"
    type: "object"
    description: ""

    object-attributes: 
  - name: "listIds"
    type: "string"
    description: ""

  - name: "geoIPCountry"
    type: "string"
    description: "The country recorded for the contact based on their last known non-mobile IP addresses."

  - name: "skipReason"
    type: "string"
    description: "The detailed reason why the contact was skipped when attempting to send to them. The skipReason property is returned if the activityType is contactskip."

  - name: "deliveryId"
    type: "string"
    description: "The ID assigned to the delivery associated with the activity."

  - name: "deliveryType"
    type: "string"
    description: "The type of delivery associated with the activity: `bulk`, `test`, `split`, `trigger`, or `ftaf` (forward to a  friend)."

  - name: "workflowName"
    type: "string"
    description: "The name of the workflow associated with the activity. The workflowName property is returned if a workflowId is returned."

  - name: "listName"
    type: "string"
    description: "The name of the list associated with the activity. The listName property is returned if a listId is returned."

  - name: "messageName"
    type: "string"
    description: "The name of the message associated with the activity. The messageName property is returned if a messageId is returned."

  - name: "emailAddress"
    type: "string"
    description: "The email address of the contact associated with the activity. The emailAddress property is returned if a contactId is returned, and an email address is stored for the associated contact."

  - name: "orderId"
    type: "string"
    description: "The ID assigned to the order. The orderId property is returned if the activityType is conversion."

  - name: "createdDate"
    type: "string"
    description: "The date the activity was recorded."

  - name: "webformAction"
    type: "string"
    description: "The activity performed on the webform. Valid values are: submitted, view. The webformAction property is returned if the activityType is webform."

  - name: "webformName"
    type: "string"
    description: "The name of the webform used. The webformName property is returned if the activityType is webform."

  - name: "listId"
    type: "string"
    description: "The ID assigned to the list that the delivery associated with the activity was sent to."

  - name: "socialNetwork"
    type: "string"
    description: "The social network the activity was performed on. The valid networks are: facebook, twitter, linkedin, digg, myspace. The bounceType property is returned if the activityType is social."

  - name: "unsubscribeMethod"
    type: "string"
    description: "The method used by the contact to unsubscribe. Valid values are: subscriberadmin, bulk, listcleaning, fbl (Feedback Loop), complaint, account, api, unclassified. The unsubscribeMethod property is returned if the activityType is unsubscribe."

  - name: "linkName"
    type: "string"
    description: "The name of the link that was clicked. The linkName property is returned if the activityType is click."

  - name: "segmentId"
    type: "string"
    description: "The ID assigned to the segment that the delivery associated with the activity was sent to."

  - name: "deliveryStart"
    type: "string"
    description: "The date/time the delivery associated with the activity was scheduled. The deliveryStart property is returned if a deliveryId is returned."

  - name: "contactId"
    type: "string"
    description: "The ID assigned to the contact associated with the activity."

  - name: "listLabel"
    type: "string"
    description: "The label assigned to the list associated with the activity. The label is the external (customer facing) name given to a list. The listLabel property is returned if a listId is returned."

  - name: "socialActivity"
    type: "string"
    description: "The activity performed. The valid activities are: view, share. The socialActivity property is returned if the activityType is social."

  - name: "automatorName"
    type: "string"
    description: "The name of the automator associated with the activity."

  - name: "webformId"
    type: "string"
    description: "The unique ID for a webform."

  - name: "bounceReason"
    type: "string"
    description: "The detailed reason why the bounce occurred. The bounceReason property is returned if the activityType is bounce."

  - name: "id"
    type: "string"
    description: "Manufactured unique ID for the activity."

  - name: "messageId"
    type: "string"
    description: "The ID assigned to the message associated with the activity."

  - name: "workflowId"
    type: "string"
    description: "The ID assigned to the workflow that sent the delivery associated with the activity."

  - name: "smsKeywordName"
    type: "string"
    description: "The name of the SMS keyword associated with the activity. The smsKeywordName property is returned if a keywordId is returned."

  - name: "keywordId"
    type: "string"
    description: "The ID assigned to the SMS keyword that the SMS delivery associated with the activity was sent to."

  - name: "activityType"
    type: "string"
    description: "The type of activity the object represents. For outbound activities, this can be `send` or `sms_send`."

  - name: "contactStatus"
    type: "string"
    description: "The status of the contact associated with the activity. Status can be `active`, `onboarding`, `transactional`, `bounce`, `unconfirmed`, or `unsub`"

  - name: "bounceType"
    type: "string"
    description: "The type of bounce recorded. The following types can be returned: Hard Bounces: bad_email, destination_unreachable, rejected_message_content. Soft Bounces: temporary_contact_issue, destination_temporarily_unavailable, deferred_message_content, unclassified. The bounceType property is returned if the activityType is bounce."

  - name: "ftafEmails"
    type: "string"
    description: "The emails that were used in the Forward To A Friend Delivery. The ftafEmails property is returned if the activityType is friendforward."

  - name: "mobileNumber"
    type: "string"
    description: "The mobile number of the contact associated with the activity. The mobileNumber property is returned if a contactId is returned, and a mobile number is stored for the associated contact."

  - name: "linkUrl"
    type: "string"
    description: "The URL of the link that was clicked. The linkUrl property is returned if the activityType is click."

  - name: "segmentName"
    type: "string"
    description: "The name of the segment associated with the activity. The segmentName property is returned if a segmentId is returned."

