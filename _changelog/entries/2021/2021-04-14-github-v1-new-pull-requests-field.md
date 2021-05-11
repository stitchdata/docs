---
title: "GitHub (v1) update: New field!"
content-type: "changelog-entry"
date: 2021-04-14
entry-type: new-feature
entry-category: integration
connection-id: github
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/109"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

New field has been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The following table now has an additional fields available for replication:

- [`pull_requests`]({{ this-connection.url | prepend: site.baseurl | append: "#pull-requests"}})


Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl }})