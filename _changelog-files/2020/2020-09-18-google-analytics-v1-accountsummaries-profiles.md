---
title: "Google Analytics (v1) integrations: Use accountSummaries: list to fetch profiles"
content-type: "changelog-entry"
date: 2020-09-18
entry-type: improvement
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/32"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

{{ this-connection.display_name }} integrations will now use [`accountSummaries`](https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference/management/accountSummaries/list){:target="new"} to fetch {{ this-connection.display_name }} profiles available for the user authorizing the integration. We've made this change to reduce the number of queries Stitch makes to {{ this-connection.display_name }} and overall API quota usage.