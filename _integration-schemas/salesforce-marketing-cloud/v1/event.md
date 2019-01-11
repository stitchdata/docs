---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
# version: 

name: "event"
doc-link: 
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/events.py
description: |
  The `{{ table.name }}` table contains info about the following event types:

  - [`BounceEvent`](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/bounceevent.htm){:target="new"}
  - [`ClickEvent`](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/clickevent.htm){:target="new"}
  - [`OpenEvent`](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/openevent.htm){:target="new"}
  - [`SentEvent`](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/sentevent.htm){:target="new"}
  - [`UnsubEvent`](https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/unsubevent.htm){:target="new"}

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve events"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/retrieving_bounce_event_details.htm"

attributes:
  - name: "SendID"
    type: "integer"
    primary-key: true
    description: "The ID of the send associated with the tracking event."
    foreign-key-id: "send-id"

  - name: "EventType"
    type: "string"
    primary-key: true
    description: |
      The type of tracking event. Possible values are:

      - `BounceEvent`
      - `ClickEvent`
      - `OpenEvent`
      - `SentEvent`
      - `UnsubEvent`

  - name: "SubscriberKey"
    type: "string"
    primary-key: true
    description: "The ID of the subscriber associated with the event."
    foreign-key-id: "subscriber-key"

  - name: "EventDate"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The date and time when a tracking event occurred."

  - name: "URL"
    type: "string"
    description: "The URL that was clicked."
---