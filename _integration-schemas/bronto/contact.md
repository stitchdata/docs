---
tap: "bronto"
# version: ""

name: "contact"
doc-link: http://dev.bronto.com/api/soap/objects/general/contactobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/schemas.py#L291
description: |
  A contact describes an individual email address and/or SMS number in Bronto, along with associated statistics and field data that you have provided.

replication-method: "Incremental"

api-method:
  name: "readContacts"
# How do we handle SOAP API endpoints?
#  doc-link: https://developer.github.com/v3/issues/assignees/#list-assignees

attributes:
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
---
