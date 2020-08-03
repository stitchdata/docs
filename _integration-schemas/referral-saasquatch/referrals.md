---
tap: "referral-saasquatch"
version: "1"

name: "referrals"
doc-link: https://docs.referralsaasquatch.com/api/methods/#open_list_referrals
singer-schema: https://github.com/singer-io/tap-referral-saasquatch/blob/master/tap_referral_saasquatch/schemas/referrals.json
description: |
  The `{{ table.name }}` table contains info about all of the referrals in your {{ integration.display_name }} tenant.

replication-method: "Key-based Incremental"
replication-key:
  name: "createdOrUpdatedSince"

api-method:
  name: "List referrals"
  doc-link: "https://docs.referralsaasquatch.com/api/methods/#list_referrals"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The referral ID."
    # foreign-key-id: "referral-id"

  - name: "dateConverted"
    type: "date-time"
    description: "The date the referral was converted."  

  - name: "programId"
    type: "string"
    description: "The program ID."  

  - name: "referredUser"
    type: "string"
    description: "The ID of the referred user."
    foreign-key-id: "user-id"

  - name: "referredAccount"
    type: "string"
    description: "The account ID of the referred user."
    foreign-key-id: "account-id"

  - name: "referredReward"
    type: "string"
    description: "The ID for the referred user's reward."

  - name: "referredModerationStatus"
    type: "string"
    description: |
      The moderation status of the referred user, which affects reward cancellation. Possible values are `PENDING`, `APPROVED`, and `DENIED`.

  - name: "referrerUser"
    type: "string"
    description: "The ID of the referring user."
    foreign-key-id: "user-id"

  - name: "referrerAccount"
    type: "string"
    description: "The account ID of the referring user."
    foreign-key-id: "account-id"

  - name: "referrerReward"
    type: "string"
    description: "The ID for the referring user's reward."

  - name: "referrerModerationStatus"
    type: "string"
    description: |
      The moderation status of the referring user, which affects reward cancellation. Possible values are `PENDING`, `APPROVED`, and `DENIED`.

  - name: "dateReferralStarted"
    type: "date-time"
    description: "The time of when the referral was started."

  - name: "dateReferralPaid"
    type: "date-time"
    description: "The time of when the referral was marked as `PAID`."

  - name: "dateReferralEnded"
    type: "date-time"
    description: "The time of when the referral was ended."

  - name: "dateModerated"
    type: "date-time"
    description: "The time of when the referral was last moderated."
---