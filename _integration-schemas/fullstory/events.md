---
tap: "fullstory"

name: "events"
doc-link: https://help.fullstory.com/technical-questions/data-export#data-export-contents
singer-schema: https://github.com/singer-io/tap-fullstory/blob/master/tap_fullstory/schemas/events.json
description: |
  The `events` table contains raw data about the events that occurred on your site, which are recorded using the FullStory JavaScript library.

replication-method: "Key-based Incremental"

attributes:
  - name: "PageId"
    type: "integer"
    primary-key: true
    description: "The ID for a particular page within the context of a single session."

  - name: "SessionId"
    type: "integer"
    primary-key: true
    description: "A unique ID for a specific user session."

  - name: "UserId"
    type: "integer"
    primary-key: true
    description: "A unique ID for a user cookie given on a device/browser. This ID may be reset if the user clears their cookies, switches devices, changes browsers, etc."

  - name: "EventStart"
    type: "string"
    replication-key: true
    description: "The time when the event first occurred, in UTC."

  - name: "IndvId"
    type: "integer"
    description: |
      A unique ID for the an individual user that combines all users (`UserId`) with the same user app key (`UserAppKey`).

      For example: If you've identified user `327` whenever they visit your site, event records for the user across devices, browsers, etc. will include this ID.

  - name: "EventTargetSelectorTok"
    type: "string"
    description: |
      The CSS selector for the target event, if applicable. This will be a fully-qualified descendant selector, starting from the HTML element and including all CSS selectors of elements that appear in the DOM when walking from the HTML element, through its children, to the event target.

      **Note**: FullStory will encode most non-alphanumeric characters within a selector. For example: `.my%2Dclass` rather than `.my-class`

  - name: "EventTargetText"
    type: "string"
    description: |
      The text of the event target and its child elements, if applicable.

      For example: If the user clicked a button that said `Pay now`, the value of this field would be `Pay now`.

      FullStory may truncate long text.

  - name: "EventType"
    type: "string"
    description: |
      The type of event that was recorded. Possible values are:

      - `abandon` - A form was abandoned.  Learn more about form abandonment.
      - `change` - The text in a text entry field was changed.  The Event Target Text field will contain the new text value.
      - `click` - An element on the page has been clicked.  The Event Target Text field will contain text of the clicked element, if applicable.
      - `navigate` - A URL change, either to a completely new page or a new hash fragment.
      - `thrash` - The user moved the mouse cursor erratically or in circles.  Learn more about thrashed cursors.

  - name: "PageActiveDuration"
    type: "integer"
    description: "The active time (mouse movement, text entry, clicks, etc.) a user spent on the page (`pageId`) during the session, in milliseconds. This is not a running total; even event for a given page will show the same duration."

  - name: "PageAgent"
    type: "string"
    description: "The full user agent string for the system on which the session was recorded."

  - name: "PageBrowser"
    type: "string"
    description: |
      The browser used for the session. Current possible values are:

      - `Chrome`
      - `Firefox`
      - `Internet Explorer`
      - `Microsoft Edge`
      - `Safari`
      - `Opera`
      - `Mobile App`
      - `Yandex`
      - `Robot`
      - `Unknown`

  - name: "PageDevice"
    type: "string"
    description: |
      The device type used for the session, as derived from the user agent (`PageAgent`). Current possible values:

      - `Desktop`
      - `Mobile`
      - `Tablet`
      - `Robot`
      - `Unknown`

  - name: "PageDuration"
    type: "integer"
    description: "The total time the user spent on the page (`pageId`) during the session, in milliseconds. This is not a running total; even event for a given page will show the same duration."

  - name: "PageIp"
    type: "string"
    description: "The IP address captured at the start of the session."

  - name: "PageLatLong"
    type: "string"
    description: "The latitutde/longitude corresponding to the session."

  - name: "PageNumInfos"
    type: "integer"
    description: |
      The number of times the JavaScript function `console.log()` was called, plus the number of times `console.info()` was called on the page during the session.

      This is a running total for the page, and will steadily increase until the user navigates to a new page.

  - name: "PageNumWarnings"
    type: "integer"
    description: |
      The number of times the JavaScript function `console.warn()` was called on the page during the session.

      This is a running total for the page.

  - name: "PageNumErrors"
    type: "integer"
    description: |
      The number of times the JavaScript function `console.error()` was called on the page, plus the number of JavaScript errors that occurred on the page during the session.

      This is a running total for the page.

  - name: "PageOperatingSystem"
    type: "string"
    description: |
      The operating system used for the session, as derived from the user agent (`PageAgent`). Current possible values:

      - `Chrome OS`
      - `OS X`
      - `iOS`
      - `Windows`
      - `Windows Phone`
      - `Linux`
      - `Robot`
      - `Unknown`

  - name: "PageUrl"
    type: "string"
    description: "The full URL of the page on which the given event occurred."

  - name: "PageRefererUrl"
    type: "string"
    description: "The URL of the page from which the user reached this page. This field may be empty if the user manually entered the page URL, the referrer has been scrubbed, etc."

  - name: "UserAppKey"
    type: "string"
    description: "The user ID passed to FullStory from your system using [FS.identify](https://help.fullstory.com/develop-js/identify)."

  - name: "UserDisplayName"
    type: "string"
    description: "The display name for the user, set via [FS.identify](https://help.fullstory.com/develop-js/identify) or [FS.setUserVars](https://help.fullstory.com/develop-js/setuservars)."

  - name: "UserEmail"
    type: "string"
    description: "The email address for the user, set via [FS.identify](https://help.fullstory.com/develop-js/identify) or [FS.setUserVars](https://help.fullstory.com/develop-js/setuservars)."
---