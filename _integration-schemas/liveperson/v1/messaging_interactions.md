---
tap: "liveperson"
version: "1.0"
key: "messaging-interaction"

name: "messaging_interactions"
doc-link: "https://developers.liveperson.com/messaging-interactions-api-overview.html#getting-started"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/messaging_interactions.json"
description: |
  The `{{ table.name }}` table contains info about contact center messaging interactions.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"

api-method:
    name: "Retrieve conversations"
    doc-link: "https://developers.liveperson.com/messaging-interactions-api-methods-conversations.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "messaging-interaction-id"

  - name: "agentParticipants"
    type: "array"
    description: ""
    subattributes:
      - name: "agentFullName"
        type: "string"
        description: ""

      - name: "agentGroupId"
        type: "integer"
        description: ""

      - name: "agentGroupName"
        type: "string"
        description: ""

      - name: "agentId"
        type: "string"
        description: ""

      - name: "agentLoginName"
        type: "string"
        description: ""

      - name: "agentNickname"
        type: "string"
        description: ""

      - name: "permission"
        type: "string"
        description: ""

      - name: "role"
        type: "string"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""

      - name: "userType"
        type: "string"
        description: ""

      - name: "userTypeName"
        type: "string"
        description: ""

  - name: "campaign"
    type: "object"
    description: ""
    subattributes:
      - name: "behaviorSystemDefault"
        type: "boolean"
        description: ""

      - name: "campaignEngagementId"
        type: "string"
        description: ""

      - name: "campaignEngagementName"
        type: "string"
        description: ""

      - name: "campaignId"
        type: "string"
        description: ""

      - name: "campaignName"
        type: "string"
        description: ""

      - name: "engagementAgentNote"
        type: "string"
        description: ""

      - name: "engagementApplicationId"
        type: "string"
        description: ""

      - name: "engagementApplicationName"
        type: "string"
        description: ""

      - name: "engagementApplicationTypeId"
        type: "string"
        description: ""

      - name: "engagementApplicationTypeName"
        type: "string"
        description: ""

      - name: "engagementSource"
        type: "string"
        description: ""

      - name: "goalId"
        type: "string"
        description: ""

      - name: "goalName"
        type: "string"
        description: ""

      - name: "lobId"
        type: "integer"
        description: ""

      - name: "lobName"
        type: "string"
        description: ""

      - name: "locationId"
        type: "string"
        description: ""

      - name: "locationName"
        type: "string"
        description: ""

      - name: "profileSystemDefault"
        type: "boolean"
        description: ""

      - name: "visitorBehaviorId"
        type: "string"
        description: ""

      - name: "visitorBehaviorName"
        type: "string"
        description: ""

      - name: "visitorProfileId"
        type: "string"
        description: ""

      - name: "visitorProfileName"
        type: "string"
        description: ""

  - name: "coBrowseSessions"
    type: "object"
    description: ""
    subattributes:
      - name: "coBrowseSessionsList"
        type: "array"
        description: ""

        subattributes:
          - name: "agentId"
            type: "string"
            description: ""

          - name: "duration"
            type: "integer"
            description: ""

          - name: "endReason"
            type: "string"
            description: ""

          - name: "endTime"
            type: "date-time"
            description: ""

          - name: "endTimeL"
            type: "integer"
            description: ""

          - name: "interactive"
            type: "boolean"
            description: ""

          - name: "sessionId"
            type: "string"
            description: ""

          - name: "startTime"
            type: "date-time"
            description: ""

          - name: "startTimeL"
            type: "integer"
            description: ""

          - name: "type"
            type: "string"
            description: ""

  - name: "consumerParticipants"
    type: "array"
    description: ""
    subattributes:
      - name: "avatarURL"
        type: "string"
        description: ""

      - name: "consumerName"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "firstName"
        type: "string"
        description: ""

      - name: "lastName"
        type: "string"
        description: ""

      - name: "participantId"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""

      - name: "token"
        type: "string"
        description: ""

  - name: "conversationSurveys"
    type: "array"
    description: ""
    subattributes:
      - name: "surveyData"
        type: "array"
        description: ""
        subattributes:
          - name: "answer"
            type: "string"
            description: ""

          - name: "question"
            type: "string"
            description: ""

      - name: "surveyStatus"
        type: "string"
        description: ""

      - name: "surveyType"
        type: "string"
        description: ""

  - name: "info"
    type: "object"
    description: ""
    subattributes:
      - name: "agentDeleted"
        type: "boolean"
        description: ""

      - name: "alertedMCS"
        type: "integer"
        description: ""

      - name: "brandId"
        type: "string"
        description: ""

      - name: "browser"
        type: "string"
        description: ""

      - name: "closeReason"
        type: "string"
        description: ""

      - name: "closeReasonDescription"
        type: "string"
        description: ""

      - name: "conversationId"
        type: "string"
        description: ""

      - name: "csatRate"
        type: "number"
        description: ""

      - name: "device"
        type: "string"
        description: ""

      - name: "duration"
        type: "integer"
        description: ""

      - name: "endTime"
        type: "string"
        description: ""

      - name: "endTimeL"
        type: "integer"
        description: ""

      - name: "firstConversation"
        type: "boolean"
        description: ""

      - name: "isPartial"
        type: "boolean"
        description: ""

      - name: "latestAgentFullName"
        type: "string"
        description: ""

      - name: "latestAgentGroupId"
        type: "integer"
        description: ""

      - name: "latestAgentGroupName"
        type: "string"
        description: ""

      - name: "latestAgentId"
        type: "string"
        description: ""

      - name: "latestAgentLoginName"
        type: "string"
        description: ""

      - name: "latestAgentNickname"
        type: "string"
        description: ""

      - name: "latestQueueState"
        type: "string"
        description: ""

      - name: "latestSkillId"
        type: "integer"
        description: ""

      - name: "latestSkillName"
        type: "string"
        description: ""

      - name: "mcs"
        type: "integer"
        description: ""

      - name: "operatingSystem"
        type: "string"
        description: ""

      - name: "source"
        type: "string"
        description: ""

      - name: "startTime"
        type: "date-time"
        description: ""

      - name: "startTimeL"
        type: "integer"
        description: ""

      - name: "status"
        type: "string"
        description: ""

  - name: "interactions"
    type: "array"
    description: ""
    subattributes:
      - name: "assignedAgentFullName"
        type: "string"
        description: ""

      - name: "assignedAgentId"
        type: "string"
        description: ""

      - name: "assignedAgentLoginName"
        type: "string"
        description: ""

      - name: "assignedAgentNickname"
        type: "string"
        description: ""

      - name: "interactionTime"
        type: "date-time"
        description: ""

      - name: "interactionTimeL"
        type: "integer"
        description: ""

      - name: "interactiveSequence"
        type: "integer"
        description: ""

  - name: "messageRecords"
    type: "array"
    description: ""
    subattributes:
      - name: "device"
        type: "string"
        description: ""

      - name: "dialogId"
        type: "string"
        description: ""

      - name: "messageData"
        type: "object"
        description: ""

        subattributes:
          - name: "msg"
            type: "object"
            description: ""

            subattributes:
              - name: "text"
                type: "string"
                description: ""

      - name: "messageId"
        type: "string"
        description: ""

      - name: "participantId"
        type: "string"
        description: ""

      - name: "sentBy"
        type: "string"
        description: ""

      - name: "seq"
        type: "integer"
        description: ""

      - name: "source"
        type: "string"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "messageScores"
    type: "array"
    description: ""
    subattributes:
      - name: "mcs"
        type: "integer"
        description: ""

      - name: "messageId"
        type: "string"
        description: ""

      - name: "messageRawScore"
        type: "integer"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""

  - name: "messageStatuses"
    type: "array"
    description: ""
    subattributes:
      - name: "messageDeliveryStatus"
        type: "string"
        description: ""

      - name: "messageId"
        type: "string"
        description: ""

      - name: "participantId"
        type: "string"
        description: ""

      - name: "participantType"
        type: "string"
        description: ""

      - name: "seq"
        type: "integer"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""

  - name: "sdes"
    type: "object"
    description: ""
    subattributes:
      - name: "events"
        type: "array"
        description: ""
        subattributes:
          - name: "cartStatus"
            type: "anything"
            description: ""

          - name: "customerInfo"
            type: "anything"
            description: ""

          - name: "marketingCampaignInfo"
            type: "anything"
            description: ""

          - name: "purchase"
            type: "anything"
            description: ""

          - name: "sdeType"
            type: "anything"
            description: ""

          - name: "serverTimeStamp"
            type: "string"
            description: ""

          - name: "serviceActivity"
            type: "anything"
            description: ""

  - name: "summary"
    type: "object"
    description: ""
    subattributes:
      - name: "lastUpdatedTime"
        type: "integer"
        description: ""

      - name: "text"
        type: "string"
        description: ""

  - name: "transfers"
    type: "array"
    description: ""
    subattributes:
      - name: "assignedAgentId"
        type: "string"
        description: ""

      - name: "by"
        type: "string"
        description: ""

      - name: "reason"
        type: "string"
        description: ""

      - name: "sourceAgentFullName"
        type: "string"
        description: ""

      - name: "sourceAgentId"
        type: "string"
        description: ""

      - name: "sourceAgentLoginName"
        type: "string"
        description: ""

      - name: "sourceAgentNickname"
        type: "string"
        description: ""

      - name: "sourceSkillId"
        type: "integer"
        description: ""

      - name: "sourceSkillName"
        type: "string"
        description: ""

      - name: "targetSkillId"
        type: "integer"
        description: ""

      - name: "targetSkillName"
        type: "string"
        description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "timeL"
        type: "integer"
        description: ""
---