---
title: "New integration: GitHub"
content-type: "changelog-entry"
date: 2018-06-04
entry-type: new-feature
entry-category: integration
connection-id: github
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new {{ this-connection.display_name }} integration is now available!

This integration lets you extract data from any {{ this-connection.display_name }} repository. You can choose from the following tables to replicate to your destination:

- `assignees`
- `collaborators`
- `commits`
- `issues`
- `pull_requests`
- `reviews`
- `stargazers`

Create a new integration today with seven days of free historical data. [Learn more in our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).