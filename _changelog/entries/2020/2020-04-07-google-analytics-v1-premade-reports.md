---
title: "Google Analytics (v1) update: Pre-made reports now available"
content-type: "changelog-entry"
date: 2020-04-07
entry-type: updated-feature
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/16"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a handful of pre-made reports to our our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:

- **Audience Overview**: Audience metrics including page views, users, bounce rate and more
- **Audience Geo Location**: A breakdown of your audience by geographical location
- **Audience Technology**: The browsers, operating systems, and devices your users employ
- **Acquisitions Overview**: The performance of your users across traffic sources and mediums
- **Behavior Overview**: Pages visited and actions performed on your website
- **Ecommerce Overview**: A breakdown of your transactions by traffic source

These reports will display as tables available for selection in the **Tables to Replicate** tab of all {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations. Check out this easy way to get started with {{ this-connection.display_name }} data!