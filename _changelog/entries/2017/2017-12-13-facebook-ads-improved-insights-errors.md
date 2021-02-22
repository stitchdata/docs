---
title: "Facebook Ads (v15-10-2015) integration: Improved error handling"
content-type: "changelog-entry"
date: 2017-12-13
entry-type: improvement
entry-category: integration
connection-id: facebook-ads
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the error handling in the F{{ this-connection.display_name }} integration to more aggressively retry when Insights jobs fail. As a result of this change, the error rate for this integration has been significantly reduced.