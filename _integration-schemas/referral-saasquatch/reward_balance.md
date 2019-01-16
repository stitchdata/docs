---
tap: "referral-saasquatch"
# version: 

name: "reward_balance"
doc-link: https://docs.referralsaasquatch.com/api/methods#list_balances
singer-schema: https://github.com/singer-io/tap-referral-saasquatch/blob/master/tap_referral_saasquatch/schemas/reward_balances.json
description: |
  The `reward_balance` table contains info about the balances for all rewards.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "userId"
    type: "string"
    primary-key: true
    description: "The user ID."

  - name: "accountId"
    type: "string"
    primary-key: true
    description: "The ID of the account the user belongs to."

  - name: "n/a"
    replication-key: true

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