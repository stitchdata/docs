---
tap: "google-adwords"
version: "1.0"

name: "ads"
doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupAdService.AdGroupAd
singer-schema: https://github.com/singer-io/tap-adwords/blob/master/tap_adwords/schemas/ads.json
description: |
  The `ads` table contains comprehensive info about ads in ad groups in your Google AdWords account.

  [This is a **Core Object** table](#replication).
notes:

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "adGroupId"
    type: "integer"
    primary-key: true
    description: "The ID of the ad group containing the ad."

  - name: "adGroupAdDisapprovalReasons"
    type: "array"
    description: "The list of disapproval reasons applicable to the ad."
    subattributes:
      - name: "value"
        type: "string"
        description: "The list of disapproval reasons."

  - name: "adGroupCreativeApprovalStatus"
    type: "string"
    description: "The approval status of the ad."

  - name: "baseAdGroupId"
    type: "integer"
    description: "The ID of the base ad group from which the draft/trial ad was created."

  - name: "baseCampaignId"
    type: "integer"
    description: "The ID of the base campaign from which the draft/trial ad was created."

  - name: "customerId"
    type: "integer"
    description: "The ID of the AdWords account that the record belongs to."

  - name: "policySummary"
    type: "object"
    description: "Summary of policy findings for the ad."
    doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupAdService.AdGroupAdPolicySummary
    subattributes:
      - name: "combinedApprovalStatus"
        type: "string"
        description: "The approval status that combines review state and status."

      - name: "reviewState"
        type: "string"
        description: "Indicates the progress in the review process."

      - name: "denormalizedStatus"
        type: "string"
        description: "The overall review status based on the policy topic entries."

      - name: "policyTopicEntries"
        type: "array"
        description: "List of policy findings."
        subattributes:
          - name: "policyTopicEntryType"
            type: "string"
            description: "The type of the policy topic entry."

          - name: "policyTopicId"
            type: "string"
            primary-key: true
            description: "The policy topic ID."

          - name: "policyTopicName"
            type: "string"
            description: "The policy topic name."

          - name: "policyTopicEvidences"
            type: "array"
            subattributes:
              - name: "evidenceText"
                type: "string"
                description: "The actual evidence that triggered the policy topic to be reported."

              - name: "policyTopicEvidenceType"
                type: "string"
                description: "The type of evidence for the policy topic."

  - name: "status"
    type: "string"
    description: "The status of the ad."

  - name: "trademarks"
    type: "array"
    description: "The trademarked items that were found in the ad."
    subattributes:
      - name: "value"
        type: "string"
        description: "The trademarked items that were found in the ad."

  - name: "trademarkDisapproved"
    type: "integer"
    description: "Indicates if the ad isn't serving because it doesn't meet trademark policy."
    doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupAdService.AdGroupAd#trademarkdisapproved
---