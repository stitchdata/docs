---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "heap"
version: "1" 

name: "sessions"
doc-link: https://docs.heapanalytics.com/docs/heap-sql-retroactive-s3-specification
description: |
  The `{{ table.name }}` table contains info about sessions. In {{ integration.display_name }}, a web session ends after 30 minutes of user inactivity, while in iOS, a session ends after the app has entered the background.

  **Note**: Custom attributes are supported for this table. As {{ integration.display_name }} schemas are dynamic, Stitch's `{{ table.name }}` documentation will only list the non-custom attributes outlined in {{ integration.display_name }}'s documentation.

replication-method: "Key-based Incremental"

replication-key:
  name: "[See Replication](#incremental-replication-for-heap)"

attributes:
  - name: "event_id"
    type: "string"
    primary-key: true
    description: "The event ID." 

  - name: "user_id"
    type: "integer"
    description: "The ID of the associated user."
    foreign-key-id: "user-id"

  - name: "session_id"
    type: "integer"
    description: "The ID of the associated session."
    foreign-key-id: "session-id"

  - name: "Custom Attributes"
    type: 
    description: "Any custom attributes applied to the session model in {{ integration.display_name }}."

  - name: "time"
    type: "string"
    description: "The UTC timestamp when the session started."

  - name: "library"
    type: "string"
    description: |
      The version of the heap library which initiated the session. Possible values are:

      - `web`
      - `iOS`

  - name: "platform"
    type: "string"
    description: "The user's operating system."

  - name: "device_type"
    type: "string"
    description: |
      The user's device type. Possible values are:

      - `Mobile`
      - `Tablet`
      - `Desktop`

  - name: "country"
    type: "string"
    description: "The country in which the user session occurred, based on IP."

  - name: "region"
    type: "string"
    description: "The region in which the user session occurred, based on IP."

  - name: "city"
    type: "string"
    description: "The city in which the user session occurred, based on IP."

  - name: "IP"
    type: "string"
    description: "The IP address for the session."

  - name: "referrer"
    type: "string"
    description: "**Applicable only to `library: Web`.** The URL that linked to the site and initiated the session. If the user navigated directly to the site or referral headers were stripped, this value will be `direct`."

  - name: "landing_page"
    type: "string"
    description: "**Applicable only to `library: Web`.** The URL of the first pageview of the session."

  - name: "browser"
    type: "string"
    description: "**Applicable only to `library: Web`.** The user's browser."

  - name: "search_keyword"
    type: "string"
    description: "**Applicable only to `library: Web`.** The search term that brought the user to the site."

  - name: "utm_source"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_source` tag associated with the session's initial pageview."

  - name: "utm_campaign"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_campaign` tag associated with the session's initial pageview."

  - name: "utm_medium"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_medium` tag associated with the session's initial pageview."

  - name: "utm_term"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_term` tag associated with the session's initial pageview."

  - name: "utm_content"
    type: "string"
    description: "**Applicable only to `library: Web`**.The GA-based `utm_content` tag associated with the session's initial pageview."

  - name: "device"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The user's device model."

  - name: "carrier"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The user's mobile phone carrier."

  - name: "app_name"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The current name of the iOS app."

  - name: "app_version"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The current version of the iOS app."   
---