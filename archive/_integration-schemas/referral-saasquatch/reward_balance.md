---
tap: "referral-saasquatch"
version: "1"

name: "reward_balance"
doc-link: https://docs.referralsaasquatch.com/api/methods#list_balances
singer-schema: https://github.com/singer-io/tap-referral-saasquatch/blob/master/tap_referral_saasquatch/schemas/reward_balances.json
description: |
  The `{{ table.name }}` table contains info about the balances for all rewards.

replication-method: "Key-based Incremental"
replication-key:
  name: "createdOrUpdatedSince"

api-method:
  name: "List reward balances"
  doc-link: "https://docs.referralsaasquatch.com/api/methods#list_balances"

attributes:
  - name: "userId"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "accountId"
    type: "string"
    primary-key: true
    description: "The ID of the account the user belongs to."
    foreign-key-id: "account-id"

  - name: "type"
    type: "string"
    description: "The type of reward. Possible values are `PCT_DISCOUNT`, `FEATURE`, `TIME_CREDIT`, or `CREDIT`."

  - name: "amount"
    type: "integer"
    description: "The amount of credit remaining."

  - name: "unit"
    type: "string"
    description: "The unit of the reward. For example: `tshirt`."
---