---
title: "Mambu (v1) update: New tables and updated API endpoints"
content-type: "changelog-entry"
date: 2020-12-18
entry-type: updated-feature
entry-category: integration
connection-id: "mambu"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mambu/pull/25"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added some new tables to the {{ this-connection.display_name }} integration:

- [`activities`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#activities)
- [`index_rate_sources`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#index_rate_sources)
- [`installments`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#installments)

We've also updated the endpoints the integration uses to extract data for the following tables:

- [`clients`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#clients) - Previously used `Get all clients`, now uses `Search clients`
- [`groups`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#groups) - Previously used `Get all groups`, now uses `Search groups`
- [`gl_journal_entries`]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#gl_journal_entries) - Previously used `Get all GL journal entries`, now uses `Search for GL journal entries`

Learn more in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}). 