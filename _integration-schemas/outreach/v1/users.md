---
tap: "outreach"
version: "1"
key: "user"

name: "users"
doc-link: "https://api.outreach.io/api/v2/docs#user"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/users.json"
description: |
  The `{{ table.name}}` table contains information about individual users that use the {{ integration.display_name }} app.

replication-method: "Key-based Incremental"

api-method:
  name: "Get users"
  doc-link: "https://api.outreach.io/api/v2/docs#user"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"
  
  - name: "updatedAt"
    type: "date-time"
    description: "The time the user was last updated."
    replication-key: true

  - name: "accountsViewId"
    type: "integer"
    description: ""

  - name: "activityNotificationsDisabled"
    type: "boolean"
    description: ""

  - name: "bounceWarningEmailEnabled"
    type: "boolean"
    description: ""

  - name: "bridgePhone"
    type: "string"
    description: ""

  - name: "bridgePhoneExtension"
    type: "string"
    description: ""

  - name: "callsViewId"
    type: "integer"
    description: ""

  - name: "controlledTabDefault"
    type: "string"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""

  - name: "currentSignInAt"
    type: "date-time"
    description: ""

  - name: "custom1"
    type: "string"
    description: ""

  - name: "custom2"
    type: "string"
    description: ""

  - name: "custom3"
    type: "string"
    description: ""

  - name: "custom4"
    type: "string"
    description: ""

  - name: "custom5"
    type: "string"
    description: ""

  - name: "dailyDigestEmailEnabled"
    type: "boolean"
    description: ""

  - name: "duties"
    type: "array"
    description: ""
    subattributes:
    - name: "name"
      type: "string"
      description: ""

    - name: "duty_type"
      type: "string"
      description: ""

    - name: "id"
      type: "integer"
      description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "enableVoiceRecordings"
    type: "boolean"
    description: ""

  - name: "engagementEmailsEnabled"
    type: "boolean"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "inboundBridgePhone"
    type: "string"
    description: ""

  - name: "inboundBridgePhoneExtension"
    type: "string"
    description: ""

  - name: "inboundCallBehavior"
    type: "string"
    description: ""

  - name: "inboundPhoneType"
    type: "string"
    description: ""

  - name: "inboundVoicemailCustomMessageText"
    type: "string"
    description: ""

  - name: "inboundVoicemailMessageTextVoice"
    type: "string"
    description: ""

  - name: "inboundVoicemailPromptType"
    type: "string"
    description: ""

  - name: "kaiaRecordingsViewId"
    type: "integer"
    description: ""

  - name: "keepBridgePhoneConnected"
    type: "boolean"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "lastSignInAt"
    type: "date-time"
    description: ""

  - name: "locked"
    type: "boolean"
    description: ""

  - name: "mailboxErrorEmailEnabled"
    type: "boolean"
    description: ""

  - name: "mailboxId"
    type: "integer"
    description: ""

  - name: "meetingEngagementNotificationEnabled"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notificationsEnabled"
    type: "boolean"
    description: ""

  - name: "oceClickToDialEverywhere"
    type: "boolean"
    description: ""

  - name: "oceGmailToolbar"
    type: "boolean"
    description: ""

  - name: "oceGmailTrackingState"
    type: "string"
    description: ""

  - name: "oceSalesforceEmailDecorating"
    type: "boolean"
    description: ""

  - name: "oceSalesforcePhoneDecorating"
    type: "boolean"
    description: ""

  - name: "oceUniversalTaskFlow"
    type: "boolean"
    description: ""

  - name: "oceWindowMode"
    type: "boolean"
    description: ""

  - name: "opportunitiesViewId"
    type: "integer"
    description: ""

  - name: "passwordExpiresAt"
    type: "date-time"
    description: ""

  - name: "phoneCountryCode"
    type: "string"
    description: ""

  - name: "phoneNumber"
    type: "string"
    description: ""

  - name: "phoneType"
    type: "string"
    description: ""

  - name: "pluginAlertNotificationEnabled"
    type: "boolean"
    description: ""

  - name: "preferredVoiceRegion"
    type: "string"
    description: ""

  - name: "prefersLocalPresence"
    type: "boolean"
    description: ""

  - name: "primaryTimezone"
    type: "string"
    description: ""

  - name: "profileId"
    type: "integer"
    description: ""

  - name: "prospectsViewId"
    type: "integer"
    description: ""

  - name: "reportsTeamPerfViewId"
    type: "integer"
    description: ""

  - name: "reportsViewId"
    type: "integer"
    description: ""

  - name: "roleId"
    type: "integer"
    description: ""

  - name: "scimExternalId"
    type: "string"
    description: ""

  - name: "scimSource"
    type: "string"
    description: ""

  - name: "secondaryTimezone"
    type: "string"
    description: ""

  - name: "senderNotificationsExcluded"
    type: "string"
    description: ""

  - name: "tasksViewId"
    type: "integer"
    description: ""

  - name: "teamsViewId"
    type: "integer"
    description: ""

  - name: "tertiaryTimezone"
    type: "string"
    description: ""

  - name: "textingEmailNotifications"
    type: "boolean"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "unknownReplyEmailEnabled"
    type: "boolean"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""

  - name: "userGuid"
    type: "string"
    description: ""

  - name: "username"
    type: "string"
    description: ""

  - name: "usersViewId"
    type: "integer"
    description: ""

  - name: "voicemailNotificationEnabled"
    type: "boolean"
    description: ""

  - name: "weeklyDigestEmailEnabled"
    type: "boolean"
    description: ""
---