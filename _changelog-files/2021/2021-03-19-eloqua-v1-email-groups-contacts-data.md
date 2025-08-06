---
title: "Eloqua (v1) update: Email groups and additional contact data"
content-type: "changelog-entry"
date: 2021-03-19
entry-type: improvement
entry-category: integration
connection-id: "eloqua"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-eloqua/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added some additional data to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

- **New table**: `email_groups`
- New `contact` fields:
  - `IsBounceBack`
  - `IsSubscribed`
  - `EmailFormat`
  - `AccountName`

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl }}).