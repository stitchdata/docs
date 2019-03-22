---
tap-reference: "referral-saasquatch"

version: "1.0"

foreign-keys:
  - id: "user-id"
    attribute: "userId"
    table: "users"
    all-foreign-keys:
      - table: "referrals"
        join-on: "referredUser"
      - table: "referrals"
        join-on: "referrerUser"
      - table: "reward_balance"
      - table: "users"
        join-on: "id"


  - id: "account-id"
    attribute: "accountId"
    table: "users"
    all-foreign-keys:
      - table: "referrals"
        join-on: "referredAccount"
      - table: "referrals"
        join-on: "referrerAccount"
      - table: "reward_balance"
      - table: "users"
---