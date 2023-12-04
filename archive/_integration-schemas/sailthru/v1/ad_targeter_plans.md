---
tap: "sailthru"
version: "1"
key: ""

name: "ad_targeter_plans"
doc-link: "https://getstarted.sailthru.com/email/ad-targeter/ad-targeter-overview/"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/ad_targeter_plans.json"
description: |
  The `{{ table.name }}` table contains information about Ad Targeter Plans in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "get AdTargeterPlan"
    doc-link: "https://getstarted.sailthru.com/developers/api/ad-plan/"

attributes:
  - name: "plan_id"
    type: "string"
    primary-key: true
    description: "The plan ID."
    #foreign-key-id: "plan-id"

  - name: "list"
    type: "string"
    description: "The list ID"
    foreign-key-id: "list-id"

  - name: "name"
    type: "string"
    description: ""
  
  - name: "schedule"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---
