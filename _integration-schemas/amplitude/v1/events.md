---
tap: "amplitude"
version: "1.0"

name: "events_[project_id]"
doc-link: https://amplitude.zendesk.com/hc/en-us/articles/115001902492-Query-Snowflake#column-schema
description: |
  `{{ table.name }}` tables contain info about the events logged in your {{ integration.display_name }} projects.

  **Note**: Each event table will have the project ID appended. For example: If a project has an ID of `168342`, the events table for the project will be named `events_168432`.

replication-method: "Key-based Incremental"

json-functions: |
  Depending on the destination you're using, you can use that destination's available JSON functions to parse the data in this column. Click the links below to view that destination's JSON function documentation:

  - [BigQuery](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions){:target="new"}
  - [PostgreSQL](https://www.postgresql.org/docs/9.4/static/functions-json.html){:target="new"}
  - [Redshift](https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html){:target="new"}
  - [Snowflake](https://docs.snowflake.net/manuals/sql-reference/functions/parse_json.html){:target}

attributes:
  - name: "uuid"
    type: "string"
    primary-key: true
    description: "The unique event ID."

  - name: "event_time"
    type: "date-time"
    replication-key: true
    description: |
      The {{ integation.display_name }} timestamp, which is the `client_event_time` adjusted by the difference between `server_received_time` and `client_upload_time`.

      {{ integration.display_name }} calculates this as:

      `event_time = client_event_time + (server_received_time - client_upload_time)`

      This is used in {{ integration.display_name }} to organize events in charts.

  - name: "adid"
    type: "string"
    description: "The Android/Google Play Services advertising ID."

  - name: "amplitude_event_type"
    type: "string"
    description: "**This is a legacy field**. Use `event_type` instead."

  - name: "amplitude_id"
    type: "number"
    description: "An internal {{ integration.display_name }} ID used to count unique users. For example: `1234567890`"

  - name: "app"
    type: "number"
    description: |
      The project ID found in your project's [{{ integration.display_name }} Settings page](https://amplitude.zendesk.com/hc/en-us/articles/235649848#projects){:target="new"}.

  - name: "city"
    type: "string"
    description: "The city where the event took place."

  - name: "client_event_time"
    type: "date-time"
    description: "The timestamp of when the device logged the event."

  - name: "client_upload_time"
    type: "date-time"
    description: "The timestamp of when the device uploaded the event."

  - name: "country"
    type: "string"
    description: "The country where the event took place."

  - name: "data"
    type: "string"
    description: |
      Dictionary where certain fields such as `first_event` and `merged_amplitude_id` are stored.

      {{ table.json-functions }}

  - name: "device_brand"
    type: "string"
    description: "The brand of device used in the event. For example: `Apple`"

  - name: "device_carrier"
    type: "string"
    description: "The mobile carrier of the device used in the event. For example: `Verizon`"

  - name: "device_family"
    type: "string"
    description: "The family of the device used in the event. For example: `Apple iPhone`"

  - name: "device_id"
    type: "string"
    description: "The specific device identifier."

  - name: "device_manufacturer"
    type: "string"
    description: "The manufacturer of the device used in the event. For example: `Apple`"

  - name: "device_model"
    type: "string"
    description: "The model of the device used in the event. For example: `iPad mini`"

  - name: "device_type"
    type: "string"
    description: "The type of the device used in the event. For example: `Apple iPhone 5s`"

  - name: "dma"
    type: "string"
    description: "The designated marketing area (DMA). For example: `San Francisco-Oakland-San Jose, CA"

  - name: "event_id"
    type: "number"
    description: "A counter that distinguishes events."

  - name: "event_properties"
    type: "string"
    description: |
      Details about the event.

      {{ table.json-functions }}

  - name: "event_type"
    type: "string"
    description: "The assigned type of the event. For example: `Add Friend`"

  - name: "followed_an_identity"
    type: "boolean"
    description: "If `true`, there was an `identify` event between this SDK event and the last SDK event seen."

  - name: "groups"
    type: "string"
    description: |
      Details about the groups associated with the event. [Refer to {{ integration.display_name }}'s documentation for more info](https://amplitude.zendesk.com/hc/en-us/articles/115001765532#account-level-reporting){:target="new"}.

      {{ table.json-functions }}

  - name: "idfa"
    type: "string"
    description: "The iOS ID for Advertiser."

  - name: "ip_address"
    type: "string"
    description: "The IP address."

  - name: "location_lat"
    type: "number"
    description: "The latitude."

  - name: "location_lng"
    type: "number"
    description: "The longitude."

  - name: "os_name"
    type: "string"
    description: "The name of the OS used in the event. For example: `ios`"

  - name: "os_version"
    type: "string"
    description: "The version of the OS used in the event. For example: `1.0`"

  - name: "paying"
    type: "string"
    description: "If `true`, the user has logged revenue at some point. The value will be `(none)` otherwise."

  - name: "region"
    type: "string"
    description: "The region where the event took place."

  - name: "server_upload_time"
    type: "date-time"
    description: "The timestamp of when the {{ integration.display_name }} servers received the event."

  - name: "session_id"
    type: "number"
    description: "The session start time, in milliseconds since epoch."

  - name: "start_version"
    type: "string"
    description: "The app version the user was first tracked on."

  - name: "user_creation_time"
    type: "date-time"
    description: "The timestamp of the user's first event."

  - name: "user_id"
    type: "string"
    description: "An ID for the user, specified by you."

  - name: "user_properties"
    type: "string"
    description: |
      Details about the user associated with the event.

      {{ table.json-functions }}

  - name: "version_name"
    type: "string"
    description: "The app version."
---