---
tap: "liveperson"
version: "1.0"
key: "engagement-history"

name: "engagement_history"
doc-link: "https://developers.liveperson.com/engagement-history-api-overview.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/engagement_history.json"
description: |
  The `{{ table.name }}` table contains info about the engagements in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"

api-method:
    name: "Retrieve engagement list by criteria"
    doc-link: "https://developers.liveperson.com/engagement-history-api-methods.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "engagement-history-id"

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

  - name: "info"
    type: "object"
    description: ""
    subattributes:
      - name: "accountId"
        type: "string"
        description: ""

      - name: "agentDeleted"
        type: "boolean"
        description: ""

      - name: "agentFullName"
        type: "string"
        description: ""

      - name: "agentGroupId"
        type: "string"
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

      - name: "agentNickName"
        type: "string"
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

      - name: "channel"
        type: "string"
        description: ""

      - name: "chatDataEnriched"
        type: "string"
        description: ""

      - name: "chatMCS"
        type: "integer"
        description: ""

      - name: "chatRequestedTime"
        type: "date-time"
        description: ""

      - name: "chatRequestedTimeL"
        type: "integer"
        description: ""

      - name: "chatStartPage"
        type: "string"
        description: ""

      - name: "chatStartUrl"
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
        type: "integer"
        description: ""

      - name: "device"
        type: "string"
        description: ""

      - name: "duration"
        type: "integer"
        description: ""

      - name: "endReason"
        type: "string"
        description: ""

      - name: "endReasonDesc"
        type: "string"
        description: ""

      - name: "endTime"
        type: "date-time"
        description: ""

      - name: "endTimeL"
        type: "integer"
        description: ""

      - name: "ended"
        type: "string"
        description: ""

      - name: "engagementId"
        type: "string"
        description: ""

      - name: "engagementSequence"
        type: "string"
        description: ""

      - name: "engagementSet"
        type: "string"
        description: ""

      - name: "firstConversation"
        type: "boolean"
        description: ""

      - name: "interactive"
        type: "string"
        description: ""

      - name: "isAgentSurvey"
        type: "string"
        description: ""

      - name: "isInteractive"
        type: "string"
        description: ""

      - name: "isPartial"
        type: "boolean"
        description: ""

      - name: "isPostChatSurvey"
        type: "string"
        description: ""

      - name: "isPreChatSurvey"
        type: "string"
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

      - name: "sharkEngagementId"
        type: "string"
        description: ""

      - name: "skillId"
        type: "string"
        description: ""

      - name: "skillName"
        type: "string"
        description: ""

      - name: "source"
        type: "string"
        description: ""

      - name: "startReason"
        type: "string"
        description: ""

      - name: "startReasonDesc"
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

      - name: "visitorId"
        type: "string"
        description: ""

      - name: "visitorName"
        type: "string"
        description: ""

  - name: "lineScores"
    type: "array"
    description: ""
    subattributes:
      - name: "lineRawScore"
        type: "integer"
        description: ""

      - name: "lineSeq"
        type: "string"
        description: ""

      - name: "mcs"
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

          - name: "isAuthenticated"
            type: "string"
            description: ""

          - name: "marketingCampaignInfo"
            type: "anything"
            description: ""

          - name: "purchase"
            type: "anything"
            description: ""

          - name: "sdeType"
            type: "string"
            description: ""

          - name: "serverTimeStamp"
            type: "string"
            description: ""

  - name: "surveys"
    type: "object"
    description: ""
    subattributes:
      - name: "postChat"
        type: "array"
        description: ""

        subattributes:
          - name: "displayName"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "questionID"
            type: "number"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "source"
            type: "string"
            description: ""

          - name: "surveyID"
            type: "number"
            description: ""

          - name: "time"
            type: "date-time"
            description: ""

          - name: "timeL"
            type: "number"
            description: ""

          - name: "value"
            type: "string"
            description: ""

          - name: "values"
            type: "array"
            description: ""

            subattributes:
              - name: "value"
                type: "string"
                description: ""

      - name: "preChat"
        type: "array"
        description: ""

        subattributes:
          - name: "displayName"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "questionID"
            type: "number"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "source"
            type: "string"
            description: ""

          - name: "surveyID"
            type: "number"
            description: ""

          - name: "time"
            type: "date-time"
            description: ""

          - name: "timeL"
            type: "number"
            description: ""

          - name: "value"
            type: "string"
            description: ""

          - name: "values"
            type: "array"
            description: ""

            subattributes:
              - name: "value"
                type: "string"
                description: ""

  - name: "transcript"
    type: "object"
    description: ""
    subattributes:
      - name: "lines"
        type: "array"
        description: ""

        subattributes:
          - name: "agentId"
            type: "string"
            description: ""

          - name: "by"
            type: "string"
            description: ""

          - name: "cannedAnswerType"
            type: "integer"
            description: ""

          - name: "controlType"
            type: "number"
            description: ""

          - name: "json"
            type: "string"
            description: ""

          - name: "lineSeq"
            type: "string"
            description: ""

          - name: "source"
            type: "string"
            description: ""

          - name: "subType"
            type: "string"
            description: ""

          - name: "text"
            type: "string"
            description: ""

          - name: "textType"
            type: "string"
            description: ""

          - name: "time"
            type: "date-time"
            description: ""

          - name: "timeL"
            type: "number"
            description: ""

  - name: "visitorInfo"
    type: "object"
    description: ""
    subattributes:
      - name: "browser"
        type: "string"
        description: ""

      - name: "browserType"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "countryCode"
        type: "string"
        description: ""

      - name: "device"
        type: "string"
        description: ""

      - name: "ipAddress"
        type: "string"
        description: ""

      - name: "isp"
        type: "string"
        description: ""

      - name: "operatingSystem"
        type: "string"
        description: ""

      - name: "org"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""
---