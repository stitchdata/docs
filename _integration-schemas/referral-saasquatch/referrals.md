---
tap: "referral-saasquatch"
# version:

name: "referrals"
doc-link: https://docs.referralsaasquatch.com/api/methods/#open_list_referrals
singer-schema: https://github.com/singer-io/tap-referral-saasquatch/blob/master/tap_referral_saasquatch/schemas/referrals.json
description: |
  The `referrals` table contains info about all of the referrals in your Referral SaaSquatch tenant.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The referral ID."

  - name: "n/a"
    replication-key: true

  - name: "referredUser"
    type: "string"
    description: "The ID of the referred user."

  - name: "referredAccount"
    type: "string"
    description: "The account ID of the referred user."

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

  - name: "referrerAccount"
    type: "string"
    description: "The account ID of the referring user."

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