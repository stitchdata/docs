---
# tap: "outbrain"

# Not currently persisted as it makes the replication take too long
# for accounts with tons of campaigns. This results in continually
# hitting Outbrain's current rate limit (2 reqs/minute) which can
# prevent successful replication.

# name: "link_performance"
# doc-link: 
# singer-schema: 
# description: |
#   The `link_performance` table contains performance metrics for links in your Outbrain campaigns.

# replication-method: "Key-based Incremental"
# api-method:
#   name: 
#   doc-link: 

# attributes:
#   - name: "campaignId" 
#     type: "
#     primary-key: true
#     description: "This is the campaign ID plus the start date (day) for the record."

#   - name: "linkId"
#     type: "
#     primary-key: true
#     description: "

#   - name: "fromDate"
#     type: "
#     primary-key: true
#     description: "

#   - name: "impressions"
#     type: "
#     description: "

#   - name: "clicks"
#     type: "
#     description: "

#   - name: "ctr"
#     type: "
#     description: "

#   - name: "spend"
#     type: "
#     description: "

#   - name: "ecpc"
#     type: "
#     description: "

#   - name: "conversions"
#     type: "
#     description: "

#   - name: "conversionRate"
#     type: "
#     description: "

#   - name: "cpa"
#     type: "
#     description: "
---