---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "google-ecommerce"
version: "15-10-2015"

name: "ecommerce[YOUR_GA_PROFILE_ID]_v2"
description: |
  The `{{ table.name }}` table contains ECommerce data from your Google Analytics account. Refer to the table schema for the metrics and dimensions that are included.

replication-method: "Key-based Incremental"

replication-key:
  name: "start-date"
## Note: This is a query param the integration passes in the API request.
## See: https://developers.google.com/analytics/devguides/reporting/core/v3/reference#startDate

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "A unique ID generated during replication."
  
  - name: "accountid"
    type: "string"
    description: "The account ID associated with your Google Analytics ECommerce account."

  - name: "campaign"
    type: "string"
    description: |
      The campaign name ([`utm_campaign`](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_campaign"

  - name: "keyword"
    type: "string"
    description: |
      This column contains the keyword description ([`utm_term`](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_keyword"

  - name: "medium"
    type: "string"
    description: |
      This column contains the medium name ([`utm_medium`](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_medium"

  - name: "profileid"
    type: "string"
    description: "Your Google Analytics profile ID."

  - name: "profilename"
    type: "string"
    description: "Your Google Analytics profile name."

  - name: "socialnetwork"
    type: "string"
    description: "This column contains the name of the social network (e.g. Facebook, YouTube, etc.)"
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_socialnetwork"

  - name: "source"
    type: "string"
    description: |
      This column contains the name of the order source. ([`utm_source`](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_source"

  - name: "transactionid"
    type: "string"
    description: |
      The order ID, which you can use to join the referral data back to your orders data. Refer to [Google’s documentation](https://support.google.com/analytics/answer/1009612?hl=en){:target="new"} for background on tracking setup and management.

  - name: "transactions"
    type: "integer"
    description: "The total number of transactions."
---