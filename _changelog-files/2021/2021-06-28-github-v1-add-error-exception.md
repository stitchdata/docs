---
title: "GitHub (v1) update: New error exception"
content-type: "changelog-entry"
date: 2021-06-28
entry-type: updated-feature
entry-category: "integration"
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/126"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

To improve the experience of our {{ this-connection.display_name }} integration, we've changed how we handle errors. Instead of bypassing an error, we will now raise an error exception. We will display the following message when an error occurs: `HTTP-error-code: 400, Error: The request is missing or has a bad parameter.`