---
title: "Pipedrive (v1) update: Removed delete_log table"
content-type: "changelog-entry"
date: 2021-06-16
entry-type: "removed"
entry-category: "integration, documentation"
connection-id: "pipedrive"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/90"
---

Due to {{ this-connection.display-name }} removing support for `delete_logs` from their API, we've removed this table from our {{ this-connection.display_name }} integration. We've also updated the [{{ this-connection.display-name }} docs]({{ site.home | append: site.baseurl | append: this-connection.url }}) to reflect this.