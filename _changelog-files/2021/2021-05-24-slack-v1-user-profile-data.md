---
title: "Slack (v1) update: User email now available in users table"
content-type: "changelog-entry"
date: 2021-05-24
entry-type: improvement
entry-category: integration
connection-id: "slack"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-slack/pull/16"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new column to the {{ this-connection.display_name }} `users` table: `profile.email`. This column contains the email address for the associated user.

**Note**: To replicate this data, you'll also need to grant the `users:read.email` scope to the [Stitch app created for the integration]({{ site.home | append: site.baseurl | append: this-connection.url | append: "#assign-scopes" }}).