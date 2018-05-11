---
tap: "referral-saasquatch"
# version:

name: "users"
doc-link: https://docs.referralsaasquatch.com/api/methods#list_users
singer-schema: https://github.com/singer-io/tap-referral-saasquatch/blob/master/tap_referral_saasquatch/schemas/users.json
description: |
  The `users` table contains info about the users in your Referral SaaSquatch tenant.

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
   
  - name: "accountId"
    type: "string"
    primary-key: true
    description: "The ID of the account the user belongs to."

  - name: "n/a"
    replication-key: true

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "firstName"
    type: "string"
    description: "The first name of the user."

  - name: "lastName"
    type: "string"
    description: "The last name of the user."

  - name: "imageUrl"
    type: "string"
    description: "The URL of the image associated with the user."

  - name: "firstSeenIp"
    type: "string"
    description: "The user's IP address on identification."

  - name: "lastSeenIp"
    type: "string"
    description: "The user's last known IP address."

  - name: "dateCreated"
    type: "date-time"
    description: "The Unix timestamp of when the user was created."

  - name: "emailHash"
    type: "string"
    description: "The hash of the user's email address."

  - name: "referralSource"
    type: "string"
    description: "The domain from which the user registered."

  - name: "locale"
    type: "string"
    description: "The user's locale, in `language_COUNTRY` format. For example: `en_US`"

  - name: "shareLink"
    type: "string"
    description: "The user's unique share link."

  - name: "facebookShareLink"
    type: "string"
    description: "The share link for Facebook."

  - name: "twitterShareLink"
    type: "string"
    description: "The share link for Twitter."

  - name: "emailShareLink"
    type: "string"
    description: "The share link for email."

  - name: "linkedInShareLink"
    type: "string"
    description: "The share link for LinkedIn."
---
