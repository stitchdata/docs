---
tap: "twitter-ads"
version: "1"
key: "targeting-conversation"

name: "targeting_conversations"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-conversations"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_conversations.json"
description: |
  The `{{ table.name }}` table contains info about the conversation-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get targeting conversations"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-conversations"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: 
    # foreign-key-id: "targeting-conversation-id"

  - name: "conversation_type"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---