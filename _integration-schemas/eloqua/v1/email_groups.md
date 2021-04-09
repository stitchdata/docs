---
tap: "eloqua"
version: "1"
key: "email-group"

name: "email_groups"
doc-link: &doc-link "https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/op-api-rest-1.0-assets-email-groups-get.html"
singer-schema: "https://github.com/singer-io/tap-eloqua/blob/master/tap_eloqua/schemas/emailGroups.json"
description: |
  The `{{ table.name }}` table contains details about the email groups in your {{ integration.display_name }} account.

  **Note**: This table is replicated using the {{ integration.display_name }} Application REST API.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of email groups"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The email group ID."
    foreign-key-id: "email-group-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the email group was last updated."

  - name: "type"
    type: "string"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "createdBy"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "depth"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "updatedBy"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "displayName"
    type: "string"
    description: ""

  - name: "isSecureNotificationsGroup"
    type: "string"
    description: ""

  - name: "isVisibleInOutlookPlugin"
    type: "string"
    description: ""

  - name: "isVisibleInPublicSubscriptionList"
    type: "string"
    description: ""

  - name: "isWelcomeCommunicationsGroup"
    type: "string"
    description: ""

  - name: "notificationEmailId"
    type: "string"
    description: ""

  - name: "requireOptIn"
    type: "string"
    description: ""

  - name: "subscriptionLandingPageId"
    type: "string"
    description: ""

  - name: "subscriptionListDataLookupId"
    type: "string"
    description: ""

  - name: "subscriptionListId"
    type: "string"
    description: ""

  - name: "unSubscriptionListDataLookupId"
    type: "string"
    description: ""

  - name: "unSubscriptionListId"
    type: "string"
    description: ""

  - name: "unsubscriptionLandingPageId"
    type: "string"
    description: ""

  - name: "useSecureChannel"
    type: "string"
    description: ""

  - name: "emailFooterId"
    type: "string"
    description: ""
    foreign-key-id: "email-footer-id"

  - name: "emailHeaderId"
    type: "string"
    description: ""
    foreign-key-id: "email-header-id"
---